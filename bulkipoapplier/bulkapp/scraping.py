from time import sleep
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select
import os
# disable logging for webdriver
os.environ['WDM_LOG_LEVEL'] = '0'
# import Driver installer
from webdriver_manager.chrome import ChromeDriverManager
class web_driver():  
    #for Heruko deployment
    """ options = webdriver.ChromeOptions()
    options.headless = False
    # add user agent
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--no-sandbox")
  
    options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
    options.add_argument("--disable-gpu") """

   
    # function that open the browser
    def open_browser(self):
        # for Heruko deployment
        # self.driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), chrome_options=self.options)
        options = webdriver.ChromeOptions()
        options.headless = True
        # add user agent
        options.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36')
        options.add_argument("--start-maximized")
        options.add_argument("--disable-extensions")
        options.add_argument("--disable-gpu")
        
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--no-sandbox")
        chrome_driver_path = ChromeDriverManager().install()
        self.driver= webdriver.Chrome(chrome_driver_path, options=options)
        self.wait = WebDriverWait(self.driver,15)
        self.driver.get("https://meroshare.cdsc.com.np/#/login")
 

def login(dp,username,password):
    web_driver.wait.until(EC.presence_of_element_located((By.TAG_NAME, "app-login")))
    # Login
    web_driver.wait.until(EC.presence_of_element_located((By.NAME, "selectBranch")))
    web_driver.driver.find_element(By.NAME ,"selectBranch").click()
    dpEntry = web_driver.driver.find_element(By.CLASS_NAME, "select2-search__field")   # Find the Dp Entry Box
    dpEntry.click()  # Click on the Dp Entry Box
    dpEntry.send_keys(dp)  # Enter the Dp Id
    dpEntry.send_keys(Keys.ENTER)  # Press Enter
    web_driver.driver.find_element(By.NAME ,"username").send_keys(username)  # Enter the Username
    web_driver.driver.find_element(By.NAME ,"password").send_keys(password)  # Enter the Password
    web_driver.driver.find_element(By.CLASS_NAME ,"sign-in").click()        # Click on the Sign In Button
    # check the url


def goto_asba():
    web_driver.wait.until(EC.presence_of_element_located((By.TAG_NAME, "app-dashboard")))
    web_driver.wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='sideBar']/nav/ul/li[8]/a/span")))
    web_driver.driver.find_element(By.XPATH,"//*[@id='sideBar']/nav/ul/li[8]/a/span").click()

    web_driver.wait.until(EC.url_to_be("https://meroshare.cdsc.com.np/#/asba"))  # Wait until the page url changes to the asba page



def open_ipo_lister():
    web_driver.driver.find_element(By.XPATH,'//*[@id="main"]/div/app-asba/div/div[1]/div/div/ul/li[1]').click()
    web_driver.wait.until(EC.presence_of_element_located((By.TAG_NAME, "app-applicable-issue")))
    web_driver.driver.implicitly_wait(1)
    IPOlist = web_driver.driver.find_elements(By.CLASS_NAME,"company-name")
    ipolist = []
    for i in IPOlist:
        ipolist.append(i.text)
    return ipolist

def ipo_selector(ind=''):
    if (ind == 0):
        iposelector_index = ''
    else:
        iposelector_index = '[{}]'.format(ind)

    apply_btn = web_driver.driver.find_element(By.XPATH,'//*[@id="main"]/div/app-asba/div/div[2]/app-applicable-issue/div/div/div/div/div' + str(iposelector_index) +'/div/div[2]/div/div[4]/button')
    apply_btn.click()
    bank_selector()



  


def bank_selector():
     # wait until the page url changes to other than asba page
    web_driver.wait.until_not(EC.url_to_be("https://meroshare.cdsc.com.np/#/asba"))
    # select and click element with name selectBank and click on it
    bank_dropdown = Select(web_driver.driver.find_element(By.XPATH,"//*[@name='selectBank']"))
    bank_list = bank_dropdown.options
    print(bank_list)
    
    # select the bank
    web_driver.driver.find_element(By.XPATH,"//*[@id='selectBank']/option[2]").click()
    

    """ if len(bank_list) > 2: 
        banks = []  # list bank accounts
        index = 1
        for bank in bank_list:
            banks.append([index-1, bank.text])
            index += 1

        banks.pop(0)
        selected_bank = 2
        web_driver.driver.find_element(By.XPATH,"//*[@id='selectBank']/option[" + str(selected_bank-1) + "]").click()
    else: """
        
def applySuccess(qty,crn,pin):
    appliedKitta = web_driver.driver.find_element(By.NAME,"appliedKitta")
    appliedKitta.send_keys(qty)
    crninput = web_driver.driver.find_element(By.NAME,"crnNumber")
    crninput.send_keys(crn)

    web_driver.driver.find_element(By.NAME,"disclaimer").click()

    # submit the form
    submit = web_driver.driver.find_element(By.XPATH,"//*[@id='main']/div/app-issue/div/wizard/div/wizard-step[1]/form/div[2]/div/div[5]/div[2]/div/button[1]")
    web_driver.wait.until(EC.element_to_be_clickable((By.XPATH,"//*[@id='main']/div/app-issue/div/wizard/div/wizard-step[1]/form/div[2]/div/div[5]/div[2]/div/button[1]")))
    submit.click()
    web_driver.wait.until(EC.presence_of_element_located((By.NAME,"transactionPIN")))

    web_driver.driver.find_element(By.NAME,"transactionPIN").send_keys(pin)
    pin_submit = web_driver.driver.find_element(By.XPATH,"//*[@id='main']/div/app-issue/div/wizard/div/wizard-step[2]/div[2]/div/form/div[2]/div/div/div/button[1]")
    web_driver.wait.until(EC.element_to_be_clickable((By.XPATH,"//*[@id='main']/div/app-issue/div/wizard/div/wizard-step[2]/div[2]/div/form/div[2]/div/div/div/button[1]")))
    pin_submit.click()
     
def close_browser():
    web_driver.driver.close()
    web_driver.driver.quit()



