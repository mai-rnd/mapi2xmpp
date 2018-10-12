from exchangelib import Credentials, Account
from pyxmpp2.simple import send_message
from config import *
import time
import html2text

if __name__ == '__main__':
    credentials = Credentials(email, epass)
    account = Account(email, credentials=credentials, autodiscover=True)
    sended = list()
    while True:
        folders = ['Support','Admin','Noreply','inbox']
        for fold in folders:
            if fold in ['inbox', 'outbox', 'trash', 'sent', 'junk', 'tasks']:
                msg = list(account.inbox.filter(is_read=False).all().values('subject','id','body','sender'))
            else:
                msg = list(account.root.glob('**/'+fold).filter(is_read=False).all().values('subject','id','body','sender'))
            if msg:
                for subject in msg:
                    if subject['id'] not in sended:
                        send_message(jid_sender, jid_sender_pass, jid, 
                                     '*'+fold+':*\n-----------\n'+
                                     str(subject['sender'].email_address)+'\n-----------\n'+
                                     subject['subject']+'\n-----------\n'+
                                     html2text.html2text(subject['body']).replace('\n','')[:500])
                        sended.append(subject['id'])
                msg.clear()        
        time.sleep(60)
