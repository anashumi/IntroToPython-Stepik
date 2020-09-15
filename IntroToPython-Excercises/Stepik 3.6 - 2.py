import requests
with open('/Users/oksana.shumilova/Library/Application Support/JetBrains/PyCharm2020.1/scratches/dataset_3378_2.txt', 'r') as dtaset:
    n = dtaset.readline().strip()

r = requests.get(str(n))
print(len(r.text.splitlines()))