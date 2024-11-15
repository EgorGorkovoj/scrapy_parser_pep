# Асинхронный парсер PEP на Scrapy

## Описание проекта:
Этот проект собирает информацию о Python используя фреймворк Scrapy, предоставляя комплексный обзор нововведений, версий и статуса разработки.
## Цель проекта:
Предоставление удобного и актуального ресурса для разработчиков, которые хотят быть в курсе последних изменений в языке Python,
а также предложений по его улучшению (PEP).
## Установка
**Клонировать репозиторий и перейти в него в командной строке:**
```
git clone https://github.com/EgorGorkovoj/scrapy_parser_pep.git
cd scrapy_parser_pep
```
**Cоздать и активировать виртуальное окружение:**
```
python -m venv venv
```
* Если у вас Linux/macOS

    ```
    source env/bin/activate
    ```

* Если у вас windows

    ```
    source venv/Scripts/activate
    ```

**Установить зависимости из файла requirements.txt:**
```
python -m pip install --upgrade pip
pip install -r requirements.txt
```
## Краткое руководство по пользованию
**Из директории scrapy_parser_pep ввести команду:**
```
scrapy crawl pep
```
Данная команда спарсит статусы PEP в директорию results/.
**В директории results/ будет 2 файла формата .csv. Например:**
```
pep_2024-11-14T21-01-29.csv
status_summary_2024-11-15_00-01-43.csv
```
