import os

project_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def get_log_file_path():
    return os.path.join(project_dir, "logs")

def get_csv_file_path():
    return os.path.join(project_dir, "testdata")

def get_settings_yaml_path():
    return os.path.join(project_dir, "settings.yaml")

if __name__ == '__main__':
    print(get_settings_yaml_path())