import re

with open('id.txt','r',encoding='utf-8') as f:
    cnt = f.read()

id_ls = re.findall(r'[:：](.+)\n',cnt)

for i in id_ls:
    print(i)