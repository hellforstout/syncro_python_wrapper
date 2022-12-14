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
def getContract(id):
    url = baseurl + "contracts/" + str(id)
    resp = requests.get(url, headers=headers)
    contract = resp.json()['contract']
    return contract

def getContracts():
    url = baseurl + "contracts"
    resp = requests.get(url, headers=headers)
    contracts = resp.json()['contracts']
    return contracts

def getCustomer(id):
    url = baseurl + "customers" + str(id)
    resp = requests.get(url, headers=headers)
    customer = resp.json()['customer']
    return customer

def getCustomers():
    url = baseurl + "customers"
    resp = requests.get(url, headers=headers)
    customers = resp.json()['customers']
    return customers

def getEstimate(id):
    url = baseurl + "estimates" + str(id)
    resp = requests.get(url, headers=headers)
    estimate = resp.json()['estimate']
    return estimate

def getEstimates():
    url = baseurl + "estimates"
    resp = requests.get(url, headers=headers)
    estimates = resp.json()['estimates']
    return estimates

def getInvoice(id):
    url = baseurl + "invoices/" + str(id)
    resp = requests.get(url, headers=headers)
    invoice = resp.json()['invoice']
    return invoice

def getInvoices():
    url = baseurl + "invoices"
    resp = requests.get(url, headers=headers)
    invoices = resp.json()['invoices']
    return invoices

def getProduct(id):
    url = baseurl + "products/" + str(id)
    resp = requests.get(url, headers=headers)
    product = resp.json()['product']
    return product

def getProducts():
    url = baseurl + "products"
    resp = requests.get(url, headers=headers)
    products = resp.json()['products']
    return products

def getProductcategories():
    url = baseurl + "products/categories"
    resp = requests.get(url, headers=headers)
    categories = resp.json()['categories']
    return categories

def getRMMalert(id):
    url = baseurl + "rmm_alerts/" + str(id)
    resp = requests.get(url, headers=headers)
    alert = resp.json()['rmm_alert']
    return alert

def getRMMalerts():
    url = baseurl + "rmm_alerts?status=active"
    resp = requests.get(url, headers=headers)
    alerts = resp.json()['rmm_alerts']
    return alerts

def getTicket(id):
    url = baseurl + "tickets/" + str(id)
    resp = requests.get(url, headers=headers)
    ticket = resp.json()['ticket']
    return ticket

def getTickets():
    url = baseurl + "tickets"
    resp = requests.get(url, headers=headers)
    tickets = resp.json()['tickets']
    return tickets

def getUser(id):
    url = baseurl + "users/" + str(id)
    resp = requests.get(url, headers=headers)
    user = resp.json()['user']
    return user

def getUsers():
    url = baseurl + "users"
    resp = requests.get(url, headers=headers)
    users = resp.json()['users']
    return users

def getUseremail(id):
    url = baseurl + "users/" + str(id)
    resp = requests.get(url, headers=headers)
    userinfo = resp.json()['user']['email']
    return userinfo

def getUserfullname(id):
    url = baseurl + "users/" + str(id)
    resp = requests.get(url, headers=headers)
    userinfo = resp.json()['user']['full_name']
    return userinfo

def getWikipages():
    url = baseurl + "wiki_pages"
    resp = requests.get(url, headers=headers)
    wiki_pages = resp.json()['wiki_pages']
    return wiki_pages


###
### Complex API Requests
###