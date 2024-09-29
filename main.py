import json

# 剪过一刀，将头部UV分离出来后的全身模型
body_cuted = open('3DScan_cut.obj','r',encoding='utf-8')
body_cuted_lines = body_cuted.readlines()

# 将UV整体右移1
for index, line in enumerate(body_cuted_lines):
    if line.startswith('vt '):
        temp , u, v = line.split(' ')
        u = str(int(u[:1])+1) + u[1:]
        body_cuted_lines[index] = f'vt {u} {v}'

with open('final_uv_data.json', 'r') as json_file:
    uv_data = json.load(json_file)

offset = 32083-1

for old_index ,data in uv_data.items():
    
    temp, old_u, old_v = body_cuted_lines[int(old_index)+ offset].strip().split(' ')
    body_cuted_lines[int(old_index)+ offset] = f'vt {data["new_u"]} {data["new_v"]}\n'

f = open("3DScan_processed.obj",'w',encoding='utf-8')
f.writelines(body_cuted_lines)
