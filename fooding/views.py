from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
def homePage(request):
    # landing page
    return render(request, 'fooding/index.html')

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
    return render(request, 'fooding/review.html') 

def menuPage(request, id):
    # can add to cart 
    return render(request, 'fooding/menu.html') 

def createGeneralOrder(request):
    return render(request, 'dashboard/generalUser/addOrder.html')

@login_required
def allGeneralOrder(request):
    return render(request, 'dashboard/generalUser/allOrder.html')