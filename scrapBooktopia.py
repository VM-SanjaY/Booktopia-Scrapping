import time
from selenium import webdriver
import random
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pandas as pd



def user_agent():
    data = [
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36",
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36",
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36",
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36",
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.192 Safari/537.36",
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36",
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36",
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36",
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.192 Safari/537.36",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36",
    ]
    agent = random.choice(data)
    return agent


options = Options()
u_agent = user_agent()
options.add_argument(f'--user-agent={u_agent}')
options.add_argument("--disable-popup-blocking")
options.add_argument("--disable-notifications")
options.add_argument('--ignore-certificate-errors')
options.add_argument('--ignore-ssl-errors')
# options.add_argument('--headless')
options.add_argument('--disable-gpu')
options.add_argument("--disable-extensions")
driver = webdriver.Chrome(options=options)
driver.implicitly_wait(15)
driver.delete_all_cookies()
userdata = input("Please mention the genre you want to get - ")
while True:
    howmany = input("Enter the number of books you need: ")
    if howmany.isdigit():
        howmany = int(howmany)
        break
    else:
        print("Invalid input. Please enter a numeric value.")

driver.get("https://www.booktopia.com.au/")
time.sleep(5)
driver.find_element(By.XPATH,"//input[@role='combobox']").send_keys(userdata,Keys.ENTER)

time.sleep(5)

booknames = driver.find_elements(By.XPATH,"//div/div/a[@class=' Product_product-image__1TCds ']")
counte = 0
urllist = []
for bookname in booknames:
    urlofbook = bookname.get_attribute('href')
    if urlofbook not in urllist:
        counte +=1
        urllist.append(urlofbook)
        if counte == howmany:
            break
print("urllist-",urllist)
time.sleep(3)
bookinfos = []
for urll in urllist:
    driver.get(urll)
    book_title = driver.find_element(By.XPATH,"//div[@class='MuiBox-root mui-style-1ebnygn']/h1").text
    author = driver.find_element(By.XPATH,"//div[@class='MuiBox-root mui-style-1ebnygn']/p/a/span").text
    type_ofbook = driver.find_element(By.XPATH,"//div[@class='MuiTabs-flexContainer mui-style-k008qs']/div[1]").text
    book_details = type_ofbook.split('\n')
    book_type = book_details[0]
    number_ofpages = book_details[1]
    selling_price = driver.find_element(By.XPATH,"//div[@class='MuiStack-root mui-style-cfla3']/div/p").text
    try:
        actual_price = driver.find_element(By.XPATH,"//div[@class='MuiStack-root mui-style-cfla3']/div/div/p/span").text
    except:
        actual_price = selling_price
    button_clicker = driver.find_element(By.XPATH,"//div[@class='MuiTabs-root mui-style-1bxqtr2']/div/div/button[2]").click()
    time.sleep(2)
    prod_detail = driver.find_elements(By.XPATH,"//div[@class='MuiBox-root mui-style-h3npb']/p")
    for prod in prod_detail:
        checker = prod.find_element(By.XPATH, ".//span").text
        if "10" in checker:
            isbn10 = prod.text
            isbn10 = isbn10.split(" ")[1]
        if "Publisher" in checker:
            publisher = prod.text
            publisher = prod.text.split(": ")[1].strip()
        if "Published" in checker:
            publish_date = prod.text
            publish_date = publish_date.split(": ")[1].strip()
    bookinfos.append({
        "book_title": book_title,
        "author": author,
        "book_type": book_type,
        "number_ofpages": number_ofpages,
        "selling_price": selling_price,
        "actual_price": actual_price,
        "publish_date": publish_date,
        "isbn10": isbn10,
        "publisher": publisher
    })
    

df = pd.DataFrame(bookinfos)
df.to_csv('books_data.csv', index=False, encoding='utf-8')
print("Data saved to books_data.csv")
