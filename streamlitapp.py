import streamlit as st
import requests
import pandas as pd
import schedule
import time

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
    schedule.every().day.at("09:00").do(crawl_and_save_data)
    schedule.every().day.at("15:00").do(crawl_and_save_data)
    schedule.every().day.at("21:00").do(crawl_and_save_data)

    while True:
        # Run pending scheduled tasks
        schedule.run_pending()
        time.sleep(1)

# Run the Streamlit app
if __name__ == "__main__":
    main()

