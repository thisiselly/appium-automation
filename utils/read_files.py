import pandas as pd
import yaml

from utils.get_file_path_util import get_settings_yaml_path

settings_yaml_path = get_settings_yaml_path()

def read_csv_file(file_path):
    return pd.read_csv(file_path).values.tolist()

def read_yaml_file(file_page):
    with open(file_page, 'r', encoding='utf-8') as file:
        data = yaml.safe_load(file)
        return data

if __name__ == '__main__':
    print(read_yaml_file(settings_yaml_path)['connection']['url'])
    print(read_yaml_file(settings_yaml_path)['capabilities'])
    print(read_yaml_file(settings_yaml_path)['apps']['yangshipin'])


