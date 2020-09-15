import requests
address = 'https://stepic.org/media/attachments/course67/3.6.3/'
with open('/Users/oksana.shumilova/Library/Application Support/JetBrains/PyCharm2020.1/scratches/dataset_3378_3.txt', 'r') as dtaset:
    n = dtaset.readline().strip() # тут в файле ссылка целиком

r = requests.get(str(n)) # тут уже только название файла

ending = r # записать в ending значение названия файла
while True:
    new_r = requests.get(address + ending.text) # вызвать к новому файлу и записать результат в переменную, этот рез исп в след вызове
    ending = new_r # тут надо обнулить ending / перезаписать в него новое значение
    # print(ending.text)
    if new_r.text.startswith('We '):
        print(new_r.text)
        break