from django.shortcuts import render

from django.http import HttpResponse
import logging
from botTest.models import Talk
import random

def index(request):

    talkList = Talk.objects.all()
    logger = logging.getLogger('command')

    ran = random.randint(1, len(talkList)) - 1
    logger.info(ran)

    lis = list()
    lis.append(talkList[ran])

    context = {'ret': lis}
    return render(request, 'botTest/index.html', context)
