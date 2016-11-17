import csv
import os
import re
import shutil

id = ['id', '아이디', '계정이름', '계정', 'identification']
name = ['name', '이름', '실명', '성함', '성명', 'real_name', 'realname']
nickname = ['nickname', '닉네임', '별명', '성함', '성명', 'nick_name', 'sub_name', 'nick-name']
phone = ['phone', '핸드폰번호', '휴대폰번호', '핸드폰', '휴대폰', '번호',
         'mobilephone', 'mobile', 'cellphone', 'cell', 'phone_num', 'phonenum']
email = ['email', '이메일', '메일주소', '메일', 'e-mail', 'e_mail', 'mail']
birthday = ['birth', '생일', 'birthday']
gender = ['gender', '성별', 'sex']

word_list = [id, name, nickname, phone, email, birthday, gender]


class reg_process():
    def __init__(self, text):
        self.__initialize()
        self.reg_dict = {}
        self.text = text.lower().replace(' ', '')

    def __initialize(self):
        self.key_list = []
        self.reg_dict = {}

    def __create_key_list(self, wlist):
        for i in range(0, len(wlist) - 1):
            self.key_list.append(wlist[0])

    def __word_key_bind(self, wlist, key_list):
        self.reg_dict = dict(zip(wlist[1:], key_list))

    def __list_to_dict(self, wlist):
        self.__create_key_list(wlist)
        self.__word_key_bind(wlist, self.key_list)

    def dict_to_reg(self, wlist):
        self.__initialize()
        self.__list_to_dict(wlist)
        rep = self.reg_dict
        rep = dict((re.escape(k), v) for k, v in iter(rep.items()))
        pattern = re.compile(r'\b(' + '|'.join(rep.keys()) + r')\b')
        self.text = pattern.sub(lambda m: rep[re.escape(m.group(0))], self.text)

    def refine_header(self):
        for wl in word_list:
            self.dict_to_reg(wl)

        return self.text


class pre_process():
    def __init__(self, filename):
        self.new_filename = os.path.dirname(filename) + '/r_' + os.path.basename(filename)

        with open(filename, 'r') as origin:
            header = origin.readline()
            new_header = reg_process(header)
            header = new_header.refine_header()
            with open(self.new_filename, 'w+') as mod:
                mod.write(header)
                shutil.copyfileobj(origin, mod)


class csv_reader():
    def __init__(self, filename):
        self.new_filename = os.path.dirname(filename) + '/r_' + os.path.basename(filename)
        pre_process(filename)

        self.file = open(self.new_filename, 'r')
        self.csv_reader = csv.reader(self.file, delimiter=',')
        self.header = self.read_header()
        self.body = self.read_body()

        self.csv_dict = dict()
        self.csv_dict['target'] = self.read_dict()

    def read_header(self):
        return next(self.csv_reader)

    def read_body(self):
        body_list = list()
        for i in self.csv_reader:
            body_list.append(i)

        return body_list

    def read_dict(self):
        csv_list = list()
        with open(self.new_filename, 'r') as csv_file:
            csv_dictdata = csv.DictReader(csv_file)
            for row in csv_dictdata:
                csv_list.append(row)

        return csv_list
