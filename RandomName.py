import random

def text(length=8):
    chinese_chars = []
    for i in range(length):
        char_code = random.randint(0x4e00, 0x9fa5)
        chinese_chars.append(chr(char_code))
    return ''.join(chinese_chars)

chinese_text = text(8)
print(f"Name: {chinese_text}")