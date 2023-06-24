import shutil
from pathlib import Path
from typing import List

from .file import File
from .ignore import load_ignore_patterns
import logging


def check_invalid(path: Path):
    name = path.name
    return name.startswith('.') or name.startswith('__')


def list_files(path: Path) -> List[File]:
    files = []
    ignore_files = load_ignore_patterns(path)

    for file in path.glob('*'):
        if file.name in ['index.html', '.icons']:
            if file.is_dir():
                shutil.rmtree(file)
            else:
                file.unlink()
            continue

        if file.name.startswith('.'):
            continue

        if file.name in ignore_files:
            continue

        f = File(file)
        logging.info(f"Read File: {f}")
        files.append(f)

    return files
