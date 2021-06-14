import pandas as pd
import requests,smtplib,os,random,time
from concurrent.futures import ThreadPoolExecutor,as_completed
from email.message import EmailMessage

PORT = 465  # For SSL
SMTP_SERVER = "smtp.gmail.com"
MY_EMAIL=os.environ.get('TRY_GMAIL_ID')
MY_EMAIL_PASSWORD=os.environ.get('TRY_GMAIL_PASSWORD')
MESSAGE = """
Hi {first_name}, 
    Your username is {username} . Your password is {password} .
"""

BASE_URL='http://127.0.0.1:8000/'
BASE_AUTH_TOKEN='88fd8855373dc491c390e6c1217dfb1c02e7d575'

BASE_SITE_URL='http://bridged-mvp-alpha.herokuapp.com/'
BASE_SITE_AUTH_TOKEN='3a0417ede31ee9fe6ca212478eae0b625f783a76'


def mailer(idx=None):
    global df
    if idx is None:
        raise ValueError('Index value must be provided.')
    row=df.loc[idx,:]

    to_address=row['email']
    to_address='celef32288@beydent.com'

    msg=EmailMessage()
    msg['Subject']='Login credentials for BridgEd'
    msg['From']=MY_EMAIL
    msg['To']=to_address
    content=MESSAGE.format(
        first_name=row['first_name'],
        username=row['username'],
        password=row['password']
    )

    msg.set_content(content)

    try:
        with smtplib.SMTP_SSL(SMTP_SERVER,PORT) as context_mailing_server:
            context_mailing_server.login(MY_EMAIL,MY_EMAIL_PASSWORD)
            context_mailing_server.send_message(msg)
        return 0
    except Exception as e:
        print(e)
        print('Could not send email to {}'.format(to_address))

    return 1


def func(index=None):
    global df,reg_failures,mail_failures
    registered=0
    if index is None:
        raise ValueError('Index must be provided.')
    row=df.loc[index,:]
    js='Already registered {}({}).'.format(row['username'],index)

    if row['registered']==0:
        data={
            'username':'{}'.format(row['username']),
            'email':row['email'],
            'password':row['password'],
            'password2': row['password']
        }
        header = {
            'Authorization': 'Token {}'.format(BASE_SITE_AUTH_TOKEN)
        }
    
        response = requests.post(url=BASE_SITE_URL+'students/register/', data=data, headers=header)
        js=response.json()
        
        if (response.status_code>201) or ('token' not in js):
            reg_failures+=1
            return 'Index: {}({}) not created.\nResponse: {}'.format(index,row['username'],response.text)
        df.loc[index,'registered']=registered=1
        
    if row['mailed']==0 and registered:
        mail_status=mailer(index)
        mail_failures+=mail_status
        df.loc[index,'mailed']=int(not mail_status)

    return js


def runner():
    global df
    threads = []
    with ThreadPoolExecutor(max_workers=10) as executor:
        for idx in range(len(df)):
            threads.append(executor.submit(func, idx))

        for task in as_completed(threads):
            print(task.result())
    return


if __name__ == '__main__':
    t1=time.time()
    df = pd.read_csv('students.csv')
    reg_failures=mail_failures=0

    runner()
    print('\nTOTAL REGISTRATIONS FAILED: {}/{}'.format(reg_failures,len(df)))
    print('\nTOTAL MAILINGS FAILED: {}/{}'.format(mail_failures,len(df)-reg_failures))

    _=df.to_csv('students.csv',header=True,index=False)

    t2=time.time()
    print('{} secs for {} tasks'.format(t2-t1,len(df)))
