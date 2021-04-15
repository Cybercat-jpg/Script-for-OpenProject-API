#!/usr/bin/env python3

#######################################################################
# This script can send projects to OpenProject.
# You need to define a project identifier without spaces in lowercase.
# E.g. "my_project"
# It also needs a project name.
# Everything else is optional, like status and status description.
# You may need to change the url to your OpenProject.
# authkey can be created using postman, you can find help here:
# https://intranet.mpi-bn.mpg.de:8443/display/Bioinf/Openproject
#######################################################################

__author__ = "Yvonne Pfeifer"
__version__= "1.0"
__status__= "tested"

import sys
import argparse # Parsing arguments with Python
import requests # for API HTML Requests
import json # for json formatting

#### initializing variables ####
pident = ""
pname = ""
pstatus = "on track" #Default Project status
pdescription = "Everything is ***fine***" #Default project status description
authkey = TOKEN #environment variable of API token
url = 'http://XXX:8080/api/v3/projects/' #URL for the POST-Request

#### Parser Arguments ####
parser = argparse.ArgumentParser()
parser.add_argument("-i", "--ident", help="project identifier. Must not contain spaces!")
parser.add_argument("-n", "--name", help="Name of the project")
parser.add_argument("-s", "--status", help="Optional. Add project status. Acceppts <on track>, <at risk> or <off track> \n"
                                           "if not specified, status set to <on track>")
parser.add_argument("-d", "--descript", help="Optional. Add description to project status")
args = parser.parse_args()

pident = args.ident
pname = args.name
pstatus = args.status

if args.status:
    pstatus = args.status

if args.descript:
    pdescription = args.descript


payload = {
    "identifier": pident,
    "name": pname,
    "status": pstatus,
    "statusExplanation": {
        "format": "markdown",
        "raw": pdescription,
        "html": "<p>" + pdescription +"</p>"
    }
}
r = requests.post(
    url,
    data= json.dumps(payload),
    headers={'Content-Type': 'application/json',
             'X-Requested-With': 'XMLHttpRequest',
             'Authorization': 'Bearer ' + authkey}
)
print(r.text)

#r = requests.get('http://172.16.12.178:8080/api/v3/projects/', headers={'Authorization': 'Bearer ' + authkey})
#print(r.text)
