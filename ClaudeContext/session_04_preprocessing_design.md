# MLflow Learning Project - Session 04 Data Preprocessing Design

## Session Context
- **Session**: 04 - Data Preprocessing and Model Design
- **Date**: 2025-01-02 (continued from Session 03)
- **Focus**: Prophet data transformation concepts and store identity decisions

## Key Concepts Explored

### 1. Prophet Data Format Requirements
**Core Prophet Structure:**
- **`ds` column**: Date column (Prophet's "datestamp")
- **`y` column**: Target variable to forecast  
- **Additional regressors**: Optional external variables

**Our Transformation Challenge:**
- **Current**: 50 rows per date (one per store) with multiple features
- **Target**: Prophet format with store-level forecasting capability

### 2. Global Model Data Architecture Decisions

#### **Decision 1: Forecasting Granularity** ✅ DECIDED
- **Choice**: Store-level forecasts (individual predictions per store)
- **Alternative**: Chain-level aggregated forecasts
- **Rationale**: Business needs individual store performance

#### **Decision 2: Target Variable Priority** ✅ DECIDED  
- **Choice**: Focus on `total_sales` first
- **Alternative**: Build both sales and guest count models simultaneously
- **Rationale**: Sales is primary business metric, guest count secondary

#### **Decision 3: Store Identity Approach** 🟡 UNDER CONSIDERATION
**Option A: Store as Features Only**
```
ds, y, store_type_Urban, region_North, baseline_1500, size_1.2
```
- ✅ Scalable for new stores
- ✅ Interpretable business insights
- ✅ Less model complexity
- ❌ May miss unique store patterns

**Option B: Store Identity Preserved**
```
ds, y, store_001, store_002, store_type_Urban, region_North  
```
- ✅ Captures unique store personalities
- ✅ Location-specific effects
- ❌ Poor predictions for new stores
- ❌ Increased model complexity (50+ parameters)

### 3. Data Transformation Strategy

#### **Current Data Structure:**
```
date, store_id, store_type, region, total_sales, guest_count, 
promotion_active, weather_factor, is_weekend, is_holiday, etc.
```

#### **Target Prophet Structure:**
```
ds (date), y (total_sales), [store features], [external regressors]
```

#### **Transformation Steps Required:**
1. **Column Mapping**: `date` → `ds`, `total_sales` → `y`
2. **One-hot Encoding**: Store types and regions
3. **Feature Engineering**: Store capacity and size factors
4. **Regressor Preparation**: Promotions, weather, holidays
5. **Data Validation**: Ensure Prophet format compliance

## Key Learning Points

### Prophet Global Model Insights
- **Global models share learning** across similar stores
- **Store characteristics become features** rather than identifiers
- **New store predictions** depend on modeling approach chosen
- **Business interpretability** varies by feature engineering approach

### QSR-Specific Considerations
- **Store personalities**: Do individual locations have unique patterns?
- **Scalability needs**: How often are new stores opened?
- **Business insights**: What drives performance differences?
- **Operational complexity**: Simpler models easier to maintain

## Session 04 Status: 🟡 IN PROGRESS

**Completed:**
- ✅ Prophet data format requirements understood
- ✅ Forecasting granularity decided (store-level)
- ✅ Target variable prioritized (total_sales first)
- ✅ Store identity trade-offs analyzed

**Pending Decision:**
- 🟡 Store identity approach (Features vs Identity)
- ⏳ Final data transformation design
- ⏳ Code implementation for preprocessing

**Next Steps:**
1. **Finalize store identity decision** (Features Only vs Store Identity)
2. **Design complete transformation pipeline**
3. **Implement preprocessing code**
4. **Validate Prophet data format**
5. **Test with sample data**

## Technical Architecture Implications

### For Option A (Features Only):
```python
# Transformation example
features = [
    'store_type_Urban', 'store_type_Mall', 'store_type_Airport',
    'region_North', 'region_South', 'region_East', 
    'avg_daily_baseline', 'size_factor',
    'promotion_active', 'weather_factor', 'is_weekend'
]
```

### For Option B (Store Identity):
```python
# Transformation example  
features = [
    'store_001', 'store_002', ..., 'store_050',  # 50 store dummies
    'store_type_Urban', 'store_type_Mall',        # Plus characteristics
    'promotion_active', 'weather_factor'         # Plus external factors
]
```

## Recommendations Analysis

### Option A (Features Only) - Recommended
**Pros:**
- Immediate predictions for new stores
- Clear business insights (store type/region performance)
- Simpler model with fewer parameters
- Better generalization across store portfolio

**Cons:**
- May miss unique location-specific patterns
- Assumes stores are primarily defined by observable characteristics

### Option B (Store Identity)
**Pros:**
- Captures unique store personalities and local effects
- May achieve higher accuracy for established stores
- Accounts for unobserved location factors

**Cons:**
- Poor new store predictions
- 50+ additional parameters increase complexity
- Less interpretable business insights

## Context for Resume
- **Current Phase**: Data preprocessing design
- **Key Decision Pending**: Store identity modeling approach
- **Ready For**: Transformation pipeline implementation
- **Data Available**: 3-year dataset with 50 stores ready
- **Infrastructure**: MLflow operational and tested
