from datetime import datetime
from time import mktime

from pytz import timezone


def get_time() -> datetime:
    return datetime.now(timezone("Asia/Seoul"))


def datetime_to_unix(n: datetime) -> int:
    return int(mktime(n.timetuple()))
