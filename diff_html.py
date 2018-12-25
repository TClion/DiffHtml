import hashlib
import requests

from lxml import etree


def get_html(firsturl=None, secondurl=None):
    try:
        firsthtml = requests.get(firsturl).content
        secondhtml = requests.get(secondurl).content
        return (firsthtml, secondhtml)
    except Exception as e:
        print(e)
        return "request error"


def md5_compare(htmls):
    firsthtml, secondhtml = htmls
    firstmd5 = hashlib.md5()
    firstmd5.update(firsthtml)
    firstmd5 = firstmd5.hexdigest()
    secondmd5 = hashlib.md5()
    secondmd5.update(secondhtml)
    secondmd5 = secondmd5.hexdigest()
    if firstmd5 == secondmd5:
        return "Two Html Same"
    else:
        return "Two Html Unsame"


def domtree_compare(htmls):
    firsthtml, secondhtml = htmls
    firstpage = etree.HTML(firsthtml)
    secondpage = etree.HTML(secondhtml)
    first_dom = firstpage.xpath('//.')
    second_dom = secondpage.xpath('//.')
    print(first_dom)
    print(second_dom)
    return first_dom == second_dom



if __name__ == '__main__':
    firsturl = 'http://www.baidu.com'
    secondurl = 'http://www.baidu.com'
    htmls = get_html(firsturl, secondurl)
    # result = md5_compare(htmls)
    result = domtree_compare(htmls)
    print(result)