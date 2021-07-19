from django.shortcuts import render
from django.http import HttpResponse
import logging


# Get an instance of a logger
logger = logging.getLogger(__name__)

# Create your views here.
def helloView(request):
    logger.info('Hello from the other side! :)')
    logger.info("'Exception': '500 Internal Server Error'")
    return HttpResponse("{'Greetings': 'Hello World!'}")
    
