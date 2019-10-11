import re
import urllib.request
import chardet

def getGtmlCode():

    html = urllib.request.urlopen("http://www.quanshuwang.com/book/44/44683").read() #获取网页源代码
    html = html.decode("gbk") #转成该网站格式
    reg = r'<li><a href="(.*?)" title=".*?">(.*?)</a></li>' #根据网站样式匹配的正则：(.*?)可以匹配所有东西，加括号为我们需要的

    reg = re.compile(reg)

    urls = re.findall(reg, html)

    for url in urls:

        #print(url)

        chapter_url = url[0] #章节路径

        chapter_title = url[1] #章节名



        chapter_html = urllib.request.urlopen(chapter_url).read() #获取该章节的全文代码

        # print(chardet.detect(chapter_html))

        chapter_html = chapter_html.decode("gbk")

        chapter_reg = r'</script>&nbsp;&nbsp;&nbsp;&nbsp;.*?<br />(.*?)<script type="text/javascript">' #匹配文章内容

        chapter_reg = re.compile(chapter_reg,re.S)

        chapter_content = re.findall(chapter_reg, chapter_html)

        for content in chapter_content:

            content = content.replace("&nbsp;&nbsp;&nbsp;&nbsp;","") #使用空格代替

            content = content.replace("<br />","") #使用空格代替

            print(content)

            f = open('{}.txt'.format(chapter_title),'w',encoding='utf-8') #保存到本地

            f.write(content)


getGtmlCode()