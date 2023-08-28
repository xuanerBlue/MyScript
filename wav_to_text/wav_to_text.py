import wave
import numpy as np
import binascii

# 打开 WAV 文件
wav = wave.open("src_file/flash_1k.wav", "r")

# 读取 PCM 数据
pcm_data = wav.readframes(wav.getnframes())

# 将 PCM 数据转换为 NumPy 数组
pcm_array = np.frombuffer(pcm_data, dtype=np.int16)

# 创建一个 C 语言数组的开头和结尾
c_array_str = "int32_t pcm_data[] = {\n"

# 初始化计数器
counter = 0

# 将每个样本转换为十六进制字符串，并添加到 C 语言数组字符串中
for sample in pcm_array:
    # 将样本转换为 bytes 对象
    orig_bytes = sample.tobytes()

    # 交换高字节和低字节
    swapped_bytes = bytes([orig_bytes[1], orig_bytes[0]])

    hex_sample = binascii.hexlify(swapped_bytes).decode()
    c_array_str += "0x" + hex_sample + ","
    counter += 1
    if counter % 20 == 0:
        c_array_str += "\n"

# 添加 C 语言数组的结尾
c_array_str += "};\n"

# 在 C 语言数组字符串的末尾添加一个注释，记录数组中的元素数量
c_array_str += f"// The array pcm_data contains {counter} elements.\n"

# 将 C 语言数组保存为文本文件
with open("dest_file/flash_1k.c", "w") as f:
    f.write(c_array_str)