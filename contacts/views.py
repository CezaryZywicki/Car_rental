from django.shortcuts import redirect, render
from django.contrib import messages

from contacts.models import Contact

# Create your views here.

def inquiry(request):
    if request.method == 'POST':
        car_id = request.POST['car_id']
        car_title = request.POST['car_title']
        user_id = request.POST['user_id']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        message = request.POST['message']
        start_date = request.POST['start_date']
        end_date = request.POST['end_date']
        city = request.POST['city']
    
     
    contact = Contact(car_id=car_id, car_title=car_title, user_id=user_id, first_name=first_name,
     last_name=last_name, message=message,
     start_date=start_date, end_date=end_date, city=city)
 
    contact.save()
    messages.success(request, 'Your request has been submitted.')
    return redirect('/cars/' +car_id)