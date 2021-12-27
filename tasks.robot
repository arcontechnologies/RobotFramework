*** Settings ***
Documentation     Robot that connect to Sangoma website.
Library           tasks.py
Variables         MyVariables.py

*** Tasks ***
Sangoma task
    connect to sangoma
    Log    ${TODAY}
