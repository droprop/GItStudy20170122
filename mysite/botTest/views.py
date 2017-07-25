from django.http import HttpResponse
from django.shortcuts import render
from botTest.models import Talk
from user_agents import parse
import logging
import json

def index(request):

    logger = logging.getLogger('command')
    logger.info('-----request-----')
    logger.info(request.META['HTTP_USER_AGENT'])

    agent = request.META['HTTP_USER_AGENT']

    logger.info(parse(agent))

    isSP = parse(agent).is_mobile
    logger.info(isSP)


    retTalk = Talk.objects.filter(name='ryo').order_by('?')[0]
    context = {'retContent': retTalk.content, 'isSP' : isSP}
    return render(request, 'botTest/index.html', context)


def ajaxFunc(request):

    retTalk = Talk.objects.filter(name='ryo').order_by('?')[0]
    logger = logging.getLogger('command')

    context = {'retContent': retTalk.content}
    logger.info(context)
    logger.info(isinstance(context, dict))
    data = json.dumps(context)

    return HttpResponse(data, content_type='application/json')

def indexS(request):

    logger = logging.getLogger('command')
    logger.info('-----request-----')
    logger.info(request.META['HTTP_USER_AGENT'])

    agent = request.META['HTTP_USER_AGENT']

    logger.info(parse(agent))

    isSP = parse(agent).is_mobile
    logger.info(isSP)


    retTalk = Talk.objects.filter(name='saki').order_by('?')[0]
    context = {'retContent': retTalk.content, 'isSP' : isSP}
    return render(request, 'botTest/saki.html', context)


def ajaxFuncS(request):

    retTalk = Talk.objects.filter(name='saki').order_by('?')[0]
    logger = logging.getLogger('command')

    context = {'retContent': retTalk.content}
    logger.info(context)
    logger.info(isinstance(context, dict))
    data = json.dumps(context)

    return HttpResponse(data, content_type='application/json')
