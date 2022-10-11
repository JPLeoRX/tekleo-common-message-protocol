from pydantic import BaseModel
from simplestr import gen_str_repr_eq


@gen_str_repr_eq
class RectanglePixel(BaseModel):
    x: int
    y: int
    w: int
    h: int

    def __init__(self, x: int, y: int, w: int, h: int) -> None:
        super().__init__(x=x, y=y, w=w, h=h)

    def get_area(self) -> int:
        return self.w * self.h
