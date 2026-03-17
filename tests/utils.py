import glob
import os
from typing import Iterable


def get_all_imgs_in_dir(dir: str) -> list[str]:
    template = os.path.join(dir, "*.{format}")

    paths = []
    for format in ["png", "jpg", "jpeg"]:
        paths += glob.glob(template.format(format=format))

    return paths


def assert_prefix(paths: Iterable[str], prefix: str) -> None:
    for path in paths:
        assert os.path.basename(path).split("_")[0] == prefix


def assert_valid_ra(ra: str) -> None:
    assert len(ra) == 6
    int(ra)
