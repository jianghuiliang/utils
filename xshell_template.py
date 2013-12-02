#!/usr/bin/env python
#-*- coding: utf-8 -*-
import os
import sys

if __name__=='__main__':
    fh=open(r'D:\template.txt')
    tmp = fh.readlines()

    for root, dirs, files in os.walk(r'D:\Work\NetSarang\Xshell\Sessions_test' ):
    #for root, dirs, files in os.walk('/Work/NetSarang/Xshell/Sessions_test/' ):
        for f in files:
            if os.path.splitext(f)[1] == '.xsh':
                fname=os.path.join(root, f)
                print fname
                fh_2 = open(fname)
                tmp2=fh_2.readlines()
                fh_2.close()
                
                
                for line2 in tmp2:
                    if line2[0:5] == 'Host=':
                        host=line2                    
                        print host
                        
                    if line2[0:5] == 'Port=':
                        port=line2
                        print port
                        
                    if line2[0:9] =='Password=':
                        pswd=line2
                        print pswd

                    if line2[0:9] == 'UserName=':
                        name=line2
                        print name
                        
                fh2=open(fname, 'w')
                for line1 in tmp:
                    if line1[0:9] == 'UserName=':
                        fh2.write(name)
                    elif line1[0:9] =='Password=':
                        fh2.write(pswd)
                    elif line1[0:5] == 'Host=':
                        fh2.write(host)
                    elif line1[0:5] == 'Port=':
                        fh2.write(port)
                    else:    
                        fh2.write(line1)
                fh2.close()
                
    
    fh.close()
