from .image_base64_input import ImageBase64Input
from .image_url_input import ImageUrlInput
from .ping_output import PingOutput
from .point_pixel import PointPixel
from .rectangle_pixel import RectanglePixel
from .rectangle_relative import RectangleRelative

from .object_detection.od_labeled_box import OdLabeledBox
from .object_detection.od_output import OdOutput
from .object_detection.od_prediction import OdPrediction
from .object_detection.od_sample import OdSample

__all__ = [
    # General
    ImageBase64Input,
    ImageUrlInput,
    PingOutput,
    PointPixel,
    RectanglePixel,
    RectangleRelative,

    # Object detection
    OdLabeledBox,
    OdOutput,
    OdPrediction,
    OdSample,
]
