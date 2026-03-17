from typing import Protocol, runtime_checkable

import numpy as np


@runtime_checkable
class ImageEffect(Protocol):
    def __call__(self, img: np.ndarray) -> np.ndarray:
        ...
        ...
