# Remote Job Market Intelligence - Web Scraping Project

## Project Overview
This project was developed as part of a Data Science Internship to analyze the remote job market using data from [RemoteOK](https://remoteok.com/). The goal is to identify in-demand skills, job title trends, and employment type distributions through ethical web scraping and data analysis.

## Project Structure
- `data/`: Contains the raw and cleaned datasets.
  - `remoteok_jobs_cleaned.csv`: The final dataset used for analysis.
- `scripts/`: Python scripts for different stages of the project.
  - `scraper.py`: The main scraping script (uses BeautifulSoup).
  - `analysis.py`: Script for data processing and visualization.
  - `generate_mock_data.py`: Utility to generate realistic data for testing.
- `visualizations/`: PNG files of the generated charts.
  - `top_skills.png`: Bar chart of the most demanded skills.
  - `job_type_distribution.png`: Pie chart of employment types.
  - `top_job_titles.png`: Horizontal bar chart of common job titles.
  - `skill_frequency_comparison.png`: Extended skill frequency analysis.
- `REPORT.md`: Detailed summary of findings and methodology.

## How to Run
1. **Install Dependencies**:
   ```bash
   pip install requests beautifulsoup4 pandas matplotlib seaborn
   ```
2. **Scrape Data**:
   Run the scraper to collect live data (Note: Ensure you have a stable connection and respect the site's `robots.txt`).
   ```bash
   python scripts/scraper.py
   ```
3. **Run Analysis**:
   Generate visualizations and comparative insights.
   ```bash
   python scripts/analysis.py
   ```

## Methodology
- **Scraping**: We used the `requests` library to fetch HTML and `BeautifulSoup` for parsing. We adhered to ethical scraping practices by setting a custom User-Agent and respecting the `Crawl-delay` specified in `robots.txt`.
- **Cleaning**: Data was processed using `pandas` to handle missing values, split skill tags, and standardize job types.
- **Visualization**: `matplotlib` and `seaborn` were used to create professional-grade charts for business intelligence.

## Ethical Compliance
This project strictly follows the rules set in RemoteOK's `robots.txt`:
- User-agent: *
- Crawl-delay: 1
- Disallow: /?action=get_jobs
