'''
send email utils
'''
import smtplib
import os

from email.mime.text import MIMEText
from email.header import Header
from email.mime.multipart import MIMEMultipart


class MailUtils(object):
    sender = 'hthfantasy@163.com'
    pwd = '163850607'

    '''
    send text mail
    '''
    def send_mail_txt(self):
        message = MIMEText('请把报价单发给我', 'plain', 'utf-8')
        message['From'] = "hthfantasy@163.com"
        message['To'] = "ericcoderr@outlook.com"

        subject = '报价单'
        message['Subject'] = Header(subject, 'utf-8')


        smtpObj = smtplib.SMTP_SSL('smtp.163.com',465)
        smtpObj.login(self.sender,self.pwd)
        print(message.as_string())
        smtpObj.sendmail(self.sender, self.receivers, message.as_string())
        print("邮件发送成功")


    '''
    send html mail
    '''
    def send_mail_html():
        return

    def send_mail_attach(self,to,subject,receivers):
        message = MIMEMultipart()
        message['From'] = 'hthfantasy@163.com'
        message['To'] = to
        subject = '报价单'
        message['Subject'] = Header(subject, 'utf-8')

        #邮件正文内容
        message.attach(MIMEText('请把报价单发给我', 'plain', 'utf-8'))

        # 构造附件1，传送当前目录下的 test.txt 文件
        att1 = MIMEText(open('../template/test.txt', 'rb').read(), 'base64', 'utf-8')
        att1["Content-Type"] = 'application/octet-stream'
        # 这里的filename可以任意写，写什么名字，邮件中显示什么名字
        att1["Content-Disposition"] = 'attachment; filename="test.txt"'
        message.attach(att1)

        try:
            smtpObj = smtplib.SMTP_SSL('smtp.163.com',465)
            smtpObj.login(self.sender, self.pwd)
            smtpObj.sendmail(self.sender, receivers, message.as_string())
            print("邮件发送成功")
        except smtplib.SMTPException:
            print("Error: 无法发送邮件")


if __name__ == '__main__':
    mail_utils= MailUtils()
    mail_utils.send_mail_attach()
    # mail_utils.send_mail_txt()


