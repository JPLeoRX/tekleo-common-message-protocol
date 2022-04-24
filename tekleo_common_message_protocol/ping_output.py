from pydantic import BaseModel
from simplestr import gen_str_repr_eq


@gen_str_repr_eq
class PingOutput(BaseModel):
    id: str
    success: bool
    timestamp: int

    def __init__(self, id: str, success: bool, timestamp: int) -> None:
        super().__init__(id=id, success=success, timestamp=timestamp)
