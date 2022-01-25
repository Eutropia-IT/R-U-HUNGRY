from seller.models import Restaurant
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
def homePage(request):
    restaurants = Restaurant.objects.filter(type='restaurant', )[:8]
    homechefs = Restaurant.objects.filter(type='home', )[:8]
    context = {
        'restaurants' : restaurants,
        'homechefs': homechefs,
    }
    # landing page
    return render(request, 'fooding/index.html', context)

def searchPage(request):
    # Search result
    return render(request, '')

def notificationsPage(request):
    # can give review 
    # can see notifications 
    return render(request, '')

def cartPage(request):
    # Can order 
    # can remove from cart 
    return render(request, '')
 
def reviewPage(request):
    # see all reviews 
    return render(request, '') 

def menuPage(request):
    # can add to cart 
    return render(request, '') 

def createGeneralOrder(request):
    return render(request, 'dashboard/generalUser/addOrder.html')

@login_required
def allGeneralOrder(request):
    return render(request, 'dashboard/generalUser/allOrder.html')