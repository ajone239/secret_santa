import smtplib, ssl, random
from credentials import *

port = 465  # For SSL

message = """\
Subject: Secret Santa Results 2019!!

Hello {}, it is your job to get a gift for {}. Good luck and Happy Hollidays!

Best,
Santa """

# Create a secure SSL context
context = ssl.create_default_context()

def send_email(combo):

    with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
        receiver_email = combo[1]
        email_mes = message.format(combo[0],combo[2])
        server.login(SENDER_EMAIL, PASSWORD)
        server.sendmail(SENDER_EMAIL, receiver_email, email_mes)

def gen_list(naemso):

    giftees = {naemso[x][0] for x in range(len(naemso))}

    try:
        for gifter in naemso:
            na = gifter[0]
            so = gifter[2]

            gift_set = list(filter(lambda x: x != na and x != so, giftees))
            
            giftee = random.choice(gift_set)

            gifter[2] = giftee
            giftees.remove(giftee)
    except:
        return False

    return True

if __name__ == "__main__":
    while not gen_list(KNOX_JOLLY_BRINGERS):
        print("Trying to make the list")

    for combo in KNOX_JOLLY_BRINGERS:
        print(combo)
        #try:
        #    send_email(combo)
        #except:
        #    print("mail didnt send")

    print("##########################################")

    while not gen_list(BORO_JOLLY_BRINGERS):
        print("Trying to make the list")

    for combo in BORO_JOLLY_BRINGERS:
        print(combo)
