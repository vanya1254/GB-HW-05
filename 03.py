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
    

string_txt = read_txt('input.txt')

list_rle = rle_compress_string_to_list(string_txt)
string_rle = rle_list_to_string(list_rle)

write_txt('output.txt', string_rle)