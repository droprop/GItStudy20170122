from django.shortcuts import render

from django.http import HttpResponse
import logging
from botTest.models import Talk
import random

def index(request):

    talkList = Talk.objects.all()
    logger = logging.getLogger('command')

    ran = random.randint(1, len(talkList)) - 1
    #tl = request.POST['talk']
    logger.info(tl)

    lis = list()
    lis.append(talkList[ran].content)
#    lis.append("aaaaaa")

    context = {'ret': lis}
    return render(request, 'botTest/index.html', context)
