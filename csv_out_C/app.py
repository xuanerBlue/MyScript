import pandas as pd
import re

def extract_hex_codes(filename):
    df = pd.read_csv(filename)

    # 提取第5列
    fifth_col = df.iloc[:, 4]

    # 使用正则表达式匹配16进制数，包括"0x"前缀
    hex_codes = [x for x in fifth_col if re.match(r'^0x[0-9a-fA-F]+$', str(x))]


    # 格式化为C语言数组
    # 格式化为C语言数组，每10个元素添加一个换行符
    c_array = 'short int hex_codes[] = {\n'
    for i in range(len(hex_codes)):
        if i > 0 and i % 10 == 0:
            c_array += '\n'
        c_array += hex_codes[i] + ', '
    c_array = c_array.rstrip(', ') + '\n};'
    
    # 计算数组大小
    array_size = len(hex_codes)
    c_array += '\n#define ARRAY_SIZE ' + str(array_size)

    # 将C语言数组写入文件
    with open('dest_file/DSP_Decode_1.c', 'w') as f:
        f.write(c_array)

# 测试函数
extract_hex_codes('src_file/DSP_Decode_1.csv')