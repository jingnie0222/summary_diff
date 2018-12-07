#!/usr/bin/python
#coding:gbk
import sys
import re

xml_head = '''
<?xml version="1.0" encoding="utf-16"?>
<DOCUMENT>
'''

xml_tail = '\n</DOCUMENT>'

structured_template = '''
<doc docId="%(DOCID)s">
%(SUMMARY)s
</doc>\n
'''

tuwen_template = '''
<doc docId="%(DOCID)s">
<item>
<display>
<url><![CDATA[%(URL)s]]></url>
<title><![CDATA[%(TITLE)s]]></title>
<imageurl><![CDATA[%(URL)s]]></imageurl>
<imagecontent><![CDATA[%(TUWEN)s]]></imagecontent>
</display>
</item>
</doc>\n
'''

normal_template = '''
<doc docId="%(DOCID)s">
<item>
<display>
<url><![CDATA[%(URL)s]]></url>
<title><![CDATA[%(TITLE)s]]></title>
<content><![CDATA[%(SUMMARY)s]]></content>
</display>
</item>
</doc>\n
'''

#read db failed or request be canceled
noresult_template = '''
<doc docId="%(DOCID)s">
<item>
<display>
<url><![CDATA[www.sogou.com]]></url>
<title><![CDATA[NO Result]]></title>
<content><![CDATA[NO Result, Check Errorlog Please!]]></content>
</display>
</item>
</doc>\n
'''

def read_file_to_list(file):
    pat_dict = {'URL':   r'\[Url\]: (.*)',
                'TITLE': r'\[Title\]: (.*)',
                'SUMMARY': r'\[Summary\]: (.*)',
                'TUWEN':  r'\[tuwen-Summary\]: (.*)',
                'DOCID': r'Send.*Result.*DocID\(([^)]*)'}

    lists = []
    node = {}
    with open(file, 'r') as f:
        for line in f.readlines():
            # line --> node
            #print("-->%s\n" % line)
            for key in pat_dict.keys():
                p = re.search(pat_dict[key], line)
                if p:
                    #print("key:%s, value:%s" % (key, p.group(1))) 
                    node[key] = p.group(1)
                    if key == 'DOCID':
                       lists.append(node)
                       node = {}
                    break

    return lists

def cmp_lists(list1, list2):
    with open('diff.xml', 'w') as f:
        f.write(xml_head)
        for i in range(len(list1)):
            same = True
            for key in ['DOCID', 'URL', 'TITLE', 'SUMMARY', 'TUWEN']:
                if key not in list1[i] and key not in list2[i]:
                    continue
                elif key not in list1[i] or key not in list2[i]:
                    same = False
                    break
                else:
                    if list1[i][key] != list2[i][key]:
                        same = False
                        break

            # Translate and format and write
            if not same:
                f.write(translate_and_format(list1[i]))
                f.write(translate_and_format(list2[i]))

        f.write(xml_tail)

def translate_and_format(node):
    if 'SUMMARY'in node and re.search(r'<item><tplid>[0-9]+', node['SUMMARY']):
        node_xml = structured_template % node
    elif 'TITLE' in node and 'TUWEN' in node and node['TUWEN'] != '':
        node_xml = tuwen_template % node
    elif 'TITLE' in node and 'SUMMARY' in node:
        node_xml = normal_template % node
    else:
        node_xml = noresult_template % node
    return node_xml


if __name__=='__main__':
   node_list1 = read_file_to_list(sys.argv[1])
   node_list2 = read_file_to_list(sys.argv[2])
   cmp_lists(node_list1, node_list2)
