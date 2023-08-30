from Sele import *
from selenium import webdriver
import pytest


@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    return driver


class TestTal2:

    @pytest.mark.usefixtures('driver')
    def test_add_client(self, driver):
        actual = add_client(driver) != 'Error'
        assert actual, "The table don't show the new client"

    @pytest.mark.usefixtures('driver')
    def test_rows_counter(self, driver):
        actual = rows_counter(driver) != 'Error'
        assert actual, "Harry potter don't have the correct amount of transactions"

    @pytest.mark.usefixtures('driver')
    def test_no_first_name(self, driver):
        actual = no_fisrt_name(driver) != 'Error'
        assert actual, 'The website add a new client without a first name'

    @pytest.mark.usefixtures('driver')
    def test_letters_no_numbers(self, driver):
        actual = letters_no_numbers(driver) != 'Error'
        assert actual, 'The website accept letters in the amount test box'