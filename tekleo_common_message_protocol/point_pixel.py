from pydantic import BaseModel
from simplestr import gen_str_repr_eq


@gen_str_repr_eq
class PointPixel(BaseModel):
    x: int
    y: int

    def __init__(self, x: int, y: int) -> None:
        super().__init__(x=x, y=y)
