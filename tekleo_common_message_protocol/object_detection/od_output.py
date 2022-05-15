from typing import List
from pydantic import BaseModel
from simplestr import gen_str_repr_eq
from tekleo_common_message_protocol.object_detection.od_prediction import OdPrediction


@gen_str_repr_eq
class OdOutput(BaseModel):
    predictions: List[OdPrediction]

    def __init__(self, predictions: List[OdPrediction]) -> None:
        super().__init__(predictions=predictions)
