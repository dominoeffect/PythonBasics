import urllib.request
import chardet
import re

page = urllib.request.urlopen('http://photo.sina.com.cn/') #打开网页

htmlCode = page.read() #获取源代码

# print(htmlCode)

# print(chardet.detect(htmlCode))


data = htmlCode.decode('utf-8')

reg = r'src="(.+?\.jpg)"'#正则表达式

reg_img = re.compile(reg)#编译一下，运行更快

imglist = reg_img.findall(data)#进行匹配

x=0

for img in imglist:

    print(img)
    urllib.request.urlretrieve(img, '%s.jpg'  % x)
    x += 1