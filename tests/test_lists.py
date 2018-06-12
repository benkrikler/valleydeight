import valedictory as vd
import pytest


@pytest.fixture()
def str_list():
    return list("hello world")


@pytest.fixture()
def int_list():
    return [1, 4, 7]


@pytest.fixture()
def int_list():
    return [1, 4, 7]


def test_list1(str_list, int_list):
    list_t1 = vd.List(vd.Str())

    assert list_t1(str_list) == str_list
    with pytest.raises(vd.ValidatorException) as e:
        list_t1(4)
        list_t1(dict(one=1, two="2"))
        list_t1(int_list)


def test_list2(str_list, int_list):
    list_t2 = vd.List(vd.Int())
    assert list_t2(int_list) == int_list
    with pytest.raises(vd.ValidatorException) as e:
        list_t2(4)
        list_t2(dict(one=1, two="2"))
        list_t2(str_list)
