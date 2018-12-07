#!/usr/bin/python
#coding:gbk
import sys
import re

structured_template = '''
<doc docId="%(docId)s">
%(summary)s
</doc>'''

tuwen_template = '''
<doc docId="%(docId)s">
<item>
<display>
<url><![CDATA[%(url)s]]></url>
<title><![CDATA[%(title)s]]></title>
<imageurl><![CDATA[%(url)s]]></imageurl>
<imagecontent><![CDATA[%(tuwen_summary)s]]></imagecontent>
</display>
</item>
</doc>'''

normal_template = '''
<doc docId="%(docId)s">
<item>
<display>
<url><![CDATA[%(url)s]]></url>
<title><![CDATA[%(title)s]]></title>
<content><![CDATA[%(summary)s]]></content>
</display>
</item>
</doc>'''

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
                    # 
                    if key == 'DOCID':
                        if node != {}:
                            lists.append(node)
                            node = {}

                    node[key] = p.group(1)
                    break
        lists.append(node)    #append the last node to list

    return lists

def cmp_lists(list1, list2):
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
            with open('diff.xml', 'w') as f:
                f.write(translate_and_format(list1[i]))
                f.write(translate_and_format(list2[i]))


def translate_and_format(node):
    key_map = {'docId':'DOCID',
               'summary':'SUMMARY',
               'url':'URL',
               'title':'TITLE',
               'tuwen_summary':'SUMMARY',
               'imageurl':'URL'}

    structured_data = {}
    for key in ['docId', 'summary']:
        structured_data[key] = node.get(key_map[key])
 
    tuwen_data = {}
    for key in ['docId', 'url', 'title', 'imageurl', 'tuwen_summary']:
        tuwen_data[key] = node.get(key_map[key])

    normal_data = {}
    for key in ['docId', 'url', 'title', 'summary']:
        normal_data[key] = node.get(key_map[key])
  
    if re.search(r'<item><tplid>.+<//tplid>', node['SUMMARY']):
        node_xml = structured_template % structured_data
    elif node.get('TUWEN') != '':
        node_xml = tuwen_template % tuwen_data
    else:
        node_xml = normal_template % normal_data
    return node_xml



if __name__=='__main__':

   node_list1 = read_file_to_list(sys.argv[1])
   node_list2 = read_file_to_list(sys.argv[2])
   cmp_lists(node_list1, node_list2)

   #for i in node_list1:
      #print i


  
   




