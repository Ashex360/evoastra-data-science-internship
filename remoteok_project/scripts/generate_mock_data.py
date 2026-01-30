import pandas as pd
import random
from datetime import datetime, timedelta

def generate_mock_data(num_records=100):
    titles = [
        "Senior Python Developer", "Full Stack Engineer", "Data Scientist", 
        "Backend Developer", "Frontend React Developer", "DevOps Engineer",
        "Product Manager", "UI/UX Designer", "Machine Learning Engineer",
        "Marketing Manager", "Sales Representative", "Customer Support Specialist",
        "Mobile App Developer (iOS/Android)", "Cloud Architect", "Security Analyst"
    ]
    
    companies = [
        "TechFlow", "CloudNine", "DataViz", "InnoSoft", "GreenEnergy", 
        "GlobalConnect", "SmartSolutions", "BrightFuture", "NextGen", "PeakPerformance"
    ]
    
    skills_pool = [
        "Python", "JavaScript", "React", "Node.js", "AWS", "Docker", "Kubernetes",
        "SQL", "NoSQL", "Machine Learning", "Data Analysis", "Project Management",
        "UI/UX", "Figma", "Go", "Rust", "Java", "C++", "Terraform", "Git"
    ]
    
    locations = ["Worldwide", "USA Only", "Europe Only", "UK Only", "Canada Only", "Latin America"]
    job_types = ["Full-Time", "Contract", "Part-Time"]
    
    data = []
    
    for _ in range(num_records):
        title = random.choice(titles)
        company = random.choice(companies)
        
        # Randomly pick 2-5 skills
        skills = ", ".join(random.sample(skills_pool, random.randint(2, 5)))
        
        location = random.choice(locations)
        job_type = random.choice(job_types)
        
        # Random salary
        salary_min = random.randint(40, 150)
        salary_max = salary_min + random.randint(20, 100)
        salary = f"${salary_min}k - ${salary_max}k"
        
        # Random date in the last 30 days
        date_posted = (datetime.now() - timedelta(days=random.randint(0, 30))).strftime("%Y-%m-%dT%H:%M:%S")
        
        data.append({
            'title': title,
            'company': company,
            'skills': skills,
            'location': location,
            'job_type': job_type,
            'salary': salary,
            'date_posted': date_posted
        })
    
    df = pd.DataFrame(data)
    os.makedirs("remoteok_project/data", exist_ok=True)
    df.to_csv("remoteok_project/data/remoteok_jobs_cleaned.csv", index=False)
    print(f"Generated {num_records} mock records in remoteok_project/data/remoteok_jobs_cleaned.csv")

if __name__ == "__main__":
    import os
    generate_mock_data(150)
