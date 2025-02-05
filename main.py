from scraper import fetch_first_news
from database import create_table  
import logging


NEWS_URL = "https://www.bbc.com/portuguese"
NEWS_SELECTOR = "ul[data-testid='topic-promos'] li h3"


def main() -> None:
    """Executa a automação de captura e armazenamento de notícias no banco de dados."""
    
    
    create_table()

    try:
        news_title = fetch_first_news(NEWS_URL, NEWS_SELECTOR)
        
        if news_title:
            logging.info(f"Notícia capturada e armazenada: {news_title}")
        else:
            logging.warning("Nenhuma notícia foi encontrada.")

    except Exception as e:
        logging.error(f"Erro na execução do script: {e}", exc_info=True)

if __name__ == "__main__":
    main()
