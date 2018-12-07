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


def extract_re():
   summary_pat = re.compile(r'.*\[Summary\]: (.+)')
   url_pat = r'.*\[Url\]: (.+)'
   title_pat = r'.*\[Title\]: (.+)'
   tuwen_pat = r'.*\[tuwen-Summary\]: (.+)'
   docid_pat = r'.+CWebSummary::.+DocID\((.+)\).+'

   #test

   docid = re.match(docid_pat, '[web_summary:LM_TRACE] [20160603 16:46:00] [1b91a700] CWebSummary::GenerateSummaryContent(164f490500000031) DocID(60c237f4b4fb3bac-0ff0cc9c655aa30e-0b285f3d23f748daf73b662e4ffd82a3) Query(��ĩ����)')
   print "docid:" + docid.group(1)

   summary = summary_pat.match( '        [Summary]: <item><tplid>51</tplid><display><title><![CDATA[?�������ܺȲ���?������ͥҽ������]]></title><shortTitle><![CDATA[?�������ܺȲ���?������ͥҽ������]]></shortTitle><url><![CDATA[http://ask.familydoctor.com.cn/q/5586260.html]]></url><doctor><![CDATA[���ڿ�ҽʦ]]></doctor><content><![CDATA[?������?�벻Ҫ?�Ȳ�?����Ҷ�����������������ʳ���е������ϣ�Ӱ�쳦�����������գ��Ӷ�����ƶѪ����ˮ��Ũ��Խ�����Ậ��Խ�ߣ�����������Ӱ��Ҳ������]]></content><content640><![CDATA[�������벻Ҫ�Ȳ衣��Ҷ�����������������ʳ���е������ϣ�Ӱ�쳦�����������գ��Ӷ�����ƶѪ����ˮ��Ũ��Խ�����Ậ��Խ�ߣ�����������Ӱ��Ҳ��Խ���ء������ڱ�����Ҫ�������壬�����ںȲ赼��ƶѪ���챳�����ۡ�ͬʱ��Ҷ�еĿ������ͨ����֭����Ӥ�����ڣ�����ʹӤ�����������κͺ�Ȼ�޹�������󡣲����ںȲ����Ӱ��ĸ��ι������Ϊ����ڼ�Ҫ�Ǻ��´����Ĳ裬���и�Ũ�ȵ�����ᱻճĤ�����գ�����Ӱ�����ٵ�ѪҺѭ������������֭�ķ��ڣ������ˮ���ڲ��㡣����������²�֮�󣬲��еĿ��ȼ��������֭�����Ӱ��Ӥ������Ӥ������Ľ���������]]></content640><contenttype><![CDATA[ҽʦ�ش�]]></contenttype><youzhiContent><![CDATA[?������?�벻Ҫ?�Ȳ�?����Ҷ�����������������ʳ���е������ϣ�Ӱ�쳦�����������գ��Ӷ�����ƶѪ����ˮ��Ũ��Խ�����Ậ��Խ�ߣ�����������Ӱ��Ҳ��Խ���ء�?������?������Ҫ�������壬?������??�Ȳ�?����ƶ������]]></youzhiContent><isContentBestAnswer><![CDATA[1]]></isContentBestAnswer><answercontent complete="0"><![CDATA[?������?�벻Ҫ?�Ȳ�?����Ҷ�����������������ʳ���е������ϣ�Ӱ�쳦�����������գ��Ӷ�����ƶѪ����ˮ��Ũ��Խ�����Ậ��������]]></answercontent><qtitle><![CDATA[?�������ܺȲ���?��]]></qtitle><content1><![CDATA[?�������ܺȲ���?��]]></content1><count><![CDATA[1]]></count><best><![CDATA[?������?�벻Ҫ?�Ȳ�?����Ҷ�����������������ʳ���е������ϣ�Ӱ�쳦�����������գ��Ӷ�����ƶѪ����ˮ��Ũ��Խ�����Ậ��Խ�ߣ�����������Ӱ��Ҳ��Խ���ء�?������?������Ҫ�������壬?������??�Ȳ�?����ƶѪ���챳�����ۡ�ͬʱ��Ҷ�еĿ������ͨ����֭����Ӥ�����ڣ�����ʹӤ�����������κͺ�Ȼ�޹��������?������??�Ȳ�?����Ӱ��ĸ��ι������Ϊ����ڼ�Ҫ�Ǻ��´����Ĳ裬���и�Ũ�ȵ�����ᱻճĤ�����գ�����Ӱ�����ٵ�ѪҺѭ������������֭�ķ��ڣ������ˮ���ڲ��㡣����������²�֮�󣬲��еĿ��ȼ��������֭�����Ӱ��Ӥ������Ӥ������Ľ���������]]></best><questiontime><![CDATA[2014-01-04]]></questiontime><showurl><![CDATA[http://ask.familydoctor.com...]]></showurl><date><![CDATA[2014-01-04]]></date><pagesize><![CDATA[54k]]></pagesize></display></item>')
   print "S:" + summary.group(1)

   url = re.match(url_pat, '        [Url]: http://baike.sogou.com/v7743639.htm?fromTitle=ssd%E7%A1%AC%E7%9B%98')
   print "U:" + url.group(1)

   title = re.match(title_pat, '        [Title]: ����Ь��Ů��ƽ�ף��������¿�Ů��?��Ь?ƽ��ѧ������Ь��?ǧ�ٶ�Ů?������Ь�У�����')
   print "T:" + title.group(1)

   tuwen1 = re.match(tuwen_pat, '        [tuwen-Summary]: ?����?�ĸ��˿ռ䡣��������������ҵ�?����?������Ͷ�塢�ղغͶ��ġ������ע��ʱ��ȡ?����?�����¶�̬���������������ɱ������ۣݡ�����������������ע���ѹ�ע��˽�š��༭��顡��������ע��������������䡡����������')

   print "TUWEN:" + tuwen1.group(1)

   tuwen2 = re.match(tuwen_pat, '        [tuwen-Summary]: ?����?�ĸ��˿ռ�()()((1))')
   print "TUWEN:" + tuwen2.group(1)
   #data = readfile(file)
   #for i in data:
       #a        


if __name__=='__main__':
    extract_re() 
