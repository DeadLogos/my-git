def convert_seconds(secs: int) -> str:
    days, secs = divmod(secs, 24 * 3600)
    hours, secs = divmod(secs, 3600)
    minutes, secs = divmod(secs, 60)
    res = f'{days}:{hours:0>2}:{minutes:0>2}:{secs:0>2}'
    return res


if __name__ == '__main__':
    pass
