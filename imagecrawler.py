# coding: utf-8

import json
import urllib2
import os
import re
import urllib
import socket
socket.setdefaulttimeout(30)

queryword = raw_input('请输入查询关键词： ')
pn = int(raw_input('请输入要获取的图片数量： '))

path = os.getcwd() + '/image/' + queryword

if not os.path.exists(path):
    os.makedirs(path)

# os.chdir('./image')
print "Images will be saved in ", path


def urlDecryption(fakeurl):
    '''解码url'''
    rep = {"w":"a","k":"b","v":"c","1":"d","j":"e","u":"f","2":"g","i":"h",
           "t":"i","3":"j","h":"k","s":"l","4":"m","g":"n","5":"o","r":"p",
           "q":"q","6":"r","f":"s","p":"t","7":"u","e":"v","o":"w","8":"1",
           "d":"2","n":"3","9":"4","c":"5","m":"6","0":"7","b":"8","l":"9",
           "a":"0","_z2C$q":":","_z&e3B":".","AzdH3F":"/"}
    rep = dict((re.escape(k), v) for k, v in rep.iteritems())
    pattern = re.compile("|".join(rep.keys()))
    realurl = pattern.sub(lambda m: rep[re.escape(m.group(0))], fakeurl)

    return realurl


#  http://image.baidu.com/search/acjson?tn=resultjson_com&ipn=rj&ct=201326592&is=&fp=result&queryWord=%E5%A3%81%E7%BA%B8&cl=2&lm=-1&ie=utf-8&oe=utf-8&adpicid=&st=-1&z=0&ic=0&word=%E5%A3%81%E7%BA%B8&s=0&se=&tab=&width=&height=&face=0&istype=2&qc=&nc=1&fr=&cg=wallpaper&pn=30&rn=30&gsm=30000001e&1472451656718=

for i in range(pn):
    url = ('http://image.baidu.com/search/acjson?tn=resultjson_com&ipn=rj&ct=201326592&is=&fp=result&cl=2&lm=-1&ie=utf-8&oe=utf-8&adpicid=&st=-1&z=0&ic=0&s=0&se=&tab=&width=&height=&face=0&istype=2&qc=&nc=1&fr=&cg=wallpaper&rn=30&gsm=30000001e&1472451656718=&')\
           + urllib.urlencode({'queryWord': queryword,
                               'word': queryword,
                               'pn': (i+1)*30})
    print "URL： ", url
    try:
    	data = urllib2.urlopen(url).read()
    	json_data = json.loads(data)
    except Exception, e:
    	print "Json load error:", e
    for idx, item in enumerate(json_data['data']):
        try:
            imgurl = urlDecryption(item['objURL'])
            print "Retrieving " + imgurl + ' ...'
            extension = '.' + imgurl.split('.')[-1]
            imgpath = unicode(path, 'utf8') + '/' + str(i) + '-' + str(idx) + extension
            img = urllib.urlretrieve(imgurl, imgpath)
            print "Done."
            print img
        except Exception, e:
            print "Something wrong happened. ", e
