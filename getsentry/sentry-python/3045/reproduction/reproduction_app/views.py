from django.http import HttpResponse
from django.shortcuts import render

import logging


# Create your views here.
def index(request):
    logger = logging.getLogger(__name__)
    logger.exception("This is an exception")
    return HttpResponse("Hello, world. You're at the index.")
