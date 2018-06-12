[![Build Status](https://img.shields.io/travis/benkrikler/valleydeight/master.svg?style=for-the-badge&longCache=true)](https://travis-ci.org/benkrikler/valleydeight)
[![codecov](https://img.shields.io/codecov/c/github/benkrikler/valleydeight/master.svg?style=for-the-badge&longCache=true)](https://codecov.io/gh/benkrikler/valleydeight)

Valleydeight
===========

> Effective dictionary and nested object validation for Python

Lately, I've found myself writing many YAML-based config files.
Being able to quickly and easily put together a schema for these files has become helpful, and the existing options out there were proving awkward to me.

The approach here is to work directly on the resulting python objects.
This allows the code here to be useful in many other situations, and to validate other types of markup easily (eg JSON, XML (?), pickled primitives, etc).

## Installation
(Coming soon:)
```
pip install --user valleydeight
```

## Usage
To be able to validate an object, you must build up a Validator.  Doing this is straight forward for most types.
There are currently many types of Validators implemented:
* Primitive types: `Str`, `Int`, `Float`, `Bool`
* Lists of items: `List`, `FixedList`
* Dictionaries of items: `Dict`
* Mixed types: `Choice`
* Custom objects: `Object`
* A validator that accepts everything: `Pass`

To make a validator, simply instantiate one of the above classes, composing together the more complicated types where needed.
To use the validator call it with the object you wish to validate.

For example, say we wish to check that we have a list of dictionaries where each dictionary has a string called "name" and a boolean called "on":
```python
import valleydeight as vd

# Build the validator
validator = vd.List(vd.Dict(name=vd.Str(), on=vd.Bool()))

# Make a test object that should pass fine
test_object = [dict(name="hello", on=True), dict(name="World", on=False)]
parsed_object = validator(test_object)


# Make a test object that will fail, since one of the elements has the wrong type:
test_object = [dict(name="hello", on=True), dict(name="World", on=2018)]
parsed_object = validator(test_object)
# Raises ValidatorException
```

The `Choice` class allows us to make complicated "custom" types:
```python
import valleydeight as vd

# Something like a pythonic Enum with mixed types:
enum_t = vd.Choice("one", 4, True)

# A mixture of validator types:
mix_t = vd.Choice(vd.Str(), vd.Dict(name=vd.Str(), value=vd.Pass()).opts(need_all_keys=True))

# A mixture of specific values and generic types
mix_t = vd.Choice(10012, False, vd.Str(), vd.List(vd.Float()))
```

The difference between a `List` and a `FixedList` is that a `List` allows an
arbitrary number of items, which must all be the same type (although this can
be a `Choice` type), whereas a `FixedList` has both a fixed length and specific types for each element.

## Example program
For an example program see the script in the [`examples/`](https://github.com/benkrikler/valleydeight/tree/master/examples) directory on GitHub.
In addition the unit tests in the [`tests/`](https://github.com/benkrikler/valleydeight/tree/master/tests) directory might be informative.
