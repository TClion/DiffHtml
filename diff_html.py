import hashlib
import requests


def get_html(firsturl=None, secondurl=None):
    try:
        firsthtml = requests.get(firsturl).content
        secondhtml = requests.get(secondurl).content
        return (firsthtml, secondhtml)
    except Exception as e:
        print(e)
        return "request error"




def diff_two_html(htmls):
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


if __name__ == '__main__':
    firsturl = 'http://www.baidu.com'
    secondurl = 'http://www.baidu.com'
    htmls = get_html(firsturl, secondurl)
    diffresult = diff_two_html(htmls)
    print(diffresult)