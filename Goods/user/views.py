from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.utils.decorators import method_decorator

from rest_framework import generics

from Goods import models
from API.serializers import CartSerializer

@login_required(login_url='login')
def myCart(request):
    cart = models.Cart.objects.get(author=request.user, is_active=True)
    cartProduct = models.CartProduct.objects.filter(cart= cart)
    context = {}
    context['cart']=cart
    context['cartpro']=cartProduct
    return render(request, 'user/detail.html', context)

@login_required(login_url='login')
def addProductToCart(request, id):
    product_id = id
    quantity = int(request.POST['quantity'])  # Convert quantity to integer
    product = models.Product.objects.get(id=product_id)
    cart, _ = models.Cart.objects.get_or_create(author=request.user, is_active=True)
    try:
        cart_product = models.CartProduct.objects.get(cart=cart, product_id=product_id)
        cart_product.quantity += quantity
        cart_product.save()
    except models.CartProduct.DoesNotExist:
        cart_product = models.CartProduct.objects.create(
            product=product, 
            cart=cart,
            quantity=quantity
        )
    if quantity and product.price:
        cart_product.total_price = quantity * float(product.price)
        cart_product.save()
    return redirect('mycart')


@login_required(login_url='login')
def substruct(request, id):
    code = id
    quantity = int(request.POST['quantity'])
    product_cart = models.CartProduct.objects.get(id=code)
    product_cart.quantity = quantity
    product_cart.save()
    if quantity and product_cart.product.price:
        product_cart.total_price = quantity * float(product_cart.product.price)
        product_cart.save()
    return redirect('mycart')

@login_required(login_url='login')
def deleteProductCart(request, id):
    product_cart = models.CartProduct.objects.get(id=id)
    product_cart.delete()
    return redirect('mycart')

@login_required(login_url='login')
def CreateOrder(request, id):
    print('boshi')
    cart = models.Cart.objects.get(id=id)
    
    cart_products = models.CartProduct.objects.filter(cart=cart)

    done_products = []

    for cart_product in cart_products:
        if cart_product.quantity <= cart_product.product.quantity:
            cart_product.product.quantity -= cart_product.quantity
            cart_product.product.save()
            done_products.append(cart_product)
        else:
            for product in done_products:
                product.product.quantity += product.quantity
                product.product.save()
            raise ValueError('Qoldiqda kamchilik')
    if request.method == 'POST':
        models.Order.objects.create(
            cart_id=cart.id,
            full_name = request.POST['full_name'],
            email = request.POST['email'],
            phone = request.POST['phone'],
            address = request.POST['address'],
            status = 1
            )
        cart.is_active = False
        cart.save()
        return render(request, 'user/order.html')
    return redirect('mycart')


@login_required(login_url='login')
def wishlist(request):
    wish_list = models.Wishlist.objects.filter(user=request.user)
    context = {}
    context['wishlist']=wish_list
    return render(request, 'user/wishlist.html', context)


@method_decorator(login_required(login_url='login'), name = 'dispatch')
class MyCartAPIView(generics.ListCreateAPIView):
    queryset = models.Cart.objects.all()
    serializer_class = CartSerializer

@method_decorator(login_required(login_url='login'), name = 'dispatch')
class MyCartRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Cart.objects.all()
    serializer_class = CartSerializer