#!/bin/python

__author__ = 'donkeyxote'

'''
module for colorful output
'''


textcolors={'gray':'\033[0;30m',\
        'red':'\033[0;31m',\
        'green':'\033[0;32m',\
        'yellow':'\033[0;33m',\
        'blue':'\033[0;34m',\
        'magenta':'\033[0;35m',\
        'cyan':'\033[0;36m',\
        'white':'\033[0;37m',\
        }


boldcolors={'gray':'\033[1;30m',\
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
    colors=textcolors


    if kwargs.__contains__('bold'):
        if kwargs['bold'] == True:
            colors=boldcolors
        kwargs.pop('bold','')


    if kwargs.__contains__('col'):
        if colors.__contains__(kwargs['col']):
            prefix=colors[kwargs.pop('col','')]
            suffix='\033[0;m'
        else:
            kwargs.pop('col','')


    if (prefix != None) & (suffix != None):
        if len(args)>1:
            args=(prefix+str(args[0]),)+args[1:len(args)-1]+(str(args[len(args)-1])+suffix,)
        elif len(args)==1:
            args=(prefix+str(args[0])+suffix,)
            
    print(*args, **kwargs)


if __name__=='__main__':
    
    for color in textcolors:
        colorprint(color, col=color)
        
    for color in boldcolors:
        colorprint(color, col=color, bold=True)
