import yaml
import os

current_script_location = os.path.dirname(os.path.realpath(__file__))

def get_config():
    with open(os.path.join(current_script_location, 'config.yaml'), 'r') as f:
        conf = yaml.safe_load(f)
    return conf