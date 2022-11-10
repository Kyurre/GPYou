import csv
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.firefox.options import Options


search_term = 'gpu'


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
    # Startup the webdriver
    options = Options()

    # switch this to chrome.exe path and use webdriver.Chrome
    options.binary_location = r"C:/Program Files/Mozilla Firefox/firefox.exe"
    driver = webdriver.Firefox(options=options)

    # instead of creating an environmental variable for ChromeDriver use this
    # URL: https://chromedriver.chromium.org/
    # Debug: https://www.selenium.dev/documentation/webdriver/getting_started/install_drivers/
    # driver = webdriver.chrome.driver(options=options, executable_path='your\path\chromedriver.exe')

    records = []
    url = get_url(search_term)

    # Go through max of 20 pages on amazon and parse information
    for page in range(1, 11):
        driver.get(url.format(page))
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        results = soup.find_all(
            'div', {'data-component-type': 's-search-result'})

        for item in results:
            record = extract_record(item)
            if record:                                         # Only add to the list of a record of an item exists
                records.append(record)

    driver.close()

    # save data to csv file
    with open('gpu.csv', 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(
            ['Description', 'Price', 'Rating', 'ReviewCount', 'Url'])
        writer.writerows(records)


runSearch('gpu')
