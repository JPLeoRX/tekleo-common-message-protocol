from pydantic import BaseModel
from simplestr import gen_str_repr_eq


@gen_str_repr_eq
class ImageUrlInput(BaseModel):
    image_url: str

    def __init__(self, image_url: str) -> None:
        super().__init__(image_url=image_url)
