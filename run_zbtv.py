# -*- coding: utf-8 -*
'''
定时自定义
0 5 * * * main.py
new Env('IPTV组播源');
'''

import os
import subprocess


if __name__ == '__main__':
    # Git 仓库地址
    repo_url = "https://github.com/JKmingo/ZBTV.git"
    # 本地仓库目录
    base_path = os.getcwd()
    repo_dir = "."
    repo_path = os.path.join(base_path, repo_dir)
    subprocess.run(["git", "clone", repo_url])
    exec(open("main.py").read())
    