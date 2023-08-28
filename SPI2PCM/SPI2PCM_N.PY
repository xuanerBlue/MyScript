
import csv
import numpy as np

hex_data = []  # 存储16进制数据的列表

with open('src_file/02_single_hz.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        if len(row) >= 5:
            hex_value = row[4]
            # print(hex_value)
            hex_value = int(hex_value.split('0x')[1],16)
            hex_data.append(hex_value)
# hex_data = np.array(hex_data,dtype = np.int16)
print(hex_data)

# for i in range(len(hex_data)-len(hex_data)%4 -4):
#     # print(i)
#     hex_data[i],hex_data[i+2] = hex_data[i+2], hex_data[i]
#     hex_data[i+2], hex_data[i+4] = hex_data[i+4],hex_data[i+2]
#     i +=4;

import wave

filename = "dest_file/02_single_hz.pcm"  # 输出文件名

with wave.open(filename, 'w') as pcm_file:
    pcm_file.setnchannels(1)  # 单声道
    pcm_file.setsampwidth(2)  # 2 字节（16 位）
    pcm_file.setframerate(16000)  # 采样率为 44100 Hz
    pcm_file.writeframes(bytes(hex_data))