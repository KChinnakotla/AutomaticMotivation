# Automatic Motivation
This app sends a daily motivational email to your inbox with an inspiring quote to start your day off right! Using Python, the app fetches quotes from the ZenQuotes API and sends an email to a specified address each morning.

## Features
Sends a motivational email to your inbox daily.
Retrieves quotes from the ZenQuotes API.
Customizable to send emails at any desired time using Task Scheduler (Windows) or Cron (Linux/macOS).
Prerequisites
Python 3.x installed on your computer.
A Gmail account (other email providers can also be configured).
Basic understanding of how to set up and schedule tasks on your OS.

### Setup
#### Clone this repository:
git clone https://github.com/KChinnakotla/motivational-email-sender.git
cd motivational-email-sender

#### Install the required Python packages:
pip install -r requirements.txt

#### Get a ZenQuotes API Key (Optional):

The ZenQuotes API is free to use without an API key, but you may want to get an API key if you need more flexibility.

#### Set up environment variables:

In the login file, enter your respective login information (this acts as an env file)

### How to Use
#### Run the Script Manually:

python send_automatic_email.py

#### Schedule the Script to Run Daily:

Windows: Use Task Scheduler to run the script every morning at a set time. Set up Task Scheduler to run python with the path to your script as an argument.

Linux/macOS: Use cron to schedule the script daily. Example cron job to run at 7:00 AM every day:

0 7 * * * /usr/bin/python3 /path/to/send_automatic_email.py
(Adjust the Python interpreter path and script path as needed.)

### Example Email Output
Every morning, you'll receive an email that looks like this:

Subject: 🌞 Your Daily Motivation!

Body:

"Success is not final, failure is not fatal: It is the courage to continue that counts."
— Winston Churchill

#### Future Improvements
- Add customization options for the types of quotes (e.g., inspirational, humorous).
- Allow scheduling flexibility directly within the app.
- Support multiple recipients.
