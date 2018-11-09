# mapi2xmpp

В одной папке с mapi2xmpp-resend.py должен быть файл config.py со следующим содержимым:

email = 'Exchange Email address' \n
epass = 'Exchange Email pass' \n
jid = 'Jabber Id' \n
jid_sender = 'Sender Jabber Id' \n
jid_sender_pass = 'Sender Jabber pass' \n
folders = ['Support','Admin','Noreply','inbox'] \тут нужно перечислить названия папок, которые проверять нужно
=======
config.py file content:

email = 'Exchange Email address'

epass = 'Exchange Email pass'

jid = 'Jabber Id'

jid_sender = 'Sender Jabber Id'

jid_sender_pass = 'Sender Jabber pass'


# Install:

python3 -m venv venv

source venv/bin/activate

pip install -r requirements.txt 

# Run:

python mapi2xmpp-resend.py 
