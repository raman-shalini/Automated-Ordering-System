from automation.playwright_base import get_browser

def order_blinkit(items):
    pw, browser = get_browser()
    page = browser.new_page()
    page.goto("https://blinkit.com")

    for item in items:
        print(f"Adding {item}")

    browser.close()
    pw.stop()
