import urllib.request, time, datetime, csv
import json

from com.config.constants import HEADERS, AZ_JSON_URL
from com.helpers.string_func import cleanUpDataStrings
from com.helpers.value_func import getCALServiceNameFromValue,getCALTitle,getRegionFromValue

from com.config.default_architecture import ports


class ServiceMappingParser:
    def __init__(self, config=ports):
        self.__config = config
        self.__dictionary = []

    def setConfig(self, config):
        self.__config = config

    def getConfig(self):
        return self.__config

    def setJSON(self, jsonParam):
        self.__json = jsonParam

    def setJSONfromURL(self, jsonUrl):
        with urllib.request.urlopen(jsonUrl) as url:
            self.__json = json.loads(url.read())

    def setJSONwithLatest(self):
        self.setJSONfromURL(AZ_JSON_URL)

    def getJSON(self):
        return self.__json

    def getCvsFilename(self):
        #prefix = 'tmp/ServiceTags_'
        prefix = ''
        extension = '.csv'

        ts = time.time()
        timestamp = str(
            datetime.datetime.fromtimestamp(ts).strftime('%Y%m%d.%H%M%S'))

        cloud = self.__json['cloud']
        changeNumber = str(self.__json['changeNumber'])

        return prefix + cloud + '_' + changeNumber + '-' + timestamp + extension

    def getCvsHeaders(self):
        return HEADERS

    def getCvsDictionary(self):
        return self.__dictionary

    def constructCvsDictionary(self):
        self.__dictionary = []

        # n^3 nested loop is ... awesome?

        for value in self.__json['values']:
            calServiceName = getCALServiceNameFromValue(value)
            calTitle = getCALTitle(self.__json['cloud'], value)
            portList = self.__config.get(value['properties']['systemService'])

            
            for addressPrefix in value['properties']['addressPrefixes']:
                
                if not portList:
                    # print (value['properties']['systemService'])
                    portList = []

                for port in portList:
                    portRow = {
                        'Network U': port['classification'],
                        'Network C': "",
                        'Low Port': port['port'],
                        'High Port': port['port'],
                        'Protocol': port['protocol'],
                        'Address Prefix': addressPrefix,
                        'Service Name': cleanUpDataStrings(calServiceName),
                        'Title': cleanUpDataStrings(calTitle),
                        '(I) Ext to DoD GW': "",
                        '(O) DoD GW to Ext': "",
                        '(I) DoD GW -> DoD DMZ or RDTE': "",
                        '(O) DoD DMZ or RDTE -> DoD GW': "",
                        '(I) DoD GW to DISN': "",
                        '(O) DISN to DoD GW': "",
                        '(I) DISN to Enclave GW': "",
                        '(O) Enclave GW to DISN': "",
                        '(I) Enclave GW to Enclave DMZ': "",
                        '(O) Enclave DMZ to Enclave GW': "",
                        '(I) Enclave GW to Enclave': "",
                        '(O) Enclave to Enclave GW': "",
                        '(I) Ext ISP to Enclave GW': "",
                        '(O) Enclave GW to Ext ISP': "",
                        '(IO) Multiple AO E2E Tunnel': "",
                        '(IO) Single AO E2E Tunnel': "",
                        'Comments': port['comment'],
                        '|': '|',

                        # RAW DATA FOLLOWS
                        'name': value['name'],
                        'id': value['id'],
                        'changeNumber': value['properties']['changeNumber'],
                        'region': value['properties']['region'],
                        'Region (cleaned)': getRegionFromValue(value),
                        'platform': value['properties']['platform'],
                        'systemService': value['properties']['systemService'],
                        'addressPrefix': addressPrefix
                    }

                    self.__dictionary.append(portRow)
