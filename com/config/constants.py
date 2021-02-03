AZ_GOV_URL = 'https://download.microsoft.com/download/6/4/D/64DB03BF-895B-4173-A8B1-BA4AD5D4DF22/ServiceTags_AzureGovernment_20210201.json'
AZ_PUB_URL = 'https://download.microsoft.com/download/7/1/D/71D86715-5596-4529-9B13-DA13A5DE5B63/ServiceTags_Public_20210201.json'

AZ_JSON_URL = AZ_PUB_URL

HEADERS = [
    # This is DoD PPSM format
    'Network U', 
    'Network C', 
    'Low Port', 
    'High Port', 
    'Protocol', 
    'Address Prefix', 
    'Service Name', 
    'Title', 
    '(I) Ext to DoD GW', 
    '(O) DoD GW to Ext', 
    '(I) DoD GW -> DoD DMZ or RDTE', 
    '(O) DoD DMZ or RDTE -> DoD GW', 
    '(I) DoD GW to DISN', 
    '(O) DISN to DoD GW', 
    '(I) DISN to Enclave GW', 
    '(O) Enclave GW to DISN', 
    '(I) Enclave GW to Enclave DMZ', 
    '(O) Enclave DMZ to Enclave GW', 
    '(I) Enclave GW to Enclave', 
    '(O) Enclave to Enclave GW', 
    '(I) Ext ISP to Enclave GW', 
    '(O) Enclave GW to Ext ISP', 
    '(IO) Multiple AO E2E Tunnel', 
    '(IO) Single AO E2E Tunnel',
    'Comments',
    '|',
    
    # RAW DATA FOLLOWS
    'name',
    'id',
    'changeNumber',
    'region',
    'Region (cleaned)',
    'platform',
    'systemService',
    'addressPrefix'
]                  
