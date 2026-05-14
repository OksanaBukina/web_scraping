import pandas as pd
from bs4 import BeautifulSoup 
import requests as rq
import sqlite3 as sql
from bs4 import MarkupResemblesLocatorWarning
import warnings

warnings.filterwarnings("ignore", category=MarkupResemblesLocatorWarning)

url = 'https://web.archive.org/web/20230902185655/https://en.everybodywiki.com/100_Most_Highly-Ranked_Films'

file = "top_50_films.csv"
db_name = 'Movies.db'
table_name = 'Top_50'
count = 0 
df = pd.DataFrame(columns=["Average Rank","Film","Year"])

html_page = rq.get(url).text
data =BeautifulSoup(html_page, 'html.parser')

tables = data.find('tbody')
#tables = data.find_all(class_='wikitable')
#print("Найдено таблиц:", len(tables))
rows = tables.find_all('tr')  # Извлекаем все tr  строки из 1 таблицы [0]

for r in rows:
    if count <50:
        col = r.find_all('td') # Извлекаем все td (ячейки) из текущей строки
        if len(col) !=0 :   # Проверяем, что строка не пуста и не заголовок
                  
            data_films = {"Average Rank":int(col[0].contents[0]), # Создаём словарь с данными из ячеек
                          "Film":str(col[1].contents[0]), #получить вложенный текст из тега (<td>1994</td> → 1994)
                          "Year":int(col[2].contents[0])}
            # создаем словарь- табличку(DataFrame) с одной строкой и тремя столбцами
            # Преобразование словаря в датафрейм и объединение его с существующим
            # данные продолжают добавляться в датафрейм с каждой итерацией цикла
            df1 = pd.DataFrame(data_films, index =[0]) 
            df = pd.concat([df,df1],ignore_index=True) #конкатенация двух БД
            count+=1
    else:
        break

print(df)
df.to_csv(file)
#соединение с базой данных  
conn = sql.connect(db_name)
#сохранить датафрейм в виде таблицы, а затем закрыть соединение.
df.to_sql(table_name,conn,if_exists='replace', index=False)
conn.close()
