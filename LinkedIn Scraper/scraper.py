from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# Function to scrape LinkedIn posts
def scrape_linkedin_posts(tag, reference, output_file):
    # Set up the Selenium webdriver
    driver = webdriver.Chrome()  # You may need to download chromedriver: https://sites.google.com/a/chromium.org/chromedriver/
    driver.get("https://www.linkedin.com")

    # You should manually log in here

    # Navigate to the LinkedIn feed
    driver.get("https://www.linkedin.com/feed/")

    # Wait for the page to load
    time.sleep(5)

    # Search for posts with specific tag
    search_box = driver.find_element_by_xpath("//input[@aria-label='Search']")
    search_box.send_keys("#" + tag)
    search_box.send_keys(Keys.RETURN)

    # Wait for search results to load
    time.sleep(5)

    # Extract posts
    posts = driver.find_elements_by_xpath("//div[contains(@class, 'occludable-update')]")

    # Write posts to a text file
    with open(output_file, 'w', encoding='utf-8') as file:
        for post in posts:
            post_text = post.text
            if reference in post_text:
                file.write(post_text + '\n')
                file.write('-' * 50 + '\n')

    # Close the webdriver
    driver.quit()

# Example usage
scrape_linkedin_posts(tag="technology", reference="research paper", output_file="linkedin_posts.txt")
