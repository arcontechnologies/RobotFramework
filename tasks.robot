*** Settings ***
Documentation     Robot that do a lot of things
Library           tasks.py
Library           pdfer.py
Variables         variables.py

*** Tasks ***
Experiments task
    connect to sangoma
    #Log    ${TODAY}
    #email to send
    #get outlook emails
    #read from excel
    #get pdf widgets
    #connect with playwright
