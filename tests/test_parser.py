import pytest
from com.parser import ServiceMappingParser

# "Constaints"

AZ_GOV_URL = 'https://download.microsoft.com/download/6/4/D/64DB03BF-895B-4173-A8B1-BA4AD5D4DF22/ServiceTags_AzureGovernment_20210201.json'
# AZ_PUB_URL = 'https://download.microsoft.com/download/7/1/D/71D86715-5596-4529-9B13-DA13A5DE5B63/ServiceTags_Public_20200824.json'
AZ_PUB_URL = 'https://download.microsoft.com/download/7/1/D/71D86715-5596-4529-9B13-DA13A5DE5B63/ServiceTags_Public_20210201.json'

JSON_TEST = {
    "changeNumber":
    0,
    "cloud":
    "TheCloud",
    "values": [{
        "name": "OneName",
        "id": "OneId",
        "properties": {
            "changeNumber":
            1,
            "region":
            "",
            "platform":
            "Azure",
            "systemService":
            "ActionGroup",
            "addressPrefixes": [
                "13.72.19.232/32", "52.127.5.156/30", "52.127.10.212/30",
                "52.244.65.137/32"
            ]
        }
    }]
}

# "Fixtures"

@pytest.fixture
def p():
    return ServiceMappingParser()

# "Test Cases"

def test_setJSONwithAZGov(p):
    p.setJSONfromURL(AZ_GOV_URL)
    j1 = p.getJSON()

    assert type(j1) == dict
    assert j1['changeNumber'] > 100
    assert j1['cloud'] == "AzureGovernment"

    # p.setJSONwithLatest()
    # j2 = p.getJSON()
    # assert type(j2) == dict
    # assert j2['changeNumber'] > 100  
    # assert j2['cloud'] == "AzureGovernment"

    # assert j1 == j2
    
def test_setJSONwithPubCloud(p):
    p.setJSONfromURL(AZ_PUB_URL)
    j = p.getJSON()
    assert type(j) == dict
    assert j['changeNumber'] > 100  
    assert j['cloud'] == "Public"

def test_setGetConfig(p):
    config = {
    'CONFIG':  
                    [{'port': '80', 'protocol': 'TCP (6)', 'io':'both' , 'classification':'U' , 'comment': ''},
                    {'port': '443', 'protocol': 'TCP (6)', 'io':'both' , 'classification':'U' , 'comment': ''}]
    }

    p.setConfig(config)

    assert p.getConfig() == config