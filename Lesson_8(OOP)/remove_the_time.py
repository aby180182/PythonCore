def shorten_to_date(long_date):
    short_date, remainder = long_date.split(',')
    return ''.join(short_date)