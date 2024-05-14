import os
import subprocess


if __name__ == '__main__':
    # Git 仓库地址
    repo_url = "https://github.com/JKmingo/ZBTV.git"
    # 本地仓库目录
    repo_dir = "ZBTV"
    # 检查本地仓库是否存在
    if not os.path.exists(repo_dir):
        # 如果本地仓库不存在，则执行 git clone
        subprocess.run(["git", "clone", repo_url])
    else:
        # 如果本地仓库存在，则执行 git pull
        os.chdir(repo_dir)  # 切换到仓库目录
        subprocess.run(["git", "pull"])

    os.chdir(repo_dir)
    exec(open(os.path.join(repo_dir, "main.py")).read())
