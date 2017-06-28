from inbox import Inbox
from smtplib import SMTP

inbox = Inbox()

SMTP_HOST = 'smtp.mydomain.com'
SMTP_INBOX = 'spamtrap@mydomain.com'
STOP_AT_COUNT = 1

@inbox.collate
def handle(to, sender, subject, body):
    print 'Forwarding Mail'
    STOP_AT_COUNT += 1
    conn = SMTP(SMTP_HOST, 25, 'localhost')
    conn.ehlo_or_helo_if_needed()
    conn.sendmail(sender, SMTP_INBOX, body)
    conn.quit()
    if STOP_AT_COUNT == 100:
        print 'Enough is enough. Closing now.'
        exit()

print 'starting server'
inbox.serve(address='0.0.0.0', port=25)
