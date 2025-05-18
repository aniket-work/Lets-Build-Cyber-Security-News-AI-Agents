from bs4 import BeautifulSoup
import asyncio
import aiohttp
from typing import List, Optional
import json

from .cyber_models import CyberStoryRequest, ArticleContentRequest, CyberStory

CYBER_NEWS_URL = "https://thehackernews.com/search/label/Cyber%20Attack"

async def scrape_cyber_articles(request: CyberStoryRequest) -> List[CyberStory]:
    async with aiohttp.ClientSession(connector=aiohttp.TCPConnector(verify_ssl=False)) as session:
        async with session.get(CYBER_NEWS_URL) as response:
            html = await response.text()
            soup = BeautifulSoup(html, 'html.parser')
            posts = soup.find_all('div', class_='body-post')
            results = []
            for post in posts:
                title_tag = post.find('h2', class_='home-title')
                url_tag = post.find('a', href=True)
                if not title_tag or not url_tag:
                    continue
                headline = title_tag.get_text(strip=True)
                link = url_tag['href']
                story = CyberStory(uid=link, headline=headline, link=link)
                if not request.search_terms or any(term.lower() in headline.lower() for term in request.search_terms):
                    results.append(story)
                if len(results) >= request.max_results:
                    break
            return results

async def fetch_article_text(request: ArticleContentRequest) -> str:
    async with aiohttp.ClientSession(connector=aiohttp.TCPConnector(verify_ssl=False)) as session:
        async with session.get(request.article_url) as response:
            if response.status == 200:
                html = await response.text()
                soup = BeautifulSoup(html, 'html.parser')
                return soup.get_text()
            return f"Failed to fetch content from {request.article_url} (status {response.status})"
