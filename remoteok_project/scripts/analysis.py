import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Set style for visualizations
sns.set_theme(style="whitegrid")

def run_analysis():
    # Load the data
    data_path = 'remoteok_project/data/remoteok_jobs_cleaned.csv'
    if not os.path.exists(data_path):
        print(f"Error: {data_path} not found.")
        return
    
    df = pd.read_csv(data_path)
    os.makedirs("remoteok_project/visualizations", exist_ok=True)

    # --- Visualization 1: Top 10 Skills Demand (Bar Chart) ---
    print("Generating Visualization 1: Top 10 Skills...")
    df_skills = df.copy()
    df_skills['skills'] = df_skills['skills'].str.split(', ')
    df_skills = df_skills.explode('skills')
    top_skills = df_skills['skills'].value_counts().head(10)

    plt.figure(figsize=(12, 6))
    sns.barplot(x=top_skills.index, y=top_skills.values, palette="viridis")
    plt.title('Top 10 Most Demanded Skills in Remote Jobs', fontsize=14, fontweight='bold')
    plt.xlabel('Skill', fontsize=12)
    plt.ylabel('Number of Job Postings', fontsize=12)
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.savefig('remoteok_project/visualizations/top_skills.png', dpi=300)
    plt.close()

    # --- Visualization 2: Job Type Distribution (Pie Chart) ---
    print("Generating Visualization 2: Job Type Distribution...")
    job_type_counts = df['job_type'].value_counts()
    plt.figure(figsize=(10, 8))
    plt.pie(job_type_counts, labels=job_type_counts.index, autopct='%1.1f%%', startangle=90, colors=sns.color_palette("pastel"))
    plt.title('Distribution of Job Types in Remote Jobs', fontsize=14, fontweight='bold')
    plt.tight_layout()
    plt.savefig('remoteok_project/visualizations/job_type_distribution.png', dpi=300)
    plt.close()

    # --- Visualization 3: Top 10 Job Titles (Horizontal Bar Chart) ---
    print("Generating Visualization 3: Top 10 Job Titles...")
    top_titles = df['title'].value_counts().head(10)
    plt.figure(figsize=(12, 8))
    sns.barplot(x=top_titles.values, y=top_titles.index, palette="magma")
    plt.title('Top 10 Most Common Remote Job Titles', fontsize=14, fontweight='bold')
    plt.xlabel('Number of Postings', fontsize=12)
    plt.ylabel('Job Title', fontsize=12)
    plt.tight_layout()
    plt.savefig('remoteok_project/visualizations/top_job_titles.png', dpi=300)
    plt.close()

    # --- Visualization 4: Skill Frequency Comparison (Horizontal Bar Chart) ---
    print("Generating Visualization 4: Skill Frequency Comparison...")
    top_skills_extended = df_skills['skills'].value_counts().head(15)
    plt.figure(figsize=(12, 10))
    sns.barplot(x=top_skills_extended.values, y=top_skills_extended.index, palette="coolwarm")
    plt.title('Top 15 Skills Frequency in Remote Job Postings', fontsize=14, fontweight='bold')
    plt.xlabel('Frequency (Count)', fontsize=12)
    plt.ylabel('Skill', fontsize=12)
    plt.tight_layout()
    plt.savefig('remoteok_project/visualizations/skill_frequency_comparison.png', dpi=300)
    plt.close()

    # --- Comparative Analysis 1: Contract vs Full-Time Roles ---
    print("\n--- Comparative Analysis: Contract vs Full-Time ---")
    full_time = df[df['job_type'] == 'Full-Time'].copy()
    contract = df[df['job_type'] == 'Contract'].copy()

    def get_top_skills(subset_df, n=10):
        s = subset_df.copy()
        s['skills'] = s['skills'].str.split(', ')
        s = s.explode('skills')
        return s['skills'].value_counts().head(n)

    top_ft_skills = get_top_skills(full_time)
    top_c_skills = get_top_skills(contract)

    print("Top Skills for Full-Time Jobs:")
    print(top_ft_skills)
    print("\nTop Skills for Contract Jobs:")
    print(top_c_skills)

    # --- Comparative Analysis 2: Skill Demand Across Job Titles ---
    print("\n--- Comparative Analysis: Skill Demand Across Top Titles ---")
    top_3_titles = df['title'].value_counts().head(3).index.tolist()

    for title in top_3_titles:
        title_jobs = df[df['title'] == title].copy()
        title_skills = get_top_skills(title_jobs, 5)
        print(f"\nTop skills for '{title}':")
        print(title_skills)

    print("\nAnalysis complete. Visualizations saved in 'remoteok_project/visualizations/'.")

if __name__ == "__main__":
    run_analysis()
