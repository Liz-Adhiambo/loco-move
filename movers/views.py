from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED, HTTP_400_BAD_REQUEST
from django.contrib.auth import get_user_model
from .serializers import *
from rest_framework import status
from .models import *

@api_view(['POST'])
@authentication_classes([])
@permission_classes([])
def user_login_view(request):
    username = request.data.get('username')
    password = request.data.get('password')
    print("one")

    user = authenticate(request, username=username, password=password)
    print("weny")

    if user is not None:
        print("9")
        # Authentication successful
        users=User.objects.get(username=username)
        refresh = RefreshToken.for_user(user)

        # Return the user's details, refresh token, and access token in the response
        return Response({
            'Success': True,
            'Code': 200,
            'Details': {
                "user_id":users.id,
                'email': users.email,
                'first_name': users.first_name,
                'last_name': users.last_name,
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            }
        }, status=HTTP_200_OK)
    else:
        # Authentication failed
        return Response({
            'Success': False,
            'Code': 401,
            'message': 'Invalid email or password.'
        }, status=HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@permission_classes([])
def driver_signup_view(request):
    serializer = SignupSerializer(data=request.data)
    if serializer.is_valid():
        email=serializer.data.get('email')
        password=serializer.data.get('password')
        first_name=serializer.data.get('first_name')
        last_name=serializer.data.get('last_name')
        username=serializer.data.get('username')
        gender=serializer.data.get('gender')
        dob=serializer.data.get('dob')
        middle_name=serializer.data.get('middle_name')

#
        # try:
        User = get_user_model()
      
        user = User.objects.create_user(email=email,
                                        password=password,
                                        first_name=first_name,
                                        last_name=last_name,
                                        username=email,is_driver=True,
        )
        mover= Driver.objects.create(user=user,
                                    middle_name= middle_name,
                                    dob= dob,gender=gender
            
                                    )


        return Response({'Success': True, 'Code': 201, 'message': 'Driver created successfully.'}, status=HTTP_201_CREATED)
        # except:
        #     return Response({'Success': False, 'Code': 400, 'message': 'Invalid username or email'}, status=HTTP_400_BAD_REQUEST)
    return Response({'Success': False, 'Code': 400, 'message': serializer.errors}, status=HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@permission_classes([])
def mover_signup_view(request):
    serializer = SignupSerializer(data=request.data)
    if serializer.is_valid():
        email=serializer.data.get('email')
        password=serializer.data.get('password')
        first_name=serializer.data.get('first_name')
        last_name=serializer.data.get('last_name')
        username=serializer.data.get('username')
        gender=serializer.data.get('gender')
        dob=serializer.data.get('dob')
        middle_name=serializer.data.get('middle_name')
        is_mover=True

#
        # try:
        User = get_user_model()
      
        user = User.objects.create_user(email=email,
                                        password=password,
                                        first_name=first_name,
                                        last_name=last_name,
                                        username=email,is_mover=True,
        )
        mover= Mover.objects.create(user=user,
                                    middle_name= middle_name,
                                    dob= dob,gender=gender
            
                                    )


        return Response({'Success': True, 'Code': 201, 'message': 'Mover created successfully.'}, status=HTTP_201_CREATED)
        # except:
        #     return Response({'Success': False, 'Code': 400, 'message': 'Invalid username or email'}, status=HTTP_400_BAD_REQUEST)
    return Response({'Success': False, 'Code': 400, 'message': serializer.errors}, status=HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@permission_classes([])
def user_signup_view(request):
    serializer = UsersignupSerializer(data=request.data)
    if serializer.is_valid():
        email=serializer.data.get('email')
        password=serializer.data.get('password')
        first_name=serializer.data.get('first_name')
        last_name=serializer.data.get('last_name')

#
        # try:
        User = get_user_model()
      
        user = User.objects.create_user(email=email,
                                        password=password,
                                        first_name=first_name,
                                        username=email
        )

        return Response({'Success': True, 'Code': 201, 'message': 'User created successfully.'}, status=HTTP_201_CREATED)
        # except:
        #     return Response({'Success': False, 'Code': 400, 'message': 'Invalid username or email'}, status=HTTP_400_BAD_REQUEST)
    return Response({'Success': False, 'Code': 400, 'message': serializer.errors}, status=HTTP_400_BAD_REQUEST)



@api_view(['GET', 'POST'])
def profile_list(request):
    if request.method == 'GET':
        profiles = Profile.objects.all()
        serializer = ProfileSerializer(profiles, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ProfileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def profile_detail(request, pk):
    try:
        profile = Profile.objects.get(pk=pk)
    except Profile.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ProfileSerializer(profile)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = ProfileSerializer(profile, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        profile.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
@api_view(['GET'])
def list_drivers(request):
    drivers = Driver.objects.all()
    serializer = DriverSerializer(drivers, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def list_movers(request):
    drivers = Mover.objects.all()
    serializer = MoverSerializer(drivers, many=True)
    return Response(serializer.data)

# request move
@api_view(['POST'])
def request_move(request):
    if request.method == 'POST':
        serializer = RequestMoveSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'Success': True, 'Code': 200, 'message': 'Request sent successfully.'}, status=HTTP_201_CREATED)
        return Response({'Success': False, 'Code': 400, 'message': serializer.errors}, status=HTTP_400_BAD_REQUEST)
    
# schedule move
@api_view(['POST'])
def schedule_move(request):
    if request.method == 'POST':
        serializer = ScheduleMoveSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'Success': True, 'Code': 200, 'message': 'Move scheduled successfully.'}, status=HTTP_201_CREATED)
        return Response({'Success': False, 'Code': 400, 'message': serializer.errors}, status=HTTP_400_BAD_REQUEST)
    
###vehiclesss
@api_view(['POST'])
def add_vehicle(request):
    serializer = VehicleSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({'Success': True, 'Code': 200, 'message': 'Vehicle added successfully.'}, status=HTTP_201_CREATED)
    return Response({'Success': False, 'Code': 400, 'message': serializer.errors}, status=HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT'])
def select_bid(request, ride_request_id):
    try:
        ride_request = MoveRequest.objects.get(pk=ride_request_id)
    except MoveRequest.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        bids = Bid.objects.filter(ride_request=ride_request)
        serializer = BidSerializer(bids, many=True)
        return Response(serializer.data)
    elif request.method == 'PUT':
        # Here, you would typically send the ID of the bid to be accepted
        bid_id = request.data.get('bid_id')
        bid = Bid.objects.get(pk=bid_id)
        ride_request.driver = bid.driver
        ride_request.status = "ride accepted"
        ride_request.save()
        return Response(status=status.HTTP_200_OK)
    

@api_view(['POST'])
def create_bid(request):
    if request.method == 'POST':
        serializer = BidSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
