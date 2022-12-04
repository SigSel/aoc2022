from pathlib import Path
from typing import Optional, List


def read_file(file: Path) -> Optional[List]:
    if file.is_file():
        with open(file, 'r') as f:
            lines = [line.strip() for line in f]
        return lines
