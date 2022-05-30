import re

headers = """
from: en
to: zh
query: enter
transtype: translang
simple_means_flag: 3
sign: 571025.808352
token: 143cb03f796000fa7ff3b1ea18b8e7ee
domain: common

"""
for line in headers.splitlines():
    # print(re.sub('^(.*?): (.*)$', '\'\\1\': \'\\2\',', line))
    print(re.sub('^(.*?): (.*)$', r'"\1": "\2",', line))

