import os
import csv
from PIL import Image
# 遍历指定文件夹中的所有图片文件，获取文件名、大小、尺寸、格式和类型，并将这些信息写入到CSV文件中
# 指定文件夹路径和CSV文件路径
# folder_path = "/Volumes/资料数据/高清实拍素材/1.精典元素实拍Our classic elements"
folder_path = "/Volumes/资料数据/资料数据/中医250G/75-赠品6 中药材图片/1-解表药/"
# 将文件夹路径转换为绝对路径
folder_path = os.path.abspath(os.path.expanduser(folder_path))

# 创建CSV文件并写入表头
with open('file_list2.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["文件名", "文件大小", "图片尺寸", "图片格式", "图片类型"])

    # 遍历文件夹中的所有文件
    for filename in os.listdir(folder_path):
        # 判断文件是否为图片文件
        if filename.endswith(".png") or filename.endswith(".jpg") or filename.endswith(".jpeg"):
            # 获取文件的完整路径
            file_path = os.path.join(folder_path, filename)

            # 获取文件大小
            file_size = os.path.getsize(file_path)

            # 获取文件名称
            file_name = os.path.basename(file_path)

            # 打开图片文件并获取图片信息
            with Image.open(file_path) as img:
                # 获取图片尺寸
                img_width, img_height = img.size

                # 获取图片格式和类型
                img_format = img.format
                img_mode = img.mode

            # 将文件信息写入CSV文件
            with open("file_list2.csv", "a", newline="") as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow([file_name, file_size, "{}x{}".format(
                    img_width, img_height), img_format, img_mode])
