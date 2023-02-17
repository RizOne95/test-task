# Импортируем библиотеки
import json
import tempfile, os
import argparse

# Создаем файл storage.data в temp, при помощи модуля os,
# работы с нашим путем и
# модуль tempfile для создания временного файла.
TEMPFILE = os.path.join(tempfile.gettempdir(), 'storage.data')

def main():

    k_v = load_file()
    # Вызываем функцию с переменными key и val
    key, val = parser_args()

    # Прописываем в словарь key и val, так же прибавляет
    # значение к предыдущему, если есть совпадение в ключах
    if key and val:
        k_v[key] = k_v.get(key, list())
        k_v[key].append(val)
        print(k_v[key])
    # Если указан ключ, получим значение ключа.
    elif key:
        for k in k_v[key]:
            print(k)
    else:
        print("Here is no such function")

    # Передаем словарь в dump_file
    bump_file(k_v)

# В функции создаем интерфейс командной строки
def parser_args():

    parser = argparse.ArgumentParser()
    # описывается переменная --key
    parser.add_argument("--key", help='Key')
    parser.add_argument("--val", help='Value')
    # Переменная args. По умолчанию принимает ввод
    args = parser.parse_args()
    # Возвращаем ввод вызванной функции.
    return args.key, args.val

# Функция принимает аргумент и записывает его в файл
def bump_file(k_v):
    with open(TEMPFILE, "w") as v:
        # Сериализуем dump() принимает два аргумента
        # 1 объект данных, который сериализуется
        # 2 файловый объект, в который будут вписаны байты.
        json.dump(k_v, v)

# Функция с исключением, если файл пустой
# # он возвращает список.
def load_file():
    try:
        with open(TEMPFILE, "r") as v:
            # Десериализация load().
            # Превращаят кодированные данные json в объект python.
            k_v = json.load(v)
    except IOError:
        k_v = {}

    return k_v

if __name__ == "__main__":
    main()