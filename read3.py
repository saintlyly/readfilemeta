import os
import csv


def get_file_size(file_path):
    """
    获取文件大小,单位为MB
    """
    size = os.path.getsize(file_path) / 1024 / 1024
    return round(size, 2)


def get_file_info(file_path):
    """
    获取文件信息：文件名、文件类型、文件大小
    """
    file_name = os.path.basename(file_path)
    file_type = os.path.splitext(file_name)[1]
    file_size = get_file_size(file_path)
    return file_name, file_type, file_size


def get_files_info(dir_path):
    """
    获取文件夹中所有文件的数据，返回文件数据和分类信息
    """
    files_data = []
    categories_csv = []
    for root, dirs, files in os.walk(dir_path):
        for file_name in files:
            file_path = os.path.join(root, file_name)
            file_info = get_file_info(file_path)
            file_data = {
                "path": file_path,
                "name": file_name,
                "type": file_info[1],
                "size": file_info[2],
                "category": [os.path.abspath(dir_path)] + os.path.relpath(root, dir_path).split(os.sep)
            }
            files_data.append(file_data)
            # 获取分类信息
            for i, category_name in enumerate(file_data["category"]):
                if i == 0:
                    continue  # 跳过根目录
                parent_name = file_data["category"][i - 1] if i > 1 else ""
                category = {"name": category_name, "parent": parent_name}
                if category not in categories_csv:
                    categories_csv.append(category)
    return files_data, categories_csv


# 示例
dir_path = "/Volumes/资料数据/高清实拍素材/1.精典元素实拍Our classic elements"
files_data, categories_csv = get_files_info(dir_path)

# 保存数据到CSV文件中
with open("files_data.csv", mode="w", newline="") as csv_file:
    fieldnames = ["path", "name", "type", "size", "category"]
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

    writer.writeheader()
    for file_data in files_data:
        writer.writerow(file_data)

# 保存分类信息到CSV文件中
with open("categories.csv", mode="w", newline="") as csv_file:
    fieldnames = ["name", "parent"]
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

    writer.writeheader()
    for category in categories_csv:
        writer.writerow(category)
