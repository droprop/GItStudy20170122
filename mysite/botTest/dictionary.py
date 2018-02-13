import os.path
from collections import defaultdict
import botTest.morph
import logging

class Dictionary:
    """思考エンジンの辞書クラス。
    クラス変数:
    DICT_KEYWORD -- ランダム辞書のファイル名
    DICT_PATTERN -- パターン辞書のファイル名
    スタティックメソッド:
    touch_dics() -- 辞書ファイルにtouch処理を行う
    make_pattern(str) -- パターン辞書読み込み用のヘルパー
    pattern_to_line(pattern) -- パターンハッシュをパターン辞書形式に変換する
    プロパティ:
    keyword -- ランダム辞書
    pattern -- パターン辞書
    template -- テンプレート辞書
    """
    DICT = {'keyword': './dics/keyword.txt',
            'pattern': './dics/pattern.txt',
            'template': './dics/template.txt',
            }

    def __init__(self):
        """ファイルから辞書の読み込みを行う。"""
        Dictionary.touch_dics()
        with open(Dictionary.DICT['keyword'], encoding='utf-8') as f:
            self._keyword = [l for l in f.read().splitlines() if l]

        with open(Dictionary.DICT['pattern'], encoding='utf-8') as f:
            self._pattern = [Dictionary.make_pattern(l) for l in f.read().splitlines() if l]

        with open(Dictionary.DICT['template'], encoding='utf-8') as f:
            self._template = defaultdict(lambda: [], {})  # set dict default value to []
            for line in f:
                count, template = line.strip().split('\t')
                if count and template:
                    count = int(count)
                    self._template[count].append(template)

    def study(self, text, parts):
        """ランダム辞書、パターン辞書、テンプレート辞書をメモリに保存する。"""
        #self.study_keyword(text)
        self.study_pattern(text, parts)
        #self.study_template(parts)

    def study_template(self, parts):
        """形態素のリストpartsを受け取り、
        名詞のみ'%noun%'に変更した文字列templateをself._templateに追加する。
        名詞が存在しなかった場合、または同じtemplateが存在する場合は何もしない。
        """
        template = ''
        count = 0
        logger = logging.getLogger('command')


        for word, part in parts:
            if botTest.morph.is_keyword(part):
                word = '%noun%'
                count += 1
            template += word
            logger.info('1346')
        
        if count > 0 and template not in self._template[count]:
            self._template[count].append(template)
        logger.info(template)

    def study_keyword(self, text):
        """ユーザーの発言textをランダム辞書に保存する。
        すでに同じ発言があった場合は何もしない。"""
        if not text in self._keyword:
            self._keyword.append(text)

    def study_pattern(self, text, parts):
        """ユーザーの発言textを、形態素partsに基づいてパターン辞書に保存する。"""
        logger = logging.getLogger('command')
        for word, part in parts:
            if botTest.morph.is_keyword(part):  # 品詞が名詞であれば学習
                # 単語の重複チェック
                # 同じ単語で登録されていれば、パターンを追加する
                # 無ければ新しいパターンを作成する
                duplicated = next((p for p in self._pattern if p['pattern'] == word), None)
                logger.info(word)
                logger.info(parts)
                if duplicated:
                    if not text in duplicated['phrases']:
                        duplicated['phrases'].append(text)
                else:
                    self._pattern.append({'pattern': word, 'phrases': [text]})

    def save(self):
        """メモリ上の辞書をファイルに保存する。"""
        with open(Dictionary.DICT['keyword'], mode='w', encoding='utf-8') as f:
            f.write('\n'.join(self.keyword))

        with open(Dictionary.DICT['pattern'], mode='w', encoding='utf-8') as f:
            f.write('\n'.join([Dictionary.pattern_to_line(p) for p in self._pattern]))

        with open(Dictionary.DICT['template'], mode='w', encoding='utf-8') as f:
            for count, templates in self._template.items():
                for template in templates:
                    f.write('{}\t{}\n'.format(count, template))

    @staticmethod
    def pattern_to_line(pattern):
        """パターンのハッシュを文字列に変換する。"""
        return '{}\t{}'.format(pattern['pattern'], '|'.join(pattern['phrases']))

    @staticmethod
    def make_pattern(line):
        """文字列lineを\tで分割し、{'pattern': [0], 'phrases': [1]}の形式で返す。
        [1]はさらに`|`で分割し、文字列のリストとする。"""
        pattern, phrases = line.split('\t')
        if pattern and phrases:
            return {'pattern': pattern, 'phrases': phrases.split('|')}

    @staticmethod
    def touch_dics():
        """辞書ファイルがなければ空のファイルを作成し、あれば何もしない。"""
        for dic in Dictionary.DICT.values():
            if not os.path.exists(dic):
                open(dic, 'w').close()

    @property
    def keyword(self):
        """ランダム辞書"""
        return self._keyword

    @property
    def pattern(self):
        """パターン辞書"""
        return self._pattern

    @property
    def template(self):
        """テンプレート辞書"""
        return self._template