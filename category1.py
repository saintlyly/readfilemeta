import csv


def path_to_category(filepath):
    # 以"/"分隔文件路径
    path_list = filepath.split("/")
    # 初始化ID、Name和ParentID
    ID = 0
    Name = ''
    ParentID = None
    # 存储节点信息的列表
    result = []
    # 循环遍历每个节点
    for i in range(len(path_list)):
        # 如果节点名不为空，则作为Name
        if path_list[i] != '':
            ID += 1
            Name = path_list[i]
            # 第一个节点的ParentID为Null
            if i == 0:
                ParentID = None
            else:
                ParentID = ID - 1
            # 将节点信息加入列表中
            result.append([ID, Name, ParentID])
    # 返回节点信息列表
    return result


filepath = '/Volumes/资料数据/资料数据/中医250G/75-赠品6 中药材图片/1-解表药'
result = path_to_category(filepath)


def save_to_csv(filepath, result):
    # 设置csv文件的列名
    fields = ['ID', 'Name', 'ParentID']
    # 打开csv文件并写入数据
    with open(filepath, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(fields)
        for row in result:
            writer.writerow(row)


save_to_csv('result.csv', result)
