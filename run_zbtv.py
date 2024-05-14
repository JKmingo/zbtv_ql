# -*- coding: utf-8 -*
'''
定时自定义
0 0 5 * * * run_zbtv.py
new Env('IPTV组播源');
'''

import os
import subprocess
import time
import shutil


if __name__ == '__main__':
    # Git 仓库地址
    repo_url = "https://github.com/JKmingo/ZBTV.git"
    # 本地仓库目录
    base_path = os.getcwd()
    repo_dir = "ZBTV"
    repo_path = os.path.join(base_path, repo_dir)
    subprocess.run(["git", "clone", repo_url, repo_dir])
    time.sleep(2)
    all_files = os.listdir(repo_path)
    for file in all_files:
        file_path = os.path.join(repo_path, file)
        if os.path.isdir(file_path):
            continue
        if os.path.exists(os.path.join(base_path, os.path.basename(file_path))):
            # 如果存在，先删除同名文件
            os.remove(os.path.join(base_path, os.path.basename(file_path)))
        shutil.move(file_path, base_path, overwrite=True)
    shutil.rmtree(repo_path)
    exec(open("main.py").read())
    
