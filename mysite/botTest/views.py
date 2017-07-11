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

    ret1 = talkList[ran].content
    logger.info(ret1)

    ran = random.randint(1, len(talkList)) - 1
    ret2 = talkList[ran].content
    logger.info(ret2)

#    logger.info(isinstance(ret2.content, str))
#    logger.info(isinstance(ret2.content, Talk))

    context = {'ret1': ret1, 'ret2' : ret2}

    return render(request, 'botTest/index.html', context)

def ajaxFunc(request):

    talkList = Talk.objects.all()
    logger = logging.getLogger('command')

    ran = random.randint(1, len(talkList)) - 1
    #tl = request.POST['talk']
    #logger.info(tl)

    lis = list()
    lis.append(talkList[ran].content)
#    lis.append("aaaaaa")

    ret1 = talkList[ran].content
    logger.info('ajaxFunc--start--')

    ran = random.randint(1, len(talkList)) - 1
    ret2 = talkList[ran].content
    logger.info(ret2)

#    logger.info(isinstance(ret2.content, str))
#    logger.info(isinstance(ret2.content, Talk))

#    context = {'ret1': ret1, 'ret2' : ret2}
    context = {'ret1': 'diaid', 'ret2' : 'ret2'}
    logger.info(context)
    logger.info(isinstance(context, dict))
    data = json.dumps(context)
    logger.info('isinstance(context, dict)')

    return HttpResponse(data, content_type='application/json')
