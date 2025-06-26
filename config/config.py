import yaml
import os
from pathlib import Path

def load_config(config_path=None):
    """Load configuration from YAML file"""
    if config_path is None:
        # Default to config.yaml in the config directory
        project_root = Path(__file__).parent.parent
        config_path = project_root / "config" / "config.yaml"
    
    with open(config_path, 'r') as file:
        config = yaml.safe_load(file)
    
    return config

def get_model_params(config):
    """Extract model parameters from config"""
    return config['model']['lightgbm']

def get_feature_config(config):
    """Extract feature engineering config"""
    return config['model']['features']

def get_mlflow_config(config):
    """Extract MLflow configuration"""
    return config['mlflow']

def get_data_paths(config):
    """Get data file paths"""
    data_dir = config['data']['dir']
    return {
        'sales_file': os.path.join(data_dir, config['data']['sales_file']),
        'store_metadata_file': os.path.join(data_dir, config['data']['store_metadata_file'])
    }

# Example usage
if __name__ == "__main__":
    config = load_config()
    print("Configuration loaded successfully!")
    print(f"Experiment name: {config['mlflow']['experiment_name']}")
    print(f"Model params: {get_model_params(config)}")
