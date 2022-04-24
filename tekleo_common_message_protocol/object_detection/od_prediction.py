from pydantic import BaseModel
from simplestr import gen_str_repr_eq
from tekleo_common_message_protocol.rectangle_pixel import RectanglePixel


@gen_str_repr_eq
class OdPrediction(BaseModel):
    label: str
    score: float
    region: RectanglePixel

    def __init__(self, label: str, score: float, region: RectanglePixel) -> None:
        super().__init__(label=label, score=score, region=region)
