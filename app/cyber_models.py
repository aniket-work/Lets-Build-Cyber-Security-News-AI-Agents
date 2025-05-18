from typing import Optional, List
from pydantic import BaseModel, Field

class CyberStoryRequest(BaseModel):
    """Request model for fetching cybersecurity stories"""
    max_results: int = Field(default=5, description="How many stories to fetch.")
    search_terms: Optional[List[str]] = Field(default=None, description="Keywords to filter stories.")
    category: str = Field(default="cyber", description="Story category, e.g. 'cyber', 'malware', 'breach'.")

class ArticleContentRequest(BaseModel):
    """Request model for fetching article content"""
    article_url: str = Field(..., description="URL of the article to fetch.")

class CyberStory(BaseModel):
    """A single cybersecurity story/article"""
    uid: str = Field(..., description="Unique identifier for the story.")
    headline: str = Field(..., description="Title of the story.")
    link: str = Field(..., description="URL to the story.")
    impact: Optional[int] = Field(default=None, description="Impact score or None if not available.")
