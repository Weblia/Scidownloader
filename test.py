# -*- coding: utf-8 -*-
# Sci自动下载

s_name = '123153141'
s_path = 'C:\\Users\\x1c\\Desktop\\scidownload\\'+s_name
import requests
import lxml.etree
import re
from tkinter import filedialog

Fpath = filedialog.askopenfilename()
print(Fpath)

