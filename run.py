import csv

from com.parser import ServiceMappingParser
from com.helpers.value_func import *
from com.helpers.string_func import *

csv.register_dialect('calDialect',
                     delimiter=',',
                     quotechar='"',
                     lineterminator='\n')


def createCsvFileFromDictionary(filename, header, dictionary):
    with open(filename, 'w') as csvfile:
        # creating a csv dict writer object
        writer = csv.DictWriter(csvfile,
                                fieldnames=header,
                                dialect='calDialect')

        # writing headers (field names)
        writer.writeheader()

        # writing data rows
        writer.writerows(dictionary)


def main():

    x = ServiceMappingParser()
    x.setJSONwithLatest()
    x.constructCvsDictionary()

    createCsvFileFromDictionary("tmp/"+x.getCvsFilename(), x.getCvsHeaders(),
                                x.getCvsDictionary())

    print('\n---- All finished creating: <' + x.getCvsFilename() + '>\n')


main()
