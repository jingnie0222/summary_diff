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


def extract_re(infile, outfile):
   docid_pat = re.compile(r'.+CWebSummary::.+DocID\((.+)\).+')
   url_pat = re.compile(r'.*\[Url\]: (.+)')
   title_pat = re.compile(r'.*\[Title\]: (.+)')
   summary_pat = re.compile(r'.*\[Summary\]: (.+)')
   tuwen_pat = re.compile(r'.*\[tuwen-Summary\]: (.+)')

   f = open(outfile, 'w')
   data = readfile(infile)
   for line in data:
       if docid_pat.match(line):
          f.write('\n===\n')
          f.write('DOCID:' + docid_pat.match(line).group(1))
       elif url_pat.match(line):
          f.write('URL:' + url_pat.match(line).group(1))
       elif title_pat.match(line):
          f.write('TITLE:' + title_pat.match(line).group(1))
       elif summary_pat.match(line):
          f.write('SUMMARY:' + summary_pat.match(line).group(1))
       elif tuwen_pat.match(line):
          f.write('TUWEN:' + tuwen_pat.match(line).group(1))
       else:
          pass
   f.close()

def getdiff(testfile, onlinefile):
   test_res =  readfile(testfile)
   online_res = readfile(onlinefile)
   return test_res

def read_file_to_list(file):
    pat_dict = {'DOCID': r' CWebSummary::.+DocID\(([^)]*)',
                'URL':   r'\[Url\]: (.*)',
                'TITLE': r'\[Title\]: (.*)',
                'SUMMARY': r'\[Summary\]: (.*)',
                'TUWEN':  r'\[tuwen-Summary\]: (.*)'}

    lists = []
    node = {}
    with open(file, 'r') as f:
        for line in f.readlines():
            # line --> node
            #print("-->%s\n" % line)
            for key in pat_dict.keys():
                p = re.search(pat_dict[key], line)
                if p:
                    print("%s:%s" % (key, p.group(1)))
                    # 
                    if key == 'DOCID':
                        if node is not {}:
                            lists.append(node)
                            node = {}

                    node[key] = p.group(1)
                    break

    print(lists)
    return lists

def cmp_lists(list1, list2):
    for i in len(list1):
        same = True
        for key in ['DOCID', 'URL', 'TITLE', 'SUMMARY', 'TUWEN']:
            if list1[i][key] != list2[i][key]:
                same = False
                break

        # 
        if not same:
            # Translate and format
            translate_and_format(list1[i])
            translate_and_format(list2[i])


    return

def translate_and_format(node):
    pass
    return

if __name__=='__main__':
   #test 
   #extract_re(sys.argv[1], sys.argv[2])
   #online
   #extract_re(sys.argv[1], sys.argv[3])
   #res = getdiff(sys.argv[1], sys.argv[2])
   #res = readfile(sys.argv[1])
   #print res[4]
   read_file_to_list(sys.argv[1])




