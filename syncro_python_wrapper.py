## SyncroMSP Python Wrapper ##
## A NETWORK GUY'S ATTEMPT AT BEING A CODER ##
##
## www.cybertek.systems ##

##Install the following dependencies!
import requests
from requests.structures import CaseInsensitiveDict
import os

## Find Main Variables from ENV
baseurl = os.environ['baseurl']
bearertoken = os.environ['bearertoken']

#Setup Requests Headers
headers = CaseInsensitiveDict()
headers["Accept"] = "application/json"
headers["Authorization"] = "Bearer " + bearertoken


####
#### BASIC API REQUESTS
####

##Create getUser class##
def getUser(id):
    url = baseurl + "users/" + str(id)
    resp = requests.get(url, headers=headers)
    userinfo = resp.json()['user']
    return userinfo

##Create getUsers class##
def getUsers():
    url = baseurl + "users"
    resp = requests.get(url, headers=headers)
    users = resp.json()['users']
    return users

##Create getUserEmail class##
def getUseremail(id):
    url = baseurl + "users/" + str(id)
    resp = requests.get(url, headers=headers)
    userinfo = resp.json()['user']['email']
    return userinfo

def getUserfullname(id):
    url = baseurl + "users/" + str(id)
    resp = requests.get(url, headers=headers)
    userinfo = resp.json()['user']['full_name']
    print(userinfo)
    return userinfo



###
### Complex API Requests
###