from bs4 import BeautifulSoup

html_doc = """

<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<div class ="hoge">
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
</div>
<a href="http://example.com/ti324" class="sister" id="link3">Tillie324</a>;
<p class="story">...</p>
"""
soup = BeautifulSoup(html_doc, 'html.parser')
# article_body = soup.find_all("a", class_="hoge")
# for a in article_body:
#     print(a.get("href"))
article_body = soup.find(class_="hoge")
link_tag_a = article_body.find_all("a")
for a in link_tag_a:
    print(a.text)
    print(a.get("href"))
