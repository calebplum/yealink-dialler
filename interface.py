import requests


# Program parameters
phone_username = ''                 # Username to the phone's web interface
phone_password = ''                 # Password to the phone's web interface
phone_ip = ''                       # IP address (or hostname if resolvable) of the phone
phone_http_protocol = 'http'        # 'http' or 'https'. Default is http
endcall_url_suffix = 'key=X'        # Suffix to be added to the end of the url to send endcall command
answer_url_suffix = 'key=ENTER'     # Suffix to be added to the end of the url to send answer command
mute_url_suffix = 'key=MUTE'        # Suffix to be added to the end of the url to send mute/unmute command
base_url = '/cgi-bin/ConfigManApp.com?'     # The part of the URL between the phone's IP address and the command to be executed (as shown above)


# Internal parameters
base_url = '%s://%s:%s@%s%s' % (phone_http_protocol, phone_username, phone_password, phone_ip, base_url)


def menu():
    print 'Options:'
    print '1. Dial out'
    print '2. Answer'
    print '3. Hang up'
    print '4. Mute/Unmute'
    selection = int(raw_input('Make your selection [1-4]: '))
    if selection == 1:
        dialoutnumber = raw_input('Enter number to dial: ')
        dialout(dialoutnumber)
    elif selection == 2:
        answer()
    elif selection == 3:
        hangup()
    elif selection == 4:
        mute()
    else:
        print ('Invalid selection')
    print ''
    menu()


def dialout(number):
    try:
        print requests.get(base_url + 'number=' + number + '&outgoing_uri=URI')
        print 'Sent dial request for '+number
    except requests.exceptions.ConnectionError:
        print 'Error: Could not connect to phone'


def hangup():
    try:
        print requests.get(base_url + endcall_url_suffix)
        print 'Sent hangup request'
    except requests.exceptions.ConnectionError:
        print 'Error: Could not connect to phone'


def answer():
    try:
        print requests.get(base_url + answer_url_suffix)
        print 'Sent Answer request'
    except requests.exceptions.ConnectionError:
        print 'Error: Could not connect to phone'


def mute():
    try:
        print requests.get(base_url + mute_url_suffix)
        print 'Sent Mute/Unmute request'
    except requests.exceptions.ConnectionError:
        print 'Error: Could not connect to phone'


menu()

