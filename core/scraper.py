from typing import Any, Dict, List, Generator

import requests
from bs4 import BeautifulSoup

TEST_URL: str = "https://www.humblebundle.com/books/hacking-101-no-starch-press-books?hmb_source=humble_home&hmb_medium=product_tile&hmb_campaign=mosaic_section_2_layout_index_2_layout_type_twos_tile_index_1_c_hacking101nostarchpress_bookbundle"
BUNDLE_URL: str = "https://www.humblebundle.com/store"


class Scraper:
    BOOK_TITLE_SEARCH: Dict[str, Any] = {
        "name": "span",
        "attrs": {
            "class": "front-page-art-image-text"
        }
    }

    BUNDLE_TITLE_SEARCH: Dict[str, Any] = {
        "name": "span",
        "attrs": {
            "class": "name"
        }
    }

    def __init__(self, url: str, search_element: Dict[str, Any] = BOOK_TITLE_SEARCH) -> None:
        super().__init__()
        self.url = url
        self.search_element = search_element

    def scrape(self) -> Generator[str, None, List[str]]:
        ls: List = list()
        for span in BeautifulSoup(self.__get_book_html(),
                                  "html.parser").find_all(**self.search_element):
            txt: str = span.get_text()
            ls.append(txt)
            yield txt
        return ls

    def __get_book_html(self):
        return requests.get(self.url).text

    def __repr__(self) -> Dict[str, Any]:
        return {"url": self.url, "search_element": self.search_element}

    def __str__(self) -> str:
        return self.url