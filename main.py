# -*- coding: utf-8 -*-
import os
import pandas as pd
import requests
import json

def main():
    folder_name = "document"
    
    # 检查文件夹是否存在
    if not os.path.exists(folder_name):
        # 如果不存在，创建文件夹
        os.makedirs(folder_name)
        print(f'文件夹 "{folder_name}" 已创建.')
    else:
        print(f'文件夹 "{folder_name}" 已存在.')
    
    # 列出文件夹中的所有Excel文件
    print(f'文件夹 "{folder_name}" 中的Excel文件：')
    for filename in os.listdir(folder_name):
        if filename.endswith(".xlsx") or filename.endswith(".xls"):
            print(filename)
            df = pd.read_excel(os.path.join(folder_name, filename))
            
            # 使用你提供的接口对每个文件的内容进行分析
            for index, row in df.iterrows():
                data = {
                    "model": "llama3",
                    "prompt": str(row)
                }
                response = requests.post("http://localhost:11434/api/generate", data=json.dumps(data))
                print(response.json())

if __name__ == "__main__":
    main()
