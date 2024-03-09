from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from django.contrib.auth.hashers import check_password,make_password
from rest_framework.response import Response
from Ecommerce.models import user_details,product_details,card,orders
from .serializers import FilesSerializer,OrderSerializer
from rest_framework import viewsets
# Create your views here.

@api_view(['POST'])
def create_user(request,format=None):
    name_input=request.data['name']
    email_input=request.data['email']
    phone_input=request.data['phone']
    password_input=request.data['password']
    obj=user_details(
        name=name_input,
        email=email_input,
        phone=phone_input,
        password=make_password(password_input)
    )
    obj.save()
    return Response({'message':'Successfully Registered'})




@api_view(['GET'])
def get_user_all(request,format=None):
    user=user_details.objects.all().values()
    return Response({'user':user})

@api_view(['POST'])
def get_user(request,format=None):
    Email=request.data['email']
    user=user_details.objects.filter(email=Email).all().values()
    return Response({'user':user})

@api_view(['POST'])
def login_user(request, format=None):
    email_input = request.data.get('email')
    password = request.data.get('password')
    try:
        user_get=user_details.objects.get(email=email_input)
    except:
        return Response({'status':'user does not found'})
    #print(user_get.password)
    if(check_password(password,user_get.password)):
        return Response({'status':'successfull loged in'})
                    
    else:
        return Response({'status':'password doesnot match'})
    




class FilesViewSet(viewsets.ModelViewSet):
    queryset = product_details.objects.all()
    serializer_class = FilesSerializer

@api_view(['POST'])
def get_product_category(request,format=None):
    Caregory=request.data['category']
    try:
        get_products=product_details.objects.filter(category=Caregory).all().values()[:100]
        return Response({'products':get_products})
    except:
        pass

@api_view(['GET'])
def get_all_products(request,format=None):
    obj=product_details.objects.all().values()[:100]
    return Response({'products':obj})

@api_view(['POST'])
def create_card(request,format=None):
    Email=request.data['email']
    Product_id=request.data['product_id']
    try:
        ob=card.objects.get(product_id=Product_id)
        return Response({'message':'Already Added to the Card'})

    except:
        obj=card(
            email=Email,
            product_id=Product_id
        )
        obj.save()
        return Response({'message':'Added to the Card successfully'})


@api_view(['POST'])
def get_card(request,format=None):
    Email=request.data['email']
    obj=card.objects.filter(email=Email).all().values()
    return Response({'cards':obj})

@api_view(['POST'])
def get_card_product(request,format=None):
    Id=request.data['product_id']
    obj=product_details.objects.filter(id=Id).all().values()
    return Response({'product':obj})

@api_view(['DELETE'])
def remove_card(request,format=None):
    Id=request.data['product_id']
    obj=card.objects.filter(product_id=Id).delete()
    return Response({"message":"deleted successfullt",
                     'data':obj
                     })


# @api_view(['POST'])
# def create_order(request,format=None):
#     Name=request.data['name']
#     Mobile=request.data['mobile']
#     Pin=request.data['pin']
#     Address=request.data['address']
#     Flat_no=request.data['flat_no']
#     State=request.data['state']

#     obj=orders(
#         name=Name,
#         mobile=Mobile,
#         pin=Pin,
#         address=Address,
#         flat_no=Flat_no,state=State
#     )
#     obj.save()
#     return Response({'message':'Successfully created order'
#                      })

@api_view(['POST'])
def create_order(request, format=None):
    serializer = OrderSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({'message': 'Successfully created order', 'order': serializer.data})
    return Response({'message': 'Failed to create order', 'errors': serializer.errors})

@api_view(['POST'])
def get_order(request,format=None):
    Email=request.data['email']
    order=orders.objects.filter(email=Email).all().values()
    return Response({'orders':order})
