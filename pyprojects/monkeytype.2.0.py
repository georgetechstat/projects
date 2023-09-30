from pynput.keyboard import Key, Controller
import time

get_words_js: str = \
"""
query = ""
for (const el of document.getElementsByClassName("word")) {
    query += el.innerText + ' ';
}
"""

def type_words(txt: str) -> None:
    kb = Controller()

    txt = txt.split(' ')
    for word in txt:
        for letter in word:
            time.sleep(0.01)
            kb.press(letter)
            kb.release(letter)
        kb.press(Key.space)
        kb.release(Key.space)

TEXT: str = \
"""
here during see have if life so how he may make feel or for how get then group here however man group by program eye work we large person way possible however person many end as both eye seem can over they order show how other place person by still ask part need come of only on mean begin a look house at much on general we during good when little year move consider on when well general ask order for say stand tell begin we for another he open first feel just high by turn need call little for
"""

time.sleep(3)
type_words(TEXT)
