import logging.config
import httpx
import rich

LOGGING_CONFIG = {
    "version": 1,
    "handlers": {
        "default": {
            "class": "logging.StreamHandler",
            "formatter": "http",
            "stream": "ext://sys.stderr",
        }
    },
    "formatters": {
        "http": {
            "format": "%(levelname)s [%(asctime)s] %(name)s - %(message)s",
            "datefmt": "%Y-%m-%d %H:%M:%S",
        }
    },
    "loggers": {
        "httpx": {
            "handlers": ["default"],
            "level": "DEBUG",
        },
        "httpcore": {
            "handlers": ["default"],
            "level": "DEBUG",
        },
    },
}


cookies_str = "buvid3=F1447596-3323-8C4A-A16D-1032D41DFCCF71001infoc; b_nut=1742052471; _uuid=4DBBA2B9-F3BA-CF33-2413-A106FF4912310B66826infoc; enable_web_push=DISABLE; enable_feed_channel=ENABLE; buvid4=952F0148-FD78-426D-5B9B-345031A54F7D73013-025031515-SqNvQQtMCzR2tsz8mJjY4A%3D%3D; header_theme_version=CLOSE; DedeUserID=1187415869; DedeUserID__ckMd5=b2d7c477f06c7648; rpdid=|(JR|uY|u|mm0J'u~RJku)uYk; fingerprint=a882f86e15c754fa49b414377b5f738d; buvid_fp_plain=undefined; buvid_fp=a882f86e15c754fa49b414377b5f738d; bp_t_offset_1187415869=1055332644981571584; CURRENT_QUALITY=80; home_feed_column=4; b_lsid=CAEB3889_196568D8E92; browser_resolution=1053-826; bili_ticket=eyJhbGciOiJIUzI1NiIsImtpZCI6InMwMyIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3NDU0NjgwODYsImlhdCI6MTc0NTIwODgyNiwicGx0IjotMX0.GKgSqk0csN_BBEv3WC1ddP-NSC-_J2AOA6Iie96gjPc; bili_ticket_expires=1745468026; SESSDATA=72932b28%2C1760760887%2Cbf1a6%2A42CjDuO40AKzfFU3hQzt8wFO3Ez0_oXW8UgqSZVMuzLX06Q8pT7__-ApZBvDW2AVwznAUSVkpiN21aZHI2V3pnZjhzcDJkNG1abndoTFh1dnA3dVN6R2ZnWVVOZHY2eW9TalQyYW1vVVVfZHc1TzM5MVRpTWhOSWViZkEzLWNpU1h6NU9Dc256a0l3IIEC; bili_jct=481e8bc8ac5b7fbe65af58aa6ae01897; sid=73fpzh7u; CURRENT_FNVAL=4048"


cookies_dict = {}
for item in cookies_str.split("; "):
    if "=" in item:
        key, value = item.split("=", 1)
        cookies_dict[key] = value

# rich.print(cookies_dict)

# 添加常用浏览器请求头
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36",
    "Referer": "https://www.bilibili.com/",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
    "Accept-Encoding": "gzip, deflate, br",
}

logging.config.dictConfig(LOGGING_CONFIG)
response = httpx.get(
    "https://www.bilibili.com/video/BV1Stwfe1E7s",
    cookies=cookies_dict,
    headers=headers,
    follow_redirects=True,
)
rich.print(response)

# 如果成功获取内容，可以打印更详细信息
if response.status_code == 200:
    rich.print("请求成功！")
    print(f"响应内容: {response.text}")

else:
    rich.print(f"请求失败，状态码: {response.status_code}")
    rich.print(f"错误信息: {response.text[:200]}")
