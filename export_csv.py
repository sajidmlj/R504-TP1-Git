import csv


def exporter(resultats: dict, chemin: str = "resultats.csv") -> None:
    with open(chemin, "w", newline="", encoding="utf-8") as f:
        ecrivain = csv.writer(f)
        ecrivain.writerow(["cible", "etat"])
        for cible, etat in resultats.items():
            ecrivain.writerow([cible, etat])
