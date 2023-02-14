from django.shortcuts import render
from django.views import View
from .models import *

# Create your views here.

def index(request):
    # all = All.objects.all()
    photoshop = Photoshop.objects.all()
    art = Art.objects.all()
    web = Web.objects.all()
    context = {
        # 'alls': all,
        'photoshops': photoshop,
        'arts': art,
        'webs': web
    }

    return render(request, 'index.html', context)


def form_submission(request):
    if request.method == "GET":
        contact = Contact()
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        contact.name = name
        contact.email = email
        contact.subject = subject
        contact.message = message
        contact.save()
#     return render(request, 'index.html')
#         name = request.POST['name']
#         email = request.POST['email']
#         subject = request.POST['subject']
#         message = request.POST['message']
#
#         form = Contact.objects.create(name=name, email=email, subject=subject, message=message)
#         form.save()
    return render(request, 'index.html')
