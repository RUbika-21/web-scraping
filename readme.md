# web-scraping

Web scraping project using Python, Requests, and BeautifulSoup to extract data from public web pages and create a structured dataset for data analytics.

---

## Features
- Multi-page web scraping
- HTML structure handling
- Data extraction using BeautifulSoup
- Custom dataset creation
- Export to Excel format

---

## Tools & Libraries Used
- Python
- Requests
- BeautifulSoup (bs4)
- Pandas
- OpenPyXL

---

## Data Source
- Website: https://quotes.toscrape.com  
- Access: Public web pages

---

## Repository Files
- `web_scraping_quotes.py` – Python script for scraping data
- `quotes_dataset.xlsx` – Extracted dataset
- `requirements.txt` – Required Python libraries
- `README.md` – Project documentation

---

## How to Run the Project

### Install dependencies
```bash
pip install -r requirements.txt

## TASK 2: Exploratory Data Analysis (EDA)

EDA was performed on the scraped dataset to understand its structure and quality.
The analysis showed that the dataset contains 50 quotes from 28 unique authors.
A small number of authors appear frequently, and tags related to inspiration,
love, and life are the most common. No missing or duplicate values were found,
indicating good data quality.
