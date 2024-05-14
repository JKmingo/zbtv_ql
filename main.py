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
    repo_dir = "ZBTV"
    
    repo_path = os.path.join(base_path, repo_dir)
    
    # 检查本地仓库是否存在
    if not os.path.exists(repo_dir):
        # 如果本地仓库不存在，则执行 git clone
        subprocess.run(["git", "clone", repo_url])
    else:
        # 如果本地仓库存在，则执行 git pull
        os.chdir(repo_path)  # 切换到仓库目录
        subprocess.run(["git", "pull"])

    os.chdir(repo_path)
    exec(open(os.path.join(repo_path, "main.py")).read())
