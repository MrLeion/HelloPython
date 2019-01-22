#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
网易新闻排行榜爬虫
'''
__author__ = 'tzl'

# requests
# import requests
# # 建立连接获取发起请求并收取响应
# response = requests.get()
# # 打印请求头
# 打印响应体
# urllib
# httplib2
# -*- coding: utf-8 -*-
import os
import sys
import urllib
import requests
import re
from lxml import etree


def StringListSave(save_path, filename, slist):
    # 创建目录
    if not os.path.exists(save_path):
        os.makedirs(save_path)
    # 文件路径及名称
    path = save_path + "/" + filename + ".txt"

    with open(path, "w+") as fp:
        for s in slist:
            fp.write("%s\t\t%s\n" % (s[0], s[1]))


##########
# 正则表达式匹配
##########
def Page_Info(myPage):
    '''Regex'''
    mypage_Info = re.findall(
        r'<div class="titleBar" id=".*?"><h2>(.*?)</h2><div class="more"><a href="(.*?)">.*?</a></div></div>', myPage,
        re.S)
    return mypage_Info


def New_Page_Info(new_page):
    '''Regex(slowly) or Xpath(fast)'''
    # new_page_Info = re.findall(r'<td class=".*?">.*?<a href="(.*?)\.html".*?>(.*?)</a></td>', new_page, re.S)
    # # new_page_Info = re.findall(r'<td class=".*?">.*?<a href="(.*?)">(.*?)</a></td>', new_page, re.S) # bugs
    # results = []
    # for url, item in new_page_Info:
    #     results.append((item, url+".html"))
    # return results
    dom = etree.HTML(new_page)
    new_items = dom.xpath('//tr/td/a/text()')
    new_urls = dom.xpath('//tr/td/a/@href')
    assert (len(new_items) == len(new_urls))
    return zip(new_items, new_urls)


def Spider(url):
    # 文件名称索引
    i = 0
    print("downloading ", url)
    # myPage = requests.get(url).content.decode("utf-8")
    myPage = requests.get(url).content.decode("gb18030")
    # 获取有多少个页面
    myPageResults = Page_Info(myPage)
    save_path = "网易新闻抓取"
    filename = str(i) + "_" + "新闻排行榜"
    # 保存目录
    StringListSave(save_path, filename, myPageResults)
    i += 1
    for item, url in myPageResults:
        print("downloading ", url)
        new_page = requests.get(url).content.decode("gb18030")
        # new_page = urllib2.urlopen(url).read().decode("gbk")
        newPageResults = New_Page_Info(new_page)
        filename = str(i) + "_" + item
        StringListSave(save_path, filename, newPageResults)
        i += 1


if __name__ == '__main__':
    print("start")
    start_url = "http://news.163.com/rank/"
    Spider(start_url)
    print("end")
