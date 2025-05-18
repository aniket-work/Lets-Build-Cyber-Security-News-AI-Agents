from typing import Optional, Type, List
from langchain.tools import BaseTool
from .cyber_models import CyberStoryRequest, ArticleContentRequest, CyberStory
from .cyber_fetch import scrape_cyber_articles, fetch_article_text

class NewsAggregatorTool(BaseTool):
    label: str = "cyber_news_aggregator"
    description: str = "Aggregates cybersecurity news stories from The Hacker News."

    def _run(self, max_results: int = 5, search_terms: Optional[List[str]] = None, category: str = "cyber"):
        req = CyberStoryRequest(max_results=max_results, search_terms=search_terms, category=category)
        return asyncio.run(scrape_cyber_articles(req))

    def _arun(self, max_results: int = 5, search_terms: Optional[List[str]] = None, category: str = "cyber"):
        req = CyberStoryRequest(max_results=max_results, search_terms=search_terms, category=category)
        return scrape_cyber_articles(req)

    args_schema: Optional[Type[CyberStoryRequest]] = CyberStoryRequest

class ArticleContentTool(BaseTool):
    label: str = "article_content_fetcher"
    description: str = "Fetches the full text content of a cybersecurity article."

    def _run(self, article_url: str):
        req = ArticleContentRequest(article_url=article_url)
        return asyncio.run(fetch_article_text(req))

    def _arun(self, article_url: str):
        req = ArticleContentRequest(article_url=article_url)
        return fetch_article_text(req)

    args_schema: Optional[Type[ArticleContentRequest]] = ArticleContentRequest
