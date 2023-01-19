from typing import List
from pydantic import BaseModel
from simplestr import gen_str_repr_eq
from tekleo_common_message_protocol.rectangle_pixel import RectanglePixel
from tekleo_common_message_protocol.point_pixel import PointPixel
from tekleo_common_message_protocol.object_detection.od_prediction import OdPrediction


@gen_str_repr_eq
class FacialPrediction(BaseModel):
    orientation: str # 'frontal' or 'profile'
    score: float
    region: RectanglePixel
    mask: List[PointPixel]
    features: List[OdPrediction]

    def __init__(self, orientation: str, score: float, region: RectanglePixel, mask: List[PointPixel], features: List[OdPrediction]) -> None:
        super().__init__(orientation=orientation, score=score, region=region, mask=mask, features=features)
