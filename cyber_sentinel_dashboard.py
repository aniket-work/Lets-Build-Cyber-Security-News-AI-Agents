import asyncio
import os
from dotenv import load_dotenv
from PIL import Image
import streamlit as st
from langchain_community.chat_models import ChatOpenAI
from langchain.memory import ConversationBufferMemory
from langchain_community.chat_message_histories import StreamlitChatMessageHistory
from langchain.schema import SystemMessage
from langchain.prompts import MessagesPlaceholder
from app.cyber_tools import NewsAggregatorTool, ArticleContentTool

st.set_page_config(page_title="Cyber Sentinel Dashboard 🛡️")

# Custom CSS for a futuristic dashboard look
st.markdown('''
    <style>
    .main {
        background: linear-gradient(120deg, #232526 0%, #414345 100%);
    }
    .stApp {
        font-family: 'Fira Sans', 'Segoe UI', 'Roboto', 'Arial', sans-serif;
        color: #e0e1dd;
    }
    .st-emotion-cache-1v0mbdj, .st-emotion-cache-1v0mbdj p {
        color: #e0e1dd;
    }
    .st-emotion-cache-1c7y2kd {
        background: #22223b;
        border-radius: 18px;
        box-shadow: 0 6px 32px rgba(0,0,0,0.12);
        padding: 2.5rem 2.5rem 1.5rem 2.5rem;
        margin-bottom: 2.5rem;
    }
    .st-emotion-cache-1v0mbdj h1 {
        color: #00b4d8;
        font-weight: 900;
        letter-spacing: 2px;
    }
    .st-emotion-cache-1v0mbdj h2 {
        color: #e0e1dd;
        font-weight: 700;
    }
    .st-emotion-cache-1v0mbdj .stButton>button {
        background: linear-gradient(90deg, #00b4d8 0%, #0077b6 100%);
        color: #fff;
        border: none;
        border-radius: 10px;
        font-weight: 700;
        padding: 0.6rem 1.7rem;
        margin-top: 1.2rem;
        transition: background 0.2s;
    }
    .st-emotion-cache-1v0mbdj .stButton>button:hover {
        background: linear-gradient(90deg, #0077b6 0%, #00b4d8 100%);
    }
    .st-emotion-cache-1v0mbdj .stTextInput>div>input {
        border-radius: 10px;
        border: 1.5px solid #00b4d8;
        padding: 0.6rem;
    }
    .st-emotion-cache-1v0mbdj .stAlert {
        border-radius: 10px;
    }
    .st-emotion-cache-1v0mbdj .stMarkdown {
        font-size: 1.15rem;
    }
    .st-emotion-cache-1v0mbdj .stChatMessage {
        background: #393e46;
        border-radius: 14px;
        margin-bottom: 0.7rem;
        padding: 1.2rem;
    }
    </style>
''', unsafe_allow_html=True)

load_dotenv()

api_key = os.getenv('OPENAI_API_KEY')
if not api_key:
    api_key = st.text_input('🔑 Enter your OpenAI API Key:', type='password')
    if not api_key:
        st.warning('API key required to proceed.', icon='⚠️')
        st.stop()

st.markdown("""
<div style='text-align:center;'>
    <img src='https://img.icons8.com/ios-filled/100/00b4d8/security-checked.png' style='margin-bottom:1rem;' />
    <h1 style='font-size:2.7rem;font-weight:900;margin-bottom:0.5rem;'>Cyber Sentinel Dashboard</h1>
    <h2 style='font-size:1.25rem;font-weight:400;color:#00b4d8;'>Monitor, analyze, and interact with the latest cybersecurity news.</h2>
</div>
---
""", unsafe_allow_html=True)

# Tools
tools = [NewsAggregatorTool(), ArticleContentTool()]
msgs = StreamlitChatMessageHistory(key="cyber_sentinel_msgs")
memory = ConversationBufferMemory(chat_memory=msgs, return_messages=True)
system_prompt = SystemMessage(content="""
You are Cyber Sentinel, an expert AI cybersecurity analyst.
You help users discover, summarize, and analyze the latest cyber attacks and security news.
If you cannot find relevant information, apologize and offer to help with another query.
When showing news, use a markdown table with columns:
UID | Headline | Link | Impact
""")

if len(msgs.messages) == 0:
    msgs.add_ai_message("Welcome to Cyber Sentinel! How can I assist your cybersecurity research today?")

llm = ChatOpenAI(temperature=0, model="gpt-4o", openai_api_key=api_key)
agent_kwargs = {
    "system_message": system_prompt,
    "extra_prompt_messages": [MessagesPlaceholder(variable_name="history")]
}
from langchain.agents import AgentType, initialize_agent
cyber_agent = initialize_agent(tools,
                              llm,
                              agent=AgentType.OPENAI_FUNCTIONS,
                              agent_kwargs=agent_kwargs,
                              verbose=True,
                              memory=memory)

async def sentinel_response(query):
    return await cyber_agent.arun(query)

for msg in msgs.messages:
    with st.container():
        st.markdown(f"<div class='stChatMessage'><b>{msg.type.capitalize()}:</b> {msg.content}</div>", unsafe_allow_html=True)

if user_input := st.chat_input(disabled=not api_key):
    with st.container():
        st.markdown(f"<div class='stChatMessage'><b>You:</b> {user_input}</div>", unsafe_allow_html=True)
    with st.spinner("Analyzing ..."):
        answer = asyncio.run(sentinel_response(user_input))
        with st.container():
            st.markdown(f"<div class='stChatMessage'><b>Sentinel:</b> {answer}</div>", unsafe_allow_html=True)
