#!/usr/bin/python3

import os
import sys
import datetime
import time

def cur_file_dir():
     path = sys.path[0]
     if os.path.isdir(path):
         return path + '/'
     elif os.path.isfile(path):
         return os.path.dirname(path)

def inc_day(adate):
    mydate = datetime.datetime.strptime(adate, "%Y.%m.%d")
    #print(mydate)
    #mydate.timedelta(days=-1)
    mydate = mydate + datetime.timedelta(days=-1)
    return mydate.strftime("%Y.%m.%d")

def rm_hide(text):
    remain_text = text
    first = text.find("<hide>")
    end = text.find("</hide>")
    if first > 0:
        remain_text = text[0:first]
        if end > 0:
            remain_text = remain_text + text[end+7:]
    return remain_text

def read_new_title(project_file,mydate, days):
    f = open(cur_file_dir() + '../projects/'+project_file, "rU")
    contents = f.read()
    i = 0
    showtitile = 1
    while i < int(days) : 
        first = contents.find('#### '+mydate)
        end = contents.find('#### ', 20+first)
        if( first > 0):
            if showtitile == 1:
                print("<font color= #66cc00>日期" +"</font> | <font color= #66cc00>"+project_file.replace('.md','') +"</font>")
                print("---|---- ")

                #print( , "||")
                showtitile = 0
            content = contents[first+len('#### '+mydate)+1:end]
            content = content.replace("\n\n", "\n")
            content = rm_hide(content)
            content = rm_hide(content)
            print(mydate, "|",content.replace('\n','<br>') )
#            else:
#                print(" |   |", mydate, "|",content.replace('\n','<br>') )
        i = i+1
        mydate = inc_day(mydate)
    if(showtitile == 0) :
        print("\n\n")
    #return f
    #print(contents)


def write2_single_one(p):
    f = open(cur_file_dir() + '../projects/log/projects_all.md', "a+")
    f.write("\n\n# " +p.replace('.md','') +'\n' )
    f.write(open(cur_file_dir() + '../projects/'+p,'r').read())
    f.close()

def cat_projects(mydate, days):
    projects = os.listdir(cur_file_dir() + '../projects/') 
    #print(projects)
    #os.remove(cur_file_dir() + '../projects/log/projects_all.md')
    for p in projects:
        if '.md' in p :
            content = read_new_title(p,mydate, days)
            #print(p)
            #print(content)
            write2_single_one(p)


if __name__ == '__main__':
    if(len(sys.argv)== 1):
        now = datetime.datetime.now()
        cat_projects(now.strftime("%Y.%m.%d"), 10)
    else:
        cat_projects(sys.argv[1], sys.argv[2])