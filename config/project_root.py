from pathlib import Path


current_file = Path(__file__).resolve()
PROJECT_ROOT = current_file.parents[1]
PROJECT_ROOT_str = str(PROJECT_ROOT)