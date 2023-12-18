'''
 *使用命令 mitmdump -p 端口号 -s ./zb.py 来启动
'''

import mitmproxy.http
from urllib.parse import urlparse

class fqxs:
    def request(self, flow: mitmproxy.http.HTTPFlow):
        parsed_url = urlparse(flow.request.url)
        if parsed_url.query.startswith("iid=") and "x-ladon" in flow.request.headers.keys() and "x-argus" in flow.request.headers.keys():
            ur = flow.request.url.split("?")[1]
            xl = flow.request.headers["x-ladon"]
            xa = flow.request.headers["x-argus"]
            ttcs = ur + "#" + xl + "#" + xa
            file_path = './fqxscsb.txt'
            with open(file_path, 'ab+') as f:
                f.seek(0)
                content = f.read().decode('utf-8')
                if ttcs in content:
                    return
                f.write((ttcs + "\n").encode('utf-8'))
addons = [
    fqxs()
]
