#!/usr/bin/env python3
"""
KI-Strategie-Simulation: Deutschland's AI-Dilemma
==================================================

Simuliert eine strategische Expertenrats-Sitzung zur Entwicklung einer
radikalen KI-Strategie für Deutschland.

Basiert auf Dan Wang's "Gavel vs. Sledgehammer" These:
- USA: Lawyerly Society (prozessorientiert, Software-fokussiert)
- China: Engineering State (ergebnisorientiert, Manufacturing-fokussiert)
- Deutschland: Engineering Economy in Lawyerly Implementation (das Dilemma)

Teilnehmer:
- Moderator (Leit-Wissenschaftler)
- Agent T (Technologe - Maschinenbau/VDMA)
- Agent F (Forscherin - DFKI/Fraunhofer)
- Agent G (Gewerkschafter - DGB)
- Agent P (Politikerin - BMWK/BMBF)
- Agent FP (First Principles Dekonstrukteur - Externer Disruptor)

Usage:
    python simulate_discussion.py [--duration MINUTES] [--output FILE] [--quiet]

    --duration: Zieldauer der Simulation in Minuten (default: 20)
    --output: Ausgabedatei für Protokoll (default: protokoll_ki_strategie.txt)
    --quiet: Reduzierte Konsolenausgabe
"""

import argparse
import sys
import time
from discussion_engine import DiscussionEngine


def parse_arguments():
    """Parse Kommandozeilenargumente"""
    parser = argparse.ArgumentParser(
        description='Simuliert strategische KI-Expertenrats-Diskussion für Deutschland',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Beispiele:
  %(prog)s                           # Standard: 20 Minuten Simulation
  %(prog)s --duration 30              # 30 Minuten Simulation
  %(prog)s --output mein_protokoll.txt # Eigene Ausgabedatei
  %(prog)s --quiet                    # Reduzierte Ausgabe
        """
    )

    parser.add_argument(
        '--duration',
        type=int,
        default=20,
        metavar='MINUTES',
        help='Zieldauer der Simulation in Minuten (default: 20)'
    )

    parser.add_argument(
        '--output',
        type=str,
        default='protokoll_ki_strategie.txt',
        metavar='FILE',
        help='Ausgabedatei für das Sitzungsprotokoll (default: protokoll_ki_strategie.txt)'
    )

    parser.add_argument(
        '--quiet',
        action='store_true',
        help='Reduzierte Konsolenausgabe (nur Zusammenfassung)'
    )

    parser.add_argument(
        '--version',
        action='version',
        version='%(prog)s 1.0 - KI-Strategie-Simulation'
    )

    return parser.parse_args()


def print_banner():
    """Zeigt Willkommens-Banner"""
    banner = r"""
╔══════════════════════════════════════════════════════════════════════════════╗
║                                                                              ║
║           🇩🇪 KI-STRATEGIE-SIMULATION: DEUTSCHLAND'S AI-DILEMMA 🇩🇪          ║
║                                                                              ║
║                   Gavel vs. Sledgehammer: Der deutsche Weg                   ║
║                                                                              ║
╚══════════════════════════════════════════════════════════════════════════════╝

    Teilnehmer:
    • Moderator (Leit-Wissenschaftler)
    • Agent T - Der Technologe (Maschinenbau/VDMA)
    • Agent F - Die Forscherin (DFKI/Fraunhofer)
    • Agent G - Der Gewerkschafter (DGB)
    • Agent P - Die Politikerin (BMWK/BMBF)
    • Agent FP - Der First Principles Dekonstrukteur

    Basiert auf Dan Wang's These:
    → USA = Lawyerly Society (Gavel) → Software/LLMs
    → China = Engineering State (Sledgehammer) → Manufacturing/AI
    → Deutschland = Engineering Economy im Gavel-Korsett = DILEMMA

"""
    print(banner)


def print_progress_indicator(current_phase: str):
    """Zeigt Fortschrittsindikator"""
    phases = {
        "opening": "🎬 PHASE 1: Eröffnung & Opening Statements",
        "conflict": "⚔️  PHASE 2: Konflikt & Debatte",
        "deconstruction": "🔨 PHASE 3: Agent FP - Dekonstruktion",
        "radical": "💥 PHASE 4: Radikale Diskussion",
        "synthesis": "🎯 PHASE 5: Synthese & Abschluss"
    }

    if current_phase in phases:
        print(f"\n{'='*80}")
        print(f"  {phases[current_phase]}")
        print(f"{'='*80}\n")


def main():
    """Hauptfunktion"""
    args = parse_arguments()

    # Banner
    if not args.quiet:
        print_banner()
        time.sleep(1)

    print(f"⚙️  Konfiguration:")
    print(f"   • Zieldauer: {args.duration} Minuten")
    print(f"   • Ausgabedatei: {args.output}")
    print(f"   • Modus: {'Leise' if args.quiet else 'Ausführlich'}")
    print()

    # Bestätigung
    if not args.quiet:
        print("🔄 Starte Simulation in 3 Sekunden...")
        for i in range(3, 0, -1):
            print(f"   {i}...")
            time.sleep(1)
        print()

    try:
        # Engine initialisieren
        engine = DiscussionEngine(verbose=not args.quiet)

        # Simulation durchführen
        start_time = time.time()

        if args.quiet:
            print("⏳ Simulation läuft (dies kann einige Minuten dauern)...")

        protocol = engine.run_simulation(target_duration_minutes=args.duration)

        duration = (time.time() - start_time) / 60

        # Protokoll speichern
        engine.save_protocol(args.output)

        # Zusammenfassung
        print("\n" + "="*80)
        print("📊 ZUSAMMENFASSUNG")
        print("="*80)
        print(f"✅ Simulation erfolgreich abgeschlossen!")
        print(f"⏱️  Tatsächliche Dauer: {duration:.1f} Minuten")
        print(f"💬 Diskussionsbeiträge: {len(engine.discussion_log)}")
        print(f"📄 Protokoll gespeichert: {args.output}")
        print()

        # Kernerkenntnisse
        print("🎯 KERNERKENNTNISSE:")
        print("   1. Das 'Gavel'-Korsett (Bürokratie) lähmt die Engineering-Economy")
        print("   2. Der Mittelstand ist teilweise selbst das Nadelöhr (risikoscheu)")
        print("   3. Radikale Idee: Meister-Forscher-Tandems als Bottom-up-Innovation")
        print("   4. Kompromiss: 60% klassisch + 40% experimentell")
        print("   5. Empfehlung: Pilot mit 100-200 Tandems, wissenschaftlich evaluiert")
        print()

        print(f"📖 Vollständiges Protokoll: {args.output}")
        print("="*80)

        return 0

    except KeyboardInterrupt:
        print("\n\n⚠️  Simulation durch Benutzer abgebrochen.")
        return 1

    except Exception as e:
        print(f"\n\n❌ FEHLER: {str(e)}", file=sys.stderr)
        import traceback
        traceback.print_exc()
        return 1


if __name__ == "__main__":
    sys.exit(main())
