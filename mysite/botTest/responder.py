import re
from random import choice
import botTest.morph
import logging


class Responder:
    """AIの応答を制御する思考エンジンの基底クラス。
    メソッド:
    response(str) -- ユーザーの入力strを受け取り、思考結果を返す
    プロパティ:
    name -- Responderオブジェクトの名前
    """

    def __init__(self, name, dictionary):
        """文字列nameを受け取り、自身のnameに設定する。
        辞書dictionaryを受け取り、自身のdictionaryに保持する。"""
        self._name = name
        self._dictionary = dictionary

    def response(self, *args):
        """文字列を受け取り、思考した結果を返す"""
        pass

    @property
    def name(self):
        """思考エンジンの名前"""
        return self._name


class WhatResponder(Responder):
    """AIの応答を制御する思考エンジンクラス。
    入力に対して疑問形で聞き返す。"""

    def response(self, text, _):
        """文字列textを受け取り、'{text}ってなに？'という形式で返す。"""
        return '{}ってなに？'.format(text)


class RandomResponder(Responder):
    """AIの応答を制御する思考エンジンクラス。
    登録された文字列からランダムなものを返す。
    """

    def response(self, *args):
        """ユーザーからの入力は受け取るが、使用せずにランダムな応答を返す。"""
        return choice(self._dictionary.keyword)


class PatternResponder(Responder):
    """AIの応答を制御する思考エンジンクラス。
    登録されたパターンに反応し、関連する応答を返す。
    """

    def response(self, text, _):
        """ユーザーの入力に合致するパターンがあれば、関連するフレーズを返す。"""
        logger = logging.getLogger('command')
        logger.info(text)
        logger.info(self._dictionary.pattern)
        for ptn in self._dictionary.pattern:
            logger.info(ptn)
            matcher = re.search(ptn['pattern'], text)
            if matcher:
                logger.info('1245')
                logger.info(matcher)
                chosen_response = choice(ptn['phrases'])
                logger.info(chosen_response)
                return chosen_response.replace('%match%', matcher[0])

        logger.info('1246')
        return choice(self._dictionary.keyword)


class TemplateResponder(Responder):
    def response(self, _, parts):
        """形態素解析結果partsに基づいてテンプレートを選択・生成して返す。"""
        keywords = [word for word, part in parts if botTest.morph.is_keyword(part)]
        count = len(keywords)
        if count > 0:
            if count in self._dictionary.template:
                template = choice(self._dictionary.template[count])
                for keyword in keywords:
                    template = template.replace('%noun%', keyword, 1)
                return template
        return choice(self._dictionary.keyword)