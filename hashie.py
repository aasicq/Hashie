# Coded By Sameera a.k.a άλφα Χ

import requests
import hashlib
import time
import sys
import re

version = "1.0"

banner = r'''

  ___ ___               .__    .__
 /   |   \_____    _____|  |__ |__| ____
/    ~    \__  \  /  ___/  |  \|  |/ __ \
\    Y    // __ \_\___ \|   Y  \  \  ___/
 \___|_  /(____  /____  >___|  /__|\___  >
       \/      \/     \/     \/        \/ v1.0

      [Coded By Sameera a.k.a άλφα Χ]


    [1] Hash Cracker
    [2] Hash Generator
    [3] Hash Identifier
    [4] Hash My Files
    [5] Update Hashie
    [6] Quit

'''


def HashMyFiles(f):
    md5Hash = hashlib.md5()
    sha1Hash = hashlib.sha1()
    sha256Hash = hashlib.sha256()
    sha384Hash = hashlib.sha384()
    sha512Hash = hashlib.sha512()
    with open(f, 'rb') as f:
        for chunk in iter(lambda: f.read(4096), b""):
            md5Hash.update(chunk)
            sha1Hash.update(chunk)
            sha256Hash.update(chunk)
            sha384Hash.update(chunk)
            sha512Hash.update(chunk)
    print("MD5 - " + md5Hash.hexdigest())
    print("SHA1 - " + sha1Hash.hexdigest())
    print("SHA256 - " + sha256Hash.hexdigest())
    print("SHA384 - " + sha384Hash.hexdigest())
    print("SHA512 - " + sha512Hash.hexdigest())


def connection(url='http://www.google.com/', timeout=5):
    try:
        req = requests.get(url, timeout=timeout)
        req.raise_for_status()
        return True
    except requests.HTTPError as e:
        print("Checking internet connection failed, status code {0}.".format(
            e.response.status_code))
    except requests.ConnectionError:
        print("No internet connection available.")
    return False


def quit():
    alpha = input("Are You Sure?[yes/no] - ").lower()
    if alpha == "yes":
        exit()
    if alpha == "no":
        print(banner)
        choice()


def crack():
    hashvalue = input("Enter a hash to decrypt - ")
    data = {'auth': '8272hgt', 'hash': hashvalue, 'string': '', 'Submit': 'Submit'}
    response = requests.post('http://hashcrack.com/index.php', data).text
    match = re.search(r'<span class=hervorheb2>(.*?)</span></div></TD>', response)
    if match:
        print("Hash cracked: " + match.group(1))
        sys.exit()
    else:
        data = {"md5": hashvalue, "x": "24", "y": "7"}
        response = requests.post(
            'http://md5.my-addr.com/md5_decrypt-md5_cracker_online/md5_decoder_tool.php', data).text
        match = re.search(r"<span class='middle_title'>Hashed string</span>: (.*?)</div>", response)
        if match:
            print("Hash cracked: " + match.group().split('span')[2][3:-6])
            sys.exit()
        else:
            response = requests.get('https://lea.kz/api/hash/' + hashvalue).text
            match = re.search(r'<title>(.*?)</title>', response)
            if match:
                print("Sorry! This hash is not present in our database.")
                sys.exit()
            else:
                print("Hash cracked: " + response[13:][:-3])
                sys.exit()


def type():
    hashvalue = input("Please enter your hash here - ")
    if len(hashvalue) == 32:
        print("Hash function = MD5")
    elif len(hashvalue) == 40:
        print("Hash function = SHA1")
    elif len(hashvalue) == 64:
        print("Hash function = SHA-256")
    elif len(hashvalue) == 96:
        print("Hash function = SHA-384")
    elif len(hashvalue) == 128:
        print("Hash function = SHA-512")
    else:
        print("Sorry! Unable to identiy " + hashvalue)


def generator():
    usr_input = input("Please enter your string here - ").encode()
    print("Generating Hashes Please Wait !!!")
    time.sleep(1.0)
    print('\n')

    # MD4
    alpha = hashlib.new("md4")
    alpha.update(usr_input)
    md4 = alpha.hexdigest()
    print("MD4 - " + md4)

    # MD5
    alpha = hashlib.new("md5")
    alpha.update(usr_input)
    md5 = alpha.hexdigest()
    print("MD5 - " + md5)

    # SHA1
    alpha = hashlib.new("sha1")
    alpha.update(usr_input)
    sha1 = alpha.hexdigest()
    print("SHA1 - " + sha1)

    # SHA224
    alpha = hashlib.new("sha224")
    alpha.update(usr_input)
    sha224 = alpha.hexdigest()
    print("SHA224 - " + sha224)

    # SHA256
    alpha = hashlib.new("sha256")
    alpha.update(usr_input)
    sha256 = alpha.hexdigest()
    print("SHA256 - " + sha256)

    # SHA384
    alpha = hashlib.new("sha384")
    alpha.update(usr_input)
    sha384 = alpha.hexdigest()
    print("SHA384 - " + sha384)

    # SHA512
    alpha = hashlib.new("sha512")
    alpha.update(usr_input)
    sha512 = alpha.hexdigest()
    print("SHA512 - " + sha512)


def choice():
    try:
        print(banner)
        selection = input("Hashie:- ")
        if selection == '1':
            if connection() == True:
                crack()
        elif selection == '2':
            generator()
        elif selection == '3':
            type()
        elif selection == '4':
            HashMyFiles(input("Enter file name to genarate hashes - "))
        elif selection == '5':
            print("Checking for updates...")
            update = requests.get(
                "https://raw.githubusercontent.com/Sameera-Madhushan/Hashie/master/hashie.py").content.decode("UTF-8")
            if version not in update:
                co = input(
                    "A new version of Hashie is available. Would you like to update?[yes/no] - ").lower()
                if co == "yes":
                    os.system(
                        'cd .. && rm -r Hashie && git clone https://github.com/Sameera-Madhushan/Hashie')
                if co == "no":
                    print(banner)
                    choice()
                else:
                    up = str(
                        input("Sorry!Invalid Selection. Do You Wish to Quit[yes/no] - ").lower())
                    if up == "yes":
                        quit()
                        if up == "no":
                            print(banner)
                            choice()
                        else:
                            exit()
            else:
                print("Digger is Upto Date.")
                exit()

        elif selection == '6':
            quit()
        else:
            omega = str(input("Sorry! Invalid selection. Do you wish to quit [yes/no] - ").lower())
            if omega == "yes":
                quit()
            if omega == "no":
                print(banner)
                choice()
            else:
                exit()

    except(KeyboardInterrupt):
        print('\n' "Programme Interrupted")


choice()

'''
- References -
http://hashcrack.com
http://md5.my-addr.com
https://lea.kz
'''
