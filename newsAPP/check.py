import requests
from bs4 import BeautifulSoup
from send import send_email
import hashlib
import logging
import os
import sys

# Set up logging
logging.basicConfig(filename='check.log', level=logging.DEBUG, 
                    format='%(asctime)s - %(levelname)s - %(message)s')

# Determine the script directory, especially for PyInstaller
script_dir = getattr(sys, '_MEIPASS', os.path.abspath(os.path.dirname(__file__)))

def read_from_file(file_path):
    try:
        with open(file_path, "r") as file:
            data = file.read().strip()
        logging.info(f"Read data from {file_path}")
        return data
    except Exception as e:
        logging.error(f"Failed to read from {file_path}: {e}")
        return ''

email_file_path = os.path.join(script_dir, 'email.txt')
emails = read_from_file(email_file_path)

url = 'https://tunis-business-school.tn/post/'
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')
logging.info("Launched")

# Find the news section (this will depend on the website's structure)
news_section = soup.find('div', {'class': 'universal-wrapper'})

if news_section:
    news_content = news_section.get_text()
    logging.info("News section found and content extracted")
else:
    logging.warning("News section with class 'universal-wrapper' not found.")
    news_content = ''

def get_content_hash(content):
    return hashlib.md5(content.encode()).hexdigest()

current_hash = get_content_hash(news_content)

last_hash_file_path = os.path.join(script_dir, 'last_hash.txt')
try:
    last_hash = read_from_file(last_hash_file_path)
except FileNotFoundError:
    last_hash = ''
    logging.warning(f"{last_hash_file_path} not found, assuming first run.")

if current_hash != last_hash:
    with open(last_hash_file_path, 'w') as file:
        file.write(current_hash)
    logging.info("New content detected, hash updated and email sent")
    # Send email notification
    send_email(emails)
else:
    logging.info("No new content detected")
    send_email(emails)

