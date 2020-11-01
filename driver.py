# -*- coding: utf-8 -*-
# Sci自动下载

import requests
import lxml.etree
import re
from tkinter import filedialog


def download_files():
    for i in pmid_list:
        data['request'] = i
        save_name = i
        print('开始下载： ' + save_name)
        download_pmid(data, save_name)

def ask_for_pmid_path():
    Fpath = filedialog.askopenfilename()
    return (Fpath)

def import_and_show_pmid_path():
    f_path = ask_for_pmid_path()        #获取导入地址
    data = {  # 先完善表单内容
        'request': 'undefined'
    }
    pmid_list = import_pmid(f_path)


def import_pmid(file_path):
    f = open(file_path, 'r')
    empty_list = list(f)
    full_list = []
    n = 0
    for i in empty_list:
        full_list.append(i.rstrip())
        n = n + 1
    print(full_list)
    print('共'+n+'篇文献')
    f.close()
    return full_list

def validateTitle(title):
    rstr = r"[\/\\\:\*\?\"\<\>\|]"
    new_title = re.sub(rstr, "_", title)  # 替换为下划线
    return new_title


def download_pmid(pmid, s_name):
    response = requests.post("https://sci-hub.se/", data=pmid)
    response_tree = lxml.etree.HTML(response.text)  # 把返回的文字东西弄成HTML格式，才能用xpath
    links = response_tree.xpath("""//a[@href="#"]/@onclick""")
    try:
        split_links = links[0].split('?')
        print(split_links)
        split_links2 = split_links[-2].split('/')
        au_year = split_links2[-1][:-4]
        print(au_year)
        title = response_tree.xpath("""//title/text()""")
        print(title)
        split_title = title[0].split('|')
        split_title2 = split_title[1].split('.')[0]
        split_title2 = validateTitle(split_title2)
        print(split_title2)

        edit_links = links[0][15:-1]  # 这是取出的onclick属性，作为一个对象，取出其中的字符串
        download = requests.get(edit_links, stream=True)  # stream 参数可以把文件切片，不是立即下载到内存里，iter才会下载，这样不会内存不足
        s_path = 'C:\\Users\\x1c\\Desktop\\scidownload\\' + au_year + '-' + s_name + '-' + split_title2 + '.pdf'
        f = open(s_path, mode="wb")
        n = 1
        for chunk in download.iter_content(chunk_size=500000):
            if chunk:
                f.write(chunk)
                print('写入中...' + str(n))
                n = n + 1
        f.close()
        print(s_name + '已保存于：' + s_path)
    except(Exception):
        print(save_name + "下载失败")


# r = requests.get('https://sci-hub.se/')
# print(r.status_code)        # 获取返回状态


