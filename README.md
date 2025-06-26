# QSR Sales Forecasting with MLflow

A comprehensive MLflow learning project for forecasting daily sales and guest counts for a large QSR chain.

## Project Structure

```
MLFlow/
├── ClaudeContext/          # Session logs and context files
├── data/                   # Generated datasets
│   ├── qsr_daily_sales.csv    # Main training data (36,500 records)
│   ├── store_metadata.csv     # Store configurations
│   └── generate_qsr_data.py   # Data generation script
├── src/                    # Source code modules
│   ├── data_processing/       # Feature engineering, data prep
│   ├── models/               # Model definitions and training
│   ├── evaluation/           # Model validation and metrics
│   └── deployment/           # Serving and deployment code
├── notebooks/              # Jupyter notebooks for exploration
├── experiments/            # MLflow experiment artifacts
├── models/                 # Saved model artifacts
├── config/                 # Configuration files
├── scripts/                # Automation and utility scripts
└── tests/                  # Unit tests
```

## Data Overview

- **Stores**: 50 QSR locations across 5 regions and 5 store types
- **Timeframe**: 2 years of daily data (2022-2023)
- **Target Variables**: 
  - Total Sales (revenue)
  - Guest Count (number of orders)
- **Features**: Seasonality, day-of-week, holidays, promotions, weather, store characteristics

## Learning Objectives

1. **MLflow Tracking**: Experiment management and comparison
2. **MLflow Models**: Standardized model packaging
3. **MLflow Registry**: Model lifecycle management
4. **MLflow Deployment**: Model serving and monitoring
5. **CI/CD Integration**: Automated workflows
6. **Production Monitoring**: Drift detection and performance tracking

## Getting Started

1. Generate data: `python data/generate_qsr_data.py`
2. Install dependencies: `pip install -r requirements.txt`
3. Start MLflow UI: `mlflow ui`
4. Run first experiment: `python src/models/baseline_model.py`

## Project Phases

- **Phase 1**: Traditional modeling approach
- **Phase 2**: MLflow tracking integration
- **Phase 3**: Model registry and lifecycle
- **Phase 4**: Deployment and monitoring
- **Phase 5**: CI/CD automation
