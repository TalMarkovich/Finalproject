import pytest
from API import *


class TestTal:
    @pytest.fixture()
    def url(self):
        return 'https://api.dictionaryapi.dev/api/v2/entries/en/'

    def test_space_bar(self, url, word="space%20bar"):
        actual = space_bar_check(url, word)
        assert actual, 'Does not give correct response'

    def test_empty_input (self, url, word=""):
        actual = empty_input_check(url, word)
        assert actual, 'Does not give correct error response'

    def test_invalid_input (self, url, word="/invalid"):
        actual = invalid_input_check(url, word)
        assert actual, 'Does not give correct error response'

    @pytest.mark.parametrize('word', ['supercalifragilisticexpialidocious', 'interdisciplinary', 'inconsequential', 'sesquipedalian'])
    def test_long_word (self, url, word):
        actual = long_word_check(url, word)
        assert actual, 'Does not accept long valid words'

