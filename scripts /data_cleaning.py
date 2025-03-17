import pandas as pd

def load_data(filepath):
    """Загружает данные из CSV файла."""
    return pd.read_csv(filepath)

def clean_data(data):
    """Очищает данные: удаляет дубликаты и обрабатывает пропущенные значения."""
    data = data.drop_duplicates()
    data = data.fillna({'designation': 'unknown', 'price': -1, 'region_2': 'unknown', 'taster_twitter_handle': 'unknown'})
    return data

def save_cleaned_data(data, filepath):
    """Сохраняет очищенные данные в CSV файл."""
    data.to_csv(filepath, index=False)

if __name__ == "__main__":
    raw_data_path = '../data/raw/wine.csv'
    cleaned_data_path = '../data/processed/cleaned_wine.csv'
    
    data = load_data(raw_data_path)
    cleaned_data = clean_data(data)
    save_cleaned_data(cleaned_data, cleaned_data_path)
