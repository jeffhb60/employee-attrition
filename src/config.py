from pathlib import Path

RANDOM_STATE = 42
PROJECT_ROOT = Path(__file__).resolve().parents[1]

DATA_DIR = PROJECT_ROOT / "data"
RAW_DATA_DIR = DATA_DIR / "raw"
PROCESSED_DATA_DIR = DATA_DIR / "processed"
MODELS_DIR = PROJECT_ROOT / "models"
RESULTS_DIR = PROJECT_ROOT / "results"
FIGURES_DIR = PROJECT_ROOT / "figures"
NOTEBOOKS_DIR = PROJECT_ROOT / "notebooks"

TRAIN_RAW_PATH = RAW_DATA_DIR / "train.csv"
TEST_RAW_PATH = RAW_DATA_DIR / "test.csv"
TRAIN_CLEAN_PATH = PROCESSED_DATA_DIR / "train_clean.parquet"
TEST_CLEAN_PATH = PROCESSED_DATA_DIR / "test_clean.parquet"
MODEL_RESULTS_PATH = RESULTS_DIR / "model_results.csv"
OOF_PREDICTIONS_PATH = RESULTS_DIR / "oof_predictions.csv"

TARGET = "Attrition"
ID_COLUMN = "EmployeeNumber"
CONSTANT_COLUMNS = ["EmployeeCount", "Over18", "StandardHours"]
DROP_FROM_MODEL = [ID_COLUMN, *CONSTANT_COLUMNS]

for directory in [PROCESSED_DATA_DIR, MODELS_DIR, RESULTS_DIR, FIGURES_DIR]:
    directory.mkdir(parents=True, exist_ok=True)