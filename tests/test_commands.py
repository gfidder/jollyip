# -*- encoding: utf-8 -*-

import os
import pytest
import jollyip.commands


@pytest.mark.parametrize("platform, uid, expected", [
    ('win', 0, True), ('linux', 0, True), ('linux', 124, False)])
def test_verify_root(monkeypatch, platform, uid, expected):
    def mock_return():
        return uid

    monkeypatch.setattr("sys.platform", platform)
    monkeypatch.setattr(os, "getegid", mock_return)

    x = jollyip.commands._verify_root()
    assert x is expected
