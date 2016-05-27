import iso8601


def format_datetime(value):
    return iso8601.parse_date(str(value)).strftime("%x")
