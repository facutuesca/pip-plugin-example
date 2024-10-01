"""Initial testing module."""

from pathlib import Path

import pytest

import pip_plugin_example


def test_version() -> None:
    version = getattr(pip_plugin_example, "__version__", None)
    assert version is not None
    assert isinstance(version, str)


class TestPlugin:
    def test_plugin_type(self) -> None:
        assert pip_plugin_example.plugin_type() == "dist-inspector"

    def test_pre_download(self) -> None:
        with pytest.raises(
            ValueError, match="Download of filename \\(hash\\) from url has been forbidden"
        ):
            pip_plugin_example.pre_download(url="url", filename="filename", digest="hash")

    def test_pre_extract(self) -> None:
        with pytest.raises(ValueError, match="Extraction of filename has been forbidden"):
            pip_plugin_example.pre_extract(dist=Path("filename"))
