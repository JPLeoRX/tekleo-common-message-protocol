from pydantic import BaseModel
from simplestr import gen_str_repr_eq
from tekleo_common_message_protocol.rectangle_relative import RectangleRelative


@gen_str_repr_eq
class OdLabeledBox(BaseModel):
    label: str
    region: RectangleRelative

    def __init__(self, label: str, region: RectangleRelative) -> None:
        super().__init__(label=label, region=region)
