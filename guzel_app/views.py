from rest_framework import status
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializer import ProductCategory,customers,Order,Product
from .models import TbProductCategory, TbOrder, TbProduct,TbCustomer
from django.conf import settings

"""
API Overview
"""
@api_view(['GET'])
def getAllCat(request):
    return Response(ProductCategory(TbProductCategory.objects.all(),many=True).data)

@api_view(['GET'])
def getAllProd(request):
    return Response(Product(TbProduct.objects.all(),many=True).data)

@api_view(['POST'])
def login(request):
    
    try:
        a=TbCustomer.objects.get(customer_email=request.data['email'],customer_password=request.data['password'])
        settings.USER_LOGIN = True
        settings.USER_=a
        return JsonResponse(customers(settings.USER_).data,safe=False)
    except:
        return Response({'error':"Login Failed, Invalid Credidentials"},status=status.HTTP_400_BAD_REQUEST)
    
    
@api_view(['POST'])
def register(request):
    c=customers(data=request.data)
    if c.is_valid():
        c.save()
        settings.USER_LOGIN = True
        settings.USER_=c
        return Response(customers(settings.USER_).data)
    else:
        return Response({'error':"Registration Failed, Invalid Credidentials"},status=status.HTTP_403_BAD_REQUEST)
    
@api_view(['GET'])
def getProdbyCat(request,pk):
    
    s=Product(TbProduct.objects.filter(product_category_id=int(pk)),many=True)
    
    return JsonResponse(s.data,safe=False)

@api_view(['GET'])
def getprod(request,pk):
    print(pk)
    return Response(Product(TbProduct.objects.filter(product_id=pk)).data)

@api_view(['POST'])
def createorder(request):
    if True:
        import string
        import random
        alph=string.ascii_lowercase
        num=range(0,10)
        code_=list(list(alph)+list(num))
        from datetime import date
        for i in list(request.data['products']):
            
            if i[0] is None:
                continue
            print(i)
            print(list(request.data['products'])[1])
            prod=TbProduct.objects.get(product_id=i[0])
            c=TbOrder.objects.create(
            order_trackingid="".join([str(random.choice(code_)) for i in range(0,26)]),
            order_customerid=1,
            order_customeremail="huzaifamaw@gmail.com",
            
            order_productid=prod.product_id,
            order_productname=prod.product_name,
            order_productsku=prod.product_sku,
            order_productprice=prod.product_price,
            order_productqty=i[1],
            order_productsubtotal=float(i[1])*float(prod.product_price),
            
            order_date=date.today(),
            order_isshipped=0)
            c.save()

        return Response({"msg":"order created"})
    else:
        return Response({'error':"User Not Logged in"},status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
def getorder(request,pk):
    return Response(TbOrder.objects.get(order_id=pk))

@api_view(['GET'])
def getorderhistory(request):
    return Response(TbOrder.objects.filter(order_customerid=settings.USER_.Customer_ID))
