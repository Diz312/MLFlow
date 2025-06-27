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