from hashlib import md5


# with open('result.json', 'r', encoding='utf-8') as f:
#     readline = f.readlines()
# for str in readline:
#     data = md5(str.encode())
#     hash = data.hexdigest()
#     print(hash)


def my_gen(file):
    with open(file, 'r', encoding='utf-8') as f:
        read_line = f.readlines()
        number_str = 0
    while number_str < len(read_line):
        data = md5(read_line[number_str].encode())
        hash_1 = data.hexdigest()
        print(f'Хэш строки № {number_str} = {hash_1}')
        yield number_str
        number_str += 1
    return None


for string in my_gen('result.json'):
    my_gen('result.json')


