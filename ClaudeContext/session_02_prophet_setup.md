# MLflow Learning Project - Session 02 Prophet Setup

## Session Context
- **Session**: 02 - Prophet Model Configuration
- **Date**: 2025-01-02 (continued from Session 01)
- **Focus**: Switched from LightGBM to Prophet, configured for global modeling approach

## Key Decisions Made

### 1. Model Architecture Change
- **FROM**: LightGBM individual store models
- **TO**: Prophet global model for all stores
- **Rationale**: Prophet better handles seasonality, trends, and holidays for time series forecasting

### 2. Data Structure Finalized
- **Training**: 2022-2023 data (2 years, ~36,500 records)
- **Validation**: 2024 data as "actuals" (1 year, ~18,250 records)
- **Total Dataset**: 3 years of data (~54,750 records)
- **Stores**: 50 QSR locations across 5 regions and store types

### 3. Global Model Configuration
- **Approach**: Single Prophet model for all stores (not per-store models)
- **Features**: One-hot encoded store types, regions, baseline capacity, size factors
- **Benefits**: Shared learning across stores, handles new stores, simpler deployment

## ✅ Session 02 Completed Tasks

### 1. Data Generation Updates
- Modified `generate_qsr_data.py` to create 3 years of data (2022-2024)
- Added 2% annual growth factor for realistic business progression
- Auto-generates 4 files:
  - `qsr_daily_sales.csv` - Full 3-year dataset
  - `qsr_train_2022_2023.csv` - Training data
  - `qsr_validation_2024.csv` - Validation "actuals"
  - `store_metadata.csv` - Store configurations

### 2. Prophet Configuration
- Completely redesigned `config.yaml` for Prophet
- Added Prophet-specific parameters (seasonality, holidays, regressors)
- Configured for global model with store-level features
- Updated requirements.txt to include `prophet` and `holidays`

### 3. Global Model Features
```yaml
regressors:
  # External factors
  - "promotion_active"
  - "weather_factor" 
  - "is_weekend"
  - "is_holiday"
  
  # Store characteristics (one-hot encoded)
  - "store_type_Urban/Suburban/Highway/Mall/Airport"
  - "region_North/South/East/West/Central"
  - "avg_daily_baseline"
  - "size_factor"
  - "store_id_encoded"
```

### 4. Evaluation Framework
- Time series metrics: MAE, MAPE, SMAPE, MASE, coverage
- Store-level performance tracking
- Business metrics: chain-wide, store-type, regional accuracy
- Cross-validation with temporal splits

## Configuration Highlights

### Prophet Model Settings
- **Growth**: Linear
- **Seasonality**: Yearly, weekly, monthly, quarterly
- **Holidays**: US holidays + QSR-specific events
- **Modeling**: Global approach with store effects

### MLflow Integration
- **Experiment**: `QSR_Prophet_Global_Forecasting`
- **Model Name**: `QSR_Prophet_Global_Model`
- **Custom logging**: Prophet requires manual tracking

### Forecasting Configuration
- **Horizon**: 365 days (1 year ahead)
- **Intervals**: 50%, 80%, 95% confidence
- **Output**: Store-level + chain-level aggregates

## Files Updated/Created
- ✅ `data/generate_qsr_data.py` - 3-year data generation
- ✅ `config/config.yaml` - Complete Prophet configuration  
- ✅ `requirements.txt` - Added Prophet dependencies
- ✅ Session documentation

## Session 02 Status: ✅ COMPLETE

**Ready for Session 03:**
1. Generate 3-year dataset: `python data/generate_qsr_data.py`
2. Install Prophet: `pip install -r requirements.txt`
3. Build first Prophet model with global approach
4. Integrate MLflow tracking

## Key Learning Points
- Prophet excels at QSR forecasting (seasonality, holidays, trends)
- Global models can leverage shared patterns across stores
- Time series requires careful train/validation splitting
- Feature engineering crucial for global model performance

## Next Session Goals
- Implement Prophet data preprocessing
- Build and train global Prophet model
- Set up MLflow experiment tracking
- Validate model performance on 2024 data
