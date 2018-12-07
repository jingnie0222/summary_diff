#!/usr/bin/python
#coding:gbk
import sys
import re
from optparse import OptionParser
from ConfigParser import RawConfigParser
import Crypto, paramiko

class SummaryDiff(object):
    def __init__(self):
        self.file1 = None
        self.file2 = None
        self.output_file = None

        self.list1 = []
        self.list2 = []
        self.diff = ""

        self.pat_dict = {}
        self.xml_head = ''
        self.xml_tail = ''
        self.structured_template = ''
        self.tuwen_template = ''
        self.normal_template = ''
        self.noresult_template = ''

    def read_cfg(self, cfg):
        self.conf = RawConfigParser()
        self.conf.read(cfg)

        self.file1 = self.conf.get('param_conf', 'onlinefile')
        self.file2 = self.conf.get('param_conf', 'testfile')
        self.output_file = self.conf.get('param_conf', 'diffoutput')

        self.xml_head = self.conf.get('result_template', 'xml_head')
        self.xml_tail = self.conf.get('result_template', 'xml_tail')

        self.pat_dict = {}
        for key,value in self.conf.items('regex_pat'):
            self.pat_dict[key] = value

        self.structured_template = self.conf.get('result_template', 'structured_template')
        self.tuwen_template = self.conf.get('result_template', 'tuwen_template')
        self.normal_template = self.conf.get('result_template', 'normal_template')
        self.noresult_template = self.conf.get('result_template', 'noresult_template')

    def parse(self):
        self.list1 = self.__read_file_to_list(self.file1) 
        self.list2 = self.__read_file_to_list(self.file2)

    def __read_file_to_list(self, file):
        lists = []
        node = {}
        with open(file, 'r') as f:
            for line in f.readlines():
                # line --> node
                for key in self.pat_dict.keys():
                    p = re.search(self.pat_dict[key], line)
                    if p:
                        #print("key:%s, value:%s" % (key, p.group(1))) 
                        if key == 'docid':
                           if node != {}:
                               lists.append(node)
                               node = {}
                           node[key] = p.group(1) + "===query:" + p.group(2)   # group(1) is docid, group(2) is query
                        else:
                           node[key] = p.group(1)
                        #print("key:%s, value:%s" %(key, node[key]))
                        break
            #append the last node
            lists.append(node)   
    
        return lists
    
    def compare(self):
        self.diff = ""
        for i in range(len(self.list1)):
            same = True
            for key in ['docid', 'url', 'title', 'summary', 'tuwen']:
                if key not in self.list1[i] and key not in self.list2[i]:
                    continue
                elif key not in self.list1[i] or key not in self.list2[i]:
                    same = False
                    break
                else:
                    if self.list1[i][key] != self.list2[i][key]:
                        same = False
                        break
    
            # Translate and format and write
            if not same:
                self.diff += "%s\n\n" % self.__translate_and_format(self.list1[i])
                self.diff += "%s\n\n" % self.__translate_and_format(self.list2[i])

    def save_diff(self):
        with open(self.output_file, 'w') as f:
            f.write("%s\n\n" % self.xml_head)
            f.write(self.diff)
            f.write("%s\n" % self.xml_tail)
 
    def __translate_and_format(self, node):
        if 'summary'in node and re.search(r'<item><tplid>[0-9]+', node['summary']):
            node_xml = self.structured_template % node
        elif 'title' in node and 'tuwen' in node and node['tuwen'] != '':
            node_xml = self.tuwen_template % node
        elif 'title' in node and 'summary' in node:
            node_xml = self.normal_template % node
        else:
            node_xml = self.noresult_template % node
        return node_xml


class ScpFile(object):
    def __init__(self):
        self.hostip = ''
        self.hostname = ''
        self.hostpasswd = ''
        self.localpath = ''
        self.remotepath= ''

    def read_cfg(self, cfg):
        self.conf = RawConfigParser()
        self.conf.read(cfg)

        self.hostip = self.conf.get('scp_conf', 'host_ip')
        self.hostname = self.conf.get('scp_conf', 'host_username')
        self.hostpasswd = self.conf.get('scp_conf', 'host_passwd')
        self.localpath = self.conf.get('scp_conf', 'local_path')
        self.remotepath = self.conf.get('scp_conf', 'remote_path')

    def scp_file(self):
        scp = paramiko.Transport((self.hostip, 22))
        scp.connect(username=self.hostname, password=self.hostpasswd)
        sftp = paramiko.SFTPClient.from_transport(scp)
        sftp.put(self.localpath, self.remotepath)
        scp.close()           


def parse_option_args():
    MSG_USAGE = '[-f<configfile>]'
    optParser = OptionParser(MSG_USAGE)
    optParser.add_option("-f", "--conffile", action="store", type="string", dest="conffile", help="config file")
    options, args = optParser.parse_args()
    #print("%s" % options)
    return options
    
def main():
    try:
        param_input = parse_option_args()
        if param_input.conffile == None:
            print("please enter config file!\n")
            sys.exit()

        sumdiff = SummaryDiff()

        sumdiff.read_cfg(param_input.conffile)
        sumdiff.parse()
        sumdiff.compare()
        sumdiff.save_diff()

        trans = ScpFile()
        trans.read_cfg(param_input.conffile)
        trans.scp_file()

 
    except Exception, e:
        print e
    
if __name__=='__main__':
    main()
    print("DONE-----")
