from exchangelib import Credentials, Account
from pyxmpp2.simple import send_message
from config import email, epass, jid, jid_sender, jid_sender_pass, folders
import time
import html2text

def send_xmpp_msg(jid_sender, jid_sender_pass, jid, message):
    try:
        send_message(jid_sender, jid_sender_pass, jid, message)
    except:
        print("Can not send message, check something :)")

def connect_mapi(email, epass):
    credentials = Credentials(email, epass)
    try:
        account = Account(email, credentials=credentials, autodiscover=True)
        return account
    except:
        print("Can not connect to mail server, check something :)")
        send_xmpp_msg(jid_sender, jid_sender_pass, jid, "Can not connect to mail server, check something :)")

def check_connection(account):
    if account:
        pass
    else:
        account = connect_mapi(email, epass)

def get_emassages(folder):
    if folder in ['inbox', 'outbox', 'trash', 'sent', 'junk', 'tasks']:
        return list(account.inbox.filter(is_read=False).all().values('subject','id','body','sender'))
    else:
        return list(account.root.glob('**/'+fold).filter(is_read=False).all().values('subject','id','body','sender'))

if __name__ == '__main__':
    account = connect_mapi(email, epass)
    sended = list()
    unreaded = list()
    while True:
        for fold in folders:
            msg = get_emassages(fold)
            if msg:
                for subject in msg:
                    unreaded.append(subject['id'])
                    if subject['id'] not in sended:
                        message = '*'+fold+':*\n-----------\n'+str(subject['sender'].email_address)+\
                                  '\n-----------\n'+subject['subject']+'\n-----------\n'+\
                                  html2text.html2text(subject['body']).replace('\n','')[:500]
                        send_xmpp_msg(jid_sender, jid_sender_pass, jid, message)
                        sended.append(subject['id'])
                msg.clear()
        for iter_msg in sended:
            if iter_msg not in unreaded:
                sended.remove(iter_msg)  
        unreaded.clear()    
        time.sleep(60)
        check_connection(account)