import pytest
from com.helpers.value_func import *

VALUE_ZERO = {
    "name": "",
    "id": "",
    "properties": {
        "changeNumber": 0,
        "region": "",
        "platform": "",
        "systemService": "",
        "addressPrefixes": []
    }
}

VALUE_ONE = {
    "name": "NameOne",
    "id": "IdOne",
    "properties": {
        "changeNumber": 0,
        "region": "regionone",
        "platform": "PlatformOne",
        "systemService": "systemServiceOne",
        "addressPrefixes": ["0.0.0.0/27"]
    }
}


def test_getRegionFromValue():
    assert getRegionFromValue(VALUE_ZERO) == ""
    assert getRegionFromValue(VALUE_ONE) == ""


def test_getRegionFromValue_RegionMismatch():
    value = {
        "name": "",
        "id": "id.REGION",
        "properties": {
            "changeNumber": 0,
            "region": "region",
            "platform": "",
            "systemService": "",
            "addressPrefixes": []
        }
    }

    assert getRegionFromValue(value) == "REGION"


def test_getCALServiceNameFromValue():
    assert getCALServiceNameFromValue(VALUE_ZERO) == ""
    assert getCALServiceNameFromValue(VALUE_ONE) == "IdOne"

def test_getCALServiceNameFromValue_SplitsWithRegion():
    value_region = {
        "name": "",
        "id": "id.REGION",
        "properties": {
            "changeNumber": 0,
            "region": "region",
            "platform": "",
            "systemService": "",
            "addressPrefixes": []
        }
    }

    assert getCALServiceNameFromValue(value_region) == "id (REGION)"

def test_getCALServiceNameFromValue_SplitsWithNoRegion():
    value_noregion = {
        "name": "",
        "id": "id.NOT_REGION",
        "properties": {
            "changeNumber": 0,
            "region": "",
            "platform": "",
            "systemService": "",
            "addressPrefixes": []
        }
    }

    assert getCALServiceNameFromValue(value_noregion) == "id.NOT_REGION"


def test_getCALTitle():
    assert getCALTitle("cloud", VALUE_ZERO) == "cloud"
    assert getCALTitle("cloud", VALUE_ONE) == "cloud / system Service One"
