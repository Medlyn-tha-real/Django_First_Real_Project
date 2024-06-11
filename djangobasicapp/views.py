import datetime
from django.http import HttpResponse
from django.shortcuts import render
import requests
import logging

from djangobasicapp.models import Authors


# Create your views here.
# Function based view
def Home(request):
    return HttpResponse("<h1>Hello world i'm back again heavily</h1>")

    
def ShowMoreMessage(request):
    return HttpResponse("<h1>Hello world i'm back again heavily</h1>"
                        "<h2>Hello world i'm back again heavily</h2>"
                        "<h3>Hello world i'm back again heavily</h3>"
                        "<h4>Hello world i'm back again heavily</h4>"
                        "<h5>Hello world i'm back again heavily</h5>")

def UseVariableAsResponse(request):
    Message = "<h1>Welcome To Django Development</h1>"
    Message += "<h2>Welcome To Django Development</h2>"
    Message += "<h3>Welcome To Django Development</h3>"
    Message += "<h4>Welcome To Django Development</h4>"
    Message += "<h5>Welcome To Django Development</h5>"
    Message += "<h6>Welcome To Django Development</h6>"
    return HttpResponse(Message)

def GetRequestVariables(request):
    if(request.method == "GET"):
        if(request.GET.get("Message")):
            Message = request.GET.get("Message")
        else:
            Message ="<h1>You haven't supplied value for Message Parameter..</h1>"

        if(request.GET.get("Country")):
            Message += request.GET.get("Country")
        else:
            Message +="<h1>You haven't supplied value for Country Parameter..</h1>"
    return HttpResponse(Message)

def ShowDateTimeInfo(request):
    TodaysDate=datetime.datetime.now()
    templatefilename="djangobasicapp/ShowTimeInfo.html"
    dict={"TodaysDate": TodaysDate}
    return render(request, templatefilename, dict)

# from datetime import date,datetime

def LoggingExample(request):
    logging.debug(f"Debug : I just entered into the View..{datetime.now()}")
    logging.info(f"Info : Confirmation that things are working as expected")
    logging.warning(f"warning : An indication that something unexpected happened")
    logging.error(f"error : Due to a more serious problem, the software has not been able to perform as expected")
    logging.critical(f"critical : A serious problem indicating that the program itself may be unable to function")
    

    custom_logger = logging.getLogger("mycustom_logger")
    custom_logger.debug(f"Debug : I just entered into the view..{datetime.now()}")
    custom_logger.info(f"Info : Confirmation that things are working as expected.")
    custom_logger.warning(f"Warning : An indication that something unexpected happened")
    custom_logger.error(f"error : Due to a more serious problem, the software has not been able to perform as expected")
    custom_logger.critical(f"critical : A serious problem indicating that the program itself may be unable to function")


    
    return HttpResponse("<h1>Logging Demo</h1>")

def iftagdemo(request):
    data = {"name": "DON Ahmeed", "isVisible": True, "loggedIn": True, "countryCode": "USA", "workExperience": 8, "statecode": None}
    templatefilename = "djangobasicapp/ifTagDemo.html"
    dict = {"Data":data}
    return render(request, templatefilename, dict)

def ShowProducts(request):
    
    Products = []

    Processors = [
        {'Category': 'AMD', 'processors': ['Ryzen 3990', 'Ryzen 3970', 'Ryzen 3960', 'Ryzen 3950']},
        {'Category': 'Intel', 'processors': ['Xeon 8362', 'Xeon 8358', 'Xeon 8380']}
    ];

    Products.append( {'productID' :1, 'productName' :"AMD Ryzen 3990", 'quantity' :100, 'unitsInStock' :50, 'disContinued' :False, 'cost' :3000})
    Products.append( {'productID' :2, 'productName' :"AMD Ryzen 3980", 'quantity' :100, 'unitsInStock' :50, 'disContinued' :False, 'cost' :4000})
    Products.append( {'productID' :3, 'productName' :"AMD Ryzen 3970", 'quantity' :100, 'unitsInStock' :50, 'disContinued' :False, 'cost' :5000})
    Products.append( {'productID' :4, 'productName' :"AMD Ryzen 3960", 'quantity' :100, 'unitsInStock' :50, 'disContinued' :False, 'cost' :6000})
    Products.append( {'productID' :5, 'productName' :"AMD Ryzen 3950", 'quantity' :100, 'unitsInStock' :50, 'disContinued' :False, 'cost' :7000})
    Products.append( {'productID' :6, 'productName' :"AMD Ryzen 3940", 'quantity' :100, 'unitsInStock' :50, 'disContinued' :False, 'cost' :8000})
    Products.append( {'productID' :7, 'productName' :"AMD Ryzen 3930", 'quantity' :100, 'unitsInStock' :50, 'disContinued' :False, 'cost' :9000})
    Products.append( {'productID' :8, 'productName' :"AMD Ryzen 3920", 'quantity' :100, 'unitsInStock' :50, 'disContinued' :False, 'cost' :10000})
    TemplateFile =  "djangobasicapp/ShowProducts.html"
    dict = {"Products" : Products, "TotalProducts" : len(Products), "Processors":Processors}
    return render(request, TemplateFile, dict)


