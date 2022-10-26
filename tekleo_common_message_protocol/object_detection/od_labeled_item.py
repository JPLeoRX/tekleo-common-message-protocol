from typing import List
from pydantic import BaseModel
from simplestr import gen_str_repr_eq
from tekleo_common_message_protocol.rectangle_relative import RectangleRelative
from tekleo_common_message_protocol.point_relative import PointRelative


@gen_str_repr_eq
class OdLabeledItem(BaseModel):
    label: str
    mask: List[PointRelative]

    def __init__(self, label: str, mask: List[PointRelative]) -> None:
        super().__init__(label=label, mask=mask)

    def get_region(self) -> RectangleRelative:
        x_values = [p.x for p in self.mask]
        y_values = [p.y for p in self.mask]
        min_x = min(x_values)
        min_y = min(y_values)
        max_x = max(x_values)
        max_y = max(y_values)
        return RectangleRelative(min_x, min_y, max_x - min_x, max_y - min_y)
