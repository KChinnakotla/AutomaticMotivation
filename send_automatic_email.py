import requests
import random
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from loginInfo import getPassword, getReciever,getSender, getSubject

# Fetch quotes from the ZenQuotes API
def fetch_quotes():
    url = 'https://zenquotes.io/api/random'
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error: {response.status_code}")
        return []

# Select a specific quote (you can modify this function to choose a quote based on criteria)
def select_quote(quotes):
    # Example: Select a random quote
    selected_quote = random.choice(quotes)
    return f"{selected_quote['q']} - {selected_quote['a']}"

# Send the selected quote via email
def send_email(quote, sender_email, receiver_email, app_password):
    subject = getSubject()
    message = "Here's the message for today:"
    body = f"{message}\n\n{quote}\n\nSee you tomorrow!"

    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    try:
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()
            server.login(sender_email, app_password)
            server.send_message(msg)
            print("Email sent successfully!")
    except Exception as e:
        print(f"Error sending email: {e}")

# Main function
def main():
    quotes = fetch_quotes()
    if quotes:
        quote_of_the_day = select_quote(quotes)

        # Your email details
        sender_email = getSender()
        receiver_email = getReciever()
        app_password = getPassword()  # Use the app password if 2FA is enabled

        send_email(quote_of_the_day, sender_email, receiver_email, app_password)

    else:
        print("No quotes fetched.")

if __name__ == "__main__":
    main()