def LoadUsers(request):
    templatefilename = "djangobasicapp/ShowUsers.html"
    response = CallRestAPI()
    dict = {"users": response.json()}
    return render(request, templatefilename, dict)

def CallRestAPI():
    BASE_URL = "https://fakestoreapi.com"
    response = requests.get(f"{BASE_URL}/users")
    return(response)

def Index(request):
    return render(request, "djangobasicapp/Index.html")

def LoadUsers2(request):
    Templatefilename = "djangobasicapp/ShowUsersAsCard.html"
    image = 'https://i.pravatar.cc';
    response = CallRestAPI()
    dict = {"users": response.json(), "image":image}
    return render(request, Templatefilename, dict)

def CallRestAPI2(userid):
    BASE_URL = "https://fakestoreapi.com"
    response = requests.get(f"{BASE_URL}/users/{userid}")
    return(response)


def LoadUserDetails(request):

    if request.method == "POST":
        counter = int(request.POST.get("useridcounter"))

        if(request.POST.get("btnNext")):
            counter += 1
            if counter >= 11:
                counter = 1
        elif(request.POST.get("btnPrevious")):
            counter -= 1
            if counter == 0:
                counter = 1
        
    else:
        counter=1
        
    templatefilename = "djangobasicapp/ShowUserDetails.html"
    response=CallRestAPI2(counter)
    image = "https://i.pravatar.cc";
    dict = {"user": response.json(), "image":image}
    return render(request, templatefilename, dict)

def PassModelTotemplate(request):
    # instantiated model class object
    obj = Authors("Raheem Don", "Europe", "Businesss")
    templatefilename = "djangobasicapp/PassModel.html"

    AuthorList = []
    AuthorList.append(Authors("Ahmeed Medlyn", "Europe", "Businesss"))
    AuthorList.append(Authors("Ahmeed MVP", "Europe", "Businesss"))
    AuthorList.append(Authors("Brown Medlyn", "Europe", "Businesss"))
    AuthorList.append(Authors("Dino Medlyn", "Europe", "Businesss"))
    AuthorList.append(Authors("Ahmeed Pelumi", "Europe", "Businesss"))
    AuthorList.append(Authors("Ahmeed Wealth", "Europe", "Businesss"))

    # Array of Objects
    Dict = {"Author":obj, "Authors": AuthorList}
    return render(request, templatefilename, Dict)


def BuiltInFiltersDemo(request):
    Processors = [
        {"name": "Ryzen 3970", "cores": 32},
        {"name": "Ryzen 3980", "cores": 16},
        {"name": "Ryzen 3930", "cores": 64},
    ]
    dict= {
        "ProbationPeriod": 4,
        "FirstName": "Raheem",
        "LastName": "Ahmeed",
        "PayForCut": 787543,
        "FirstQuarter": ["Jan", "Feb", "Mar"],
        "SecondQuarter": ["Apr", "May", "Jun"],
        "FQuarter": [1,2,3],
        "SQuarter": [4,5,6],
        "AboutMe": "God like aura",
        "now": datetime.datetime.now(),
        "PreviousCut": "",
        "NextCut": None,
        "Processors": Processors,
        "Message": "<h1>I am the main character</h1>",
        "Website": " https://www.uiacademy.co.in"
    }
    return render(request, "djangobasicapp/BIFDemo.html", dict)
        
def CustomFiltersDemo(request):
    webframeworks = {
        'Description' : "This is my life, i am the main character and i am the DON!!",
        'InDemand' : "4.9",
        'PollNumber' : 34565
        }
    return render(request, "djangobasicapp/TestCustomFilters.html", webframeworks)


























