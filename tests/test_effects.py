import numpy as np
import pytest

from unicamp_effects import ImageEffect
from unicamp_effects.registry import get_all_effects


@pytest.mark.parametrize("effect", list(get_all_effects().values()),
                         ids=lambda effect: effect.__qualname__)
def test_effect(effect: ImageEffect):
    generator = np.random.default_rng(0)
    img = generator.integers(0, 255,
                             endpoint=True,
                             size=(10, 10, 3),
                             dtype=np.uint8)

    img_result = effect(img)

    assert isinstance(img_result, np.ndarray)
    assert img_result.shape == img.shape
    assert img_result.dtype == np.uint8
