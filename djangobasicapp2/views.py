from django.shortcuts import render

# Create your views here.
def Home(request):
    templatefilename="djangobasicapp2/Home.html"
    return render(request, templatefilename)





