import os

def file_sizes(path):
    files_stat = [0, 0, 0]
    for i_elem in os.listdir(path):
        if os.path.isfile(os.path.abspath(os.path.join(path, i_elem))):
            file_path = os.path.abspath(os.path.join(path, i_elem))
            file_size = os.path.getsize(file_path)
            files_stat[0] += file_size/1024
            files_stat[1] += 1
        else:
            result = file_sizes(os.path.abspath(os.path.join(path, i_elem)))
            files_stat[0] += result[0]
            files_stat[1] += result[1]
            files_stat[2] += 1
    return files_stat


directory_path = input("Введите путь до каталога: ")
size, files, dirs = file_sizes(directory_path)
print(f"Размер каталога (в Кбайтах): {size}")
print(f"Количество подкаталогов: {dirs}")
print(f"Количество файлов: {files}")
