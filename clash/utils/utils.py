import requests
import random
import string
import yaml
import os
from urllib.parse import quote


def fetch_url(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.text
    except Exception as e:
        return ""


def get_random_name(prefix):
    data_set = string.ascii_letters + string.digits
    random_value = "".join(random.choices(data_set, k=5))
    return f"{prefix}-{random_value}"


def generate_clash_config(nodes):
    """生成Clash配置文件"""
    with open("template.yaml", "r", encoding="utf-8") as f:
        yaml_config = yaml.safe_load(f)
    for config in nodes:
        yaml_config["proxies"].append(config)
        yaml_config["proxy-groups"][0]["proxies"].append(config["name"])
    return yaml.dump(yaml_config, allow_unicode=True, sort_keys=False)


# 钉钉 markdown 只渲染可访问的图片地址，data URI / base64 会原样显示成文本。
SUBSCRIBE_URL = (
    "https://raw.githubusercontent.com/YangLang116/auto_gen/master/clash/gen_clash_config.yaml"
)


def send_markdown_toDing(nodes):
    # 二维码由国内服务按订阅地址现生成，避免钉钉拉取 GitHub 外链失败。
    qr_url = "https://api.pwmqr.com/qrcode/create/?url=" + quote(SUBSCRIBE_URL, safe="")
    response = requests.request(
        "POST",
        "https://oapi.dingtalk.com/robot/send",
        json={
            "msgtype": "markdown",
            "markdown": {
                "title": "VPN",
                "text": (
                    f"- 更新节点数: {len(nodes)}\n"
                    f"- 订阅地址: {SUBSCRIBE_URL}\n"
                    f"![QR]({qr_url})"
                ),
            },
        },
        params={"access_token": os.environ["CLASH_DING_TOKEN"]},
    )
    print(f"send result: {response.text}")
