from imap_tools import MailBox
from func import *

EMAIL = "ti.dev99@gmail.com"
PASSWORD = "01060878@Ti"

print("Connexion à la boîte de {}...".format(EMAIL))

with MailBox('imap.gmail.com').login(EMAIL, PASSWORD, initial_folder='INBOX') as mailbox:

    nbr_msgs = 0
    msgs = []
    msgs_pj = []

    print("Connexion OK")
    print("Découverte des messages...")

    print("Découverte terminée")
    print("Analyse de la découverte:\n")

    for msg in mailbox.fetch():
        sender = msg.from_ 
        pjs = msg.attachments
        pjs_nbr = len(pjs)

        msgs.append(sender)
        nbr_msgs += 1

        print("E-mail: {}".format(sender))
        print("Pièces jointes: {}".format(pjs_nbr))

        if pjs_nbr > 0:
            msgs_pj.append(msg)
            print(">>> Pièce jointe détectée: {}".format(pjs_nbr))

        print()

    nbr_msgs_pj = len(msgs_pj)

    print(msgs_pj)

    print("{} messages découverts".format(nbr_msgs))
    print("{} messages découverts avec pièces jointes".format(nbr_msgs_pj))

    for m in msgs:
        print(m)

    
    liste_data_marchands=get_marchands("marchands.csv")

    for message in  msgs_pj:

        email_marchand = message.from_

        marchand=email_in(email_marchand,liste_data_marchands)

        if marchand is not None:

            chemin=creation_dossier(marchand)

            for att in message.attachments:
            
                ##print(att.filename, att.content_type)

                chemin_pj = gestion_redondance(att.filename,chemin)
        
                with open(chemin_pj, 'wb') as f:
                    f.write(att.payload)
"""
    for att in msg.attachments:
        print(att.filename, att.content_type)
        
        with open('tmp/{}'.format(att.filename), 'wb') as f:
            f.write(att.payload)
"""