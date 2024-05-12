from pathlib import Path
from typing import Dict, List, Optional, Tuple, Union
import json


def load_list_from_file(file_path: Union[str, Path]) -> list[str]:
    file_path = Path(file_path)
    return file_path.read_text().splitlines()


def load_text_from_file(file_path: Union[str, Path]) -> str:
    file_path = Path(file_path)
    return file_path.read_text().strip()


def load_json_from_file(file_path: Union[str, Path]) -> dict:
    file_path = Path(file_path)
    with file_path.open(mode="r", encoding="utf-8") as fin:
        data = json.load(fin)
    return data
