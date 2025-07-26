import requests
import logging
logger = logging.getLogger(__name__)


def request_page(url):
    try:
        response = requests.get(url)
        response.raise_for_status()

        if response.status_code == 200:
            logging.info("Request successful")
            return response.text, True 
        else:
            logging.error(f"Request failed with status code {response.status_code}")
            return response.text, False
    except Exception as e:
        logging.error(f"An error occurred: {e}")
        return None, False

