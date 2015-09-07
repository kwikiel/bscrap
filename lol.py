#!/usr/bin/env python
import requests
from lxml import html
page = requests.get("http://bitlendingclub.com/user/index/id/4630")
print(page.status_code)
tree = html.fromstring(page.text)
# tree.xpath('//span[@class="profile-summary-label"]//following-sibling::text()')
