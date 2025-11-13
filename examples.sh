#!/bin/bash

# Beispiel-Skripte für die KI-Strategie-Simulation

echo "🇩🇪 KI-Strategie-Simulation - Beispiele"
echo "========================================"
echo ""

# Beispiel 1: Basis-Simulation (20 Minuten)
echo "1️⃣  Basis-Simulation (Standard):"
echo "   python3 simulate_discussion.py"
echo ""

# Beispiel 2: Kurze Simulation zum Testen
echo "2️⃣  Kurze Test-Simulation (5 Minuten):"
echo "   python3 simulate_discussion.py --duration 5"
echo ""

# Beispiel 3: Lange, ausführliche Simulation
echo "3️⃣  Ausführliche Simulation (30 Minuten):"
echo "   python3 simulate_discussion.py --duration 30"
echo ""

# Beispiel 4: Leiser Modus
echo "4️⃣  Leiser Modus (nur Zusammenfassung):"
echo "   python3 simulate_discussion.py --quiet"
echo ""

# Beispiel 5: Eigene Ausgabedatei
echo "5️⃣  Eigene Ausgabedatei:"
echo "   python3 simulate_discussion.py --output meine_diskussion_$(date +%Y%m%d).txt"
echo ""

# Beispiel 6: Kombination
echo "6️⃣  Kombination (lang + eigene Datei):"
echo "   python3 simulate_discussion.py --duration 30 --output long_discussion.txt"
echo ""

# Frage, welches Beispiel ausgeführt werden soll
echo "Welches Beispiel möchten Sie ausführen? (1-6, oder 'q' zum Beenden)"
read -p "Ihre Wahl: " choice

case $choice in
    1)
        echo "Starte Basis-Simulation..."
        python3 simulate_discussion.py
        ;;
    2)
        echo "Starte kurze Test-Simulation..."
        python3 simulate_discussion.py --duration 5
        ;;
    3)
        echo "Starte ausführliche Simulation..."
        python3 simulate_discussion.py --duration 30
        ;;
    4)
        echo "Starte im leisen Modus..."
        python3 simulate_discussion.py --quiet
        ;;
    5)
        FILENAME="diskussion_$(date +%Y%m%d_%H%M%S).txt"
        echo "Starte mit Ausgabedatei: $FILENAME"
        python3 simulate_discussion.py --output "$FILENAME"
        ;;
    6)
        FILENAME="long_discussion_$(date +%Y%m%d_%H%M%S).txt"
        echo "Starte lange Simulation mit Ausgabedatei: $FILENAME"
        python3 simulate_discussion.py --duration 30 --output "$FILENAME"
        ;;
    q|Q)
        echo "Auf Wiedersehen!"
        exit 0
        ;;
    *)
        echo "Ungültige Auswahl. Bitte wählen Sie 1-6 oder 'q'."
        exit 1
        ;;
esac
