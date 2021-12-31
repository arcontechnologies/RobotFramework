from exceler import read_excel_as_table
from RPA.Tables import Tables
from variables import today
import emailer

from RPA.Browser.Selenium import Selenium
from RPA.Robocorp.Vault import Vault
from robot.api import logger

import logging
import sys

from playwright.sync_api import sync_playwright

stdout = logging.StreamHandler(sys.stdout)

logging.basicConfig(
    level=logging.INFO,
    format="[{%(filename)s:%(lineno)d} %(levelname)s - %(message)s",
    handlers=[stdout],
)

lib = Selenium()


secret = Vault().get_secret("credentials")

username = secret["username"] #"aidemobot@gmail.com"
password = secret["password"] # "Dasilva2010"

def connect_to_sangoma():
    lib.open_available_browser("https://portal.sangoma.com/")
    lib.input_text("id:email_address", username)
    lib.input_text("id:password", password)
    lib.click_button("css=button[class=\"btn btn-primary btn-block\"]")
    selected_option = "//span[text()='Users/Customers']"
    lib.wait_until_element_is_visible(selected_option) # must read doc
    lib.click_element(selected_option) # must read doc
    selected_option = "//a[text()='List Users']"
    lib.click_element(selected_option)
    import time
    time.sleep(5)
    logger.info("Connection to Sangoma has been completed.", html=True)

def connect_with_playwright():
    with sync_playwright() as p:
        for browser_type in [p.chromium]:
            browser = browser_type.launch()
            page = browser.new_page()
            page.goto('http://whatsmyuseragent.org/')
            page.screenshot(path=f'my-browser-specs-{browser_type.name}.png')
            browser.close()

def email_to_send():
    receiver_name = "Ali"
    name = f"{receiver_name}"
    recipient = "aidemobot@gmail.com"
    subject = "This a Robot speaking to Ali!"
    body = (
        f"Hi, {name}! "
        f"Remember that you have to finish your wonderful robot and get it up and running on {today()}."
    )
    emailer.send_outlook_email(recipient, subject, body)

def get_outlook_emails():
    account_name = "ali.belcaid@datapiens.com"
    folder_name = "Inbox"
    emails = emailer.get_outlook_email(account_name,folder_name)
    for email in emails:
        #print(email)
        print(email["Sender"] + " **** " + email["Subject"])
        
def read_from_excel():
    table = Tables()
    path = "D:\\RobotFramework\\documents\\persons.xlsx"
    table = read_excel_as_table(path)
    rows, columns = table.dimensions
    print(rows,columns) 
    for i in range(1, rows):
        row = table.get_row(i)
        print(row["Name"] + " *** " + row["email"] + " *** " + row["Location"])
        table.group_by_column

if __name__ == "__main__":
    LOGGER = logging.getLogger(__name__)
    #connect_to_sangoma()
    #email_to_send()
    
