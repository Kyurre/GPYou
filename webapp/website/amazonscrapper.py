import csv
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.firefox.service import Service
# from selenium.webdriver.firefox.options import Options
# from webdriver_manager.firefox import GeckoDriverManager
# this file was authored by Dave P.


def get_url(search_term):
    template = 'https://www.amazon.com/s?k={}&ref=nb_sb_noss_1'
    search_term = search_term.replace(' ', '+')

    # add term query to url
    url = template.format(search_term)

    # add page query placeholder
    url += '&page{}'

    return url


def extract_record(item):
    """ Extract and return data from single record"""

    # description and url
    atag = item.h2.a
    description = atag.text.strip()
    url = 'https://www.amazon.com' + atag.get('href')

    # price
    try:
        price_parent = item.find('span', 'a-price')
        price = price_parent.find('span', 'a-offscreen').text
    except AttributeError:
        return

    # Review and rating
    try:
        rating = item.i.text
        review_count = item.find('span', {
                                 'class': 'a-size-base puis-light-weight-text s-link-centralized-style'}).text
    except AttributeError:
        rating = ''
        review_count = ''

    result = (description, price, rating, review_count, url)
    return result


def runSearch(search_term):
    """Run main program routine"""
    # URL: https://chromedriver.chromium.org/
    # Debug: https://www.selenium.dev/documentation/webdriver/getting_started/install_drivers/

    # Startup the chrome webdriver
    options = Options()
    options.page_load_strategy = 'normal'
    service = Service(
        executable_path="webapp/website/webdrivers/chromedriver.exe")
    driver = webdriver.Chrome(options=options, service=service)

    # Firefox driver use firefox imports
    # options = Options()
    # options.binary_location = r"C:\Program Files (x86)\Mozilla Firefox"
    # driver = webdriver.Firefox(options=options)
    # driver = webdriver.Firefox(options=options, executable_path=GeckoDriverManager().install()) #ls

    records = []
    url = get_url(search_term)

    # Go through max of 20 pages on amazon and parse information
    for page in range(1, 21):
        driver.get(url.format(page))
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        results = soup.find_all(
            'div', {'data-component-type': 's-search-result'})

        for item in results:
            record = extract_record(item)
            if record:                                         # Only add to the list of a record of an item exists
                records.append(record)

    driver.close()

    # print(records)

    # save data to csv file
    with open('webapp/website/csv/gpu.csv', 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(
            ['Description', 'Price', 'Rating', 'ReviewCount', 'Url'])
        writer.writerows(records)


# runSearch('gpu')
