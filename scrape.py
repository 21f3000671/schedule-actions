import json
import httpx
import sys
from datetime import datetime, UTC
from lxml import html
from typing import List, Dict


def scrape_imdb() -> List[Dict[str, str]]:
    """Scrape IMDb Top 250 movies using httpx and lxml.

    Returns:
        List of dictionaries containing movie title, year, and rating.
    """
    try:
        headers = {"User-Agent": "Mozilla/5.0 (compatible; IMDbBot/1.0)"}
        response = httpx.get("https://www.imdb.com/chart/top/", headers=headers, timeout=30)
        response.raise_for_status()

        tree = html.fromstring(response.text)
        movies = []

        for item in tree.cssselect(".ipc-metadata-list-summary-item"):
            title = (
                item.cssselect(".ipc-title__text")[0].text_content()
                if item.cssselect(".ipc-title__text")
                else None
            )
            year = (
                item.cssselect(".cli-title-metadata span")[0].text_content()
                if item.cssselect(".cli-title-metadata span")
                else None
            )
            rating = (
                item.cssselect(".ipc-rating-star")[0].text_content()
                if item.cssselect(".ipc-rating-star")
                else None
            )

            if title and year and rating:
                movies.append({"title": title, "year": year, "rating": rating})

        print(f"Successfully scraped {len(movies)} movies")
        return movies
    
    except Exception as e:
        print(f"Error scraping IMDb: {e}")
        sys.exit(1)


def main():
    """Main function to scrape and save data."""
    print("Starting IMDb scraper...")
    
    # Scrape data and save with timestamp
    now = datetime.now(UTC)
    movies = scrape_imdb()
    
    filename = f'imdb-top250-{now.strftime("%Y-%m-%d")}.json'
    data = {"timestamp": now.isoformat(), "movies": movies}
    
    try:
        with open(filename, "w") as f:
            json.dump(data, f, indent=2)
        print(f"Data saved to {filename}")
    except Exception as e:
        print(f"Error saving data: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()