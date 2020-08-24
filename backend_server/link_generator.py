from hashlib import md5
from datetime import datetime


def generator(link):
    '''
    Generates a shortened link using a simple hash(link + salt) approach. Result is truncated to 7 chars for readability
    :param: link: string
    

    '''
    if type(link) == str:
        newString = link + str(getTime())
        return md5(newString.encode()).hexdigest()[0:7]
    else:
        raise TypeError

def getTime():
    return datetime.now()
