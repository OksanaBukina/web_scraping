# Web Scraping + Pandas + SQLite (Учебная памятка)

Учебный проект по основам **web scraping** на Python.  
Для тех, кто изучает тему или хочет быстро вспомнить основы.

## Что делает проект

Скрипт:

1. Получает HTML-страницу из интернета (`requests`)
2. Парсит HTML (`BeautifulSoup`)
3. Извлекает таблицу с фильмами
4. Собирает данные в `DataFrame` (`pandas`)
5. Сохраняет данные в CSV
6. Записывает данные в SQLite базу

Источник данных: список наиболее высоко оценённых фильмов.

---

## Используемые библиотеки

```python
import pandas as pd
from bs4 import BeautifulSoup
import requests as rq
import sqlite3 as sql


Для чего каждая библиотека:
requests	-> Получение HTML со страницы
BeautifulSoup	-> Парсинг HTML
pandas ->	Работа с таблицами (DataFrame)
sqlite3 ->	Работа с локальной SQL-базой
warnings ->	Отключение предупреждений



Запуск -> установить зависимости:

pip install pandas beautifulsoup4 requests
python main.py

