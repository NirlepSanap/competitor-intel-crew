from typing import Type
from crewai.tools import BaseTool
from pydantic import BaseModel, Field
import requests
from bs4 import BeautifulSoup


class SentimentScrapeInput(BaseModel):
    """Input schema for SentimentScrapeTool."""
    url: str = Field(
        ...,
        description=(
            "Full URL of the page to scrape reviews from. "
            "Works best on Amazon product pages, brand review pages, "
            "and Google review sections."
        )
    )


class SentimentScrapeTool(BaseTool):
    """
    Custom tool that fetches a product/review page and returns
    only the review text — strips nav, headers, footers, ads.

    This gives the Sentiment Analyst agent cleaner input than
    the generic ScrapeWebsiteTool which returns the whole page.

    Used by: Sentiment Analyst
    Requires: pip install beautifulsoup4 requests
    """

    name: str = "Sentiment Review Scraper"
    description: str = (
        "Scrapes customer reviews from a product or review page URL. "
        "Returns only the review text, stripping out navigation, "
        "headers, and ads. Use this for Amazon reviews, brand review "
        "pages, and Google review sections."
    )
    args_schema: Type[BaseModel] = SentimentScrapeInput

    def _run(self, url: str) -> str:
        try:
            headers = {
                "User-Agent": (
                    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                    "AppleWebKit/537.36 (KHTML, like Gecko) "
                    "Chrome/120.0.0.0 Safari/537.36"
                )
            }
            response = requests.get(url, headers=headers, timeout=10)
            response.raise_for_status()

            soup = BeautifulSoup(response.text, "html.parser")

            # Remove noise elements
            for tag in soup(["nav", "header", "footer", "script",
                              "style", "aside", "form", "iframe"]):
                tag.decompose()

            # Try to find review-specific sections first
            review_sections = soup.find_all(
                attrs={"data-hook": "review"},  # Amazon
            )

            if review_sections:
                texts = [r.get_text(separator=" ", strip=True)
                         for r in review_sections]
                return "\n\n".join(texts[:20])  # cap at 20 reviews

            # Fallback: return cleaned body text
            body = soup.get_text(separator="\n", strip=True)
            lines = [l.strip() for l in body.splitlines() if len(l.strip()) > 40]
            return "\n".join(lines[:80])

        except requests.exceptions.Timeout:
            return f"ERROR: Request timed out for {url}. Try a different URL."
        except requests.exceptions.HTTPError as e:
            return f"ERROR: HTTP {e.response.status_code} for {url}. Page may be blocked."
        except Exception as e:
            return f"ERROR: Could not scrape {url}. Reason: {str(e)}"


sentiment_scrape_tool = SentimentScrapeTool()