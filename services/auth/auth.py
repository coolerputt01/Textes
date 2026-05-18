from ..models.models import Profile 
from ..utils.utils import date_now

def create_user(username: str, bio: str="I am a Textes user") -> int:
    if not username or not username.strip():
        print(f"Username invalid")
        return 1

    existing = Profile.get_or_none(Profile.username == username)
    if existing:
        print(f"Username exists!")
        return 1

    try:
        Profile.create(
            username=username,
            bio=bio,
            session=0,
            join_date=date_now()
            )
        return 0
    except Exception as e:
        print(f"Database insertion failed: {e}")
        return 1
