import requests
from rest_framework.decorators import api_view, permission_classes, action
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from .serializer import CreateUserSerializer, UserSerializer

# Client ID and AccessToken get from Application create in db
CLIENT_ID = 'BwRi7vofWyieSaGILcQPfm9ytq6AUrlmjIIt1Sbu'
CLIENT_SECRET = 'FRgi0uEZKj79EfBifp2xk1KSbUqnmVEij88WW3jQXgmTXNOiMlEyuts5YNqzYHHKWG79EqpZjF8erXNCtWaJAxdnGRbOu1FiLXXjueXbHg3t8mvbxvxBYlbsxOlSOdHl'


@api_view(['POST'])
@permission_classes([AllowAny])
def register(request):
    """
    Registers user to the server. Input should be in the format:
    {"email": "email", "password": "1234abcd"}
    """
    # Put the data from the request into the serializer
    serializer = CreateUserSerializer(data=request.data)
    # Validate the data
    if serializer.is_valid():
        # If it is valid, save the data (creates a user).
        serializer.save()
        # Then we get a token for the created user.
        # This could be done differently
        # r = requests.post('http://127.0.0.1:8000/o/token/',
        #                   data={
        #                       'grant_type': 'password',
        #                       'email': request.data['email'],
        #                       'password': request.data['password'],
        #                   },
        #                   )
        # return Response(r.json())
        return Response(serializer.data)
    return Response(serializer.errors)


@api_view(['POST'])
@permission_classes([AllowAny])
def token(request):
    """
    Gets tokens with email and password. Input should be in the format:
    {"email": "email", "password": "1234abcd"}
    """
    r = requests.post(
        'http://127.0.0.1:8000/o/token/',
        data={
            'grant_type': 'password',
            'email': request.data['email'],
            'password': request.data['password'],
            'client_id': CLIENT_ID,
            'client_secret': CLIENT_SECRET,
        },
    )
    print(r.json())
    return Response(r.json())


@api_view(['POST'])
@permission_classes([AllowAny])
def refresh_token(request):
    """
    Registers user to the server. Input should be in the format:
    {"refresh_token": "<token>"}
    """
    r = requests.post(
        'http://127.0.0.1:8000/o/token/',
        data={
            'grant_type': 'refresh_token',
            'refresh_token': request.data['refresh_token'],
            'client_id': CLIENT_ID,
            'client_secret': CLIENT_SECRET,
        },
    )
    return Response(r.json())


@api_view(['POST'])
@permission_classes([AllowAny])
def revoke_token(request):
    """
    Method to revoke tokens.
    {"token": "<token>"}
    """
    r = requests.post(
        'http://127.0.0.1:8000/o/revoke_token/',
        data={
            'token': request.data['token'],
            'client_id': CLIENT_ID,
            'client_secret': CLIENT_SECRET,
        },
    )
    # If it goes well return success message (would be empty otherwise)
    if r.status_code == requests.codes.ok:
        return Response({'message': 'token revoked'}, r.status_code)
    # Return the error if it goes badly
    return Response(r.json(), r.status_code)
