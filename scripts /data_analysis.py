from .utils import print_missing_values
from . import utils, data_cleaning
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def load_cleaned_data(filepath):
    """Загружает очищенные данные."""
    return pd.read_csv(filepath)

def analyze_data(data):
    """Анализирует данные и строит графики."""
    # Пример анализа: распределение цен
    plt.figure(figsize=(10, 6))
    sns.histplot(data['price'].dropna(), bins=30, kde=True)
    plt.title('Распределение цен на вина')
    plt.xlabel('Цена')
    plt.ylabel('Частота')
    plt.savefig('../reports/figures/price_distribution.png')
    plt.show()

if __name__ == "__main__":
    cleaned_data_path = '../data/processed/cleaned_wine.csv'
    data = load_cleaned_data(cleaned_data_path)
    analyze_data(data)
