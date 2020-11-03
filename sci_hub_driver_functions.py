# -*- coding: utf-8 -*-
# 下载sci-hub文献的静态方法

import re
import requests
import lxml


def download_pmid(pmid, s_name, file_dir):
    print('开始请求' + str(pmid))
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
        print(split_title2)
        split_title2 = validatetitle(split_title2)
        print(split_title2)

        edit_links = links[0][15:-1]  # 这是取出的onclick属性，作为一个对象，取出其中的字符串
        download = requests.get(edit_links, stream=True)  # stream 参数可以把文件切片，不是立即下载到内存里，iter才会下载，这样不会内存不足
        s_path = file_dir + '/' + au_year + '-' + s_name + '-' + split_title2 + '.pdf'
        print(s_path)
        f = open(s_path, mode="wb")
        n = 1
        for chunk in download.iter_content(chunk_size=500000):
            if chunk:
                f.write(chunk)
                print('写入中...' + str(n))
                n = n + 1
        f.close()
        print(s_name + '已保存于：' + s_path)
    except():
        print(s_name + "下载失败")


def validatetitle(title):
    rstr = r"[\/\\\:\*\?\"\<\>\|]"
    new_title = re.sub(rstr, "_", title)  # 替换为下划线
    return new_title
