from typing import List
from pydantic import BaseModel
from simplestr import gen_str_repr_eq
from tekleo_common_message_protocol.rectangle_pixel import RectanglePixel
from tekleo_common_message_protocol.point_pixel import PointPixel


@gen_str_repr_eq
class OdPrediction(BaseModel):
    label: str
    score: float
    region: RectanglePixel
    mask: List[PointPixel]

    def __init__(self, label: str, score: float, region: RectanglePixel, mask: List[PointPixel]) -> None:
        super().__init__(label=label, score=score, region=region, mask=mask)
