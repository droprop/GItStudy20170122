from django.shortcuts import render

from django.http import HttpResponse
import logging
from botTest.models import Talk

def index(request):

    talkList = Talk.objects.all()
    logger = logging.getLogger('command')
    logger.info(talkList[0])

    context = {'ret': 'aaaabbbb'}
    return render(request, 'botTest/index.html', context)
