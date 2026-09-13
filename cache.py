

cache = {}
def is_cache(url):
    return url in cache
def get_from_cache(url):
    return cache[url]
def save_to_cache(url,response):
    cache[url] = response
