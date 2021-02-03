import pytest
from com.helpers.string_func import *

## -----------------------------------------------------------------------------------------
## test convertCamelCase


def test_convertCamelCase_empty():
    assert convertCamelCase("") == ""


def test_convertCamelCase_twoWords():
    assert convertCamelCase("HelloWorld") == "Hello World"


def test_convertCameCase_threeWords():
    assert convertCamelCase("HelloAgainWorld") == "Hello Again World"


## -----------------------------------------------------------------------------------------
# test cleanUpDataStrings


def test_cleanUpDataStrings_usdodeast():
    assert cleanUpDataStrings("bobusdodeast") == "bobUSDoDEast"
