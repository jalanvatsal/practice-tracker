from collections import defaultdict
from .database import get_sessions

def get_practice_time_by_focus() -> dict[str, int]:
    """Calculate total practice minutes for each focus."""
    sessions = get_sessions()

    practice_time = defaultdict(int)

    for session in sessions:
        _, _, minutes, focus = session
        practice_time[focus] += minutes

    return dict(practice_time)