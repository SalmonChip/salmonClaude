from pathlib import Path

import pytest

from salmon_claude.config import get_config


def test_max_steps_nonpositive_rejected(monkeypatch):
    monkeypatch.setenv("SALMON_MAX_STEPS", "0")   # 环境变量名要和 config.py 一致
    with pytest.raises(ValueError):
        get_config()


def test_get_config_defaults():
    config = get_config()
    assert config.model == "deepseek-chat"
    assert config.base_url == "https://api.deepseek.com/v1"
    assert config.api_key is None
    assert config.max_steps == 20
    assert config.workspace_root == Path(".")
