from airflow.decorators import dag, task
from pendulum import datetime
from src import request_pages, scrape_informations


@dag(
    schedule="@daily",
    start_date=datetime(2024, 1, 1),
    catchup=False,
    tags=["scraper", "dynamic"],
)
def scraper_dag():

    @task
    def found_pages():
        page = 1
        pages_founded = []

        while True:
            html, status = request_pages.request_page(
                f"https://quotes.toscrape.com/page/{page}/"
            )
            if not status:
                break
            soup = scrape_informations.parse_page(html)
            if scrape_informations.flag_for_break_scrape(soup):
                break
            pages_founded.append(page)
            page += 1

        return pages_founded

    @task
    def get_html(page_number: int):
        html, status = request_pages.request_page(
            f"https://quotes.toscrape.com/page/{page_number}/"
        )
        if not status:
            raise ValueError(f"Página {page_number} falhou")
        return html  # agora pode, é str

    @task
    def parse_and_extract(html: str):
        soup = scrape_informations.parse_page(html)
        scrape_informations.scrape_quotes(soup)

    paginas = found_pages()
    htmls = get_html.expand(page_number=paginas)
    dados_extraidos = parse_and_extract.expand(html=htmls)


scraper_dag()
