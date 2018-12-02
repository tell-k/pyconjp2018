import os
import sys

# 1. 親プロセスが実行
if os.fork():  # 2. 子プロセス生成
   sys.exit(0) # 3. 親は終了

# ここからは子プロセスしか実行しない
os.setsid()

if os.fork(): # 2. 子プロセス生成
   sys.exit(0) # 3. 親は終了
