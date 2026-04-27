from crewai_tools import ScrapeWebsiteTool

# ScrapeWebsiteTool fetches a URL and extracts readable text.
# The agent decides which URL to pass — it reads whatever
# the search tool returned as a link.
#
# Used by: Web Researcher (product pages, brand sites)
#          Sentiment Analyst (review pages)
#
# Important limits to know:
#   - Amazon product pages: works most of the time
#   - Flipkart: often returns a bot-block page
#     → if scraping Flipkart fails, fall back to
#       search_tool snippets which are usually enough
#   - Instagram / social media: will not work — skip
#
# No API key needed — scrapes directly.

scrape_tool = ScrapeWebsiteTool()