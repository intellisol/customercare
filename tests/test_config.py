import os
from importlib import reload

import customer_care.config as cfg


def test_config_defaults(monkeypatch):
    monkeypatch.delenv("CC_RECIPIENTS", raising=False)
    reload(cfg)
    config = cfg.Config()
    assert config.recipients == ["support@example.com"]
    assert config.db_port == 5432
