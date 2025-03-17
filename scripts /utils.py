def print_missing_values(data):
    """Выводит информацию о пропущенных значениях в данных."""
    missing_values = data.isnull().sum()
    print("Пропущенные значения:")
    print(missing_values[missing_values > 0])
