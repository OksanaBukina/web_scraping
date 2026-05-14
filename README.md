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
