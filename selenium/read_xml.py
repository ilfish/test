import xml.dom.minidom

# 打开xml文档
dom=xml.dom.minidom.parse('info.xml')

# nodeName 为结点名字。
# nodeValue 是结点的值，只对文本结点有效。
# nodeType 是结点的类型。

root=dom.documentElement


# 获得标签信息
# print(root.nodeName)
# print(root.nodeValue)
# print(root.nodeType)
# print(root.ELEMENT_NODE)


# 获得任意标签名
# tagname=root.getElementsByTagName('maxid')
# print(tagname[0].tagName)
#
# tagname=root.getElementsByTagName('caption')
# print(tagname[2].tagName)
#
# tagname=root.getElementsByTagName('item')
# print(tagname[1].tagName)


# 获得标签属性值   getAttribute()方法可以获得元素的属性所对应的值。
# logins=root.getElementsByTagName('login')
# username=logins[0].getAttribute('username')
# print(username)


# 获得标签对之间的数据  firstChild 属性返回被选节点的第一个子节点，data 表示获取该节点的数据。
captions=dom.getElementsByTagName('caption')
c1=captions[0].firstChild.data
print(c1)
