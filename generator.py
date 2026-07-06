import json
import itertools
from datetime import datetime, timedelta

# ==============================================================================
# 1. A PONTOS CSAPATTAGOK BEÁLLÍTÁSA
# ==============================================================================
LEADERS = [
    "girlinshadow",
    "|Joseph|",
    "Renegades87",
    "Lost ~ Phantom♡",
    "22Nico22"
]

TAGOK = [
    "Emmanuel80",
    "ReiJ",
    "⚙♦⚙", 
    "itsLeah", 
    "SmellyDerek", 
    "kuntulmax", 
    "sTrangers", 
    "leo~paw", 
    "plantolume", 
    "Psychfish", 
    "LunaMoonShadow", 
    "Jamput", 
    "Kingeorgemlm", 
    "Lord3YMZz91-XC", 
    "CosmicStar", 
    "Roymod76", 
    "kadodaanny", 
    "Lord3YD0tF1-6E", 
    "Malpaso",
    "ShadowHeel",
    "Ultraman21",
    "Bluebaron121",
    "BATCAT",
    "hax2025",
    "Ockye",
    "Lord3YbP0vV-TN",
    "HunterHeroGlauco",
    "akssh"
]

# ==============================================================================
# 2. MENETREND GENERÁLÓ MOTOR
# ==============================================================================
def convoy_menetrend_gyarto(napok_szama=90, fajlnev="menetrend.json"):
    """
    Legenerálja a convoyok beosztását és elmenti JSON formátumban.
    A dátumok lesznek a kulcsok (YYYY-MM-DD), így JS-ből azonnal kereshető.
    """
    leader_pool = itertools.cycle(LEADERS)
    tag_pool = itertools.cycle(TAGOK)
    
    ma = datetime.now()
    napnevek = ["Hétfő", "Kedd", "Szerda", "Csütörtök", "Péntek", "Szombat", "Vasárnap"]
    
    vegeredmeny = {}
    
    for i in range(napok_szama):
        jovo_datum = ma + timedelta(days=i)
        datum_kulcs = jovo_datum.strftime("%Y-%m-%d")
        nap_neve = napnevek[jovo_datum.weekday()]
        
        aktualis_leader = next(leader_pool)
        aktualis_tag1 = next(tag_pool)
        aktualis_tag2 = next(tag_pool)
        
        vegeredmeny[datum_kulcs] = {
            "nap": nap_neve,
            "csucs_hely_leader": aktualis_leader,
            "hely_2_tag": aktualis_tag1,
            "hely_3_tag": aktualis_tag2
        }
        
    with open(fajlnev, "w", encoding="utf-8") as f:
        json.dump(vegeredmeny, f, ensure_ascii=False, indent=4)
        
    print(f"✅ SIKERES GENERÁLÁS!")
    print(f" -> {napok_szama} nap rögzítve a '{fajlnev}' fájlban.")
    print(f" -> Most már behúzhatod a weboldaladra!")

if __name__ == "__main__":
    convoy_menetrend_gyarto(napok_szama=1000)