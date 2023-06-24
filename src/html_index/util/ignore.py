import os
from pathlib import Path
from typing import List

IGNORE_FILE = '.indexignore'


def load_ignore_patterns(path: Path) -> List[str]:
    ignore_file = os.path.join(path, IGNORE_FILE)
    try:
        with open(ignore_file, 'r') as f:
            patterns = f.read().splitlines()
    except:
        patterns = []

    return patterns
