import requests

# 设置请求的URL
url = "https://www.opsalert.cn/msgpush/api/send/a51b7450-ffc2-4b93-84cc-afe4cb2023ea"

# 准备要发送的数据，这里假设有一个中文字段'name'
data = {
    "title": "我来了",
    "priority": 1,
    "content": "我来了",
    "message_title": "我来了",
}  # 中文名字

# 发送POST请求，指定headers中的Content-Type为application/x-www-form-urlencoded
# 并确保服务器能够正确解析中文编码
headers = {"Content-Type": "application/json; charset=utf-8"}
# headers = {"Content-Type": "application/x-www-form-urlencoded; charset=utf-8"}

# 使用requests.post发送请求，注意params参数需要被编码为url编码格式
response = requests.post(url, data=data, headers=headers)

# 检查响应状态码
if response.status_code == 200:
    # 如果一切正常，打印响应内容
    print("请求成功，响应内容：")
    print(response.text)
else:
    # 如果出现错误，打印错误信息
    print(f"请求失败，状态码：{response.status_code}")
    print(response.text)
