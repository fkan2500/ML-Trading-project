import yfinance as yf
import requests
import pandas as pd

def download_stock_data(ticker, start, end):
    data = yf.download(ticker, start=start, end=end)

    if not data.empty:
        data.to_csv("/home/farrukh/ML_stock_experiment/yfinance_experiment/MSFT_stock_data.csv")
        print("Stock data saved to CSV")
    else:
        print("No stock data was retrieved.")
    
    return data

def fetch_news(query, api_key):
    url = f'https://newsapi.org/v2/everything?q={query}&apiKey={api_key}'
    response = requests.get(url)
    
    if response.status_code == 200:
        articles = response.json().get('articles', [])
        return articles
    else:
        print("Failed to fetch news:", response.status_code, response.text)
        return []

def save_articles_to_csv(articles, filename):
    if articles:
        df = pd.DataFrame(articles)
        df.to_csv(filename, index=False)
        print(f"Articles saved to {filename}")
    else:
        print("No articles to save.")

stock_data = download_stock_data("MSFT", start="2022-01-01", end="2024-11-11")
articles = fetch_news("Microsoft", "[Inset Api key here]")

save_articles_to_csv(articles, "/home/farrukh/ML_stock_experiment/yfinance_experiment/Microsoft_news_articles.csv")
