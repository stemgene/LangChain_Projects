import os


env_vars = os.environ

# 打印环境变量及其值
for key, value in env_vars.items():
    print(f"{key}: {value}")
