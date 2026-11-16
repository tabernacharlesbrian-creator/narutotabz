"""Local (offline) Sharingan stage evaluator. No API key / internet needed.

generate(text) -> "tomoe 1" | "tomoe 2" | "tomoe 3" | "mangekyou"
"""
import re

# Phrases that sound deadly but are NOT the loss of a loved one
_NEUTRALIZE = [
    "brink of death", "near death", "near-death", "life-or-death", "life or death",
    "close to death", "face of death", "death match",
]

_LOSS = [
    r"\bdied\b", r"\bdies\b", r"\bdead\b", r"\bdeath of\b", r"\bkilled\b", r"\bmurdered\b",
    r"\bslain\b", r"\bpassed away\b", r"\bnever (see|hold|speak to) (him|her|them) again\b",
    r"\blost (him|her|them) forever\b", r"\bslipped from mine\b", r"\bdying in my arms\b",
    r"\bwatched (him|her|them)\b.*\b(fall|die|burn|drown)\b", r"\bfell? into the abyss\b",
    r"\bwatched helplessly\b.*\b(struck|hit|killed)\b",
]

_LOVED = [
    "wife", "husband", "best friend", "brother", "sister", "sibling", "mother", "father",
    "mom", "dad", "son", "daughter", "girlfriend", "boyfriend", "partner", "love of my life",
    "fiancee", "fiancé", "fiance", "teammate", "master",
]

_T3 = [
    "sever", "bond", "resolve", "harden", "mentor", "slow motion", "cold desire",
    "let go", "letting go", "break my limit", "breaking past", "choice", "decision",
    "heart", "shift", "former", "betray",
]
_T2 = [
    "limit", "cornered", "backed into", "armed", "exhausted", "focus", "counter",
    "dodge", "fight", "duel", "stress", "thieves", "attack", "lunged", "strike",
    "pushed", "predict", "movement", "footwork",
]
_T1 = [
    "panic", "terror", "terrified", "scared", "afraid", "fear", "protect", "save",
    "sprint", "ran", "adrenaline", "grief", "sad", "longing", "miss", "cry", "rockslide",
    "desperate",
]


def _count(text: str, words) -> int:
    return sum(1 for w in words if w in text)


def generate(input_text: str) -> str:
    text = (input_text or "").lower()
    for phrase in _NEUTRALIZE:
        text = text.replace(phrase, " ")

    has_loss = any(re.search(p, text) for p in _LOSS)
    has_loved = any(w in text for w in _LOVED)
    if has_loss and has_loved:
        return "mangekyou"

    t3, t2, t1 = _count(text, _T3), _count(text, _T2), _count(text, _T1)
    if t3 >= 3 and t3 >= t2 - 1:
        return "tomoe 3"
    if t2 >= 3 and t2 > t1:
        return "tomoe 2"
    if t3 >= 2 and t3 > t2:
        return "tomoe 3"
    if t2 >= 2 and t2 > t1:
        return "tomoe 2"
    return "tomoe 1"
