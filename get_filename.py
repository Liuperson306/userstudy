import os

# folder_list = {
#     "user_study/BIWI/codetalk",
#     "user_study/BIWI/faceformer",
#     "user_study/BIWI/gt",
#     "user_study/BIWI/meshtalk",
#     "user_study/BIWI/voca",
#     "user_study/VOCASET/codetalk",
#     "user_study/VOCASET/faceformer",
#     "user_study/VOCASET/gt",
#     "user_study/VOCASET/meshtalk",
#     "user_study/VOCASET/voca"
# }

# Ours vs. VOCA 
# Ours vs. MeshTalk 
# Ours vs. FaceFormer 
# Ours vs. codetalk
# Ours vs. GT

# for folder_path in folder_list:
#     # 获取文件夹中的文件名列表
#     file_names = os.listdir(folder_path)
#     # 确定文本文件的路径：如BIWI_codetalk
#     txt_file_name = "_".join(folder_path.split("/")[1:])
#     # txt文件路径
#     txt_file_path = fr"filename/{txt_file_name}.txt"
#     # 打开txt文件并写入文件名
#     with open(txt_file_path, 'w') as txt_file:
#         for file_name in file_names:
#             txt_file.write(folder_path + '/' + file_name + '\n')

# folder_list = {
#     "user_study/BIWI/voca",
#     "user_study/BIWI/meshtalk",
#     "user_study/BIWI/faceformer",
#     "user_study/BIWI/codetalk",
#     "user_study/BIWI/gt",
#     "user_study/VOCASET/voca",
#     "user_study/VOCASET/meshtalk",
#     "user_study/VOCASET/faceformer",
#     "user_study/VOCASET/codetalk",
#     "user_study/VOCASET/gt",
# }


# Ours vs. VOCA 
# Ours vs. MeshTalk 
# Ours vs. FaceFormer 
# Ours vs. codetalk
# Ours vs. GT
folder_list = [
    "BIWI_voca.txt",
    "BIWI_meshtalk.txt",
    "BIWI_faceformer.txt",
    "BIWI_codetalk.txt",
    "BIWI_gt.txt",
    "VOCASET_voca.txt",
    "VOCASET_meshtalk.txt",
    "VOCASET_faceformer.txt",
    "VOCASET_codetalk.txt",
    "VOCASET_gt.txt"
]

output_file = "filenames.txt"  # 存储行的输出文件
num_lines = 3  # 每个文件需要提取的行数

# 清空或创建输出文件
with open(output_file, 'w') as f:
    pass

for j in range(10):
    # 循环处理每个文本文件
    for txt_name in folder_list:
        # 读取指定范围的行
        with open('filename/' + txt_name, 'r') as f:
            print(f'读取第{j*num_lines}行')
            lines = f.readlines()[j*num_lines : (j+1)*num_lines]
            print(lines)

        # 将提取的行追加到输出文件中
        with open(output_file, 'a') as f:
            f.writelines(lines)



