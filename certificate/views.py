from django.shortcuts import render,redirect
from PIL import Image, ImageFont, ImageDraw 
from django.http import HttpResponse
from .forms import *
from .models import Certificate
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.views.generic import ListView
from django.contrib.auth import authenticate, login, logout



def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('view-certi')
        else:
            return render(request, 'certificate/no-certi.html',)

    return render(request,'certificate/login.html')

def logoutUser(request):
    logout(request)
    return redirect('login')

def view_certi(request, *args, **kwargs):
    user = request.user
    c=0
    context = {'user':user}
    if user.certificate.eureka_jr:
        image = Image.open(user.certificate.eureka_jr.path)
        draw = ImageDraw.Draw(image)
        myfont = ImageFont.truetype("calibrib.ttf", 100)
        points = 800,700
        string = user.username
        draw.text(points, string, "black", font=myfont)
        file_name = user.username+'eureka_jr.png'
        image.save(file_name)
        context['btn_value1'] = 'eureka_jr'
        c=1
    else:
        pass

    if user.certificate.workshop:
            image = Image.open(user.certificate.workshop.path)
            draw = ImageDraw.Draw(image)
            myfont = ImageFont.truetype("calibrib.ttf", 70)
            points = 700,600
            string = user.username
            draw.text(points, string, "black", font=myfont)
            file_name = user.username+'workshop.png'
            image.save(file_name)
            context['btn_value2'] = 'workshop'
            c=1
    else :
        pass
        
    if user.certificate.bootcamp:
            image = Image.open(user.certificate.bootcamp.path)
            draw = ImageDraw.Draw(image)
            myfont = ImageFont.truetype("calibrib.ttf", 150)
            points = 1300,1100
            string = user.username
            draw.text(points, string, "black", font=myfont)
            file_name = user.username+'bootcamp.png'
            image.save(file_name)
            context['btn_value3'] = 'bootcamp'
            c=1
    else :
        pass
   
    return render(request, 'certificate/view_certi.html',context)
    

def dd_certi(request,filename):
    user = request.user
    
    user_path =     user.username+filename+".png"
    template_path = 'certificate/download.html'
    context = {'user_path': user_path}
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')
    # To download
    # response['Content-Disposition'] = 'attachment; filename="report.pdf"'
    response['Content-Disposition'] = 'attachment; filename="report.pdf"'

    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(
       html, dest=response)
    # if error then show some funy view
    if pisa_status.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response
  
    