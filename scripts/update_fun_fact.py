"""Replace the text between <!--FACT:START--> and <!--FACT:END--> in README.md
with a different fun fact each day (rotates through the list by date)."""
import datetime
import pathlib
import re

FACTS = [
    "Honey never spoils — archaeologists have found 3,000-year-old pots of honey in ancient Egyptian tombs that are still perfectly edible.",
    "Octopuses have three hearts and blue blood.",
    "A day on Venus is longer than a year on Venus.",
    "Bananas are berries, but strawberries aren't.",
    "The first computer 'bug' was a real moth found stuck in a Harvard Mark II relay in 1947.",
    "Sharks existed before trees — by roughly 50 million years.",
    "The word 'robot' comes from the Czech word 'robota', meaning forced labour.",
    "Wombat poop is cube-shaped.",
    "There are more possible games of chess than atoms in the observable universe.",
    "Python is named after Monty Python's Flying Circus, not the snake.",
    "A teaspoon of neutron star material would weigh about a billion tonnes on Earth.",
    "Sea otters hold hands while sleeping so they don't drift apart.",
    "The Eiffel Tower can grow about 15 cm taller in summer as the iron expands.",
    "Your brain uses roughly 20% of your body's energy while being about 2% of its weight.",
    "The first 1 GB hard drive (IBM, 1980) weighed over 200 kg and cost around $40,000.",
    "Light from the Sun takes about 8 minutes and 20 seconds to reach Earth.",
    "Cows have best friends and get stressed when separated from them.",
    "The original name of Google was 'BackRub'.",
    "Butterflies taste with their feet.",
    "A group of flamingos is called a 'flamboyance'.",
    "The Great Wall of China is not visible to the naked eye from space.",
    "JavaScript was created in about 10 days by Brendan Eich in 1995.",
    "Hot water can sometimes freeze faster than cold water — it's called the Mpemba effect.",
    "Koalas have fingerprints almost indistinguishable from human ones.",
    "There are more trees on Earth than stars in the Milky Way.",
    "The 'QWERTY' layout was designed partly to stop early typewriter keys from jamming.",
    "Water can boil and freeze at the same time at its triple point.",
    "Humans share about 60% of their DNA with bananas.",
    "The first website ever made is still online at info.cern.ch.",
    "An octopus can taste with its arms.",
    "Venus is the hottest planet in the solar system, even though Mercury is closer to the Sun.",
    "Linux's mascot, Tux, was chosen because Linus Torvalds was once bitten by a penguin.",
    "Sloths can hold their breath longer than dolphins — up to 40 minutes.",
    "The human nose can distinguish at least a trillion different smells.",
    "The 'Turing test' was proposed by Alan Turing in 1950 as 'the imitation game'.",
    "Saturn would float in water if you could find a bathtub big enough — its density is lower than water's.",
    "The shortest war in history, between Britain and Zanzibar in 1896, lasted under 45 minutes.",
    "A bolt of lightning is about five times hotter than the surface of the Sun.",
    "The first email was sent by Ray Tomlinson in 1971 — and he chose the @ symbol.",
    "Tardigrades can survive the vacuum of space.",
    "Some metals, like gallium, melt in your hand.",
    "ChatGPT reached 100 million users about two months after launch, one of the fastest-growing apps ever.",
    "A single cloud can weigh more than a million kilograms.",
    "The heart of a blue whale is about the size of a small car.",
    "'Debugging' with a rubber duck — explaining code line by line to a toy — is a real technique from 'The Pragmatic Programmer'.",
]

readme = pathlib.Path(__file__).resolve().parent.parent / "README.md"
today = datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=5, minutes=30))).date()
fact = FACTS[today.toordinal() % len(FACTS)]

text = readme.read_text(encoding="utf-8")
new = re.sub(r"(<!--FACT:START-->\n).*?(\n<!--FACT:END-->)",
             lambda m: m.group(1) + fact + m.group(2), text, flags=re.S)
if new == text:
    print("Fact unchanged.")
else:
    readme.write_text(new, encoding="utf-8")
    print("New fact:", fact)
