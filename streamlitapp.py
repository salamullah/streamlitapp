import streamlit as st
import requests
import pandas as pd
import schedule
from datetime import datetime, timedelta

# Function to crawl weather data and save to CSV
def crawl_and_save_data():
    # Replace the URL with the actual weather data URL you want to scrape
    weather_url = "https://example.com/weather"
    
    # Make an HTTP request to the weather website
    response = requests.get(weather_url)
    
    if response.status_code == 200:
        # Parse the HTML content or use any other method to extract data
        # For demonstration purposes, assuming the website returns JSON data
        weather_data = response.json()
        
        # Process the data and save it to a DataFrame
        df = pd.DataFrame(weather_data)
        
        # Save the DataFrame to CSV file on Streamlit server
        df.to_csv("weather_data.csv", index=False)
        st.success("Weather data crawled and saved to CSV.")
    else:
        st.error(f"Failed to crawl weather data. Status code: {response.status_code}")

# Streamlit app
def main():
    st.title("Weather Data Crawler App")

    # Schedule crawling task to run every 24 hours
    now = datetime.now()
    schedule_time_1 = datetime(now.year, now.month, now.day, 9, 0)  # 9:00 AM
    schedule_time_2 = datetime(now.year, now.month, now.day, 15, 0)  # 3:00 PM
    schedule_time_3 = datetime(now.year, now.month, now.day, 21, 0)  # 9:00 PM
    
    schedule.every().day.at(schedule_time_1.strftime('%H:%M')).do(crawl_and_save_data)
    schedule.every().day.at(schedule_time_2.strftime('%H:%M')).do(crawl_and_save_data)
    schedule.every().day.at(schedule_time_3.strftime('%H:%M')).do(crawl_and_save_data)

    while True:
        # Run pending scheduled tasks
        schedule.run_pending()
        time.sleep(1)

# Run the Streamlit app
if __name__ == "__main__":
    main()
