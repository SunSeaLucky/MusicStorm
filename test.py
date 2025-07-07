import requests

headers = {
    "Accept": "*/*",
    "Accept-Language": "en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7",
    "Authorization": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyIjp7InVzZXJuYW1lIjoidGVzdCJ9LCJleHAiOjE3NTE5ODIyODF9.KjqCbUYoZIc3pBaIHYDGivD_XaREnyqBEeIzh9LZAJA",
    "Cache-Control": "no-cache",
    "Connection": "keep-alive",
    'Content-Type': 'application/json',
    "Origin": "http://localhost:5173",
    "Pragma": "no-cache",
    "Referer": "http://localhost:5173/",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-site",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36",
    "sec-ch-ua": "\"Google Chrome\";v=\"137\", \"Chromium\";v=\"137\", \"Not/A)Brand\";v=\"24\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"macOS\""
}

url = "http://sunsealucky.cn:8080/post/addPost"

params = {
    "id": "11",
    "user_id": "10", 
    "user_name": "张三",
    "user_avatar": "http://www.example.com/avatar.jpg",
    "content": "今天天气不错，想听歌。",
    "time": "2022-01-11 10:00:00",
    "tracks_id": "1",
    "tracks_name": "海",
    "tracks_artist": "周杰伦",
    "likes": "500"
}

response = requests.get(url, headers=headers, params=params)

print(response.text)
print(response)