from playwright.sync_api import sync_playwright
from typing import Optional
from database import insert_news, create_table 
import logging


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler("news_scraper.log"),  
        logging.StreamHandler()  
    ]
)


def fetch_first_news(url: str, news_selector: str, timeout: int = 30_000) -> Optional[str]:
    """
    Acessa um site de notícias, captura o título da primeira notícia e insere no banco de dados.

    :param url: URL do site de notícias.
    :param news_selector: Seletor CSS para encontrar a notícia.
    :param timeout: Tempo máximo de espera para carregamento (padrão: 10s).
    :return: Título da primeira notícia ou None caso falhe.
    """
    try:
        with sync_playwright() as playwright:
            browser = playwright.chromium.launch(headless=True)
            with browser.new_page() as page:
                page.goto(url, timeout=timeout)
                page.wait_for_selector(news_selector, timeout=timeout)

                news_items = page.locator(news_selector).all()
                
                if news_items:
                    first_news_title = news_items[0].inner_text()
                    logging.info(f"Notícia capturada: {first_news_title}")

                    create_table()

                    insert_news(first_news_title)

                    return first_news_title
                else:
                    logging.warning("Nenhuma notícia encontrada.")
                    return None

    except Exception as error:
        logging.error(f"Erro ao capturar a notícia: {error}", exc_info=True)
        return None
