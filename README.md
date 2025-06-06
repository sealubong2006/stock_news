```markdown
# 📈 Tesla Stock Tracker & News Alert Bot

This is a Python automation project that monitors Tesla Inc. (TSLA) stock prices using real-time data from Alpha Vantage. If the stock price fluctuates significantly (more than 5%), it fetches the latest news about the company and sends a formatted summary directly to your email.

---

## 🚀 Features

- 📉 Tracks daily stock prices using Alpha Vantage API  
- 📰 Fetches relevant news from NewsAPI when a significant price change occurs  
- 📧 Sends the news summary via email with clear formatting  
- 🔔 Uses simple logic to detect meaningful price changes  
- 🐍 Built entirely in Python using requests, smtplib, and email libraries  

---

## 📌 Example Output

```

TSLA: 🔻6%

Headline: Tesla stock dips after disappointing delivery numbers.
Brief: Tesla’s recent vehicle delivery numbers fell short of analyst expectations, raising concerns about demand and production scaling.

Headline: Elon Musk says Tesla will focus on robotaxis and AI.
Brief: The CEO highlighted Tesla’s push toward autonomous driving and AI integration during a recent shareholder update.

Headline: Market reacts to Tesla's price cuts across key markets.
Brief: Tesla has initiated price reductions in several regions to boost demand amid economic uncertainties.

````

---

## 🛠️ Setup Instructions

1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-username/tesla-stock-alert.git
   cd tesla-stock-alert
````

2. **Install dependencies:**

   ```bash
   pip install requests
   ```

3. **Set up your email credentials** inside the script:

   ```python
   sender_email = "your_email@example.com"
   receiver_email = "receiver_email@example.com"
   email_password = "your_app_password"
   ```

   ⚠️ If you're using Gmail, make sure to enable **App Passwords**.

4. **Replace API Keys:**

   * Alpha Vantage: [https://www.alphavantage.co/support/#api-key](https://www.alphavantage.co/support/#api-key)
   * NewsAPI: [https://newsapi.org/register](https://newsapi.org/register)

5. **Run the script:**

   ```bash
   python main.py
   ```

---

## 🧠 Concepts Practiced

* API consumption with `requests`
* Parsing JSON data
* Conditional logic
* Working with SMTP to send emails
* Automating alerts and notifications

---

## 🎓 Inspired By

This project was created as part of the 100DaysOfCode challenge and the [Udemy Python Bootcamp](https://www.udemy.com/course/100-days-of-code/) by **#AngelaYu**.

---

## 📬 License

This project is open-source and free to use

---

## 🙌 Let's Connect

Feel free to fork, improve, or reach out for collaboration!

\#Python #automation #stockmarket #tesla #emailalerts #100DaysOfCode #AngelaYu #UdemyPythonBootcamp

```
