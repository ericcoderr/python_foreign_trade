'''
Description : excel utils
     Author : eric
      date  : 2018-03-28
'''
import excel_utils
import mail_utils

class App(object):

    def send_attach_mail(self):
        data_list = excel_utils.read_excel(self)
        print(data_list)
        for email_row in data_list:
            print("dsad")
