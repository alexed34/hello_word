import os


def count_lines_fail(path):
    with open(path, 'r', encoding='utf8', errors='ignore') as f:
        file = f.read()
    return file.count('\n')




dir_name = r'C:\Users\asus\PycharmProjects\hello_word\BigBookPythonResources'
test = os.listdir(dir_name)
cont_dict = {}
for name in test[3:]:
    counter = count_lines_fail(name)
    cont_dict[name] = counter
ddict = sorted(cont_dict, key=cont_dict.get)
# print(ddict)
# print(cont_dict)
for i in ddict:
    with open('2_list.txt', 'a') as f:
        f.write(f'{i} - {cont_dict[i]}\n')
    print(f'{i} - {cont_dict[i]}')

