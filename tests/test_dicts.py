import valedictory as vd
import pytest


@pytest.fixture()
def d1():
    return dict(one="hello", two="world")


def test_dict(d1):
    dict_t = vd.Dict(one=vd.Str(), two=vd.Str())

    assert dict_t(d1) == d1
    with pytest.raises(vd.ValidatorException) as e:
        dict_t(4)
        dict_t(dict(one=1, two="2"))
        dict_t(int_list)
