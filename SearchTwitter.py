CONSUMER_KEY            = '**************************************************'
CONSUMER_SECRET_KEY     = '**************************************************'
ACCESS_TOKEN            = '**************************************************'
ACCESS_TOKEN_SECRET     = '**************************************************'

# 日本語をURLエンコードするためのモノ
import urllib.parse

from twitter import *
from janome.tokenizer import Tokenizer

#import requests
#from bs4 import BeautifulSoup

# WikipediaAPIのインストールとja版に設定変更を行った。
import wikipedia
wikipedia.set_lang("ja")



def searching(WORD):
        test = wikipedia.search(WORD)
        print (test)
        print ("\n\n\n")

        print (test[0])
        test2 = urllib.parse.quote(test[0])
        print(test2)

        ans = ("https://ja.wikipedia.org/wiki/" + test2)
        return test[0],ans



GetTwitter = Twitter(auth=OAuth(ACCESS_TOKEN,ACCESS_TOKEN_SECRET,CONSUMER_KEY,CONSUMER_SECRET_KEY))
Sentence = Tokenizer()
i :int = 0
timelines = GetTwitter.statuses.home_timeline()

# 連続したデータtimelinesを分割したtweetに変更する.
for timeline in timelines:
        #tl = '[{username}]:{text}'.format(
        #        id=timeline['id'], username=timeline['user']['name'], text=timeline['text'])
        one_tweet = [timeline['text'],timeline['id_str'],timeline['user']['screen_name']]


        # 分割したtweetを形態素解析をする.
        tester = [token.surface for token in Sentence.tokenize(one_tweet[0]) 
                if token.part_of_speech.startswith('名詞')]
        for index, word in enumerate(tester):
                # 形態素解析によって分割されたリスト状のデータを一つ一つ判別する.
                if word == "何":
                        del tester[index:]
                        tester.reverse()
                        ANSWER = searching(tester[0])
                        reply = ("@" + str(one_tweet[2]) +"\n" + ANSWER[0] + "\n" + ANSWER[1])
                        print (reply)
                        GetTwitter.statuses.update(status=reply,in_reply_to_status_id = one_tweet[1])


        i = 0




"""
# スクレイピングしようとしたら空のリストになって返ってしまい、対策も調べても中々出てこないので断念
param = {'q':'ドイツ'}
result = requests.get("https://search.yahoo.co.jp/search",params=param)

print (result.url)

soup = BeautifulSoup(result.text, "html.parser")

link_info = soup.select('.sw-Card__title sw-Card__title--cite > a')

print (link_info)
"""