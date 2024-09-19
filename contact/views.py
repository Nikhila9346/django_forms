from django.shortcuts import render
from django.http import HttpResponse
from .forms import ContactForm
from .models import Contact

# Create your views here.
def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("Your data is submitted successfully")
        else:
            return HttpResponse("Something went wrong")
    form = ContactForm()
    context = {
        'forms': form
    }
    return render(request, 'form.html', context)






# def contact(request):
#     if request.method == "POST":
#         f = ContactForm(request.POST)
#         if f.is_valid():
#             #retrieving processed data
#             fname = f.cleaned_data['full_name']
#             name = f.cleaned_data['name']
#             email = f.cleaned_data['email']
#             message = f.cleaned_data['message']
#             Contact.objects.create(
#                 fname = fname,
#                 name = name,
#                 email = email,
#                 msg = message
#             )
#         else:
#             return HttpResponse("Invalid data Please try again!")
#     c = ContactForm()
#     context ={
#         'form':c
#     }
#     return render(request, 'form.html', context)