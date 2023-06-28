import requests
from bs4 import BeautifulSoup
import os
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

def download_image(url, directory):
    """
    This is a function for downloading and saving images from URLs.
    
    The function checks the URL is valid (starts with “http”) then sends a GET request, storing the response object, whose status is checked. 
    If the status code is 200 (successful request), the function extracts the file name and constructs a new file path for the save directory.
    The image is then saved in the correct directory. 
    
    Success/fail messages have been commented out for now.

    """
    if url.startswith("http"):
        response = requests.get(url)
        if response.status_code == 200:
            file_name = url.split("/")[-1]
            file_path = os.path.join(directory, file_name)
            with open(file_path, "wb") as file:
                file.write(response.content)
            # print(f"Downloaded {file_name}")
        #else:
            # print(f"Failed to download {url}")
    #else:
        # print(f"Invalid URL: {url}")

def scrape_images(url, num_images, directory, driver):
    """
    This function downloads and saves images from a specified webpage. 

    It takes a URL, number of images (to download), directory address for saving images into and a driver.
    The driver allows for simulated behaviour on webpages (scrolling etc.) which is useful for accessing images.
    It then sends a GET request to the specified URL, if the request is successful (status 200), the HTML content is parsed via the BeautifulSoup class. 
    This class has method for retrieving <img> elements from the parsed HTML. 
    The function then checks for the specified directory and creates it if does not yet exist. 
    The URL of each image is extracted and the download_image function is used to download and save each image, up to the specified limit of images.

    """
    driver.get(url)  # Load the URL for the current search query

    # Simulate scrolling
    body = driver.find_element(By.CSS_SELECTOR, 'body')
    num_scrolls = num_images // 20  # Assuming each scroll fetches 20 images
    for _ in range(num_scrolls):
        # scrolls to the bottom of the webpage every 1 second
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(1)

    # Get the HTML source after scrolling
    html_source = driver.page_source

    # Scrape images from the HTML source
    soup = BeautifulSoup(html_source, 'html.parser')
    image_elements = soup.find_all("img")

    # Create directory if it doesn't exist
    if not os.path.exists(directory):
        os.makedirs(directory)

    # Download images
    count = 0
    for image_element in image_elements:
        if count == num_images:
            break
        image_url = image_element["src"]
        download_image(image_url, directory)
        count += 1

search_query_rock = "hand making a fist"
search_query_paper = "hand flat palm down"
search_query_scissors = "scissors finger hand gesture"
num_images = 1000

# Constructs URLS for the search queries

search_query_rock = search_query_rock.replace(" ", "+")
search_query_paper = search_query_paper.replace(" ", "+")
search_query_scissors = search_query_scissors.replace(" ", "+")
url_rock = f"https://www.google.com/search?q={search_query_rock}&tbm=isch"
url_paper = f"https://www.google.com/search?q={search_query_paper}&tbm=isch"
url_scissors = f"https://www.google.com/search?q={search_query_scissors}&tbm=isch"
chromedriver_path = "/home/frances/Documents/chromedriver" 

for url, directory in zip([url_rock, url_paper, url_scissors], ["rock_images", "paper_images", "scissors_images"]):
    # the service object starts and stops chrome driver
    service = Service(chromedriver_path)
    driver = webdriver.Chrome(service=service)
    

    scrape_images(url, num_images, directory, driver)
    
    driver.quit()  # Close the WebDriver
