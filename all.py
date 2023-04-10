import os
import csv
import random

# 遍历文件夹及其子文件夹内的文件，获取文件名、大小、类型等信息


def read_folder(folder_path, category_dict):
    file_list = []
    for root, dirs, files in os.walk(folder_path):
        category_id = category_dict[root]
        for file in files:
            file_path = os.path.join(root, file)
            file_name, file_ext = os.path.splitext(file)
            file_size = os.path.getsize(file_path)
            file_type = file_ext[1:].upper() if file_ext else 'UNKNOWN'
            file_list.append([file_name, file_type, file_size, category_id])
        if not files and not dirs:
            parent_dir = os.path.dirname(root)
            parent_id = category_dict.get(parent_dir, None)
            category_list[parent_id][1] = os.path.basename(root)  # 处理空文件夹
    return file_list

# 根据文件夹及其路径生成类目结构，包括id，name，parent_id，path


def generate_category(folder_path):
    category_list = []
    category_dict = {}
    category_id = 0
    for root, dirs, files in os.walk(folder_path):
        path_list = root.split(os.sep)
        for i in range(len(path_list)):
            path = os.sep.join(path_list[:i+1])
            parent_id = category_dict.get(os.sep.join(path_list[:i]), None)
            category_name = path_list[i] if i == 0 else os.path.basename(
                os.path.normpath(path))  # 处理类目名
            if path not in category_dict:
                category_dict[path] = category_id
                is_hot = random.choice([True, False])  # 随机设置是否热门
                category_list.append(
                    [category_id, category_name, parent_id, is_hot, path])
                category_id += 1
    return category_list, category_dict

# 将生成的数据保存到csv文件中


def save_to_csv(file_list, category_list):
    with open('file_table.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['ID', 'name', 'type', 'size', 'category_id'])
        for i, row in enumerate(file_list):
            writer.writerow([i, row[0], row[1], row[2], row[3]])
    with open('category_table.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['id', 'name', 'parent_id', 'is_hot', 'path'])
        for row in category_list:
            writer.writerow(row)


# 测试代码
folder_path = '/Volumes/资料数据/108套别墅新农村自建房图纸'
category_list, category_dict = generate_category(folder_path)
file_list = read_folder(folder_path, category_dict)
save_to_csv(file_list, category_list)
