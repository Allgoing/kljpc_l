# -- coding: utf-8 --
import pytest

from common.checkpoint import CheckPoint


@pytest.fixture(autouse=True)
def use_checkpoint():
    check = CheckPoint()
    return check
