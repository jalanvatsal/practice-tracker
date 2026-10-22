import argparse

VALID_FOCUSES: list[str] = [
    "Waving",
    "Popping",
    "Animation",
    "Boogaloo",
    "Tutting",
    "Musicality",
    "Freestyle",
]

parser = argparse.ArgumentParser()

parser.add_argument("minutes", help="minutes spent practicing within a particular focus", type=int)
parser.add_argument("focus", help="specific focus for practice session", type=str.title, choices=VALID_FOCUSES)

args = parser.parse_args()

print(f"You practiced {args.focus} for {args.minutes} minutes!")

