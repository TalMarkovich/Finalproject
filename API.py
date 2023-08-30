import requests


def space_bar_check(url, word):
    res = requests.get(url + word)
    return res.status_code < 400

def empty_input_check(url, word):
    res = requests.get(url + word)
    return "Cannot GET" in res.text and res.status_code >= 400

def invalid_input_check(url, word):
    res = requests.get(url + word)
    return "Cannot GET" in res.text and res.status_code >= 400

def long_word_check(url, word):
    res = requests.get(url + word)
    return "meanings" in res.text and res.status_code < 400