import argparse
from enum import Enum

from .database import initialize_database, create_session, get_sessions

class VALID_FOCUSES(Enum):
    WAVING = "Waving"
    POPPING = "Popping"
    ANIMATION = "Animation"
    BOOGALOO = "Boogaloo"
    TUTTING = "Tutting"
    MUSICALITY = "Musicality"
    FREESTYLE = "Freestyle"    

parser = argparse.ArgumentParser(description="Track your practice.")
subparsers = parser.add_subparsers(
    dest="command",
    required=True
)

# Log Subcommand
log_parser = subparsers.add_parser("log", help="log a new practice session")

log_parser.add_argument(
    "--minutes", "-m",
    help="minutes spent practicing",
    type=int,
    required=True
)

log_parser.add_argument(
    "--focus", "-f",
    help="specific focus for practice session",
    type=str.title,
    choices=[focus.value for focus in VALID_FOCUSES],
    required=True
)

# History Subcommand
history_parser = subparsers.add_parser("history", help="view logged practice sessions")

args = parser.parse_args()

initialize_database()

if args.command == "log":
    create_session(args.minutes, args.focus)
    print(f"You practiced {args.focus} for {args.minutes} minutes!")

elif args.command == "history":
    sessions = get_sessions()

    if not sessions:
        print("No practice sessions have been logged yet.")
    else:
        print(sessions)

