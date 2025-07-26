from bs4 import BeautifulSoup
import logging
import json
import lxml.etree as etree

logger = logging.getLogger(__name__)


def parse_page(html):
    soup = BeautifulSoup(html, "html.parser")
    logging.info("Page parsed and found informations")
    return soup


def scrape_quotes(soup):
    dict_scrape = {}
    dict_scrape["text"] = _scrape_text(soup)
    dict_scrape["author"] = _scrape_author(soup)
    dict_scrape["tags"] = _scrape_tags(soup)

    logging.info("Scraped data: %s", json.dumps(dict_scrape, ensure_ascii=False))


def _scrape_text(soup):
    soup = soup.find_all("span", class_="text")
    return [quote.text.strip() for quote in soup]


def _scrape_author(soup):
    soup = soup.find_all("small", class_="author")
    return [author.text.strip() for author in soup]


def _scrape_tags(soup):
    soup = soup.find_all("div", class_="tags")
    return [tag.text.strip() for tag in soup]


def flag_for_break_scrape(soup):
    dom = etree.HTML(str(soup))
    end_page = dom.xpath("/html/body/div/div[2]/div[1]")[0].text
    if end_page.strip() == "No quotes found!":
        logger.info("End of page reached")
        return True
    else:
        return False
