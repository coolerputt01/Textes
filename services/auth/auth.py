from ..models.models import Profile 
from ..utils.utils import date_now

def create_user(username: str, bio: str) -> int:
    if not username or not username.strip():
        return 1

    existing = Profile.get_or_none(Profile.username == username)
    if existing:
        return 1

    try:
        Profile.create(
            username=username,
            bio=bio,
            session=0,
            join_date=lambda :date_now
            )
        return 0
    except Exception:
        return 1
