from pathlib import Path
from icecream import ic

dir_path = Path(__file__).resolve().parents[1]
ic(dir_path)