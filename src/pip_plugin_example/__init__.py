"""The `pip-plugin-example` APIs."""

from pathlib import Path
from typing import Literal

__version__ = "0.0.1"

PluginType = Literal["dist-inspector"]


def plugin_type() -> PluginType:
    """Return the plugin type.

    Currently, the only supported plugin type is "dist-inspector"
    """
    return "dist-inspector"


def pre_download(url: str, filename: str, digest: str) -> None:
    """Inspect the file about to be downloaded by pip.

    This hook is called right before pip downloads a distribution
    file. It doesn't return anything, and it can only raise `ValueError`
    to signal to pip that the operation should be aborted.
    """
    error_msg = f"Download of {filename} ({digest}) from {url} has been forbidden"
    raise ValueError(error_msg)


def pre_extract(dist: Path) -> None:
    """Inspect the file about to be extracted by pip.

    This hook is called right before pip extracts a distribution
    file. It doesn't return anything, and it can only raise `ValueError`
    to signal to pip that the operation should be aborted.
    """
    error_msg = f"Extraction of {dist} has been forbidden"
    raise ValueError(error_msg)
