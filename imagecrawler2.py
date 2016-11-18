# coding: utf-8

import urllib
import urllib.parse
import urllib.request
import re
import os
import socket

socket.setdefaulttimeout(15)


def get_imglist(url):
    '''获取给定网页内的图片链接列表'''
    html = urllib.request.urlopen(url).read()
    return re.findall('"objURL":"(.*?)",', html.decode('utf8'))


def get_filename(objurl):
    '''从图片链接里获取图片文件名'''
    return objurl.split('/')[-1]


def download(url, path=None, count=0):
    '''下载给定url内图片'''
    if path is None:
        path = r'D:/MasterFiles/ImgRecer/test20161117/'
    elif not os.path.exists(path):
        print("The path %s doesn't exist, will be created." % path)
        os.makedirs(path)
        print("%s created OK." % path)

    for idx, img_url in enumerate(get_imglist(url)):
        print(str(count) + '_' + str(idx) + ' - Downloading ' + img_url + '...', end=' ')
        try:
            urllib.request.urlretrieve(img_url, os.path.join(path, get_filename(img_url)))
            print('Done!')
        except:
            print('Fail!')


word = input('Input what u want:')
page_number = int(input('Input how many pages u want:'))
path = input('Input where u want to save:')
base_url = 'http://image.baidu.com/search/flip?tn=baiduimage&ie=utf-8&'

for page in range(page_number):
    url = base_url + urllib.parse.urlencode({'word': word, 'pn': int(page)*20})
    print(url)
    download(url, path=path, count=page+1)
