import json


# 新UV数据
data = open("new_UV_data_order_corrected.txt",'r',encoding='utf-8')
# 剪过一刀，将头部UV分离出来后的全身模型
body_cuted = open('../0_source_obj/3DScan_cut_head_uv.obj','r',encoding='utf-8')
# 头部模型
head = open('../0_source_obj/3DScan_head.obj','r',encoding='utf-8')

data_lines = data.readlines()
body_cuted_lines = body_cuted.readlines()
head_lines= head.readlines()

body_vts = []
head_vts = []

for index , line in enumerate( body_cuted_lines):
    if line.startswith('vt '):
        body_vts.append(line)

for index , line in enumerate(head_lines):
    if line.startswith('vt '):
        head_vts.append(line)

output={}
border_new_index_list=[
    # 5330,
    # 5333,
    # 5348,
    # 5352,
    # 5355,
    # 5360,
    # 5363,
    # 5366,
    # 5369,
    # 5372,
    # 5375,
    # 5378,
    # 5381,
    # 5384,
    # 5438,
    # 5448,
    # 5449,
    # 5465,
    # 5469,
    # 5470,
    # 5483,
    # 5490,
    # 5491,
    # 5501,
    # 5505,
    # 5518,
    # 5787,
    # 5789,
    # 5806,
    # 5807,
    # 5812,
    # 5815,
    # 5817,
    # 5819,
    # 5822,
    # 5825,
    # 5827,
    # 5830,
    # 5834,
    # 5837,
    # 5840,
    # 5843,
    # 5907,
    # 5920,
    # 5936,
    # 5943,
    # 5953,
    # 5957,
    # 5967,
    # 5971,
    11631,
    11632,
    11633,
    11634,
    11635,
    11636,
    11637,
    11638,
    11639,
    11640,
    11641,
    11642,
    11643,
    11644,
    11645,
    11646,
    11647,
    11648,
    11649,
    11650,
    11651,
    11652,
    11653,
    11654,
    11655,
    11656,
    11657,
    11658,
    11659,
    11660,
    11661,
    11662,
    11663,
    11664,
    11665,
    11666,
    11667,
    11668,
    11669,
    11670,
    11671,
    11672,
    11673,
    11674,
    11675,
    11676,
    11677,
    11678,
    11679,
    11680,
    11681,
    11682,
    11683,
    11684,
    11685,
    11686,
    11687,
    11688,
    11689,
    11690,
    11691,
]

for new_index , uv_line in enumerate(head_vts):
    old_index = body_vts.index(uv_line)

    # # 找出重合点
    # if body_vts.count(uv_line) >1:
    #     print(new_index)

    # 新切出来的下边界有些点被归为上面的UV shell，有些点被归为下面的UV shell
    if new_index in border_new_index_list:
        old_index = body_vts.index(uv_line,old_index+1) # 查找第二次出现的位置作为old_index

    temp, old_u,old_v = uv_line.strip().split(' ')

    new_u,new_v = data_lines[new_index].strip().split(' ')

    output[str(old_index)]= {
        "old_u": old_u,
        "old_v": old_v,
        "new_u": new_u,
        "new_v": new_v,
        "new_index": new_index
    }

f = open("final_output.json",'w',encoding='utf-8')
json.dump(output,f)
f.close()



# 剪过一刀，将头部UV分离出来后的全身模型
body_cuted = open('../0_source_obj/3DScan_cut_head_uv.obj','r',encoding='utf-8')
# body_cuted = open('1_source_data/3DScan_cut_head_uv_temp.obj','r',encoding='utf-8')
body_cuted_lines = body_cuted.readlines()

# 将UV整体右移1
for index, line in enumerate(body_cuted_lines):
    if line.startswith('vt '):
        temp , u, v = line.split(' ')
        u = str(int(u[:1])+1) + u[1:]
        body_cuted_lines[index] = f'vt {u} {v}'

with open('final_output.json', 'r') as json_file:
    uv_data = json.load(json_file)

offset = 32083-1

for old_index ,data in uv_data.items():
    
    temp, old_u, old_v = body_cuted_lines[int(old_index)+ offset].strip().split(' ')
    # print(old_u, old_v)
    # break
    # if old_u == data["old_u"] and old_v == data["old_v"]:
        # print('processsing')
    body_cuted_lines[int(old_index)+ offset] = f'vt {data["new_u"]} {data["new_v"]}\n'

f = open("3DScan_processed.obj",'w',encoding='utf-8')
f.writelines(body_cuted_lines)
