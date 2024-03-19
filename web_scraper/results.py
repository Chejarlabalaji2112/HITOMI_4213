from bs4 import BeautifulSoup
from urllib.request import urlopen


def checker(results_type, available_results_links):  # results_type specifies what results we are looking for and available_results_links are to check whether the results we are looking is there or not.
    """This function checks whether the specified year results released or not. """
    pass


def html_res_par(url):
    """This function gets response and parse the response"""
    response = urlopen(url).read()
    soup = BeautifulSoup(response, "html.parser")
    all_available_links = soup.find




