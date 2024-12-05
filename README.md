# Проект асинхронного парсинга pep
## Описание
Проект предназначен для парсинга актуальной информации о стандартах PEP (номер, название, статус, кол-во)
## Стек технологий
Python, Scrapy
## Функционал парсера
1. Получение списка всех PEP, включая номер, название и статус
2. Получение результирующего списка всех статусов PEP с указанием их кол-ва
## Как установить
### Клонировать репозиторий и перейти в него в командной строке
```
git clone  https://github.com/PotashevIlya/scrapy_parser_pep
```
### Создать и активировать виртуальное окружение
```
python -m venv venv
```
```
source venv/Scripts/activate
```
### Установить зависимости из файла requirements.text
```
python -m pip install --update pip
```
```
pip install -r requirements.txt
```
### Запустить парсинг командой
```
scrapy crawl pep
```
___  
#### Автор проекта:    
:small_orange_diamond: [Поташев Илья](https://github.com/PotashevIlya)
