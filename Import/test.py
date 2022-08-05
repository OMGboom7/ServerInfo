import GetPassword

info = GetPassword.get_yaml_data('config.yaml')
# print(info['server1'])
# print(list(info))
server_num = len(info)
for i in list(info):
    # print(info[i])
    # print(list(info[i].keys()))
    # print(list(info[i].values()))
    keys = list(info[i].keys())
    values = list(info[i].values())

print(values[0])
# for i in len(info):
num = type(values[0])
print(num)