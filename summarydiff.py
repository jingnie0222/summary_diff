#!/usr/bin/python
#coding:gbk
import sys
import re

def readfile(filename):
    try:
        file = open(filename)
    except Exception, e:
        print e
    content = file.readlines()
    file.close()
    return content


def extract_re(file):
   docid_pat = re.compile(r'.+CWebSummary::.+DocID\((.+)\).+')
   url_pat = re.compile(r'.*\[Url\]: (.+)')
   title_pat = re.compile(r'.*\[Title\]: (.+)')
   summary_pat = re.compile(r'.*\[Summary\]: (.+)')
   tuwen_pat = re.compile(r'.*\[tuwen-Summary\]: (.+)')

   data = readfile(file)
   for line in data:
       if docid_pat.match(line):
          print "DOCID:" +   docid_pat.match(line).group(1)
       elif url_pat.match(line):
          print "URL:" +   url_pat.match(line).group(1)
       elif title_pat.match(line):
          print "TITLE:" +   title_pat.match(line).group(1)
       elif summary_pat.match(line):
          print "SUMMARY:" +   summary_pat.match(line).group(1)
       elif tuwen_pat.match(line):
          print "TUWEN:" +   tuwen_pat.match(line).group(1)
             

if __name__=='__main__':
    extract_re(sys.argv[1]) 
