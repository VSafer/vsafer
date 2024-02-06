import os
import sys
from pathlib import Path

from vsafer.types import Version


def version_tostring(ver: Version) -> str:
    return ".".join([str(n) for n in ver])


def assets_path() -> str:
    try:
        return sys._MEIPASS  # type: ignore[attr-defined]
    except AttributeError:
        utils_dir = Path(os.path.dirname(__file__))
        assets_dir = utils_dir.parent.parent.absolute() / "assets"
        return str(assets_dir)
