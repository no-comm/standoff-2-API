from playwright.sync_api import Playwright, sync_playwright, expect
import requests

def run(playwright: Playwright, id: str) -> None:
    browser = playwright.chromium.launch(headless=True)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://store.standoff2.com/")
    page.get_by_placeholder("ID").click()
    page.get_by_placeholder("ID").fill(id)
    page.query_selector('//*[@id="boom"]/div/div/div/div[3]/div[2]/button').click()
    url = page.locator("img").nth(1).get_attribute("src")
    name = page.query_selector('//*[@id="boom"]/div/div/div/div[4]/div/div[2]/div[2]').text_content()
    context.close()
    browser.close()
    return [name, url]

def account(id: str) -> list["name", "url"]:
    with sync_playwright() as playwright:
        return run(playwright, id)

def avatar(url: str):
    f=open(r'image.webp', "wb")
    ufr = requests.get(url)
    f.write(ufr.content)
    f.close()
