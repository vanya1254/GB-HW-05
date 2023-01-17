# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.
# aaaaabbbcccc -> 5a3b4c
# 5a3b4c -> aaaaabbbcccc

def read_txt(name_txt):
    with open(f'{name_txt}', 'r') as data:
        return data.read()

    
def write_txt(name_txt, string):
    with open(f'{name_txt}', 'w') as data:
        data.write(string)


def rle_compress_string_to_list(string):
    rle_list = []
    count = 1
    
    for i in range(len(string) - 1):
        if string[i] == string[i + 1]:
            count += 1
            if i + 1 == len(string) - 1:
                rle_list.append([f'{count}', string[i]])
        else:
            rle_list.append([f'{count}', string[i]])
            count = 1
    if rle_list[-1][-1] != string[len(string) - 1]:
        rle_list.append(['1', string[len(string) - 1]])
    
    return rle_list


def rle_list_to_string(rle_list):
    rle_string = ''
    
    for i in range(len(rle_list)):
        rle_string += ''.join(rle_list[i])
        
    return rle_string


def rle_string_to_string(rle_string):
    string = ''
    
    for i in range(0, len(rle_string) - 1, 2):
        string += int(rle_string[i]) * rle_string[i + 1]
    
    return string


string_txt = read_txt('input.txt')

if not string_txt[0].isdigit():
    list_rle = rle_compress_string_to_list(string_txt)
    string_rle = rle_list_to_string(list_rle)
    write_txt('output.txt', string_rle)
    # print(string_rle)
else:
    string_not_rle = rle_string_to_string(string_txt)
    write_txt('output.txt', string_not_rle)
    # print(string_not_rle)