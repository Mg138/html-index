import logging
import sys
from pathlib import Path

from lib import icon_manager
from lib.assets import Assets
from lib.index import Index
from lib.writer import Writer


def main():
    args = sys.argv
    if not len(args) > 1:
        logging.error("Please provide a path!")
        exit(1)

    # init
    root = Path(__file__).parent
    assets = Assets(root.joinpath('assets'))

    icon_manager.read_icons(assets)

    # actual program
    path = Path(args[1])
    index = Index.read_from_path(path)
    writer = Writer(assets)
    writer.write_deep([index])


if __name__ == "__main__":
    main()
