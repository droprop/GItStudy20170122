from django.shortcuts import render

from django.http import HttpResponse
import logging
from botTest.models import Talk
import random

def index(request):

    talkList = Talk.objects.all()
    logger = logging.getLogger('command')

    ran = random.randint(0, len(talkList)) - 1
    logger.info(ran)


    context = {'ret': talkList[ran]}
    return render(request, 'botTest/index.html', context)
