#!/usr/bin/env python3
import sys,rp
rule=['init n=0',
      'init m=999',
      'sqs  ::=  range? parms  fileid ',
      'range::=  n "-" m ',
      'n    ::=  r"[0-9]"* ',
      'm    ::=  r"[0-9]"* ',      
      'parms::=  sep car* sep ',
      'sep  ::=  r"\S" ',
      'car  ::=  r"." ^sep ',
      'fileid::= r"\S"* ']
parms=' '.join(sys.argv[1:])

cmp=rp.match(rule,parms)
if cmp==None:
    print ("Error in parsing:")
else:
    id=None
    try:
        id=open(cmp.fileid)
        for l in id.readlines():
            if l.find(cmp.car,int(cmp.n),int(cmp.m))>-1: 
                print l[:-1]
    except Exception,e:
        print e
    else:
        if id!=None: id.close()