from bs4 import BeautifulSoup
from getpass import getpass
from playwright.sync_api import sync_playwright
from myKoob.get_tasks import get_tasks
from myKoob.format_tasks import format_tasks

def get_mykoob_tasks():
    email = input("enter email: ")
    password = getpass("enter password: ")

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=50)
        page = browser.new_page()
        page.goto("https://login.mykoob.lv/#/lv")
        page.click("button.css-6strkb")
        page.fill("input.input", email)
        page.fill("input.password-input", password)
        page.click("button[type=submit]")
        page.is_visible("div.item")
        html = page.inner_html("#profile_right_data")

        soup = BeautifulSoup(html, "html.parser")
        task_html = soup.find_all(True, {"class": "item"})
        task_soup = BeautifulSoup(str(task_html), "html.parser")
        
        task_bod = task_soup.find_all("td", attrs={"style": "overflow-wrap:anywhere"})
        task_str = BeautifulSoup(str(task_bod), "html.parser").get_text()

        tasks = get_tasks(task_str)

        formatted_tasks = format_tasks(tasks)

        return formatted_tasks