from django.shortcuts import render

from django.http import HttpResponse
import logging
from botTest.models import Talk
import random
import json

def index(request):

    talkList = Talk.objects.all()
    logger = logging.getLogger('command')

    ran = random.randint(1, len(talkList)) - 1
    #tl = request.POST['talk']
    #logger.info(tl)

    lis = list()
    lis.append(talkList[ran].content)
#    lis.append("aaaaaa")

    ret1 = talkList[ran]
    logger.info(ret1)

    ran = random.randint(1, len(talkList)) - 1
    ret2 = talkList[ran]
    logger.info(ret2)

    context = {'ret1': ret1, 'ret2' : ret2}
    data = json.loads(context)
    return render(request, 'botTest/index.html', data)
