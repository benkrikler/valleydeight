import valleydeight as vd
import pytest


def test_choice_static():
    choice_t = vd.Choice("one", 4, True)

    assert choice_t("one") == "one"
    assert choice_t(True) is True
    assert choice_t(4) == 4
    with pytest.raises(vd.ValidatorException):
        choice_t(8)
    with pytest.raises(vd.ValidatorException):
        choice_t(dict(one=1, two="2"))
    with pytest.raises(vd.ValidatorException):
        choice_t("two")


def test_choice_validators():
    choice_t = vd.Choice(vd.Str(), vd.Bool())

    assert choice_t(True) is True
    assert choice_t("True") == "True"
    with pytest.raises(vd.ValidatorException):
        choice_t(8)
    with pytest.raises(vd.ValidatorException):
        choice_t(dict(one=1, two="2"))


def test_choice_mixed():
    choice_t = vd.Choice(3, 2.22, vd.Str(), vd.Bool())

    assert choice_t(True) is True
    assert choice_t("True") == "True"
    assert choice_t(3) == 3
    assert choice_t(2.22) == 2.22
    with pytest.raises(vd.ValidatorException):
        choice_t(8)
    with pytest.raises(vd.ValidatorException):
        choice_t(dict(one=1, two="2"))
    with pytest.raises(vd.ValidatorException):
        choice_t(7.92342)
