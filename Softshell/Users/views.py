from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import Users
from .serializers import UserSerializer
from rest_framework.decorators import action
from django.conf import settings
from rest_framework_jwt.utils import jwt_payload_handler, jwt
from django.contrib.auth import user_logged_in


class UsersViewSet(viewsets.ModelViewSet):
    queryset = Users.objects.all()
    serializer_class = UserSerializer
    permission_classes = []

    @action(detail=True, methods=['post'], permission_classes=[])
    def authenticate_user(request):
        try:
            email = request.data['email']
            password = request.data['password']

            user = Users.objects.get(email=email, password=password)
            if user:
                try:
                    payload = jwt_payload_handler(user)
                    token = jwt.encode(payload, settings.SECRET_KEY)
                    user_details = {}
                    user_details['name'] = "%s %s" % (
                        user.first_name, user.last_name)
                    user_details['token'] = token
                    user_logged_in.send(sender=user.__class__,
                                        request=request, user=user)
                    return Response(user_details, status=status.HTTP_200_OK)

                except Exception as e:
                    raise e
            else:
                res = {
                    'error': 'can not authenticate with the given credentials or the account has been deactivated'}
                return Response(res, status=status.HTTP_403_FORBIDDEN)
        except KeyError:
            res = {'error': 'please provide a email and a password'}
            return Response(res)



# TODO JWT convertir ce qui suit pour la modelViewSet 

# @api_view(['POST'])
# @permission_classes([AllowAny, ])
# def authenticate_user(request):

#     try:
#         email = request.data['email']
#         password = request.data['password']

#         user = User.objects.get(email=email, password=password)
#         if user:
#             try:
#                 payload = jwt_payload_handler(user)
#                 token = jwt.encode(payload, settings.SECRET_KEY)
#                 user_details = {}
#                 user_details['name'] = "%s %s" % (
#                     user.first_name, user.last_name)
#                 user_details['token'] = token
#                 user_logged_in.send(sender=user.__class__,
#                                     request=request, user=user)
#                 return Response(user_details, status=status.HTTP_200_OK)

#             except Exception as e:
#                 raise e
#         else:
#             res = {
#                 'error': 'can not authenticate with the given credentials or the account has been deactivated'}
#             return Response(res, status=status.HTTP_403_FORBIDDEN)
#     except KeyError:
#         res = {'error': 'please provide a email and a password'}
#         return Response(res)