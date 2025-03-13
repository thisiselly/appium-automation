import os

class GetFilePath:
    project_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    def get_log_file_path(self):
        return os.path.join(self.project_dir, "logs")
