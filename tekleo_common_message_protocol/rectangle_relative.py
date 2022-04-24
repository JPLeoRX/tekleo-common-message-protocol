from pydantic import BaseModel
from simplestr import gen_str_repr_eq


# Relative coordinates, from 0.0 to 1.0
@gen_str_repr_eq
class RectangleRelative(BaseModel):
    x: float
    y: float
    w: float
    h: float

    def __init__(self, x: float, y: float, w: float, h: float) -> None:
        if not (0.0 <= x <= 1.0):
            raise RuntimeError("X value is not in [0.0, 1.0] range")
        if not (0.0 <= y <= 1.0):
            raise RuntimeError("Y value is not in [0.0, 1.0] range")
        if not (0.0 <= w <= 1.0):
            raise RuntimeError("W value is not in [0.0, 1.0] range")
        if not (0.0 <= h <= 1.0):
            raise RuntimeError("H value is not in [0.0, 1.0] range")
        super().__init__(x=x, y=y, w=w, h=h)
