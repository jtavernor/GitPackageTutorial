import yaml
import os

current_script_location = os.path.dirname(os.path.realpath(__file__))
run_location = os.getcwd()

def get_config():
    config_path = os.path.join(run_location, 'config.yaml')
    if not os.path.exists(config_path):
        # Config doesn't exist, load default config file and copy to the correct location
        with open(os.path.join(current_script_location, 'config.yaml'), 'r') as f:
            conf = yaml.safe_load(f)
        with open(config_path, 'w') as f:
            f.write(yaml.dump(conf))
    with open(config_path, 'r') as f:
        conf = yaml.safe_load(f)
    return conf