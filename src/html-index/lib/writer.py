import logging
from typing import List

from src.lib import Assets
from src.lib import Index


class Writer:
    def __init__(self, assets: Assets):
        self.__index_template = assets.index_template().read_text()
        self.__file_template = assets.file_template().read_text()
        self.__icon_folder = assets.icon_folder()

    def write(self, indexes: List[Index]):
        for index in indexes:
            path = index.path.joinpath('index.html')
            logging.info(f"Writing {path}")

            html = index.to_html(self.__index_template, self.__file_template)

            path.write_text(html)

    def write_deep(self, indexes: List[Index]):
        if len(indexes) <= 0:
            return

        self.write(indexes)

        for index in indexes:
            self.write_deep(index.list_sub_indexes())
