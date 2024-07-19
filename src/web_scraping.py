import time
from bs4 import BeautifulSoup
from fpdf import FPDF
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

def scrape_and_save_to_pdf(url, output_file):
    # Set up Chrome WebDriver options
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")  # To run Chrome in headless mode
    options.add_argument("--disable-gpu")
    options.add_argument("--window-size=1920x1080")
    options.add_argument("--no-sandbox")
    options.add_argument("--verbose")
    options.add_argument("--log-path=D:\\chrome.log")

    # Set up ChromeDriverManager to fetch the latest Chrome WebDriver binary
    driver_path = ChromeDriverManager().install()
    driver_path = 'C:/Users/Hafeez/.wdm/drivers/chromedriver/win64/126.0.6478.182/chromedriver-win32/chromedriver.exe'
    # Initialize Chrome WebDriver with options
    driver = webdriver.Chrome(executable_path=driver_path, options=options)

    try:
        # Send a GET request to the URL
        driver.get(url)
        
        # Wait for dynamic content to load (adjust sleep time as needed)
        time.sleep(10)  # Adjust sleep time as per the page load time

        # Get the page source after dynamic content has loaded
        html_content = driver.page_source
        soup = BeautifulSoup(html_content, 'html.parser')

        # Extract relevant information from the HTML (customize as per your needs)
        # Example: Finding all <p> tags
        paragraphs = soup.find_all('p')

        # Initialize PDF document
        pdf = FPDF()
        pdf.add_page()

        # Add DejaVuSans.ttf font (you need to provide the correct path)
        pdf.add_font('DejaVuSans', '', 'src/DejaVuSans.ttf', uni=True)
        pdf.set_font('DejaVuSans', size=12)

        # Add content to PDF
        for paragraph in paragraphs:
            text = paragraph.get_text(strip=True)
            pdf.multi_cell(200, 10, txt=text)  # Adjusting cell width to 200

        # Output PDF
        pdf.output(output_file)

        print(f"Data from {url} successfully saved to {output_file}")

    except Exception as e:
        print(f"An error occurred: {str(e)}")
    finally:
        driver.quit()

if __name__ == "__main__":
    url = "https://www.ihg.com/intercontinental/hotels/us/en/reservation"
    output_file = "hotel_info.pdf"
    scrape_and_save_to_pdf(url, output_file)
