# MLflow Installation Instructions

## Overview
MLflow is a Python package that runs entirely in your existing Python environment. No additional software installation required - just Python packages and a web browser.

## What MLflow Actually Needs
- ✅ Python 3.8+ (you already have this)
- ✅ Python packages (install via pip)
- ✅ Web browser (for MLflow UI)
- ✅ Local storage (for SQLite database and artifacts)

**That's it!** No servers, databases, or complex infrastructure needed.

---

## Installation Steps

### Step 1: Install Python Packages

**Both Mac and Windows use the same commands:**

```bash
# Navigate to project directory
cd /Users/ismar.dupanovic/myCode/MLFlow    # Mac
cd e:\Github\MLFlow                        # Windows

# Install MLflow and dependencies
pip install mlflow
pip install prophet
pip install -r requirements.txt
```

**Note on Prophet Installation:**
- **Mac**: Usually installs smoothly
- **Windows**: May require Visual Studio Build Tools if installation fails

### Step 2: Verify Installation

**Test that everything works (same on both OS):**

```bash
# Test MLflow
python -c "import mlflow; print(f'MLflow version: {mlflow.__version__}')"

# Test Prophet
python -c "import prophet; print('Prophet installed successfully')"

# Test configuration
python config/config.py
```

### Step 3: Start MLflow UI

**Same command on both Mac and Windows:**

```bash
mlflow ui
```

Then open your browser to: **http://localhost:5000**

---

## OS-Specific Differences

### Mac
- Use `pip3` instead of `pip` if you have multiple Python versions
- Prophet typically installs without issues
- MLflow UI opens at localhost:5000

### Windows
- Use `pip` (not `pip3`)
- If Prophet fails to install:
  ```bash
  # Option 1: Try conda instead
  conda install -c conda-forge prophet
  
  # Option 2: Install build tools first
  # Download Visual Studio Build Tools from Microsoft
  ```
- MLflow UI opens at localhost:5000 (same as Mac)

---

## What Gets Created

When you run MLflow, it automatically creates:

```
MLFlow/
├── mlflow.db          # SQLite database (experiment metadata)
├── mlruns/            # Experiment artifacts and models
│   ├── 0/            # Default experiment
│   └── <exp_id>/     # Your experiments
└── logs/             # Application logs (if configured)
```

---

## Troubleshooting

### Prophet Installation Issues

**Mac:**
```bash
# If Prophet fails, try:
pip install prophet --no-cache-dir

# Or update Xcode tools:
xcode-select --install
```

**Windows:**
```bash
# If Prophet fails, install build tools first:
# 1. Download "Microsoft C++ Build Tools"
# 2. Install with "C++ build tools" workload
# 3. Then retry: pip install prophet
```

### MLflow UI Issues

**Both Mac and Windows:**
```bash
# If port 5000 is busy:
mlflow ui --port 5001

# If database issues:
rm mlflow.db
mlflow ui  # Creates new database
```

### Import Errors

**Both Mac and Windows:**
```bash
# Check installed packages:
pip list | grep mlflow
pip list | grep prophet

# Reinstall if needed:
pip uninstall mlflow prophet
pip install mlflow prophet
```

---

## Quick Verification Script

**Save this as `test_mlflow.py` and run it:**

```python
#!/usr/bin/env python3
"""Quick MLflow verification script"""

def test_imports():
    """Test that all packages import correctly"""
    try:
        import mlflow
        print(f"✅ MLflow {mlflow.__version__}")
        
        import prophet
        print("✅ Prophet imported successfully")
        
        import pandas as pd
        import numpy as np
        import yaml
        print("✅ Supporting packages imported")
        
        return True
    except ImportError as e:
        print(f"❌ Import error: {e}")
        return False

def test_mlflow_basic():
    """Test basic MLflow functionality"""
    try:
        import mlflow
        
        # Set tracking URI
        mlflow.set_tracking_uri("sqlite:///test_mlflow.db")
        
        # Create test experiment
        with mlflow.start_run():
            mlflow.log_param("test_param", "test_value")
            mlflow.log_metric("test_metric", 0.95)
        
        print("✅ MLflow basic functionality works")
        
        # Clean up
        import os
        if os.path.exists("test_mlflow.db"):
            os.remove("test_mlflow.db")
            
        return True
    except Exception as e:
        print(f"❌ MLflow test failed: {e}")
        return False

def test_config():
    """Test configuration loading"""
    try:
        from config.config import load_config
        config = load_config()
        print("✅ Configuration loads successfully")
        return True
    except Exception as e:
        print(f"❌ Config test failed: {e}")
        return False

if __name__ == "__main__":
    print("🧪 Testing MLflow installation...")
    print("-" * 40)
    
    all_tests_passed = (
        test_imports() and
        test_mlflow_basic() and
        test_config()
    )
    
    print("-" * 40)
    if all_tests_passed:
        print("🎉 All tests passed! MLflow is ready to use.")
        print("\nNext steps:")
        print("1. Generate data: python data/generate_qsr_data.py")
        print("2. Start MLflow UI: mlflow ui")
        print("3. Open browser: http://localhost:5000")
    else:
        print("❌ Some tests failed. Check installation above.")
```

**Run the test:**
```bash
python test_mlflow.py
```

---

## Summary

MLflow installation is straightforward:
1. **Install packages**: `pip install mlflow prophet`
2. **Start UI**: `mlflow ui`
3. **Open browser**: http://localhost:5000

The main difference between Mac and Windows is Prophet installation - Mac is usually smoother, Windows may need build tools.

Everything else (MLflow UI, database, artifacts) works identically on both platforms.
