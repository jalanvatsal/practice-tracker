import argparse
from enum import Enum

from .database import initialize_database, create_session

class VALID_FOCUSES(Enum):
    WAVING = "Waving"
    POPPING = "Popping"
    ANIMATION = "Animation"
    BOOGALOO = "Boogaloo"
    TUTTING = "Tutting"
    MUSICALITY = "Musicality"
    FREESTYLE = "Freestyle"    

parser = argparse.ArgumentParser()

parser.add_argument("--minutes", "-m", help="minutes spent practicing within a particular focus", type=int, required=True)
parser.add_argument("--focus", "-f", help="specific focus for practice session", type=str.title, choices=[focus.value for focus in VALID_FOCUSES], required=True)

args = parser.parse_args()

initialize_database()
create_session(args.minutes, args.focus)

print(f"You practiced {args.focus} for {args.minutes} minutes!")
