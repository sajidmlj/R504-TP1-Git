import platform
import subprocess
import sys

from utils import ip_valide


def ping(hote: str) -> bool:
    option = "-n" if platform.system() == "Windows" else "-c"
    resultat = subprocess.run(["ping", option, "1", hote], capture_output=True)
    return resultat.returncode == 0


if __name__ == "__main__":
    cible = sys.argv[1] if len(sys.argv) > 1 else "127.0.0.1"
    if not ip_valide(cible):
        print("Adresse IP invalide")
    else:
        print(cible, "repond" if ping(cible) else "ne repond pas")
