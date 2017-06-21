#!/usr/bin/env python
# encoding: utf-8
'''
Created on 2016年10月25日

@author: alibaba
'''
import sys
# 
# poem = '''\
# Programming is fun
# When the work is done
# if you wanna make your work also fun:
# use Python! '''
# print('START!')
# f = file('poem.txt', 'w') # open for 'w'riting   'a'追加 'w'写 'r'读 
# f.write(poem) # write text to file
# f.close() # close the file
# f = file('poem.txt')
# while True:
#     line = f.readline()
#     if len(line) == 0: # Zero length indicates EOF
#         break 
#     print line,
# # Notice comma to avoid automatic newline added by Python
# f.close()

try:
    s=raw_input('Enter something--')
except EOFError:
    print '\nWhy did you do an EOF on me?'
    sys.exit()
except:
    print '\nSome error/exception occurred.'
print 'Done'