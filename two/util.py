from random import choice
from pkg_resources import resource_stream

def two():
    stream = resource_stream("two", "src/data.txt")
    datas = [_v.decode().strip("\n") for _v in stream.readlines()]
    print(choice(datas))
    stream.close()
