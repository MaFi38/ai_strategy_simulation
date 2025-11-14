#!/usr/bin/env python3
"""
Diskussions-Engine für die KI-Strategie-Simulation
Steuert den Ablauf, Phasen und Interaktionen zwischen Agenten
"""

import time
import random
from typing import List, Dict, Tuple
from agents import Agent, AgentTF, AgentÖ, AgentG, AgentP, AgentFP


class Moderator:
    """Der Leit-Wissenschaftler als Moderator"""

    def __init__(self):
        self.name = "Moderator (Leit-Wissenschaftler)"

    def opening(self) -> str:
        """Eröffnung der Diskussion"""
        return """
═══════════════════════════════════════════════════════════════════════════════
        EXPERTENRAT KI-SONDERWEG - STRATEGISCHE SONDERSITZUNG
═══════════════════════════════════════════════════════════════════════════════

Meine Damen und Herren, willkommen zur entscheidenden Sitzung dieses Gremiums.

Wir wurden einberufen, weil Deutschland vor einem historischen Scheideweg steht.
Die bisherigen Ansätze - 'Plattform Industrie 4.0', 'Trusted AI', 'Gaia-X' - sind
in der Theorie exzellent. Aber die harte Realität ist: Die KI-Adoption im
industriellen Mittelstand, dem Herz unserer Wirtschaft, ist alarmierend gering.

Deutschland droht, seinen industriellen Kern zu verlieren.

Ich möchte Ihnen heute eine analytische Linse anbieten, die der Analyst Dan Wang
entwickelt hat - die 'Gavel vs. Sledgehammer'-These:

→ Die USA sind eine 'LAWYERLY SOCIETY' - dominiert von prozessorientiertem Denken.
  Das System ist besessen von Verfahren, Rechtsstreitigkeiten, dem Schutz des
  Status quo. Dieser 'Richterhammer' (Gavel) blockiert effektiv den Bau physischer
  Infrastruktur. Die Konsequenz: US-KI fokussiert auf das Unkörperliche - Software,
  Dienstleistungen, Large Language Models.

→ China ist ein 'ENGINEERING STATE' - regiert von ergebnisorientierten Technokraten.
  Das System priorisiert physischen Aufbau - Infrastruktur, Fabriken - um jeden Preis.
  Dieser 'Vorschlaghammer' (Sledgehammer) erzwingt Ergebnisse, oft mit immensen
  sozialen Kosten. Die Konsequenz: China-KI fokussiert auf das Körperliche -
  AI + Manufacturing, Robotik, industrielle Optimierung.

→ Und DEUTSCHLAND? Wir sind ein Engineering State - unsere Wirtschaft ist Maschinenbau,
  Automotive, Chemie. Aber wir sind gefangen in einer Lawyerly Society - Bürokratie,
  DSGVO, EU AI Act, Bedenkenträgertum. Dieses 'Gavel'-Korsett lähmt unsere
  'Sledgehammer'-Wirtschaft.

Das ist unser Dilemma.

Die bisherigen Konsens-Vorschläge ('Trusted AI als Gütesiegel') wurden als zu schwach
bewertet. Heute ist unser Auftrag: Eine ECHTE Strategie entwickeln, die Deutschlands
'Engineering'-DNA mit der KI-Realität versöhnt und die 'Gavel'-Blockaden durchbricht
oder umgeht.

Ich bitte Sie um radikales Denken. Konsens ist nicht das Ziel - Wahrheit ist das Ziel.

Beginnen wir mit den Opening Statements.
"""

    def transition_to_conflict(self) -> str:
        """Übergang zur Konfliktphase"""
        return """
────────────────────────────────────────────────────────────────────────────

MODERATOR: Ich höre verschiedene Perspektiven - alle valide. Aber ich höre auch
fundamentale Spannungen:

• Agent T spricht von GESCHWINDIGKEIT - 'der Markt wartet nicht'
• Agent F spricht von NACHHALTIGKEIT - 'ethisch, sicher, langfristig'
• Agent G spricht von MENSCHEN - 'nicht auf deren Kosten'
• Agent P spricht von REALISMUS - 'was ist umsetzbar?'

Diese Positionen sind teilweise INKOMPATIBEL. Lassen Sie mich provozieren:

Ist es möglich, dass wir ALLE falsche Annahmen haben? Dass der 'deutsche Sonderweg',
den wir suchen, eine DISRUPTION des bestehenden Systems erfordert?

Ich möchte jetzt die Diskussion öffnen - reagieren Sie aufeinander. Wo sind die
echten Konflikte?

────────────────────────────────────────────────────────────────────────────
"""

    def introduce_fp(self) -> str:
        """Führt Agent FP ein"""
        return """
────────────────────────────────────────────────────────────────────────────

MODERATOR: Wir haben einen externen Berater eingeladen - Agent FP. Seine Aufgabe
ist explizit NICHT, Konsens zu schaffen. Seine Aufgabe ist es, unsere Grundannahmen
zu dekonstruieren und mit 'First Principles'-Denken neue Lösungsräume zu öffnen.

Das wird unbequem werden. Aber das ist der Punkt.

Agent FP - Sie haben das Wort.

────────────────────────────────────────────────────────────────────────────
"""

    def challenge_agents(self, phase: str) -> str:
        """Fordert Agenten heraus"""
        challenges = {
            "conflict": """
MODERATOR: Ich fordere Sie heraus! Jeder von Ihnen verteidigt sein Revier:
- Agent T: Die Industrie
- Agent F: Die Forschung
- Agent G: Die Arbeitnehmer
- Agent P: Die Politik

Aber WER verteidigt die ZUKUNFT? Wer ist bereit, heilige Kühe zu schlachten?
""",
            "radical": """
MODERATOR: Agent FP hat eine radikale These präsentiert. Sie können nicht einfach
sagen 'das geht nicht' - begründen Sie, WARUM nicht. Oder zeigen Sie, wie eine
abgeschwächte Version funktionieren könnte.

Die Zeit der Allgemeinplätze ist vorbei. Konkret werden!
""",
            "synthesis": """
MODERATOR: Wir nähern uns dem Ende dieser Sitzung. Die Frage ist: Gibt es einen
Kern in Agent FP's Provokation, der - in modifizierter Form - Teil unserer Strategie
werden könnte?

Ich erwarte von jedem von Ihnen eine abschließende Position: Was nehmen Sie mit?
Was haben Sie gelernt? Wo haben Sie Ihre Meinung geändert?
"""
        }
        return challenges.get(phase, "")

    def closing(self, synthesis: str) -> str:
        """Abschluss der Sitzung"""
        return f"""
═══════════════════════════════════════════════════════════════════════════════
                            ABSCHLUSS DER SITZUNG
═══════════════════════════════════════════════════════════════════════════════

MODERATOR: Wir haben heute eine intensive Debatte geführt. Von klassischen Positionen
über Konflikte bis zu radikalen Dekonstruktionen.

{synthesis}

Das Protokoll dieser Sitzung geht an die Bundesregierung. Es ist kein Konsens-Papier.
Es ist ein Dokument der Wahrheit - unbequem, radikal, aber ehrlich.

Deutschland steht vor der Wahl: Entweder wir finden einen Weg, unser 'Gavel'-System
flexibler zu machen, oder wir akzeptieren, dass andere - mit ihren 'Sledgehammers' -
die Zukunft bestimmen werden.

Die Sitzung ist geschlossen.

═══════════════════════════════════════════════════════════════════════════════
"""


