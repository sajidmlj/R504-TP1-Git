import socket

from utils import ip_valide


def port_ouvert(hote: str, port: int, delai: float = 1.0) -> bool:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.settimeout(delai)
        return s.connect_ex((hote, port)) == 0


if __name__ == "__main__":
    hote = "127.0.0.1"
    if ip_valide(hote):
        for port in (22, 80, 443):
            print(port, "ouvert" if port_ouvert(hote, port) else "ferme")
# Option future : --timeout en ligne de commande
