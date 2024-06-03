import datetime
from django.http import HttpResponse
from django.shortcuts import render

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

import logging
from datetime import date,datetime

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





