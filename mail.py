from imap_tools import MailBox

EMAIL = "ti.dev99@gmail.com"
PASSWORD = "01060878@Ti"

print("Connexion à la boîte de {}...".format(EMAIL))

with MailBox('imap.gmail.com').login(EMAIL, PASSWORD, initial_folder='INBOX') as mailbox:

    nbr_msgs = 0
    msgs = []
    msgs_pj = []

    print("Connexion OK")
    print("Découverte des messages...")

    msgs_data = mailbox.fetch()

    print("Découverte terminée")
    print("Analyse de la découverte:\n")

    for msg in mailbox.fetch():
        sender = msg.from_ 
        pjs = msg.attachments
        pjs_nbr = len(pjs)

        nbr_msgs += 1

        print("E-mail: {}".format(sender))
        print("Pièces jointes: {}".format(pjs_nbr))

        msgs.append(msg)

        if pjs_nbr > 0:
            msgs_pj.append(msg)
            print(">>> Pièce jointe détectée: {}".format(pjs_nbr))

        print()

    nbr_msgs_pj = len(msgs_pj)

    print("{} messages découverts".format(nbr_msgs))
    print("{} messages découverts avec pièces jointes".format(nbr_msgs_pj))

    #for msg in mailbox.fetch():

    """
    for att in msg.attachments:
        print(att.filename, att.content_type)
        
        with open('tmp/{}'.format(att.filename), 'wb') as f:
            f.write(att.payload)
    """
