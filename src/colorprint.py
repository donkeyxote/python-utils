#!/bin/python

__author__ = 'donkeyxote'

'''
module for colorful output
'''

colors={'gray':'\033[1;30m',\
        'red':'\033[1;31m',\
        'green':'\033[1;32m',\
        'yellow':'\033[1;33m',\
        'blue':'\033[1;34m',\
        'magenta':'\033[1;35m',\
        'cyan':'\033[1;36m',\
        'white':'\033[1;37m',\
        }

def colorprint(*args, **kwargs ):

    prefix=None
    suffix=None

    if kwargs.__contains__('col'):
        if colors.__contains__(kwargs['col']):
            prefix=colors[kwargs.pop('col','')]
            suffix='\033[1;m'
        else:
            kwargs.pop('col','')

    if (prefix != None) & (suffix != None):
        if len(args)>1:
            args=(prefix+str(args[0]),)+args[1:len(args)-1]+(str(args[len(args)-1])+suffix,)
        elif len(args)==1:
            args=(prefix+str(args[0])+suffix,)
            
    print(*args, **kwargs)

if __name__=='__main__':
    for color in colors:
        colorprint(color, col=color)
