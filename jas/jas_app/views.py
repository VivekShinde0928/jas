import json
import django.db
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from .models import Contact

baseURL = "/"


@csrf_exempt
def home(request):
    return render(request,'index.html',{'baseURL':baseURL})


@csrf_exempt
def sendMail(request):
    try:
        if request.method == 'POST':
            response = {}
            name = request.POST.get('name')
            email = request.POST.get('email')
            remarks = request.POST.get('remarks')
            phone = request.POST.get('phone')

            obj = Contact.objects.create(name=name, email=email,remarks=remarks,phone=phone)
            obj.save()


            response['msg'] = "true"
            return JsonResponse(json.dumps(response), safe=False)

    except Exception as e:
        print("Err: ", e)
        return "Email not sent"
