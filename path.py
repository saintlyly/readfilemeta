import json
import os


def read_directory(directory_path, category_id):
    items = os.listdir(directory_path)
    result = []

    for item in items:
        item_path = os.path.join(directory_path, item)

        if os.path.isdir(item_path):
            children = read_directory(item_path, category_id + '/' + item)
            result.append({
                'name': item,
                'categoryid': category_id,
                'children': children,
            })
        else:
            result.append({
                'name': item,
                'categoryid': category_id,
            })

    return result


directory_path = '/Volumes/资料数据/108套别墅新农村自建房图纸'
category_id = 'root'
data = read_directory(directory_path, category_id)

with open('output.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False)
