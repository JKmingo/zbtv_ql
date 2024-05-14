# -*- coding: utf-8 -*
'''
定时自定义
0 0 5 * * * run_zbtv.py
new Env('IPTV组播源');
'''

import os
import subprocess


if __name__ == '__main__':
    # Git 仓库地址
    repo_url = "https://github.com/JKmingo/ZBTV.git"
    # 本地仓库目录
    base_path = os.getcwd()
    subprocess.run(["git", "clone", repo_url, base_path])
    exec(open("main.py").read())
    
