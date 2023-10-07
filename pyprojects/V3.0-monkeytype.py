from helium import start_chrome
from bs4 import BeautifulSoup
from pynput.keyboard import Key, Controller
import time

url = "https://monkeytype.com/"

browser = start_chrome(url, headless=False) # headless = True if you want the browser window to NOT appear
soup = BeautifulSoup(browser.page_source, "html.parser")
kb = Controller()
time.sleep(2) # Let the browser fully load dynamic DOM elements
KEYDELAY: float = 0.05

word_element = soup.find_all(attrs={"class":"word"})

def extract_words(words) -> list[str]:
    query = ""
    for word in words:
        current_letters = word.find_all("letter")

        for letter in current_letters:
            query += letter.text
        query += " "
    return query.split(" ")[:-1] # [:-1] simply doesn't include the empty string at the end of the list

def write_text(txt: list[str]) -> None:
    start = time.time()
    for word in txt:
        if time.time() - start >= 30:
            break

        for letter in word:
            kb.press(letter)
            time.sleep(KEYDELAY)
            kb.release(letter)
        kb.press(Key.space)
        time.sleep(KEYDELAY)
        kb.release(Key.space)

time.sleep(2)
write_text(extract_words(word_element))
