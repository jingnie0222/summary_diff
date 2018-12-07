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

   docid = re.match(docid_pat, '[web_summary:LM_TRACE] [20160603 16:46:00] [1b91a700] CWebSummary::GenerateSummaryContent(164f490500000031) DocID(60c237f4b4fb3bac-0ff0cc9c655aa30e-0b285f3d23f748daf73b662e4ffd82a3) Query(清末枭雄)')
   print "docid:" + docid.group(1)

   summary = summary_pat.match( '        [Summary]: <item><tplid>51</tplid><display><title><![CDATA[?哺乳期能喝茶吗?？　家庭医生在线]]></title><shortTitle><![CDATA[?哺乳期能喝茶吗?？　家庭医生在线]]></shortTitle><url><![CDATA[http://ask.familydoctor.com.cn/q/5586260.html]]></url><doctor><![CDATA[普内科医师]]></doctor><content><![CDATA[?哺乳期?请不要?喝茶?。茶叶中所含的鞣酸可以与食物中的铁相结合，影响肠道对铁的吸收，从而引起贫血。茶水的浓度越大，鞣酸含量越高，对铁的吸收影响也．．．]]></content><content640><![CDATA[哺乳期请不要喝茶。茶叶中所含的鞣酸可以与食物中的铁相结合，影响肠道对铁的吸收，从而引起贫血。茶水的浓度越大，鞣酸含量越高，对铁的吸收影响也就越严重。哺乳期本就需要补益身体，哺乳期喝茶导致贫血无异背道而驰。同时茶叶中的咖啡因可通过乳汁进入婴儿体内，容易使婴儿发生肠痉挛和忽然无故啼哭现象。哺乳期喝茶更会影响母乳喂养。因为这段期间要是喝下大量的茶，茶中高浓度的鞣酸会被粘膜给吸收，进而影响乳腺的血液循环，会抑制乳汁的分泌，造成奶水分泌不足。还有妈妈喝下茶之后，茶中的咖啡碱会渗入乳汁并间接影响婴儿，对婴儿身体的健康不利。]]></content640><contenttype><![CDATA[医师回答]]></contenttype><youzhiContent><![CDATA[?哺乳期?请不要?喝茶?。茶叶中所含的鞣酸可以与食物中的铁相结合，影响肠道对铁的吸收，从而引起贫血。茶水的浓度越大，鞣酸含量越高，对铁的吸收影响也就越严重。?哺乳期?本就需要补益身体，?哺乳期??喝茶?导致贫．．．]]></youzhiContent><isContentBestAnswer><![CDATA[1]]></isContentBestAnswer><answercontent complete="0"><![CDATA[?哺乳期?请不要?喝茶?。茶叶中所含的鞣酸可以与食物中的铁相结合，影响肠道对铁的吸收，从而引起贫血。茶水的浓度越大，鞣酸含量．．．]]></answercontent><qtitle><![CDATA[?哺乳期能喝茶吗?？]]></qtitle><content1><![CDATA[?哺乳期能喝茶吗?？]]></content1><count><![CDATA[1]]></count><best><![CDATA[?哺乳期?请不要?喝茶?。茶叶中所含的鞣酸可以与食物中的铁相结合，影响肠道对铁的吸收，从而引起贫血。茶水的浓度越大，鞣酸含量越高，对铁的吸收影响也就越严重。?哺乳期?本就需要补益身体，?哺乳期??喝茶?导致贫血无异背道而驰。同时茶叶中的咖啡因可通过乳汁进入婴儿体内，容易使婴儿发生肠痉挛和忽然无故啼哭现象。?哺乳期??喝茶?更会影响母乳喂养。因为这段期间要是喝下大量的茶，茶中高浓度的鞣酸会被粘膜给吸收，进而影响乳腺的血液循环，会抑制乳汁的分泌，造成奶水分泌不足。还有妈妈喝下茶之后，茶中的咖啡碱会渗入乳汁并间接影响婴儿，对婴儿身体的健康不利。]]></best><questiontime><![CDATA[2014-01-04]]></questiontime><showurl><![CDATA[http://ask.familydoctor.com...]]></showurl><date><![CDATA[2014-01-04]]></date><pagesize><![CDATA[54k]]></pagesize></display></item>')
   print "S:" + summary.group(1)

   url = re.match(url_pat, '        [Url]: http://baike.sogou.com/v7743639.htm?fromTitle=ssd%E7%A1%AC%E7%9B%98')
   print "U:" + url.group(1)

   title = re.match(title_pat, '        [Title]: 鱼嘴鞋　女　平底－２１５新款女夏?凉鞋?平底学生鱼嘴鞋　?千百度女?款鱼嘴鞋有．．．')
   print "T:" + title.group(1)

   tuwen1 = re.match(tuwen_pat, '        [tuwen-Summary]: ?匿名?的个人空间。　你可以在这里找到?匿名?的最新投稿、收藏和订阅。点击关注随时获取?匿名?的最新动态！　哔哩哔哩　干杯儿　［］～（￣￣）～＊　关注　已关注　私信　编辑简介　＞＞　关注　｛｛　ｆｒｉｅｎｄ　｝｝．．．')

   print "TUWEN:" + tuwen1.group(1)

   tuwen2 = re.match(tuwen_pat, '        [tuwen-Summary]: ?匿名?的个人空间()()((1))')
   print "TUWEN:" + tuwen2.group(1)
   #data = readfile(file)
   #for i in data:
       #a        


if __name__=='__main__':
    extract_re() 
