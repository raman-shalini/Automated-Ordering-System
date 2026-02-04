from automation.selenium_base import get_driver
import time

def book_uber(pickup, drop, ride_type):
    driver = get_driver()
    driver.get("https://m.uber.com")

    # NOTE: login + selectors change frequently
    # This is skeleton logic

    print(f"Booking Uber from {pickup} to {drop} ({ride_type})")

    time.sleep(5)
    # stop at COD / confirmation step
    driver.quit()
