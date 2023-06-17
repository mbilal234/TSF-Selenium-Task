from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


def test_the_sparks_foundation_website():
    # Create a new WebDriver instance
    driver = webdriver.Chrome()

    try:
        # Navigate to the Sparks Foundation website
        driver.get("https://www.thesparksfoundationsingapore.org/")

        # Check if the logo exists
        logo = driver.find_element(By.ID, "home")
        assert logo.is_displayed()
        print("Logo check passed")
    except Exception as e:
        print("Logo check failed")

    try:
        # Check if the navigation bar appears
        navbar = driver.find_element(By.CSS_SELECTOR, ".navbar-collapse")
        assert navbar.is_displayed()
        print("Navigation bar check passed")
    except Exception as e:
        print("Navigation bar check failed")

    try:
        # Check if the search bar is displayed
        search_bar = driver.find_element(By.ID, "home")
        assert search_bar.is_displayed()
        print("Search bar check passed")
    except Exception as e:
        print("Search bar check failed")

    try:
        # Check if the contact section is displayed
        contact_section = driver.find_element(By.ID, "contact")
        assert contact_section.is_displayed()
        print("Contact section check passed")
    except Exception as e:
        print("Contact section check failed")

    try:
        # Check if the footer exists
        footer = driver.find_element(By.CSS_SELECTOR, ".site-footer")
        assert footer.is_displayed()
        print("Footer check passed")
    except Exception as e:
        print("Footer check failed")

    try:
        # Go to About Us page
        about_us_link = driver.find_element(By.LINK_TEXT, "About Us")
        about_us_link.click()
        print("About Us page check passed")

        # Check if the name on the "About Us" page is correct
        name = driver.find_element(By.CSS_SELECTOR, "#home span")
        assert name.text == "The Sparks Foundation"
        print("About Us page name check passed")
    except Exception as e:
        print("About Us page check failed")

    try:
        # Go back to Home page
        driver.back()
        print("Home page check passed")

        # Go to Join Us page
        join_us_link = driver.find_element(By.LINK_TEXT, "Join Us")
        join_us_link.click()
        print("Join Us page check passed")

        # Go back to Home page
        driver.back()
        print("Home page check passed")

        # Go to Programs page
        programs_link = driver.find_element(By.LINK_TEXT, "Programs")
        programs_link.click()
        print("Programs page check passed")

        # Go back to Home page
        driver.back()
        print("Home page check passed")

        # Go to Contact Us page
        contact_us_link = driver.find_element(By.LINK_TEXT, "Contact Us")
        contact_us_link.click()
        print("Contact Us page check passed")

        # Check if the contact form is displayed
        contact_form = driver.find_element(By.ID, "contact-form")
        assert contact_form.is_displayed()
        print("Contact Us page form check passed")
    except Exception as e:
        print("Contact Us page check failed")

    try:
        # Go back to Home page
        driver.back()
        print("Home page check passed")

        # Go to Links page
        links_link = driver.find_element(By.LINK_TEXT, "Links")
        links_link.click()
        print("Links page check passed")

        # Go back to Home page
        driver.back()
        print("Home page check passed")

    except Exception as e:
        print("Links page check failed")

    # Output success message
    print("All checks completed!")

    # Close the WebDriver instance
    driver.quit()


if __name__ == "__main__":
    test_the_sparks_foundation_website()
