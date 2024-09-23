from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request,'home.html')

def aboutUs(request):
    data1= {'ceo':'manikanta',
            'cto':'kotesh',
            'student_details':[
                {'name':'mani','phone':9347595946},
                {'name':'kotesh','phone':9912021361}
            ],'number':[10,20,30,40,50]
            }
    
    return render(request,'aboutus.html',data1)
def services(request):
    return render(request,'services.html')
def contact(request):
    return render(request,'contact.html')
def learnmore(request):
    return render(request,'404.html')
def servicesnumber(request,servicesnumber):
       
    rem = "you entered the valid service " + str(servicesnumber)
    return HttpResponse( rem )
    #    else:
    #        return HttpResponse("It is the invalid course")