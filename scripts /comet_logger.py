from comet_ml import Experiment
import yaml

# Загружаем конфигурацию Comet ML
with open("config/comet_config.yaml", "r") as f:
    comet_config = yaml.safe_load(f)

COMET_API_KEY = comet_config["api_key"]
PROJECT_NAME = comet_config["project_name"]
WORKSPACE = comet_config["workspace"]

# Инициализируем Comet ML
experiment = Experiment(
    api_key=COMET_API_KEY,
    project_name=PROJECT_NAME,
    workspace=WORKSPACE
)

def log_metrics(metrics: dict, step: int = None):
    """Логирует метрики в Comet ML."""
    experiment.log_metrics(metrics, step=step)

def log_params(params: dict):
    """Логирует гиперпараметры модели в Comet ML."""
    experiment.log_parameters(params)

def log_model(model_path: str, model_name: str):
    """Загружает модель в Comet ML."""
    experiment.log_model(model_name, model_path)
