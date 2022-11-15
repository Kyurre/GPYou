import website.amazonscrapper as AWSC

def test_get_url():
    search_term = 'test'
    url = AWSC.get_url(search_term)
    assert 'test' in url
