from helium import start_chrome
from bs4 import BeautifulSoup
from pynput.keyboard import Key, Controller
import time

url = "https://monkeytype.com/"
browser = start_chrome(url, headless=False) # headless = True if you want the browser window to NOT appear
kb = Controller()
time.sleep(2) # Let the browser fully load dynamic DOM elements

# You can set these properties
# KEYDELAY and total_time in seconds
KEYDELAY: float = 0.05
total_time: float | int = 30

def get_words():
    soup = BeautifulSoup(browser.page_source, "html.parser")
    breakpoint_word = soup.find(attrs={"class", "word active"})
    words = breakpoint_word.find_all_next(attrs={"class", "word"})

    query = ""

    for letter in breakpoint_word.find_all("letter"):
        query += letter.text
    query += " "

    for word in words:
        current_letters = word.find_all("letter")
        for letter in current_letters:
            query += letter.text
        query += " "
    
    return query.split(" ")[:-1] # [:-1] simply doesn't include the empty string at the end of the list

def type_word(word) -> None:
    for letter in word:
        kb.press(letter)
        time.sleep(KEYDELAY)
        kb.release(letter)
    kb.press(Key.space)
    time.sleep(KEYDELAY)
    kb.release(Key.space)

def timeout(st):
    return time.time() - st <= total_time

idx = 0
current = get_words()

time.sleep(2)
start_time = time.time()

while (timeout(start_time)):
    if idx == current.__len__() - 1:
        type_word(current[idx])
        current = get_words()
        idx = 0

    type_word(current[idx])
    idx += 1
