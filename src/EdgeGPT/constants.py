import random
import uuid

DELIMITER = "\x1e"


# Generate random IP between range 13.104.0.0/14
FORWARDED_IP = f"1.0.0.{random.randint(0, 255)}"

HEADERS = {
    "accept": "application/json",
    "accept-language": "en-US,en;q=0.9",
    "content-type": "application/json",
    "sec-ch-ua": '"Not_A Brand";v="99", Microsoft Edge";v="110", "Chromium";v="110"',
    "sec-ch-ua-arch": '"x86"',
    "sec-ch-ua-bitness": '"64"',
    "sec-ch-ua-full-version": '"109.0.1518.78"',
    "sec-ch-ua-full-version-list": '"Chromium";v="110.0.5481.192", "Not A(Brand";v="24.0.0.0", "Microsoft Edge";v="110.0.1587.69"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-model": "",
    "sec-ch-ua-platform": '"Windows"',
    "sec-ch-ua-platform-version": '"15.0.0"',
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "x-ms-client-request-id": str(uuid.uuid4()),
    "x-ms-useragent": "azsdk-js-api-client-factory/1.0.0-beta.1 core-rest-pipeline/1.10.0 OS/Win32",
    "Referer": "https://www.bing.com/search?q=Bing+AI&showconv=1&FORM=hpcodx",
    "Referrer-Policy": "origin-when-cross-origin",
    "x-forwarded-for": FORWARDED_IP,
}

HEADERS_INIT_CONVER = {
    "authority": "www.bing.com",
    "accept": "application/json",
    "accept-language": "en-US,en;q=0.9",
    "cache-control": "max-age=0",
    "sec-ch-ua": '"Chromium";v="110", "Not A(Brand";v="24", "Microsoft Edge";v="110"',
    "sec-ch-ua-arch": '"x86"',
    "sec-ch-ua-bitness": '"64"',
    "sec-ch-ua-full-version": '"110.0.1587.69"',
    "sec-ch-ua-full-version-list": '"Chromium";v="110.0.5481.192", "Not A(Brand";v="24.0.0.0", "Microsoft Edge";v="110.0.1587.69"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-model": '""',
    "sec-ch-ua-platform": '"Windows"',
    "sec-ch-ua-platform-version": '"15.0.0"',
    "upgrade-insecure-requests": "1",
    "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36 Edg/112.0.1722.46",
    "x-edge-shopping-flag": "1",
    "x-forwarded-for": FORWARDED_IP,
}

HEADERS_UPLOAD_IMAGE = {
    'authority': 'www.bing.com',
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9',
    'content-type': 'multipart/form-data; boundary=----WebKitFormBoundary3njPohmXErfkAszW',
    'origin': 'https://www.bing.com',
    'referer': 'https://www.bing.com/search?q=bing&cvid=efee7dd5930e49639e5abccc5b5c2c99&aqs=edge.0.69i59l2j69i57j0j46j69i60l4.931j0j4&FORM=ANAB01&PC=U531&rdr=1&rdrig=D2F07E7C924A4A45946BCC72D299D8C2',
    'sec-ch-ua': '"Not/A)Brand";v="99", "Microsoft Edge";v="115", "Chromium";v="115"',
    'sec-ch-ua-arch': '"arm"',
    'sec-ch-ua-bitness': '"64"',
    'sec-ch-ua-full-version': '"115.0.1901.183"',
    'sec-ch-ua-full-version-list': '"Not/A)Brand";v="99.0.0.0", "Microsoft Edge";v="115.0.1901.183", "Chromium";v="115.0.5790.99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-model': '""',
    'sec-ch-ua-platform': '"macOS"',
    'sec-ch-ua-platform-version': '"13.4.0"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'sec-ms-gec': '7E3FF3637700A5BCCD74E182B21D74AC5043A8B15E6DBA73C827F1CD721D258B',
    'sec-ms-gec-version': '1-115.0.1901.183',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36 Edg/115.0.1901.183'
}
