
# Cyber Sentinel Dashboard 🛡️

The **Cyber Sentinel Dashboard** is an AI-powered cybersecurity news aggregator and analyzer. It leverages OpenAI's GPT-4o model and web scraping tools to provide users with the latest cybersecurity news, summaries, and insights. The dashboard is built using Streamlit for an interactive and visually appealing user interface.

---

## Features

- **News Aggregation**: Fetches the latest cybersecurity news from trusted sources like *The Hacker News*.
- **Article Analysis**: Summarizes and analyzes the content of cybersecurity articles.
- **Interactive Chat**: Engage with an AI-powered cybersecurity analyst for insights and recommendations.
- **Customizable Search**: Filter news by keywords and categories.
- **Modern UI**: A futuristic dashboard design for an enhanced user experience.

---

## Prerequisites

Before running the project, ensure you have the following installed:

1. **Python**: Version 3.8 or higher.
2. **Pip**: Python package manager.
3. **Node.js** (optional): For advanced Streamlit customization.
4. **Environment Variables**:
   - `OPENAI_API_KEY`: Your OpenAI API key.

---

## Installation

Follow these steps to set up and run the project:

### 1. Clone the Repository

```bash
git clone https://github.com/your-repo/Lets-Build-Cyber-Security-News-AI-Agents.git
cd Lets-Build-Cyber-Security-News-AI-Agents
```

### 2. Set Up a Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables

Create a `.env` file in the root directory and add your OpenAI API key:

```env
OPENAI_API_KEY=your_openai_api_key
```

---

## Running the Application

### 1. Start the Streamlit Dashboard

Run the following command to launch the dashboard:

```bash
streamlit run cyber_sentinel_dashboard.py
```

### 2. Access the Dashboard

Open your browser and navigate to:

```
http://localhost:8501
```

### 3. Interact with the AI

- Enter your OpenAI API key in the input field if prompted.
- Use the chat interface to ask questions or request cybersecurity news.

---

## Project Structure

The project is organized as follows:

```
Lets-Build-Cyber-Security-News-AI-Agents/
│
├── app/
│   ├── cyber_fetch.py          # Web scraping logic for fetching news and articles.
│   ├── cyber_models.py         # Pydantic models for request and response validation.
│   ├── cyber_tools.py          # Tools for news aggregation and article fetching.
│
├── cyber_sentinel_dashboard.py # Main Streamlit application.
├── requirements.txt            # Python dependencies.
├── .env                        # Environment variables (not included in the repo).
└── README.md                   # Project documentation.
```

---

## Key Components

### 1. **Streamlit Dashboard**

The `cyber_sentinel_dashboard.py` file contains the main application logic. It uses:

- **Streamlit**: For the user interface.
- **LangChain**: To manage AI interactions and memory.
- **Custom Tools**: For news aggregation and article fetching.

### 2. **Web Scraping**

The `cyber_fetch.py` file handles web scraping using `aiohttp` and `BeautifulSoup`. It fetches:

- Cybersecurity news headlines and links.
- Full article content for detailed analysis.

### 3. **Data Models**

The `cyber_models.py` file defines Pydantic models for:

- **CyberStoryRequest**: Request parameters for fetching news.
- **ArticleContentRequest**: Request parameters for fetching article content.
- **CyberStory**: Structure of a single news story.

### 4. **Custom Tools**

The `cyber_tools.py` file defines tools for:

- **News Aggregation**: Fetching and filtering cybersecurity news.
- **Article Content Fetching**: Retrieving full text from article URLs.

---

## Usage Guide

### 1. Fetch Cybersecurity News

- Use the chat interface to request news.
- Example: "Show me the latest cybersecurity news about ransomware."

### 2. Analyze an Article

- Provide an article URL to fetch and analyze its content.
- Example: "Analyze this article: [URL]"

### 3. Customize Search

- Use keywords to filter news.
- Example: "Find news about data breaches."

---

## Troubleshooting

### 1. Missing API Key

If you see the warning `API key required to proceed`, ensure:

- Your `.env` file contains the correct `OPENAI_API_KEY`.
- You entered the key in the input field when prompted.

### 2. Dependencies Not Installed

If you encounter import errors, run:

```bash
pip install -r requirements.txt
```

### 3. Streamlit Not Found

If `streamlit` is not recognized, install it manually:

```bash
pip install streamlit
```

---

## Contributing

Contributions are welcome! To contribute:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Submit a pull request with a detailed description.

---

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

---

## Acknowledgments

- **OpenAI**: For the GPT-4o model.
- **Streamlit**: For the interactive dashboard framework.
- **BeautifulSoup & aiohttp**: For web scraping capabilities.

---

## Contact

For questions or support, please contact:
    
https://github.com/aniket-work  | https://www.linkedin.com/in/aniket-hingane-data-ai-ml/


