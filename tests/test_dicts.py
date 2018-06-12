import valedictory as vd
import pytest


@pytest.fixture()
def d1():
    return dict(one="hello", two="world")


def test_dict(d1):
    dict_t = vd.Dict(one=vd.Str(), two=vd.Str())

    assert dict_t(d1) == d1

    parsed_dict = dict_t(d1)
    assert parsed_dict.one == "hello"
    assert parsed_dict.two == "world"
    assert parsed_dict["one"] == "hello"
    assert parsed_dict["two"] == "world"

    with pytest.raises(vd.ValidatorException):
        dict_t(4)
    with pytest.raises(vd.ValidatorException):
        dict_t(dict(one=1, two="2"))
    with pytest.raises(vd.ValidatorException):
        dict_t([1, 2, 3])
    with pytest.raises(vd.ValidatorException):
        dict_t(dict(one=1, two="2", three=3))


def test_named_dict():
    nd = vd.dict_types._Namespace(one="sadlfiyhasd", two=434)
    nd.hey = "teacher"
    with pytest.raises(AttributeError):
        left = nd.not_valid


def test_dict_unknown_keys(d1):
    dict_t = vd.Dict(one=vd.Str(), two=vd.Str()).opts(only_known_keys=False)

    d1["three"] = 79
    assert dict_t(d1) == d1

    parsed_dict = dict_t(d1)
    assert parsed_dict.one == "hello"
    assert parsed_dict.two == "world"
    assert parsed_dict["one"] == "hello"
    assert parsed_dict["two"] == "world"
    assert parsed_dict["three"] == 79


def test_dict_default_value(d1):
    dict_t = vd.Dict(one=vd.Str(), two=vd.Str()).opts(only_known_keys=False, default_val_type=vd.Str())

    d1["three"] = "a string"
    assert dict_t(d1) == d1

    parsed_dict = dict_t(d1)
    assert parsed_dict.one == "hello"
    assert parsed_dict.two == "world"
    assert parsed_dict["one"] == "hello"
    assert parsed_dict["two"] == "world"
    assert parsed_dict["three"] == "a string"

    d1["three"] = 79
    with pytest.raises(vd.ValidatorException):
        dict_t(d1)


def test_dict_need_all_keys(d1):
    dict_t = vd.Dict(one=vd.Str(), two=vd.Str(), three=vd.Bool()).opts(need_all_keys=True)

    with pytest.raises(vd.ValidatorException):
        dict_t(d1)

    d1["three"] = True
    assert dict_t(d1) == d1
