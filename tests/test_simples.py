import valedictory as vd
import pytest


def test_str():
    str_t = vd.Str()
    assert str_t("hello world") == "hello world"

    with pytest.raises(vd.ValidatorException) as e:
        str_t(4)
    with pytest.raises(vd.ValidatorException) as e:
        str_t(True)


def test_int():
    int_t = vd.Int()
    assert int_t(355) == 355

    with pytest.raises(vd.ValidatorException) as e:
       int_t("hello world")
    with pytest.raises(vd.ValidatorException) as e:
       int_t(0.444)


def test_bool():
    bool_t = vd.Bool()
    assert bool_t(True) == True

    with pytest.raises(vd.ValidatorException) as e:
       bool_t("hello world")
    with pytest.raises(vd.ValidatorException) as e:
       bool_t(0.444)
    with pytest.raises(vd.ValidatorException) as e:
       bool_t(42)


def test_float():
    float_t = vd.Float()
    assert float_t(0.444) == 0.444

    with pytest.raises(vd.ValidatorException) as e:
       float_t("hello world")
    with pytest.raises(vd.ValidatorException) as e:
       float_t(True)
    with pytest.raises(vd.ValidatorException) as e:
       float_t(4)
