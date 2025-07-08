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

# params = {
#     "id": 100001,
#     "user_id": 123123, 
#     "user_name": "paddddddd",
#     "user_avatar": "https://ts1.tc.mm.bing.net/th/id/OIP-C.-rCxIbM2E5yv46Ndkv1lkAHaHa?w=197&h=211&c=8&rs=1&qlt=90&o=6&dpr=1.1&pid=3.1&rm=2",
#     "content": "海的形状",
#     "time": "2025-07-07 10:12:45",
#     "tracks_id": "1",
#     "tracks_name": "海の形",
#     "tracks_artist": "昙轩",
#     "likes": "1.3w"
# }

# params = {
#     "id": 100004,
#     "user_id": 123123, 
#     "user_name": "paddddddd",
#     "user_avatar": "https://p1.music.126.net/S7fYKauzveE9NDDVstBQvw==/109951171178959502.jpg",
#     "content": "生活の伪造 いつも通り 通り过ぎて",
#     "time": "2025-07-07 10:12:45",
#     "tracks_id": "2",
#     "tracks_name": "秒针を噛む",
#     "tracks_artist": "ずっと真夜中でいいのに",
#     "likes": "3451"
# }

params = {
    "id": 100005,
    "user_id": 123123, 
    "user_name": "paddddddd",
    "user_avatar": "https://p1.music.126.net/DVi9B70oYVFtDxVqZf_56g==/109951171264259694.jpg?param=130y130",
    "content": "姥姥",
    "time": "2025-07-07 10:12:45",
    "tracks_id": "2",
    "tracks_name": "莫愁乡",
    "tracks_artist": "亞細亞曠世奇才",
    "likes": "3451"
}

response = requests.get(url, headers=headers, params=params)

print(response.text)
print(response)