import re


def convertCamelCase(str):
    s1 = re.sub('(.)([A-Z][a-z]+)', r'\1 \2', str)
    return re.sub('([a-z0-9])([A-Z])', r'\1 \2', s1)


def cleanUpDataStrings(str):
    str = str.replace("usdodeast", "USDoDEast").replace(
        "usdodcentral",
        "USDoDCentral").replace("usgovarizona", "USGovArizona").replace(
            "usgoviowa",
            "USGovIowa").replace("usgovtexas",
                                 "USGovTexas").replace("usgovvirginia",
                                                       "USGovVirginia")
    str = str.replace("Cosmos DB",
                      "CosmosDB").replace("Azure AD", "AzureAD").replace(
                          "Api", "API").replace("Io T", "IoT").replace(
                              "Sql", "SQL").replace("Power BI", "PowerBI")
    return str
