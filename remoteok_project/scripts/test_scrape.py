import requests
from bs4 import BeautifulSoup

def test_scrape():
    url = "https://remoteok.com/"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36",
        "Accept-Language": "en-US,en;q=0.9",
    }
    
    print(f"Fetching {url}...")
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        print("Successfully fetched the page.")
        
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # RemoteOK jobs are usually in table rows with class 'job'
        job_rows = soup.find_all('tr', class_='job')
        print(f"Found {len(job_rows)} job rows.")
        
        for i, row in enumerate(job_rows[:3]):
            print(f"\n--- Job {i+1} ---")
            # Title
            title_elem = row.find('h2', itemprop='title')
            title = title_elem.text.strip() if title_elem else "N/A"
            
            # Company
            company_elem = row.find('h3', itemprop='name')
            company = company_elem.text.strip() if company_elem else "N/A"
            
            # Tags/Skills
            tags = [tag.text.strip() for tag in row.find_all('div', class_='tag')]
            
            # Location & Salary (often in 'location' class)
            locations = [loc.text.strip() for loc in row.find_all('div', class_='location')]
            
            print(f"Title: {title}")
            print(f"Company: {company}")
            print(f"Tags: {tags}")
            print(f"Locations/Salary: {locations}")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    test_scrape()