class DiscussionEngine:
    """Steuert den gesamten Diskussionsablauf"""

    def __init__(self, verbose: bool = True):
        self.moderator = Moderator()
        self.agents: List[Agent] = [
            AgentTF(),
            AgentÖ(),
            AgentG(),
            AgentP(),
            AgentFP()
        ]
        self.verbose = verbose
        self.discussion_log: List[Tuple[str, str]] = []
        self.phase = "opening"

    def _calculate_rounds(self, target_duration_minutes: int) -> Dict:
        """
        Berechnet Diskussionsparameter basierend auf Zieldauer

        Args:
            target_duration_minutes: Gewünschte Dauer in Minuten

        Returns:
            Dictionary mit rounds, interactions und reactions
        """
        if target_duration_minutes < 10:
            # Kurze Diskussion (~40-50 Beiträge)
            return {
                "initial_rounds": 2,
                "initial_interactions": 3,
                "fp_reactions_1": 2,
                "fp_reactions_2": 2,
                "fp_reactions_3": 3,
                "final_rounds": 1,
                "final_interactions": 3
            }
        elif target_duration_minutes < 25:
            # Standard Diskussion (~60-70 Beiträge)
            return {
                "initial_rounds": 3,
                "initial_interactions": 4,
                "fp_reactions_1": 4,
                "fp_reactions_2": 4,
                "fp_reactions_3": 5,
                "final_rounds": 2,
                "final_interactions": 5
            }
        elif target_duration_minutes < 40:
            # Lange Diskussion (~100-120 Beiträge)
            return {
                "initial_rounds": 5,
                "initial_interactions": 5,
                "fp_reactions_1": 5,
                "fp_reactions_2": 5,
                "fp_reactions_3": 6,
                "final_rounds": 3,
                "final_interactions": 6
            }
        else:
            # Sehr lange Diskussion (~150-200 Beiträge)
            return {
                "initial_rounds": 7,
                "initial_interactions": 6,
                "fp_reactions_1": 6,
                "fp_reactions_2": 6,
                "fp_reactions_3": 8,
                "final_rounds": 5,
                "final_interactions": 7
            }


    def log(self, speaker: str, statement: str):
        """Protokolliert einen Diskussionsbeitrag"""
        self.discussion_log.append((speaker, statement))
        if self.verbose:
            self._print_statement(speaker, statement)

    def _print_statement(self, speaker: str, statement: str):
        """Formatierte Ausgabe eines Statements"""
        print(f"\n{'='*80}")
        print(f"🎤 {speaker}")
        print(f"{'='*80}")
        print(statement)
        print()
        time.sleep(0.5)  # Kleine Pause für Lesbarkeit

    def run_simulation(self, target_duration_minutes: int = 20) -> str:
        """
        Führt die komplette Simulation durch

        Args:
            target_duration_minutes: Zieldauer in Minuten (Simulation passt Länge an)

        Returns:
            Vollständiges Protokoll als String
        """
        # Berechne Parameter basierend auf Zieldauer
        params = self._calculate_rounds(target_duration_minutes)

        print(f"\n🚀 Starte KI-Strategie-Simulation (Zieldauer: {target_duration_minutes} Minuten)...")
        print(f"📊 Diskussionsumfang: ", end="")
        if target_duration_minutes < 10:
            print("Kurz (~40-50 Beiträge)")
        elif target_duration_minutes < 25:
            print("Standard (~60-70 Beiträge)")
        elif target_duration_minutes < 40:
            print("Lang (~100-120 Beiträge)")
        else:
            print("Sehr lang (~150-200 Beiträge)")
        print("=" * 80)

        start_time = time.time()

        # PHASE 1: Eröffnung
        self.log("MODERATOR", self.moderator.opening())

        # PHASE 2: Opening Statements (ohne Agent FP)
        self.phase = "opening"
        for agent in self.agents[:-1]:  # Alle außer Agent FP
            statement = agent.get_opening_statement()
            self.log(agent.name, statement)
            time.sleep(0.3)

        # PHASE 3: Erste Diskussionsrunde
        self.log("MODERATOR", self.moderator.transition_to_conflict())
        self.phase = "conflict"

        # Mehrere Runden von Antworten/Reaktionen (dynamisch skaliert)
        self._run_discussion_rounds(
            rounds=params["initial_rounds"],
            interactions_per_round=params["initial_interactions"]
        )

        # PHASE 4: Agent FP Einführung
        self.log("MODERATOR", self.moderator.introduce_fp())

        # Agent FP's Dekonstruktion - Phase für Phase
        agent_fp = self.agents[-1]

        # Phase 1: Fundamentale Wahrheiten (dynamisch skaliert)
        self.log(agent_fp.name, agent_fp.get_deconstruction_phase1())
        self._get_reactions_to_fp(phase=1, num_reactions=params["fp_reactions_1"])

        # Phase 2: Annahmen-Check (dynamisch skaliert)
        time.sleep(0.5)
        self.log(agent_fp.name, agent_fp.get_deconstruction_phase2())
        self._get_reactions_to_fp(phase=2, num_reactions=params["fp_reactions_2"])

        # Phase 3: Neuaufbau (dynamisch skaliert)
        time.sleep(0.5)
        self.log(agent_fp.name, agent_fp.get_deconstruction_phase3())
        self._get_reactions_to_fp(phase=3, num_reactions=params["fp_reactions_3"])

        # Phase 4: Implementierung
        time.sleep(0.5)
        reactions = self._collect_recent_reactions()
        self.log(agent_fp.name, agent_fp.get_deconstruction_phase4(reactions))

        # PHASE 5: Finale Diskussion (dynamisch skaliert)
        self.log("MODERATOR", self.moderator.challenge_agents("radical"))
        self.phase = "radical"
        self._run_discussion_rounds(
            rounds=params["final_rounds"],
            interactions_per_round=params["final_interactions"]
        )

        # PHASE 6: Synthese
        self.log("MODERATOR", self.moderator.challenge_agents("synthesis"))
        self.phase = "synthesis"

        # Finale Statements
        for agent in self.agents:
            final_statement = self._generate_final_statement(agent)
            self.log(agent.name, final_statement)
            time.sleep(0.3)

        # Abschluss
        synthesis = self._generate_synthesis()
        self.log("MODERATOR", self.moderator.closing(synthesis))

        # Zeitmessung
        duration = (time.time() - start_time) / 60
        print(f"\n✅ Simulation abgeschlossen! Dauer: {duration:.1f} Minuten")
        print(f"📊 Gesamtzahl Diskussionsbeiträge: {len(self.discussion_log)}")

        return self._generate_full_protocol()

    def _run_discussion_rounds(self, rounds: int, interactions_per_round: int):
        """Führt mehrere Diskussionsrunden durch"""
        for round_num in range(rounds):
            for _ in range(interactions_per_round):
                # Zufällige Auswahl von zwei Agenten für Interaktion
                speaker = random.choice(self.agents[:-1] if self.phase != "radical" else self.agents)
                target = random.choice([a for a in self.agents if a != speaker and a.name != "Agent FP"])

                # Generiere Kontext
                context = {
                    "phase": self.phase,
                    "round": round_num,
                    "recent_topics": self._get_recent_topics()
                }

                # Hole Antwort
                statement = speaker.respond_to(target.name, "general discussion", context)
                self.log(speaker.name, statement)

                # Emotionale Dynamik
                speaker.adjust_emotion(
                    delta_frustration=random.randint(-5, 10),
                    delta_conviction=random.randint(-10, 5)
                )

                time.sleep(0.2)

    def _get_reactions_to_fp(self, phase: int, num_reactions: int):
        """Sammelt Reaktionen der anderen Agenten auf Agent FP"""
        reactions_map = {
            1: {  # Nach Phase 1: Fundamentale Wahrheiten
                "Agent TF": """Moment... Sie nennen den Mittelständler das 'Nadelöhr'? Das höre ich zum
ersten Mal so direkt. Aber... es stimmt. Ich kenne Dutzende solcher Fälle - viele
Eigentümer WOLLEN nicht digitalisieren. Aus Angst, aus Überforderung. Ist brutal, aber wahr.""",

                "Agent Ö": """Ihre 'Wahrheiten' sind ökonomisch interessant. Ja, der Mittelständler ist
risikoscheu - das ist rational bei asymmetrischer Information! Aber Sie ignorieren institutionelles
Wissen und Pfadabhängigkeiten - das lässt sich nicht einfach 'extrahieren'.""",

                "Agent G": """'Wahrheit 2' - ja, das Wissen ist in Facharbeitern. Endlich sagt das jemand!
Aber Ihre Richtung macht mir Angst. Wenn Sie die Menschen vom Unternehmen 'abkoppeln' wollen...""",

                "Agent P": """First Principles - das ist Silicon Valley-Sprache. Ich bin skeptisch. Aber:
Die Frage 'Warum ist der Mittelständler die Konstante?' ist... berechtigt. Unbequem, aber berechtigt."""
            },
            2: {  # Nach Phase 2: Annahmen-Check
                "Agent TF": """STOPP. Sie greifen meine Grundannahme an - dass der Mittelständler der Vektor
sein muss. Aber was ist die Alternative? 1000 Start-ups, die das Rad neu erfinden?
Das ist Chaos, keine Strategie!""",

                "Agent Ö": """Ihre Annahmen-Kritik ist methodisch interessant. Tatsächlich frage ich mich auch:
Warum optimieren wir immer INNERHALB des Systems Mittelstand? Vielleicht ist laterale Disruption
ökonomisch effizienter als inkrementelle Transformation?""",

                "Agent G": """'Anstellungsverhältnis ist 20. Jahrhundert-Denken' - das ist eine PROVOKATION!
Das Anstellungsverhältnis schützt Menschen vor Ausbeutung! Ihr 'Gründer-Modell' - das ist
Gig-Economy, das ist Prekarisierung!""",

                "Agent P": """'Das System ist das Problem' - wenn ich das im Bundestag sage, werde ich
ausgepfiffen. Aber... unter uns... manchmal denke ich das auch. Unser System IST langsam.
Nur: Wie ändert man ein System von innen?"""
            },
            3: {  # Nach Phase 3: Neuaufbau
                "Agent TF": """'Meister-Forscher-Tandems'... 'Industrial AI App Store'... das ist...
eigentlich... brillant? Sie umgehen ALLE Blockaden. Kein risikoScheuer Eigentümer, kein
langwieriges Gaia-X-Komitee. Direct to market. Aber - wer schützt IP? Wer verhindert Wildwuchs?""",

                "Agent Ö": """Ökonomisch ist das faszinierend! Sie schaffen einen NEUEN MARKT für implizites
Wissen. Das ist creative destruction à la Schumpeter. Aber: Die Transaktionskosten? Die
Koordination? Wie verhindern Sie Marktversagen bei 1000 unkoordinierten Akteuren?""",

                "Agent G": """DAS IST ENTEIGNUNG! Der Facharbeiter hat sein Wissen IM UNTERNEHMEN erworben,
am Arbeitsplatz, bezahlt vom Arbeitgeber. Sie sagen jetzt 'das gehört dem Arbeiter' - rechtlich
ist das HOCHPROBLEMATISCH! Und sozial: Was ist mit 50-jährigen ohne Gründer-Gen?""",

                "Agent P": """Sie wollen Subventionen stoppen? Für den Mittelstand? Die CDU/CSU würde TOBEN.
Das ist politischer Selbstmord. ABER... ein Pilot? 100 Tandems? 'Innovation Lab'? DAS könnte ich
vielleicht verkaufen... unter dem Radar...""",

                "Agent FP": """Ich höre Widerstand - gut. Aber niemand widerlegt die LOGIK. Sie sagen 'geht nicht',
aber nicht 'ist falsch'. Das ist aufschlussreich."""
            }
        }

        for agent_name, reaction in list(reactions_map.get(phase, {}).items())[:num_reactions]:
            self.log(agent_name, reaction)
            time.sleep(0.3)

    def _collect_recent_reactions(self) -> Dict:
        """Sammelt die letzten Reaktionen für Kontext"""
        recent = self.discussion_log[-10:]
        return {
            "mentioned_social": any("sozial" in s[1].lower() for s in recent),
            "mentioned_mittelstand": any("mittelstand" in s[1].lower() for s in recent)
        }

    def _get_recent_topics(self) -> List[str]:
        """Extrahiert kürzlich diskutierte Themen"""
        topics = ["Gaia-X", "Mittelstand", "Transfer", "Geschwindigkeit", "Mitbestimmung"]
        return random.sample(topics, 2)

    def _generate_final_statement(self, agent: Agent) -> str:
        """Generiert abschließendes Statement eines Agenten"""
        final_statements = {
            "Agent TF": """Ich nehme mit: Das Transfer-Problem ist größer als gedacht. Der Mittelständler IST
teilweise das Nadelöhr - das schmerzt zuzugeben. Agent FP's Ansatz ist radikal, vielleicht
zu radikal. Aber die IDEE, Forscher und Praktiker DIREKT zu verbinden und Wissen zu monetarisieren,
hat Charme. Vielleicht nicht als Hauptstrategie, aber als Experimentierfeld? Ich wäre dabei.""",

            "Agent Ö": """Volkswirtschaftlich ist Agent FP's Ansatz interessant: Creative Destruction,
neue Märkte, Wissensmonetarisierung. Aber ich sehe auch Risiken: Transaktionskosten, Koordinationsprobleme,
Skalierungsfragen. Mein Vorschlag: Pilot mit 100-200 Tandems, begleitet von ökonomischer Evaluation.
Messen wir Produktivitätseffekte, Spillovers, Wohlfahrtswirkung. Dann entscheiden wir datenbasiert.""",

            "Agent G": """Ich bleibe skeptisch. Sehr skeptisch. ABER: Wenn es FREIWILLIG ist, wenn es
Rückkehrrechte gibt, wenn soziale Absicherung da ist - dann könnte ich einen PILOT akzeptieren.
Unter einer Bedingung: Gewerkschaften sind im Beirat. Wir schützen die Teilnehmer.""",

            "Agent P": """Politisch ist das ein Minenfeld. Aber... vielleicht IST das der 'Deutsche Sonderweg':
Nicht entweder Top-down ODER Bottom-up, sondern UND. Die 5 Milliarden aufteilen:
- 3 Mrd. für klassische Infrastruktur (Gaia-X, Transfer, Qualifizierung)
- 2 Mrd. für radikale Experimente (Tandems, Sandboxes, Wagniskapital)
Das könnte ich verkaufen.""",

            "Agent FP": """Sie haben verstanden: Es geht nicht darum, mein Modell 1:1 umzusetzen.
Es geht darum, Denkmuster zu brechen. Wenn Sie jetzt über 'Pilot', 'Sandbox', 'Freiwilligkeit'
reden - dann hat die Dekonstruktion funktioniert. Sie denken anders als vor 3 Stunden.
Mission accomplished."""
        }
        return final_statements.get(agent.name, "Kein abschließendes Statement.")

    def _generate_synthesis(self) -> str:
        """Generiert Synthese der Diskussion"""
        return """
SYNTHESE DES MODERATORS:

Diese Sitzung hat gezeigt:

1) KONSENS: Das bestehende System ('Gavel'-Bürokratie + risikoScheuer Mittelstand) ist zu langsam.

2) DISSENS: Wie radikal die Lösung sein darf/muss.
   - Agent G fordert soziale Absicherung
   - Agent F fordert Qualitätssicherung
   - Agent T fordert Geschwindigkeit
   - Agent P fordert politische Machbarkeit

3) NEUE HYPOTHESE (Agent FP):
   'Meister-Forscher-Tandems' als Bottom-up-Innovationsmechanismus.
   - Umgeht institutionelle Blockaden
   - Monetarisiert implizites Wissen
   - Beschleunigt Transfer

   EINWÄNDE: Sozial riskant, rechtlich komplex, qualitativ unsicher.
   POTENZIAL: Als PILOT (100-200 Tandems) mit Absicherung und Evaluation machbar.

4) KOMPROMISS-LINIE:
   • 60% klassische Strategie (Trusted AI, Gaia-X, Qualifizierung)
   • 40% experimentelle Strategie (Tandems, Sandboxes, Risikokapital)

   Dies kombiniert 'Gavel'-Sicherheit mit 'Sledgehammer'-Geschwindigkeit.

5) OFFENE FRAGEN:
   - Wer trägt das Risiko bei gescheiterten Tandems?
   - Wie skaliert man erfolgreiche Modelle?
   - Wie verhindert man Wissens-Abfluss ins Ausland?

Empfehlung: Kabinettvorlage für Pilotprogramm 'KI-Gründer-Tandems' (200 Mio. €, 2 Jahre).
"""

    def _generate_full_protocol(self) -> str:
        """Generiert vollständiges Sitzungsprotokoll"""
        protocol = """
╔═══════════════════════════════════════════════════════════════════════════════╗
║                    SITZUNGSPROTOKOLL - EXPERTENRAT KI-SONDERWEG               ║
║                                                                               ║
║  Datum: """ + time.strftime("%d.%m.%Y") + """                                                              ║
║  Dauer: """ + f"{len(self.discussion_log)} Diskussionsbeiträge".ljust(67) + """║
║  Status: VERTRAULICH - NUR FÜR BUNDESREGIERUNG                                ║
╚═══════════════════════════════════════════════════════════════════════════════╝

"""
        for speaker, statement in self.discussion_log:
            protocol += f"\n{'='*80}\n"
            protocol += f"{speaker}\n"
            protocol += f"{'='*80}\n"
            protocol += f"{statement}\n"

        protocol += f"\n{'='*80}\n"
        protocol += "ENDE DES PROTOKOLLS\n"
        protocol += f"{'='*80}\n"

        return protocol

    def save_protocol(self, filename: str = "protokoll_ki_strategie.txt"):
        """Speichert das Protokoll in eine Datei"""
        protocol = self._generate_full_protocol()
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(protocol)
        print(f"✅ Protokoll gespeichert: {filename}")
