import valedictory as vd
import pytest


def test_base_validator():
    base_t = vd.base.BaseValidator(node="testing")
    assert base_t.node == "testing"
    with pytest.raises(NotImplementedError):
        base_t(4)


def test_pass():
    pass_t = vd.Pass()
    assert pass_t(5) == 5
    assert pass_t("hello2") == "hello2"
