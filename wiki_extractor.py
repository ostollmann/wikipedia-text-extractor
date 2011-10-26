from BeautifulSoup import BeautifulSoup
import re
import urllib2

def get_content_paras_from_wiki_html(html):
    content_div_class = "mw-content-ltr"

    soup = BeautifulSoup(html)
    paras = soup.find("div", {"class": content_div_class}).findAll("p")
    paras = map(lambda x: str(x), paras)
    return paras

def get_data(file_name):
    f = open(file_name)
    data = f.read()
    f.close()
    return data

def strip_tags(html):
    r = re.compile(r'<.*?>')
    return r.sub('', html)

def strip_other(text):
    r = re.compile(r'\[.*?\]')
    return r.sub('', text)

def wiki_html_to_text(html):
    paras = get_content_paras_from_wiki_html(html)
    paras = map(strip_tags, paras)
    paras = map(strip_other, paras)
    text = ' '.join(paras)
    return text

def get_content_from_wiki_file(file_name):
    html = get_data(file_name)
    return wiki_html_to_text(html)

def get_content_from_wiki_url(url):
    opener = urllib2.build_opener()
    opener.addheaders = [('User-agent', 'Mozilla/5.0')]
    f = opener.open(url)
    html = f.read()
    return wiki_html_to_text(html)

if __name__ == "__main__":
    import sys
    url = sys.argv[1]
    url = url + "?printable=yes"
    print "Getting Wikipedia article content from: %s" % url
    file_name = sys.argv[2]
    print "Saving to file: %s" % file_name

    content = get_content_from_wiki_url(url)
    with open(file_name, 'w') as f:
        f.write(content)
    



