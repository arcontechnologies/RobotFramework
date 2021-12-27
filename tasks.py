import  RPA.Robocorp.Vault

from RPA.Browser.Selenium import Selenium
from RPA.Robocorp.Vault import Vault
from robot.api import logger

import logging
import sys

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


if __name__ == "__main__":
    LOGGER = logging.getLogger(__name__)
    connect_to_sangoma()
    
