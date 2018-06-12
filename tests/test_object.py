import valleydeight as vd
import pytest


@pytest.fixture()
def MyClass():
    class _aClass():
        def __init__(self, name, value):
            self.name = name
            self.value = value
    return _aClass


def test_object_dict(MyClass):
    object_t = vd.Object(MyClass)

    args = dict(name="first", value=355)
    instance = object_t(args)

    assert instance.name == "first"
    assert instance.value == 355


def test_object_list(MyClass):
    object_t = vd.Object(MyClass)

    args = ["first", 355]
    instance = object_t(args)

    assert instance.name == "first"
    assert instance.value == 355

    object_t = vd.Object(MyClass, expand_lists=False)
    with pytest.raises(TypeError) as e:
        object_t(args)


def test_list_object(MyClass):
    object_t = vd.List(vd.Object(MyClass))

    args = [dict(name="first", value=355),
            dict(name="second", value=0.55),
           ]
    instance = object_t(args)

    assert instance[0].name == "first"
    assert instance[0].value == 355
    assert instance[1].name == "second"
    assert instance[1].value == 0.55


def test_object_args_dict(MyClass):
    arg_spec = vd.Dict(name=vd.Str(), value=vd.Int())
    object_t = vd.Object(MyClass, args = arg_spec)

    args = dict(name="first", value=355)
    instance = object_t(args)

    assert instance.name == "first"
    assert instance.value == 355


def test_object_args_list(MyClass):
    arg_spec = vd.FixedList(vd.Str(), vd.Int())
    object_t = vd.Object(MyClass, args = arg_spec)

    args = ["first", 355]
    instance = object_t(args)

    assert instance.name == "first"
    assert instance.value == 355


def test_object_args_both(MyClass):
    arg_spec_dict = vd.Dict(name=vd.Str(), value=vd.Int())
    arg_spec_list = vd.FixedList(vd.Str(), vd.Int())
    arg_spec = vd.Choice(arg_spec_list, arg_spec_dict)

    object_t = vd.Object(MyClass, args = arg_spec)

    args = ["first", 355]
    instance = object_t(args)

    assert instance.name == "first"
    assert instance.value == 355

    args = dict(name="first", value=355)
    instance = object_t(args)

    assert instance.name == "first"
    assert instance.value == 355
