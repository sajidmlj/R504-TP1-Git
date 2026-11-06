import ipaddress


def ip_valide(adresse: str) -> bool:
    """Renvoie True si la chaine est une adresse IPv4 ou IPv6 valide."""
    try:
        ipaddress.ip_address(adresse)
        return True
    except ValueError:
        return False
