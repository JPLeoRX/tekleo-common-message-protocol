from pydantic import BaseModel
from simplestr import gen_str_repr_eq


@gen_str_repr_eq
class Text(BaseModel):
    text: str

    def __init__(self, text: str) -> None:
        super().__init__(text=text)
