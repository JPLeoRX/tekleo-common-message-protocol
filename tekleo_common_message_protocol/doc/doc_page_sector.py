from typing import List
from pydantic import BaseModel
from simplestr import gen_str_repr_eq
from tekleo_common_message_protocol.rectangle_pixel import RectanglePixel
from tekleo_common_message_protocol.point_pixel import PointPixel


@gen_str_repr_eq
class DocPageSector(BaseModel):
    page_index: int                         # Index of this page on document, from 0, page number is = page_index + 1
    sector_index: int                       # Index of this sector on page, from 0
    label: str                              # Label from the model
    region_on_page: RectanglePixel          # Region from the model
    mask_on_page: List[PointPixel]          # Mask from the model
    text: str                               # Text, if this is parsable (depending on label), or empty string

    def is_title(self) -> bool:
        return self.label == 'title'

    def is_header(self) -> bool:
        return self.label == 'header'

    def is_media(self) -> bool:
        return self.label.startswith("media")

    def get_width(self) -> int:
        return self.region_on_page.w

    def get_height(self) -> int:
        return self.region_on_page.h


    # def __init__(self, index: int, text: str, label: str, start_char: int, end_char: int) -> None:
    #     super().__init__(index=index, text=text, label=label, start_char=start_char, end_char=end_char)
