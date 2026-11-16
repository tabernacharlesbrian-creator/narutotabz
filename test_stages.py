"""Run: python test_stages.py"""
from evolution_of_sharingan import generate

CASES = [
 ("I was hiking with my little brother when a sudden rockslide started. I looked up and saw a massive boulder tumbling down the hill, heading straight for him. I had never felt such sheer panic and terror in my life. Driven by pure adrenaline and a desperate need to save him, I sprinted faster than I ever have before to push him out of the way.", "tomoe 1"),
 ("I was backed into a corner in a dark alley by three armed thieves. I had already taken a bad hit to the ribs and was completely exhausted. As the leader lunged at me with a pipe, I realized I couldn't just brace for impact anymore. Under the extreme stress of the fight, I forced my mind to focus entirely on his footwork and muscle twitches, pushing my physical limits to dodge the strike and counter-attack.", "tomoe 2"),
 ("I was locked in a brutal, bloody duel with my former mentor inside a burning building. He was faster and stronger, and I was on the brink of death. I realized my lingering respect for him was holding me back. In a split second, I made the agonizing choice to completely sever our past bond and harden my heart. With my resolve instantly shifted from hesitation to a cold desire to survive, his previously blinding movements suddenly looked like they were moving in slow motion.", "tomoe 3"),
 ("During the chaotic evacuation of the collapsing city, the scaffolding gave way beneath my wife. I managed to grab her hand just in time, but my grip was slipping due to the rain. She looked up at me, smiled, and told me she loved me before her hand slipped from mine. I screamed in agonizing, soul-crushing despair as I watched the love of my life fall into the abyss, knowing I would never see her again.", "mangekyou"),
 ("I watched helplessly as a car struck my best friend. They died in my arms before the ambulance could arrive.", "mangekyou"),
 ("I was walking home when a dog attacked my little sister. I was so scared but I jumped in front of her to take the bite.", "tomoe 1"),
 ("My best friend and I were fighting a group of bullies. We were exhausted, beaten down, and I couldn't keep up with their movements, but I forced myself to focus harder to win.", "tomoe 2"),
]

bad = 0
for text, expected in CASES:
    got = generate(text)
    ok = got == expected
    bad += not ok
    print(("PASS" if ok else "FAIL"), expected, "->", got)
raise SystemExit(1 if bad else 0)
