# main.py
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time
import os

# Function to take screenshots
def take_screenshot(driver, file_path):
    driver.save_screenshot(file_path)

# Main Automation Function
def main():
    # Setup Chrome driver with WebDriver Manager
    service = Service(ChromeDriverManager().install())
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=service, options=options)
    driver.maximize_window()
    wait = WebDriverWait(driver, 15)

    # Step 1: Navigate to Shine.com
    driver.get("https://www.shine.com")
    print("Page Title:", driver.title)
    print("Current URL:", driver.current_url)

    # Step 2: Click Login button
    top_login_btn = wait.until(EC.element_to_be_clickable(
        (By.XPATH, "//button[contains(text(),'Login')]")
    ))
    top_login_btn.click()

    # Step 3: Enter credentials
    email_field = wait.until(EC.visibility_of_element_located((By.ID, "id_email_login")))
    email_field.send_keys("navyasri11488@gmail.com")

    password_field = driver.find_element(By.ID, "id_password")
    password_field.send_keys("Navyasri@123")

    final_login_btn = driver.find_element(
        By.XPATH,
        "//*[@id=\"cndidate_login_widget\"]/div[1]/form[5]/ul[1]/li[4]/div/button"
    )
    final_login_btn.click()

    # Step 4: Wait for login to complete
    wait.until(EC.url_contains("shine.com"))
    take_screenshot(driver, "screenshots/1_login_success.png")
    print("✅ Logged in successfully")

    # Step 5: Click search container
    search_container = wait.until(EC.element_to_be_clickable((
        By.XPATH, "//*[@id='ReactContainer']/div[1]/div/div/div[1]/div[1]/div/div/div"
    )))
    search_container.click()
    time.sleep(1.5)

    # Step 6: Enter Job Title
    job_input = wait.until(EC.visibility_of_element_located((By.ID, "id_q")))
    job_input.clear()
    job_input.send_keys("Software Tester")

    # Step 7: Enter Location
    location_input = wait.until(EC.visibility_of_element_located((By.ID, "id_loc")))
    location_input.clear()
    location_input.send_keys("Hyderabad")

    # Step 8: Select Experience
    exp_dropdown = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='search_exp_div']")))
    exp_dropdown.click()

    two_years = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='item-key-2']/label")))
    two_years.click()

    # Step 9: Click Search button
    search_button = wait.until(EC.element_to_be_clickable(
        (By.XPATH, "//*[@id=\"frm_adv_srch\"]/div[2]")
    ))
    search_button.click()

    take_screenshot(driver, "screenshots/2_search_filled.png")
    print("✅ Search submitted")

    # Step 10: Click 2nd Job in the list
    time.sleep(4)
    second_job_card = wait.until(EC.element_to_be_clickable(
        (By.XPATH, "//*[@id='__next']/div[3]/div[2]/div[2]/div/div/div[2]/div[5]")
    ))
    second_job_card.click()

    # Step 11: Wait for Job Details
    job_title_elem = wait.until(EC.visibility_of_element_located(
        (By.XPATH, "//*[@id='jdCardNova']/div[1]/div[1]/div[1]/h1")
    ))
    company_name_elem = wait.until(EC.visibility_of_element_located(
        (By.XPATH, "//*[@id='jdCardNova']/div[1]/div[1]/div[1]/span")
    ))

    print("🧾 Job Title:", job_title_elem.text)
    print("🏢 Company Name:", company_name_elem.text)
    take_screenshot(driver, "screenshots/3_job_detail.png")

    # Step 12: Click Apply button
    apply_btn = wait.until(EC.element_to_be_clickable(
        (By.XPATH, "//*[starts-with(@id, 'id_apply_')]")
    ))
    apply_btn.click()

    take_screenshot(driver, "screenshots/4_applied_successfully.png")
    print("✅ Applied successfully!")

    driver.quit()

# Entry point
if __name__ == "__main__":
    main()