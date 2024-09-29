import json

# 纠正被打乱的UV点序

f = open("new_UV_data.txt",'r',encoding='utf-8')
uv_lines = f.readlines()

# 头部模型
head = open('../0_source_obj/3DScan_head.obj','r',encoding='utf-8')
head_lines= head.readlines()

temp = open("3DScan_UV_manual_corrected.obj",'r',encoding='utf-8')
err_head_lines = temp.readlines()

order_err_uv_data = open("new_UV_data.txt",'r',encoding='utf-8')
err_uv_data = order_err_uv_data.readlines()

my_map = {}
output = [None for _ in range(11692)]

for index, line in enumerate(head_lines):
    if line.startswith('f '):
        temp, one ,two, three,four = line.strip().split(' ')
        temp1 , one ,tem2 = one.split('/')
        temp1 , two ,tem2 = two.split('/')
        temp1 , three ,tem2 = three.split('/')
        temp1 , four ,tem2 = four.split('/')

        temp, err_one ,err_two, err_three,err_four = err_head_lines[index].strip().split(' ')
        temp1 , err_one ,tem2 = err_one.split('/')
        temp1 , err_two ,tem2 = err_two.split('/')
        temp1 , err_three ,tem2 = err_three.split('/')
        temp1 , err_four ,tem2 = err_four.split('/')

        if one not in my_map:
            output[int(one)-1] = err_uv_data[int(err_one)-1]
            my_map[one] = err_one
        else:
            if not my_map[one]==err_one:
                print(f"index:{index}")
                raise

        if two not in my_map:
            output[int(two)-1] = err_uv_data[int(err_two)-1]
            my_map[two] = err_two
        else:
            if not my_map[two]==err_two:
                print(f"index:{index}")
                raise

        if three not in my_map:
            output[int(three)-1] = err_uv_data[int(err_three)-1]
            my_map[three] = err_three
        else:
            if not my_map[three]==err_three:
                print(f"index:{index}")
                raise

        if four not in my_map:
            output[int(four)-1] = err_uv_data[int(err_four)-1]
            my_map[four] = err_four
        else:
            if not my_map[four]==err_four:
                print(f"index:{index}")
                raise

f = open("new_UV_data_order_corrected.txt",'w',encoding='utf-8')
f.writelines(output)


# # 辅助处理数据
# f = open("2_wrap4d/new_UV_data.txt",'r',encoding='utf-8')
# lines = f.readlines()

# for index, line in enumerate(lines):
#     # 丢掉y坐标
#     x,y,z = line.split(' ')
#     lines[index] = f'{x} {z}'

# f = open("2_wrap4d/new_UV_data.txt",'w',encoding='utf-8')
# f.writelines(lines)



# # 将UV作为平面
# f = open("3DScan_head_UV.obj",'r',encoding='utf-8')
# lines = f.readlines()

# for index, line in enumerate(lines):
#     if line.startswith("vn "):
#         lines[index] = 'vn 0.000000 1.000000 0.000000\n'
#     elif line.startswith("f "):
#         parts = line.split(' ')
#         node1= parts[1].split('/')
#         node2= parts[2].split('/')
#         node3= parts[3].split('/')
#         if len(parts)>4:
#             node4= parts[4].split('/')
#             lines[index] = f'f {node1[1]}//{node1[2]} {node2[1]}//{node2[2]} {node3[1]}//{node3[2]} {node4[1]}//{node4[2]}\n'
#         else:
#             lines[index] = f'f {node1[1]}//{node1[2]} {node2[1]}//{node2[2]} {node3[1]}//{node3[2]}\n'

# f = open("3DScan_head_UV.obj",'w',encoding='utf-8')
# f.writelines(lines)

# 108 = 3*3*3*2*2
# 2*2*2*3*3



# 求UV上下左右边界
# f = open("VFace_head_no_mouth.obj",'r')
#
# u_points= []
# v_points = []
#
# for line in f:
#     if line.startswith('vt '):
#         temp, u,v = line.split(' ')
#         u_points.append(u)
#         v_points.append(v)
#
# u_points = sorted(u_points)
# v_points= sorted(v_points)
#
# print(u_points[0])
# print(u_points[-1])
# print(v_points[0])
# print(v_points[-1])


# 将3DScan的UV放大
# with open('3DScan_head.obj', 'r', encoding='utf-8') as file:
#     lines = file.readlines()
#
# for index, line in enumerate(lines):
#     if line.startswith('vt '):
#         temp,u,v = line.split(' ')
#         u= format((float(u) -0.013440) * 1.808582116655771 + 0.002020, '.6f')
#         v=format((float(v) -0.570720) * 2.370938176970504 + 0.002040, '.6f')
#         lines[index] = f'vt {u} {v}\n'
#
# # 将修改后的内容写回文件
# with open('3DScan_head.obj', 'w', encoding='utf-8') as file:
#     file.writelines(lines)
#
# 3DScan UV边界
# u：0.013440 ~ 0.564120 0.55068
# v：0.570720 ~ 0.990790 0.42007
# VFace UV边界
# u:0.002020 ~ 0.997970 0.99595
# v:0.002040 ~ 0.998000 0.99596
#
# U=(U -0.013440) * 1.808582116655771 + 0.002020
# V= (V-0.570720) * 2.370938176970504 + 0.002040
