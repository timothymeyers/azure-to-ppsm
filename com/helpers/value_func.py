## Contains helper functions for parsing ServiceMapping JSON "value" objects

from com.helpers.string_func import cleanUpDataStrings, convertCamelCase


def getRegionFromValue(value):
    idSplit = value['id'].split('.')

    if len(idSplit) > 1:
        if value['properties']['region']:
            # nearly all splits > 1 are for regions, but the 'region' field is always populated.
            return cleanUpDataStrings(idSplit[1])

    return ""


def getCALServiceNameFromValue(value):

    idSplit = value['id'].split('.')

    region = ""
    if len(idSplit) > 1:
        if value['properties']['region']:
            # nearly all splits > 1 are for regions, but the 'region' field is always populated.
            region = cleanUpDataStrings(idSplit[1])
        else:
            # special case for strange Frontend/Backend/ServiceEndpoint splits.
            idSplit[0] = value['id']

    calServiceName = idSplit[0]

    if region and value['properties']['region'] == region.lower():
        calServiceName += ' (' + region + ')'

    return calServiceName


def getCALTitle(cloud, value):

    cloud = convertCamelCase(cloud)

    systemService = ""

    if value['properties']['systemService']:
        systemService = ' / ' + convertCamelCase(
            value['properties']['systemService'])

    return cloud + systemService