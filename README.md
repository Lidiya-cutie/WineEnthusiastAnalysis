# Wine Enthusiast Analysis

Проект для анализа данных о винах из набора данных Wine Enthusiast.

## О проекте

* на наборе данных из соревнования на *kaggle*.

Допустим, что после просмотра документального фильма о сомелье вы захотели создать прогностическую модель для оценки вин вслепую, как это делает сомелье.

Определив бизнес-задачу, вы перешли к сбору данных для обучения модели. После нескольких недель парсинга сайта [WineEnthusiast](https://www.wineenthusiast.com/) вам удалось собрать около 130 тысяч строк обзоров вин для анализа и обучения.

Вот какие признаки вам удалось собрать:

* **country** — страна-производитель вина.
* **description** — подробное описание.
* **designation** — название виноградника, где выращивают виноград для вина.
* **points** — баллы, которыми WineEnthusiast оценил вино по шкале от 1 до 100.
* **price** — стоимость бутылки вина.
* **province** — провинция или штат.
* **region_1** — винодельческий район в провинции или штате (например Напа).
* **region_2** — конкретный регион. Иногда в пределах винодельческой зоны указываются более конкретные регионы (например Резерфорд в долине Напа), но это значение может быть пустым.
* **taster_name** — имя сомелье.
* **taster_twitter_handle** — твиттер сомелье.
* **title** — название вина, которое часто содержит год и другую подробную информацию.
* **variety** — сорт винограда, из которого изготовлено вино (например Пино Нуар).
* **winery** — винодельня, которая производила вино.

## Структура проекта

- **data/**: Папка для хранения данных.
  - **raw/**: Исходные данные.
  - **processed/**: Обработанные данные.
- **notebooks/**: Папка для Jupyter Notebooks.
- **scripts/**: Папка для скриптов.
  - **data_cleaning.py**: Скрипт для очистки данных.
  - **data_analysis.py**: Скрипт для анализа данных.
  - **utils.py**: Вспомогательные функции.
- **models/**: Папка для хранения моделей.
- **reports/**: Папка для отчетов и визуализаций.
  - **figures/**: Папка для графиков и диаграмм.
- **requirements.txt**: Файл с зависимостями.
- **README.md**: Описание проекта.

## Установка

1. Клонируйте репозиторий:
   ```bash
   git clone https://github.com/yourusername/wine_enthusiast_analysis.git
   cd wine_enthusiast_analysis
   ```

2. Установите зависимости:
   ```bash
   pip install -r requirements.txt
   ```

3. Запустите Jupyter Notebook:
   ```bash
   jupyter notebook
   ```

## Описание зависимостей

1. **pandas**: Для работы с табличными данными (чтение, очистка, анализ).
2. **numpy**: Для численных операций и работы с массивами.
3. **matplotlib**: Для построения графиков и визуализации данных.
4. **seaborn**: Для улучшенной визуализации данных (построение красивых графиков).
5. **jupyter**: Для работы с Jupyter Notebook.
6. **scikit-learn**: Для машинного обучения и анализа данных (если потребуется).
7. **scipy**: Для научных вычислений и статистики.
8. **statsmodels**: Для статистического анализа данных.
9. **openpyxl**: Для работы с Excel-файлами (если данные будут в формате .xlsx).
10. **xlrd**: Для чтения старых Excel-файлов (если потребуется).

## Использование

- **data_cleaning.py**: Очистка данных.
- **data_analysis.py**: Анализ данных и построение графиков.
- **WineEnthusiast.ipynb**: Основной ноутбук для анализа данных.
