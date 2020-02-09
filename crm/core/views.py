from django.shortcuts import HttpResponse

# Create your views here.
def home(request):
    #============================================
    html_response = "<h1>Bienvenido a crm confival</h1>"
    return HttpResponse(html_response)

