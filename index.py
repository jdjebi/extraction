import csv
import os
from func import *

liste_data_marchands=get_marchands("marchands.csv")

marchand=email_in("payment@kamycity.com",liste_data_marchands)

chemin=creation_dossier(marchand)

chemin_enregistrement = gestion_redondance("entre.txt",chemin)

print(chemin_enregistrement)
