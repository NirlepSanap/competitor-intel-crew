from crewai_tools import SerperDevTool

# SerperDevTool calls the serper.dev Google Search API.
# Returns: titles, snippets, URLs for the top results.
#
# Used by: Web Researcher, Sentiment Analyst
#
# Requires in .env:
#   SERPER_API_KEY=your_key_here
#
# Free tier: 2500 searches/month at serper.dev

search_tool = SerperDevTool()