import yaml


def get_yaml_data(yaml_file):
    # print('****** 获取pwd.yaml数据 ******')
    with open(yaml_file, encoding='utf-8') as file:
        content = file.read()
        # print(content)
        # print(type(content))

        # print('\n****** 转换yaml数据为字典或列表 ******')
        # 设置Loader=yaml.FullLoader忽略YAMLLoadWarning警告
        data = yaml.load(content, Loader=yaml.FullLoader)
        # print(data)
        # print(type(data))
        return data

        # lists = list(data)
        # return lists


if __name__ == "__main__":
    get_yaml_data("config.yaml")
