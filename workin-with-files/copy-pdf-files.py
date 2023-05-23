import os
import glob
import shutil

current_path = os.path.dirname(os.path.realpath(__file__))

print("Укажите путь к папке, из которой скопировать файлы\n(по умолчанию директория скрипта)")
host_dir_path = input()
if not host_dir_path:
    host_dir_path = current_path

print("Укажите расширение файлов, которые нужно скопировать\n(по умолчанию pdf)")
file_extension = input()
if not file_extension:
    file_extension = 'pdf'

print("Укажите путь к папке, в которую выполнить копирование\n(по умолчанию каталог _new, в директории скрипта")
new_dir_path = input()
if not new_dir_path:
    new_dir_path = os.path.join(host_dir_path, '_new')

all_pdf_files = glob.glob(os.path.join(host_dir_path, '**\*.' + file_extension) , recursive=True)

#Создание новой директории для копирования туда файлов
if not os.path.exists(new_dir_path):
    os.mkdir(new_dir_path)

#Копирование файлов pdf
counter = 0
for e in all_pdf_files:
    new_file_path = os.path.join(new_dir_path, e.split('\\')[-1])
    if not os.path.exists(new_file_path):
        shutil.copy(e, new_file_path)
        counter +=1

print(f"Скрипт закончил работу, скопировано {counter} файлов")
input()