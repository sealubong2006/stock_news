import requests
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# ----------------- CONSTANTS -------------------
STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

STOCK_API_KEY = "G6Y97OGXKTHW5YAI"  # Alpha Vantage API Key
NEWS_API_KEY = "c7a09f373cd64b4bbf0b5f39cfe2d992"  # News API Key

# ----------------- STEP 1: GET STOCK DATA -------------------
stock_api_parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": STOCK_API_KEY,
}

# Request stock data
stock_response = requests.get(STOCK_ENDPOINT, params=stock_api_parameters)
data = stock_response.json()["Time Series (Daily)"]
data_list = [value for (key, value) in data.items()]  # Extract daily prices

# Get yesterday's and the day before yesterday's closing prices
yesterday_data = data_list[0]
yesterday_closing_price = yesterday_data["4. close"]
print(f"Yesterday's Close: {yesterday_closing_price}")

day_before_yesterday_data = data_list[1]
day_before_yesterday_closing_price = day_before_yesterday_data["4. close"]
print(f"Day Before Yesterday's Close: {day_before_yesterday_closing_price}")

# Calculate difference and percentage change
closing_price_difference = float(yesterday_closing_price) - float(day_before_yesterday_closing_price)
up_down = "🔺" if closing_price_difference > 0 else "🔻"

average_of_closing_prices = (float(yesterday_closing_price) + float(day_before_yesterday_closing_price)) / 2
closing_percentage_difference = round((closing_price_difference / average_of_closing_prices) * 100)
print(f"Change: {closing_percentage_difference}%")

# ----------------- STEP 2: GET NEWS IF PRICE FLUCTUATION > 5% -------------------
if abs(closing_percentage_difference) > 5:
    news_api_parameters = {
        "apikey": NEWS_API_KEY,
        "q": COMPANY_NAME,
    }

    news_response = requests.get(NEWS_ENDPOINT, params=news_api_parameters)
    articles = news_response.json()["articles"]
    three_articles = articles[:3]  # Take top 3 relevant articles

    # Format articles
    formatted_articles = [
        f"{STOCK_NAME}: {up_down}{closing_percentage_difference}%\n"
        f"Headline: {article['title']}\n"
        f"Brief: {article['description']}"
        for article in three_articles
    ]

    # ----------------- STEP 3: SEND EMAIL -------------------
    # Email configuration
    sender_email = "your_email@example.com"         # Replace with your email
    receiver_email = "receiver_email@example.com"   # Replace with recipient's email
    email_password = "your_email_password_or_app_password"  # Use App Password if needed
    smtp_server = "smtp.gmail.com"
    smtp_port = 587

    # Create email message
    subject = f"{STOCK_NAME} Stock Alert"
    body = "\n\n".join(formatted_articles)

    msg = MIMEMultipart()
    msg["From"] = sender_email
    msg["To"] = receiver_email
    msg["Subject"] = subject

    msg.attach(MIMEText(body, "plain"))

    # Send the email
    try:
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()  # Secure the connection
            server.login(sender_email, email_password)
            server.sendmail(sender_email, receiver_email, msg.as_string())
            print("Email sent successfully.")
    except Exception as e:
        print(f"An error occurred while sending the email: {e}")
