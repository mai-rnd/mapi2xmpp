# mapi2xmpp

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
