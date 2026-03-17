import numpy as np

from unicamp_effects.registry import register


@register(prefix="MY_RA")
def effect_name(img: np.ndarray) -> np.ndarray:
    ...
