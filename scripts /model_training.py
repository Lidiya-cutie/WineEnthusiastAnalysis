import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
import joblib

def load_cleaned_data(filepath):
    """Загружает очищенные данные."""
    return pd.read_csv(filepath)

def train_model(data):
    """Обучает модель на данных."""
    # Пример: обучение модели регрессии для предсказания цены
    X = data.drop(columns=['price'])
    y = data['price']
    
    # Разделение данных на обучающую и тестовую выборки
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Обучение модели
    model = RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    
    # Оценка модели
    y_pred = model.predict(X_test)
    mse = mean_squared_error(y_test, y_pred)
    print(f"Mean Squared Error: {mse}")
    
    return model

def save_model(model, filepath):
    """Сохраняет обученную модель."""
    joblib.dump(model, filepath)

if __name__ == "__main__":
    cleaned_data_path = '../data/processed/cleaned_wine.csv'
    model_save_path = '../models/trained_models/wine_price_model.pkl'
    
    data = load_cleaned_data(cleaned_data_path)
    model = train_model(data)
    save_model(model, model_save_path)
