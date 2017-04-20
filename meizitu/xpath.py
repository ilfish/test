from lxml import etree
# def getxpath(html):
#     return etree.HTML(html)
# # 下面是我们实战的第一个html
# sample1 ="http://www.mzitu.com/all"
# # 获取xml结构
# s1 = getxpath(sample1)
#
# # 获取标题(两种方法都可以)
# #有同学在评论区指出我这边相对路径和绝对路径有问题，我搜索了下
# #发现定义如下图
# s1.xpath('//title/text()')
# s1.xpath('/html/head/title/text()')


text = '''
<div>
    <ul>
         <li class="item-0"><a href="link1.html">first item</a></li>
         <li class="item-1"><a href="link2.html">second item</a></li>
         <li class="item-inactive"><a href="link3.html"><span class="bold">third item</span></a></li>
         <li class="item-1"><a href="link4.html">fourth item</a></li>
         <li class="item-0"><a href="link5.html">fifth item</a>
     </ul>
 </div>
'''
html=etree.HTML(text)
result1=html.xpath('//li/@class')#获取li标签下的所有class
result2=html.xpath('//li/a[@href="link1.html"]')#获取li标签下href=link1.html的<a>标签
result3=html.xpath('//li//span')#获取li标签下的所有span标签
result4=html.xpath('//li/a//@class')#获取li标签下的所有class，但不包括li
result5=html.xpath('//li[last()]/a/@href') #获取最后一个li的a的href

result6=html.xpath('//li[last()-1]/a')
result61=result6[0].text #获取倒数第二个元素的内容

result7=html.xpath('//*[@class="bold"]')  # 获取class为bold的标签名
result71=result7[0].tag

print(result71)

