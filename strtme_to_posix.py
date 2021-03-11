from datetime import datetime
from calendar import timegm


def strtime_to_posix(dt_text, fmt='%Y-%m-%d %H:%M:%S %z') -> int:
    """ Converts a date & time string in the fmt provided
        Returns an integer timestamp
        Default fmt fits Subversion datetime in the format '%Y-%m-%d %H:%M:%S %z'
        which expects a date-time str e.g., '2019-11-06 22:15:04 -0800'
    """

    try:
        datetime.strptime(dt_text, fmt)
    except ValueError:
        raise ValueError(f'Incorrect date format, expected {fmt}')

    date = datetime.strptime(dt_text, fmt)
    return timegm(date.utctimetuple())


if __name__ == '__main__':

    print(strtime_to_posix('2019-11-06 22:15:04 -0800'))

