from .serializers import *
from .models import *
from rest_framework.views import APIView
from portals.GM2 import GenericMethodsMixin
from rest_framework.response import Response
from rest_framework import status
from portals.services import generate_token,my_mail,user_creation_mail
from django.contrib.auth.hashers import check_password
from random import randint



class UserApi(GenericMethodsMixin,APIView):
    model = User
    serializer_class = UserSerializer1
    lookup_field = "id"
    
from django.db import transaction
class RegisterUserApi(APIView):
    def post(self,request,*args, **kwargs):
        try : 
            with transaction.atomic() : 
                print(request.data)
                serializer = UserSerializer(data=request.data)
                if  serializer.is_valid():
                    user = serializer.save()
                    print(user.id)
                    token = generate_token(user.email)
                    res = user_creation_mail(user.email)
                    return Response({"message" : "User Created Successfully" , "data" : UserSerializer1(user).data , "token" : token},status=status.HTTP_201_CREATED)
                return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        except Exception as e :
            return Response({"error" : True , "message" : str(e)},status=status.HTTP_400_BAD_REQUEST)

class LoginAPI(APIView):
    def post(self,request,*args, **kwargs):
        try : 
            email       = request.data.get('email')
            password    = request.data.get('password')
            # Generate Token
            user = User.objects.filter(email=email).first()
            if user is None : 
             return Response({"error" : False,"data" : "User Not Exists"},status=status.HTTP_404_NOT_FOUND)
            token = generate_token(user.email)
            # password_match = check_password(password,user.password)
            password_match = check_password(password,user.password)
            serializer = UserSerializer1(user)
            data = {"error" : False, "message": "User logged in successfully","user_info": serializer.data,"token" : token}
            if password == user.password  or password_match:
                return Response(data,status=status.HTTP_200_OK)
            return Response({"error" : True, "message" : "Password is not Matched"},status=status.HTTP_400_BAD_REQUEST)
        except Exception as e :
            return Response({"error" : True, "message" : str(e)},status=status.HTTP_400_BAD_REQUEST)

class ChangePasswordApi(APIView):
    def post(self,request,*args, **kwargs):
        try : 
            serializer = ChangePasswordSerializer(data=request.data,context={'request': self.request})
            if serializer.is_valid():
                serializer.save()
                return Response({"Success": "Password updated successfully"},status=status.HTTP_202_ACCEPTED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e :
                return Response({"error" : True, "message" : str(e)},status=status.HTTP_400_BAD_REQUEST)
from portals.email_utility import send_email_async


class ForgotPasswordAPI(APIView):
    def post(self,request,*args, **kwargs):
        try :
            mail = request.data.get('email')
            print("in user",mail)
            user = User.objects.get(email=mail)
            print(user)
            otp = randint(1000,9999)
            send_email_async("Email OTP",otp, [mail])
            res = my_mail(mail,otp)
            print(res)
            return Response(data={'Success':'Otp Mail sent successfully to '+ mail,'OTP':str(otp)},status=status.HTTP_200_OK)
        except:
            return Response(data={"error": True,"message" : "User Email Does not exists"},status=status.HTTP_400_BAD_REQUEST )

class UpdateUserAPI(APIView):
    def put(self,request,*args, **kwargs):
        try :
            user = User.objects.get(id=request.thisUser)
            serializer = UserSerializer1(user, data=request.data,partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response({"error" : False, "message": "User updated successfully",},status=status.HTTP_202_ACCEPTED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e :
            return Response({"error" : True , "message" : str(e)},status=status.HTTP_400_BAD_REQUEST)


    
class ResetPasswordAPI(APIView):
    def post(self,request,*args, **kwargs):
        try : 
            email = request.data.get('email')
            password = request.data.get('password')
            if User.objects.filter(email=email):
                user = User.objects.get(email=email)
                user.set_password(password)
                user.save()
                return Response(data={'Success':'Password for Email ' +str(user) +' reset successful'},status=status.HTTP_200_OK)
            return Response(data = {'Error':'Email does not exists'})
        except Exception as e :
                return Response({"error" : True , "message" : str(e)},status=status.HTTP_400_BAD_REQUEST)


class PageNotFoundAPI(APIView):
    def get(self,request,*args, **kwargs):
        return Response({"error" : True, "message" : "This API Does not exists in this Application"},status=status.HTTP_404_NOT_FOUND)


# filter  api 
# from date to date purchase sold,sell,all => all details 
# base amount
# date wise/specific vehicle  : maintance 
 
