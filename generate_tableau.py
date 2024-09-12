import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
import os

file = 'Superstore_Orders.csv'
df = pd.read_csv(file)
            
# Set Up Chrome WebDriver
chrome_options = Options()
chrome_options.add_argument("--headless")  # Run Chrome in headless mode
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--no-sandbox")

# add chromedriver path
chrome_driver_path = 'C:\Program Files\ChromeDriver\chromedriver.exe'
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service, options=chrome_options)

# Define the base Tableau Public URL
base_url1 = "https://public.tableau.com/authoring/Helio_Campus_Presentation/Sheet1/Dashboard%202#1"
base_url2 = "https://public.tableau.com/authoring/Helio_Campus_Presentation/Sheet1/Dashboard%202#1"

# Create an output directory for images
output_directory = "output_images"
if not os.path.exists(output_directory):
    os.makedirs(output_directory)

# Loop through DataFrame and apply filters in the URL
for state in df.iterrows():
    state_filter = state['State']
    
    # Construct the URL with filters
    filter_url = f"{base_url1}?:embed=y&State={state_filter}"
    filter_url2 = f"{base_url2}?:embed=y&State={state_filter}"
    
    # Load the URL in the browser
    driver.get(filter_url)
    time.sleep(5)  # Wait for the dashboard to load completely

    # Define the output path for the screenshot
    screenshot_path = os.path.join(output_directory, f"{state_filter}.png")

    # Take a screenshot of the dashboard
    driver.save_screenshot(screenshot_path)
    print(f"Dashboard image saved: {screenshot_path}")

    # Load the URL in the browser
    driver.get(filter_url2)
    time.sleep(5)  # Wait for the dashboard to load completely

    # Define the output path for the screenshot
    screenshot_path = os.path.join(output_directory, f"{state_filter}.png")

    # Take a screenshot of the dashboard
    driver.save_screenshot(screenshot_path)
    print(f"Dashboard image saved: {screenshot_path}")

# Close the browser
driver.quit()
