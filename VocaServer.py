import requests
import json

openApiURL = "http://aiopen.etri.re.kr:8000/WiseWWN/Homonym"
accessKey = "5418db70-482a-45ca-8ec5-a61d542a1e99"  # 여기에 자신의 ETRI에서 발급받은 Access Key 입력
word = "심심하다"  # 여기에 동음이의어를 조회하고자 하는 단어 입력

requestJson = {
    "argument": {
        "word": word
    }
}

headers = {
    "Content-Type": "application/json; charset=UTF-8",
    "Authorization": accessKey
}

response = requests.post(openApiURL, headers=headers, data=json.dumps(requestJson))

print("[responseCode] " + str(response.status_code))
print("[responBody]")

# JSON 데이터 파싱
data = json.loads(response.text)

if data['result'] == 0:
    homonyms = data['return_object']['homonym']
    for homonym in homonyms:
        word = homonym['word']
        description = homonym['description']
        example = description.split("[[예제]] ")[1][:-1] if "[[예제]]" in description else "예제 없음"
        print(f"단어: {word}")
        print(f"정답: {description}")
        print(f"문제: {example}")
        print()
else:
    print("동음이의어를 찾을 수 없습니다.")
