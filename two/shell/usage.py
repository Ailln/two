from time import ctime

from two.version import VERSION


def run():
    cur_time = ctime()
    text = f"""
    # two
    
    Version {VERSION} ({cur_time} +0800)
    """
    print(text)
