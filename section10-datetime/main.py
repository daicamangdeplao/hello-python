import datetime


def run():
    # POINT-1: Current date-time
    now = datetime.datetime.now(datetime.timezone.utc)
    print(now)
    print(now.date())
    print(now.time())
    print(now.timestamp())
    # POINT-2: Manipulate datetime
    the_eve = datetime.date.fromisoformat('2023-12-31')
    print(the_eve)
    the_eve += datetime.timedelta(days=1)
    print(the_eve)
    # POINT-3: Construct a random datetime
    some_date = datetime.datetime.fromisoformat('2015-10-14T11:30:00')
    print(some_date)


if __name__ == '__main__':
    run()
