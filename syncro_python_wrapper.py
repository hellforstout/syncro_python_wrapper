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

def getAppointment(id):
    url = baseurl + "appointments/" + str(id)
    resp = requests.get(url, headers=headers)
    appointment = resp.json()['appointment']
    return appointment
def getAppointments():
    url = baseurl + "appointments"
    resp = requests.get(url, headers=headers)
    appointments = resp.json()['appointments']
    return appointments

def getAsset(id):
    url = baseurl + "customer_assets/" + str(id)
    resp = requests.get(url, headers=headers)
    asset = resp.json()['asset']
    return asset
def getAssets():
    url = baseurl + "customer_assets"
    resp = requests.get(url, headers=headers)
    assets = resp.json()['assets']
    return assets

def getContact(id):
    url = baseurl + "contacts/" + str(id)
    resp = requests.get(url, headers=headers)
    contact = resp.json()['contact']
    return contact

def getContacts():
    url = baseurl + "contacts"
    resp = requests.get(url, headers=headers)
    contacts = resp.json()['contacts']
    return contacts

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
def getItems():
    url = baseurl + "items"
    resp = requests.get(url, headers=headers)
    items = resp.json()['items']
    return items

def getLead(id):
    url = baseurl + "leads/" + str(id)
    resp = requests.get(url, headers=headers)
    lead = resp.json()['lead']
    return lead

def getLeads():
    url = baseurl + "leads"
    resp = requests.get(url, headers=headers)
    leads = resp.json()['leads']
    return leads
def getLineitems():
    url = baseurl + "line_items"
    resp = requests.get(url, headers=headers)
    lineitems = resp.json()['line_items']
    return lineitems
def getPaymentmethods():
    url = baseurl + "payment_methods"
    resp = requests.get(url, headers=headers)
    paymentmethods = resp.json()['payment_methods']
    return paymentmethods
def getPayment(id):
    url = baseurl + "payments/" + str(id)
    resp = requests.get(url, headers=headers)
    payment = resp.json()['payment']
    return payment
def getPayments():
    url = baseurl + "payments"
    resp = requests.get(url, headers=headers)
    payments = resp.json()['payments']
    return payments

def getPortalusers():
    url = baseurl + "portal_users"
    resp = requests.get(url, headers=headers)
    portalusers = resp.json()['portal_users']
    return portalusers
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

def getPurchaseorder(id):
    url = baseurl + "purchase_orders/" + str(id)
    resp = requests.get(url, headers=headers)
    purchaseorder = resp.json()['purchase_order']
    return purchaseorder

def getPurchaseorders():
    url = baseurl + "purchase_orders"
    resp = requests.get(url, headers=headers)
    purchaseorders = resp.json()['purchase_orders']
    return purchaseorders

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

def getSchedule(id):
    url = baseurl + "schedules/" + str(id)
    resp = requests.get(url, headers=headers)
    schedule = resp.json()['schedule']
    return schedule
def getSchedules():
    url = baseurl + "schedules"
    resp = requests.get(url, headers=headers)
    schedules = resp.json()['schedules']
    return schedules
def getTicket(id):
    url = baseurl + "tickets/" + str(id)
    resp = requests.get(url, headers=headers)
    ticket = resp.json()['ticket']
    return ticket

def getSettings():
    url = baseurl + "settings"
    resp = requests.get(url, headers=headers)
    settings = resp.json()['settings']
    return settings

def getSettingstabs():
    url = baseurl + "settings/tabs"
    resp = requests.get(url, headers=headers)
    tabs = resp.json()['tabs']
    return tabs
def getTickets():
    url = baseurl + "tickets"
    resp = requests.get(url, headers=headers)
    tickets = resp.json()['tickets']
    return tickets

def getTicketssettings():
    url = baseurl + "tickets/settings"
    resp = requests.get(url, headers=headers)
    ticketsettings = resp.json()
    return ticketsettings

def getTickettimers():
    url = baseurl + "tickets_timers"
    resp = requests.get(url, headers=headers)
    ticketstimers = resp.json()['tickets_timers']
    return ticketstimers


def getTimelogs():
    url = baseurl + "timelogs"
    resp = requests.get(url, headers=headers)
    timelogs = resp.json()['timelogs']
    return timelogs

def getTimelogs_user(id):
    url = baseurl + "timelogs?user_id=" + str(id)
    resp = requests.get(url, headers=headers)
    usertimelogs = resp.json()['timelogs']
    return usertimelogs

def getTimelogs_user_last(id):
    url = baseurl + "timelogs/last?user_id=" + str(id)
    resp = requests.get(url, headers=headers)
    lastusertimelogs = resp.json()['timelogs']
    return lastusertimelogs

def getVendor(id):
    url = baseurl + "vendors/" + str(id)
    resp = requests.get(url, headers=headers)
    vendor = resp.json()['vendor']
    return vendor

def getVendors():
    url = baseurl + "vendors"
    resp = requests.get(url, headers=headers)
    vendors = resp.json()['vendors']
    return vendors
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