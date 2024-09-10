import json
import pandas as pd
import os


file_path = 'bd.xlsx'
df = pd.read_excel(file_path)

search_client = input('Enter Client: ')

json_data = df.to_json(orient='records')

# Создание json файла из XLSX
with open('data.json', 'w') as json_file:
    json_file.write(json_data)

# Считывание этого JSON файла
with open('data.json', 'r') as json_file:
    data_dict = json.load(json_file)

# Заполнение пустых полей клиента
for step in range(len(data_dict)):
    if data_dict[step]['Client'] == None:
        data_dict[step]['Client'] = data_dict[step-1]['Client']

# Создание отфильтрованного JSON
json_data = json.dumps([item for item in data_dict if item['Client'] == search_client], indent=4, ensure_ascii=False)

# Сохранение нужного клиента в отдельный JSON
with open('ans.json', 'w', encoding='utf-8') as json_file:
    json.dump(json_data, json_file, indent=4, ensure_ascii=False)

# Вывод в консоль
print(json_data)

os.system("pause")
