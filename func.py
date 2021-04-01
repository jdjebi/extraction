import os

def get_marchands(marchands_file):
    """ recuperer les éléments necessaire contenu dans le fichier initial"""
    liste_data_marchands= {}

    with open(marchands_file, newline='') as csvfile:
        spamreader = csv.reader(csvfile,delimiter=";")
        for row in spamreader:
            liste_data_marchands[row[4]]={
                "nom":row[0].strip(), 
                "ville":row[1],
                "email":row[4]
            }
    return liste_data_marchands

def email_in(email,liste_marchands):
    """ verifier si un email de la boite de reception correspond à un email de la liste des marchands"""
   return liste_marchands.get(email)

def creation_dossier(marchand,pj=None):
    """créer un dossier recevant les pièces jointes d'un marchants"""
    chemin="marchands\{ville}\{nom_marchand}".format(ville=marchand["ville"],nom_marchand=marchand["nom"])
    try:
        os.makedirs(chemin)
    except FileExistsError:
        pass

    return chemin

def gestion_redondance(pj_name,chemin):
    """gérer la redondance du nom des pièces jointes par ajout de surfixe numérique ordonné"""
    for root, dirs, files in os.walk(chemin, topdown=False):
        if pj_name in files:
            c = files.count(pj_name)
            if c >= 1:
                pj_name = format_pj_name(pj_name,c)
    return os.path.join(chemin,pj_name)

def format_pj_name(pj_name,nbr_occurences):
    """déterminer le nom surfixé d'une pièce jointe en fonction de son nombre de redondances dans son dossier de reception"""
    elems = pj_name.split('.')
    basename = elems[:len(elems) - 1][0]
    extension = elems[-1]
    pj_name = "{}-{}.{}".format(basename,nbr_occurences+1,extension)
    return pj_name