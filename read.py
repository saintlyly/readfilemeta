import os
import csv
from PIL import Image

# 文件夹路径
folder_path = '/Volumes/资料数据/108套别墅新农村自建房图纸'

# 将文件夹路径转换为绝对路径
folder_path = os.path.abspath(os.path.expanduser(folder_path))

# 打开CSV文件
with open('read1.csv', 'w', newline='') as f:
    # 创建CSV写入器
    writer = csv.writer(f)

    # 获取文件夹中的所有文件
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            # 获取文件名称和路径
            file_name = os.path.splitext(file)[0]
            file_path = os.path.join(root, file)
            file_size = os.path.getsize(file_path)
            file_format = os.path.splitext(file)[1]

            # 获取图片尺寸
            try:
                with Image.open(file_path) as img:
                    img_size = img.size
            except:
                img_size = 'N/A'
            # 将文件名称和路径保存到CSV文件中
            rel_path = os.path.relpath(file_path, folder_path)
            writer.writerow(
                [file_name, file_path, file_size, file_format, img_size])
