from pydantic import BaseModel
from simplestr import gen_str_repr_eq


@gen_str_repr_eq
class PointRelative(BaseModel):
    x: float # 0.0 - 1.0
    y: float

    def __init__(self, x: float, y: float) -> None:
        super().__init__(x=x, y=y)
