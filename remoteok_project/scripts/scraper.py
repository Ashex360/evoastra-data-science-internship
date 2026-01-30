import requests
from bs4 import BeautifulSoup
import pandas as pd
import time
import random
import os

class RemoteOKScraper:
    def __init__(self):
        self.url = "https://remoteok.com/"
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36",
            "Accept-Language": "en-US,en;q=0.9",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8",
        }
        self.jobs_data = []

    def fetch_page(self):
        """Fetches the main page of RemoteOK."""
        print(f"Connecting to {self.url}...")
        try:
            # In a real scenario, we'd use a session and handle retries
            response = requests.get(self.url, headers=self.headers, timeout=15)
            response.raise_for_status()
            return response.content
        except requests.exceptions.RequestException as e:
            print(f"Error fetching page: {e}")
            return None

    def parse_jobs(self, html_content):
        """Parses job listings from the HTML content."""
        if not html_content:
            return

        soup = BeautifulSoup(html_content, 'html.parser')
        # RemoteOK uses 'tr' with class 'job' for each listing
        job_rows = soup.find_all('tr', class_='job')
        
        print(f"Found {len(job_rows)} potential job listings.")

        for row in job_rows:
            try:
                # Extracting data based on RemoteOK's structure
                title = row.find('h2', itemprop='title').text.strip() if row.find('h2', itemprop='title') else "N/A"
                company = row.find('h3', itemprop='name').text.strip() if row.find('h3', itemprop='name') else "N/A"
                
                # Tags/Skills
                tags = [tag.text.strip() for tag in row.find_all('div', class_='tag')]
                skills = ", ".join(tags)
                
                # Location and Salary are often in 'location' divs
                locations = [loc.text.strip() for loc in row.find_all('div', class_='location')]
                
                # Usually, the first location div is the actual location, 
                # and others might be salary or job type
                location = "Remote"
                salary = "N/A"
                job_type = "Full-Time" # Default
                
                for loc in locations:
                    if '$' in loc:
                        salary = loc
                    elif any(t in loc for t in ['Full-time', 'Contract', 'Part-time']):
                        job_type = loc
                    else:
                        location = loc

                # Date posted (RemoteOK uses 'time' tag)
                date_elem = row.find('time')
                date_posted = date_elem['datetime'] if date_elem and date_elem.has_attr('datetime') else "N/A"

                self.jobs_data.append({
                    'title': title,
                    'company': company,
                    'skills': skills,
                    'location': location,
                    'job_type': job_type,
                    'salary': salary,
                    'date_posted': date_posted
                })
                
                # Respectful scraping: small delay between processing if needed
                # (Though here we already have the full HTML)
                
            except Exception as e:
                print(f"Error parsing a job row: {e}")
                continue

    def save_to_csv(self, filename="remoteok_jobs.csv"):
        """Saves the collected data to a CSV file."""
        if not self.jobs_data:
            print("No data to save.")
            return
        
        df = pd.DataFrame(self.jobs_data)
        df.to_csv(filename, index=False)
        print(f"Data saved to {filename}")

    def run(self):
        """Main execution method."""
        content = self.fetch_page()
        if content:
            self.parse_jobs(content)
            self.save_to_csv("remoteok_project/data/remoteok_jobs_raw.csv")
        else:
            print("Failed to retrieve data. Please check connection or site status.")

if __name__ == "__main__":
    scraper = RemoteOKScraper()
    scraper.run()
