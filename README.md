# Introduction 
A converter that takes the Azure IP Ranges and Service Tags json file and converts it into a csv that resembles [DoD PPSM format](https://public.cyber.mil/connect/faq-ppsm/).

* [Az Public Cloud IP Ranges and Service Tags](https://www.microsoft.com/en-us/download/confirmation.aspx?id=56519)
* [US Gov Cloud IP Ranges and Service Tags](https://www.microsoft.com/en-us/download/confirmation.aspx?id=57063)

# Caveat Emptor
This code is not blessed or good by any means. It is the very first python program I ever wrote, so use with caution.

# Build and Test

Start the Python Virtual Environment

`python3 -m venv .venv`

`source .venv/bin/activate`

Execute Unit Tests

`python3 -m pytest -v`

Run application from command line

`python3 run.py`


# Notes

The [default_architecture.py](https://github.com/timothymeyers/azure-to-ppsm/blob/master/com/config/default_architecture.py) file maintains a list of services that appear in these JSON files. You can edit this file or create a new file in this format, with a limited list of services, custom ports, and comments for those ports, if you'd like.

The [constants.py](https://github.com/timothymeyers/azure-to-ppsm/blob/master/com/config/constants.py) file contains the current URLs of the Azure Commercial and Azure Government cloud JSON files. They may need to be occassionally updated.
