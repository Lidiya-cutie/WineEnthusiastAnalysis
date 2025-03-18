from comet_logger import log_metrics, log_params, log_model

# Логирование параметров модели
params = {
    "learning_rate": 0.001,
    "batch_size": 32,
    "num_epochs": 50
}
log_params(params)

# Логирование метрик
for epoch in range(50):
    train_loss = 0.05 * (50 - epoch)  # Заглушка
    log_metrics({"train_loss": train_loss}, step=epoch)

# Логирование модели
log_model("models/trained_models/wine_model.pkl", "Wine Model")
