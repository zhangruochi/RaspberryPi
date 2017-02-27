#!/usr/bin/env python3
import os
import re
import smtplib
from email.mime.text import MIMEText
from email.header import Header 


def get_ips():
    pattern = re.compile("inet [0-9]{3}.[0-9]+.[0-9]+.[0-9]+")
    result = re.findall(pattern,os.popen("ifconfig").read())
    try:
        result.remove('inet 127.0.0.1')
    except:
        pass    
     
    return ", ".join([ip.strip("inet ") for ip in result])


def send_email(ip):
    print("get ip: ",ip)
    from_addr = "185987278@qq.com"
    password = "skgmfjzjhrscbiha"
    # 输入收件人地址:
    to_addr = "lvduzhen@gmail.com"
    smtp_server = "smtp.qq.com"  #发送邮件的服务器

    msg = MIMEText("get the ip: {}".format(ip))
    msg["Subject"] = "Email Test"
    msg["From"]    = from_addr
    msg["To"]      = to_addr
    
    try:
        server = smtplib.SMTP_SSL(smtp_server, 465) # 采用 SSL 坑啊！
        server.login(from_addr, password)
        print("login success!")
        server.sendmail(from_addr, [to_addr], msg.as_string())
        server.quit()
        print("send success!")
    except:
        print("send failed!")


def check():
    while True:
        result = os.system("ping 8.8.8.8 -c 2")
        if result:
            print("failed")
            sleep(5)
        else:
            print("connect successful!")
            break
    return True  


def main():
    check()
    ip = get_ips()
    send_email(ip)



if __name__ == '__main__':
    main()
    