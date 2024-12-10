
import os
import requests
import streamlit as st
from langchain.llms import OpenAI
from langchain.embeddings.openai import OpenAIEmbeddings 

from langchain.chains import RetrievalQAWithSourcesChain as QAChain
from langchain.text_splitter import RecursiveCharacterTextSplitter as TextSplitter
from langchain.document_loaders import UnstructuredURLLoader 
from langchain.vectorstores import FAISS as FaissIndex
from dotenv import load_dotenv
from urllib.parse import urlparse

st.set_page_config(page_title="ClimaBot Tool", layout="wide")

load_dotenv()

news_api_key = os.getenv("NEWS_API_KEY")

def validate_url(url):
    try:
        result = urlparse(url)
        return all([result.scheme, result.netloc])
    except ValueError:
        return False
def preprocess_query(query):
    return query.lower().strip().replace('?', '')

weather_keywords = [
    "weather", "climate", "temperature", "rainfall", "humidity",
    "storm", "air quality", "precipitation", "greenhouse gases", 
    "flood", "drought", "tornado", "hurricane", "wildfire", "snowfall", 
    "global warming", "heat wave", "ozone layer", "carbon footprint", 
    "sea level rise", "pollution", "renewable energy", "sustainability", 
    "wind patterns", "monsoon", "environment", "arctic ice", "extreme weather"
]

#fetching news articles from NewsAPI based on weather and climate-related keywords
def fetch_weather_climate_news():
    if news_api_key is None:
        st.error("NewsAPI key is not found. Please check your environment variables.")
        return {}
    query = " OR ".join(weather_keywords)
    url = f"https://newsapi.org/v2/everything?q={query}&language=en&apiKey={news_api_key}"
    response = requests.get(url)
    return response.json()

#splitting text into smaller chunks with semantic boundaries
def split_text(loaded_data):
    primary_delimiters = ['\n\n', '\n', '.', '?', '!']
    fallback_delimiters = [';', ' ', '|']
    doc_splitter = TextSplitter(separators=primary_delimiters, chunk_size=600)
    split_documents = doc_splitter.split_documents(loaded_data)
    return split_documents

openai_api_key = os.getenv("OPENAI_API_KEY")
if openai_api_key is None:
    raise ValueError("OpenAI API key not found")

def set_background_color():
    st.markdown(
        """
        <style>
        .stApp {
            background-color: #76ABAE;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

set_background_color()

st.title("ClimaBot Tool")

st.sidebar.header("🔗 Enter URLs Here")
input_urls = [st.sidebar.text_input(f"URL {i+1}") for i in range(3)]
start_processing = st.sidebar.button("Submit")

status_container = st.container()

faiss_directory = "faiss_store"
if not os.path.exists(faiss_directory):
    os.makedirs(faiss_directory)

language_model = OpenAI(api_key=openai_api_key, temperature=0.9, max_tokens=500)
llm_embeddings = OpenAIEmbeddings(api_key=openai_api_key, model="text-embedding-ada-002")

if start_processing:
    valid_urls = [url for url in input_urls if validate_url(url)]
    if not valid_urls:
        status_container.error("Please enter valid URLs.")
    else:
        status_container.info("Processing URLs...")
        try:
            url_loader = UnstructuredURLLoader(urls=valid_urls)
            loaded_data = url_loader.load()
            split_documents = split_text(loaded_data)
            vectorindex_openai = FaissIndex.from_documents(split_documents, llm_embeddings)
            vectorindex_openai.save_local(faiss_directory)

            status_container.success("URLs processed successfully!")
        except Exception as e:
            status_container.error(f"Error processing URLs: {e}")

user_query = st.text_input("🔍 Type your query here")

if user_query:
    user_query = preprocess_query(user_query)
    if os.path.isdir(faiss_directory):
        try:
            loaded_faiss_index = FaissIndex.load_local(faiss_directory, llm_embeddings, allow_dangerous_deserialization=True)
            retriever = loaded_faiss_index.as_retriever(search_k=10)
            qa_chain = QAChain.from_llm(llm=language_model, retriever=retriever)
            query_result = qa_chain({"question": user_query}, return_only_outputs=True)

            st.subheader("Answer")
            st.write(query_result["answer"])

            sources = query_result.get("sources", "")
            if sources:
                st.subheader("Sources")
                st.write(sources.replace("\n", ", "))

            news_response = fetch_weather_climate_news()
            st.subheader("Related News Articles")
            if news_response.get("articles"):
                for i, article in enumerate(news_response["articles"][:10]):
                    st.write(f"**{article['title']}** - {article['source']['name']}")
                    st.write(f"[Read More]({article['url']})")
            else:
                st.write("No related news articles found.")
        except Exception as e:
            status_container.error(f"Error loading FAISS index or processing query: {e}")
    else:
        status_container.error("FAISS index not found. Please process the URLs first.")
