import requests
from bs4 import BeautifulSoup
import pandas as pd

# Website URL
url = "https://realpython.github.io/fake-jobs/"

# Headers
headers = {
    "User-Agent": "Mozilla/5.0"
}

try:
    # Send Request
    response = requests.get(url, headers=headers)

    # Check Request Status
    response.raise_for_status()

    # Parse HTML
    soup = BeautifulSoup(response.text, "lxml")

    # Find All Job Cards
    jobs = soup.find_all("div", class_="card-content")

    # Empty List For Storing Data
    job_list = []

    # Loop Through Jobs
    for job in jobs:

        # Get Job Title
        title = job.find("h2", class_="title")

        # Get Company Name
        company = job.find("h3", class_="company")

        # Get Location
        location = job.find("p", class_="location")

        # Store Data In Dictionary
        job_data = {
            "Job Title": title.text.strip() if title else "N/A",
            "Company": company.text.strip() if company else "N/A",
            "Location": location.text.strip() if location else "N/A"
        }

        # Add Data Into List
        job_list.append(job_data)

    # Convert List To DataFrame
    df = pd.DataFrame(job_list)

    # Print Data
    print("\n===== JOB DATA =====\n")
    print(df)

    # Save CSV File
    df.to_csv("jobs_data.csv", index=False)

    print("\nCSV File Created Successfully!")
    print("File Name: jobs_data.csv")

except requests.exceptions.RequestException as e:
    print("Request Error:", e)

except Exception as e:
    print("Error:", e)