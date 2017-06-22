# -*- coding: utf-8 -*-
import requests
import config
import random
url = 'https://maker.ifttt.com/trigger/time_to_eat/with/key/' + config.KEY
def random_dict(dictionary):
    index = random.randint(0, len(dictionary) - 1)
    return dictionary[index]
def random_text():
    dictionary = [u"人是铁，饭是钢，一顿不吃饿得慌。", u"民以食为天", u"吃饭不积极，脑子有问题", u"千补万补，不如饭补。", u"吃得，才能做得。", u"听人劝，吃饱饭", u"日求三餐 夜求一宿", u"有万贯家财 一日仅用三餐", u"吃千吃万 不如吃饭", u"脸皮儿壮，吃的胖。", u"干版直正，饿的头疼。", u"该吃吃，该喝喝，有事甭往心里搁。", u"鸡儿不吃豆，豆是他舅。", u"今朝有酒今朝醉。", u"金窝银窝，不如家里的灶火窝。", u"口大吃四方。", u"老天爷，下大雨，蒸锅馒头供香你。", u"千里做官，为了吃穿。", u"不信山羊不吃楝楝豆。", u"饱汉不知饿汉饥。", u"天上有个长不老，地上有个吃不饱。"]
    return random_dict(dictionary)
def random_user():
    dictionary = ['zjcfbyr']
    return "@" + random_dict(dictionary)
text = random_text()
user = random_user()
payload = {'value1': text, 'value2': user}
requests.post(url, json=payload)
