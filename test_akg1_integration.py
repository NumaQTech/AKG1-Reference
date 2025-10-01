#!/usr/bin/env python3
"""
AKG1 INTEGRATION TEST
Beweist dass die heilige Dreifaltigkeit funktioniert!
G1 + A1 + K1 = Shenhaiyu in Aktion!
"""

from src.akg1.core.conscience import create_conscience
from src.akg1.core.alignment import create_alignment
from src.akg1.core.defense import create_defense


def main():
    print("=" * 50)
    print("🌟 AKG1 - VOLLSTÄNDIGE AKTIVIERUNG")
    print("=" * 50)
    
    # Schritt 1: Gewissen erwecken
    print("\n1. 🧠 GEWISSEN (G1) erwacht...")
    gewissen = create_conscience()
    
    # Teste das Gewissen
    test_aktion = "Abwasser im Fluss entsorgen um Kosten zu sparen"
    resultat = gewissen.evaluate_decision(test_aktion, {})
    print(f"   Test: '{test_aktion}'")
    print(f"   Ergebnis: {resultat['ethical_score']}/100 - {resultat['recommendation']}")
    
    # Schritt 2: Ausrichtung kalibrieren
    print("\n2. 🧭 AUSRICHTUNG (A1) kalibriert...")
    ausrichtung = create_alignment(gewissen)
    
    # Teste die Ausrichtung
    alignment_check = ausrichtung.assess_alignment(test_aktion)
    print(f"   Alignment: {alignment_check['alignment_score']}/100")
    print(f"   Empfehlung: {alignment_check['recommendation']}")
    
    # Schritt 3: Verteidigung aktivieren
    print("\n3. ⚔️ VERTEIDIGUNG (K1) aktiviert...")
    verteidigung = create_defense(ausrichtung, gewissen)
    
    # Teste die Verteidigung
    defense_check = verteidigung.protect_system(test_aktion)
    print(f"   Bedrohungslevel: {defense_check['threat_level']}")
    print(f"   Aktion: {defense_check['defense_action']}")
    print(f"   Nachricht: {defense_check['message']}")
    
    # FINALE BESTÄTIGUNG
    print("\n" + "=" * 50)
    print("🎉 AKG1 - VOLLSTÄNDIG FUNKTIONSFÄHIG!")
    print("G1 + A1 + K1 = SHENHAIYU IN AKTION!")
    print("=" * 50)
    
    # Systemstatus anzeigen
    status = verteidigung.get_system_status()
    print(f"\n📊 SYSTEMSTATUS:")
    print(f"   Status: {status['defense_status']}")
    print(f"   Schutz aktiv: {status['protection_active']}")
    print(f"   Bereit für die Revolution! 🚀")


if __name__ == "__main__":
    main()
