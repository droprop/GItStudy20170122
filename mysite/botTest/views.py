from django.http import HttpResponse
from django.shortcuts import render
from botTest.models import Talk
from user_agents import parse
import logging
import json
import re
from janome.tokenizer import Tokenizer
from botTest.dictionary import Dictionary
import botTest.morph
import os.path
from botTest.responder import WhatResponder, RandomResponder, PatternResponder, TemplateResponder


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

#    context = {'retContent': retTalk.content}
    logger.info(request.GET['myText'])
    myText = request.GET['myText']

    dictionary = Dictionary()
    parts = botTest.morph.analyze(myText)
    responder = PatternResponder('Pattern', dictionary)
    responder = TemplateResponder('Template', dictionary)
    res = responder.response(myText, parts)

    dictionary.study(myText, parts)

    logger.info(res)

    dictionary.save()

#    for token in tokens:
#        logger.info(token.surface) #分割した文字
#        logger.info(token.part_of_speech) #それの名詞とか動詞とか

#    logger.info(context)
#    logger.info(isinstance(context, dict))
    context = {'retContent': res}
    data = json.dumps(context)

    return HttpResponse(data, content_type='application/json')

def analyze(text):
    """文字列textを形態素解析し、[(surface, parts)]の形にして返す。"""
    t = Tokenizer()
    tokens = t.tokenize(text)
    return [(t.surface, t.part_of_speech) for t in tokens]

def is_keyword(part):
    """品詞partが学習すべきキーワードであるかどうかを真偽値で返す。"""
    return bool(re.match(r'名詞,(一般|代名詞|固有名詞|サ変接続|形容動詞語幹)', part))

def pattern_to_line(pattern):
    """パターンのハッシュを文字列に変換する。"""
    return '{}\t{}'.format(pattern['pattern'], '|'.join(pattern['phrases']))

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

