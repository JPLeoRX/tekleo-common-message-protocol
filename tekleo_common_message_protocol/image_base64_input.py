from pydantic import BaseModel
from simplestr import gen_str_repr


@gen_str_repr
class ImageBase64Input(BaseModel):
    image_base64: str

    def __init__(self, image_base64: str) -> None:
        super().__init__(image_base64=image_base64)
