#Import syncro_python_wrapper for functions. Import requests for functionality
from syncro_python_wrapper import *
import requests
import pandas
from pandas.io.json import json_normalize
import pandas as pd


## Test ## Playing with Pandas ##
#url = "https://api.exchangerate-api.com/v4/latest/USD"
#df = pd.read_json(url)
#print(df)

##############################################
#
#     Use set_environment_variables.py to set baseurl and bearertoken
#
################################################

############  Script Example starts below ############

#Testing getUsers() class
#allusers = getUsers()
#print(allusers)

#Testing getContracts() class
contracts = getContracts()
print(contracts)

#Testing getCustomers() class
#customers = getCustomers()
#print(customers)

#Print users
#print(allusers)

#Print subsection of users
#print(allusers[2])