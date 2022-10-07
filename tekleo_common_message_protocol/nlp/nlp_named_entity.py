from pydantic import BaseModel
from simplestr import gen_str_repr_eq


@gen_str_repr_eq
class NlpNamedEntity(BaseModel):
    text: str
    label: str
    start_char: int
    end_char: int

    def __init__(self, text: str, label: str, start_char: int, end_char: int) -> None:
        super().__init__(text=text, label=label, start_char=start_char, end_char=end_char)
