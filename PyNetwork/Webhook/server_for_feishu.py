import json
from flask import Flask, request
from gevent.pywsgi import WSGIServer

import base64
import hashlib
import hmac
from datetime import datetime
import requests

'''
pip install flask
pip install gevent
'''

#-------------------------------------------------------------------------
WEBHOOK_URL = "https://open.feishu.cn/open-apis/bot/v2/hook/209cbae5-a4ce-4fc2-989b-ffdc82ea66fc"
WEBHOOK_SECRET = "zq0YnujLaCwkUq4PKpQS2f"
timestamp = int(datetime.now().timestamp())

def gen_sign(secret):
    # 拼接时间戳以及签名校验
    string_to_sign = '{}\n{}'.format(timestamp, secret)

    # 使用 HMAC-SHA256 进行加密
    hmac_code = hmac.new(
        string_to_sign.encode("utf-8"), digestmod=hashlib.sha256
    ).digest()

    # 对结果进行 base64 编码
    sign = base64.b64encode(hmac_code).decode('utf-8')

    return sign
#-------------------------------------------------------------------------

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    prometheus_data = json.loads(request.data)
    print(prometheus_data)

    sign = gen_sign(WEBHOOK_SECRET)
    params = {
        "timestamp": timestamp,
        "sign": sign,
        "msg_type": "text",
        "content": {"text": "点火发射！Local Python Call : server_for_feishu"},
    }

    resp = requests.post(WEBHOOK_URL, json=params)
    resp.raise_for_status()
    if (resp.status_code != 204
            and 'content-type' in resp.headers
            and 'application/json' in resp.headers['content-type']):
        parsed = resp.json()
        print('✅ parsed response: 👉️', parsed)
    else:
        # 👇️ this runs
        print('⛔️ conditions not met')

    print("消息发送成功")
    return "success"

if __name__ == '__main__':
    WSGIServer(('0.0.0.0', 5000), app).serve_forever()