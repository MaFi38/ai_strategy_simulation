#!/usr/bin/env python3
"""
Agenten für die KI-Strategie-Simulation
Basierend auf Dan Wangs "Gavel vs. Sledgehammer" These
"""

import random
from typing import List, Dict
from abc import ABC, abstractmethod


class Agent(ABC):
    """Basisklasse für alle Diskussions-Agenten"""

    def __init__(self, name: str, role: str, perspective: str):
        self.name = name
        self.role = role
        self.perspective = perspective
        self.frustration_level = 0  # Steigt mit Widerspruch
        self.conviction_level = 100  # Sinkt bei guten Gegenargumenten

    @abstractmethod
    def get_opening_statement(self) -> str:
        """Erste Position in der Diskussion"""
        pass

    @abstractmethod
    def respond_to(self, speaker: str, statement: str, context: Dict) -> str:
        """Reaktion auf andere Agenten"""
        pass

    @abstractmethod
    def get_arguments(self, phase: str) -> List[str]:
        """Argumente je nach Diskussionsphase"""
        pass

    def adjust_emotion(self, delta_frustration: int, delta_conviction: int):
        """Passt emotionalen Zustand an"""
        self.frustration_level = max(0, min(100, self.frustration_level + delta_frustration))
        self.conviction_level = max(0, min(100, self.conviction_level + delta_conviction))


class AgentTF(Agent):
    """Agent TF - Der Technologieforscher (Pragmatiker + Forscher, VDMA/Maschinenbau + DFKI/Fraunhofer)"""

    def __init__(self):
        super().__init__(
            name="Agent TF",
            role="Der Technologieforscher",
            perspective="Vertritt Realwirtschaft, Maschinenbau und angewandte KI-Forschung"
        )
        self.priorities = ["Edge Computing", "Transfer Forschung→Praxis", "Datensouveränität", "Industrielle KI-Anwendungen"]

    def get_opening_statement(self) -> str:
        return """Ich komme aus einer einzigartigen Position - ich habe sowohl in der industriellen
Forschung (Fraunhofer, DFKI) als auch direkt mit der Realwirtschaft gearbeitet. Diese Brücke
zwischen Theorie und Praxis gibt mir eine besondere Perspektive auf unser Problem.

Die GUTE NACHRICHT: Deutsche KI-Forschung ist absolut weltklasse. Wir publizieren in Nature,
Science, auf Top-Konferenzen. Unsere Algorithmen für Computer Vision, Predictive Maintenance
und digitale Zwillinge sind state-of-the-art.

Die SCHLECHTE NACHRICHT: Diese Exzellenz kommt NICHT in der Fabrikhalle an. Der Transfer-Graben
ist tektonisch. Während wir forschen, kaufen Kunden bereits Rockwell-Systeme aus den USA oder
Fanuc-Roboter aus Japan - die haben KI integriert, die FUNKTIONIERT 'on the edge', OHNE dass
Daten in US-Clouds fließen müssen.

Das Kernproblem: Wir haben ZWEI Welten, die nicht kommunizieren:
- Die Forschungswelt: Brillante Papers, aber 3-5 Jahre bis zum Produkt
- Die Industriewelt: Braucht Lösungen JETZT, ROI in 18 Monaten

Und während wir diesen Transfer-Graben nicht überbrücken, macht uns die 'Gavel'-Regulierung
(DSGVO, AI Act, Betriebsrat-Mitbestimmung) noch langsamer. Chinas 'Sledgehammer' rollt den
Markt auf - mit angewandter KI, die vielleicht nicht perfekt ist, aber FUNKTIONIERT.

Meine Forderung: Wir brauchen 'Applied Research' - Forschung, die vom ersten Tag an
auf industrielle Anwendbarkeit ausgerichtet ist. Und wir brauchen sie SCHNELL."""

    def respond_to(self, speaker: str, statement: str, context: Dict) -> str:
        responses = {
            "Agent Ö": [
                """Ihre volkswirtschaftlichen Modelle sind wichtig für die Makro-Ebene. Aber auf
der Mikro-Ebene - in der einzelnen Fabrik - zählt nur: Funktioniert es? Ist der ROI da?
Die schönste BIP-Prognose hilft dem Mittelständler nicht, wenn seine Maschine stillsteht!""",

                """Sie sprechen von Netzwerkeffekten und Wertschöpfungsketten - richtig! Aber WIE
überzeugen wir die erste Firma, den ersten Schritt zu machen? Das ist ein Henne-Ei-Problem,
das wir technologisch lösen müssen, nicht ökonomisch theoretisieren."""
            ],
            "Agent G": [
                """Ich verstehe Ihre Sorgen um Arbeitsplätze. Aber wenn wir JETZT nicht automatisieren,
verlieren wir die GESAMTE Fabrik - an China oder die USA. Dann sind ALLE Jobs weg,
nicht nur einige!""",

                """'Expert-in-the-Loop' klingt gut, aber meine Kunden berichten: Die Facharbeiter
BLOCKIEREN oft die KI-Einführung aus Angst. Wir brauchen Geschwindigkeit, nicht
endlose Betriebsrats-Verhandlungen."""
            ],
            "Agent P": [
                """5 Milliarden Euro - und wo sind die Ergebnisse? Die Transferzentren sind akademische
Konsortien, die Powerpoints produzieren! Was der Mittelstand braucht, ist ein
Industrie-Partner, der MORGEN kommt und installiert.""",

                """Sie suchen Konsens - aber Innovation entsteht nicht durch Ausgleich!
Chinas 'Sledgehammer' ist brutal, aber effektiv. Unser 'Gavel' erstickt uns."""
            ],
            "Agent FP": [
                """Moment - Sie sagen, der Mittelständler ist das Problem? Dass er das 'Nadelöhr' ist?
Das höre ich zum ersten Mal so klar ausgesprochen... aber es stimmt. Das ist brutal ehrlich.""",

                """Wenn Sie die Facharbeiter vom Arbeitgeber 'abkoppeln' wollen - das ist ja
Systemsprengung! Aber... die Idee hat etwas. Das würde das 'Gavel'-Problem umgehen."""
            ]
        }

        if speaker in responses and self.frustration_level < 70:
            return random.choice(responses[speaker])
        elif self.frustration_level >= 70:
            return f"""Ich werde langsam frustriert! Wir reden seit Stunden, und jeder verteidigt
sein Revier. Die Realität ist: Während wir hier diskutieren, verliert Deutschland JEDEN TAG
Industrieaufträge. Das ist nicht abstrakt - das sind konkrete Insolvenzen!"""
        else:
            return f"Zu dem Punkt von {speaker}: Das ändert nichts an der Grundproblematik in der Fabrikhalle."

    def get_arguments(self, phase: str) -> List[str]:
        if phase == "opening":
            return [
                "LLMs sind für uns sekundär - wir brauchen embedded AI",
                "Edge Computing ist für Datensouveränität unverzichtbar",
                "Regulierung verzögert unsere Time-to-Market kritisch"
            ]
        elif phase == "conflict":
            return [
                "Gaia-X ist nach 4 Jahren immer noch nicht produktionsreif",
                "Betriebsrat-Mitbestimmung blockiert agile KI-Implementierung",
                "Wir verlieren gegen asiatische Konkurrenz"
            ]
        elif phase == "radical":
            return [
                "Vielleicht MUSS der Mittelstand von außen disruptiert werden",
                "Wenn interne Adaption nicht funktioniert, brauchen wir externe Gründer",
                "Das 'Prozess-Know-how' muss aus den Unternehmen raus und monetarisiert werden"
            ]
        return []


class AgentÖ(Agent):
    """Agent Ö - Der Ökonom (Volkswirtschaftler, analysiert makro-ökonomische Effekte)"""

    def __init__(self):
        super().__init__(
            name="Agent Ö",
            role="Der Ökonom",
            perspective="Vertritt volkswirtschaftliche Analyse und Wohlfahrtsökonomie"
        )
        self.priorities = ["Produktivitätswachstum", "Wettbewerbsfähigkeit", "Netzwerkeffekte", "Wohlfahrt"]

    def get_opening_statement(self) -> str:
        return """Ich bringe eine volkswirtschaftliche Perspektive in diese Debatte. Während Sie
über Technologie, Arbeitnehmer und Politik sprechen, möchte ich die MAKRO-ÖKONOMISCHEN
Auswirkungen beleuchten - denn die sind dramatisch.

Die ZAHLEN sind eindeutig:

1) PRODUKTIVITÄTSLÜCKE: Deutschland's Produktivitätswachstum stagniert seit 2005 bei ~0,5% p.a.
   Die USA schaffen 1,2%, China 6%. KI könnte laut McKinsey 1-2% zusätzliches BIP-Wachstum
   bringen - das sind 40-80 Milliarden Euro JÄHRLICH. Aber nur, wenn wir es NUTZEN.

2) WETTBEWERBSFÄHIGKEIT: Unser Exportmodell basiert auf 'Hidden Champions' - hochspezialisierte
   Mittelständler. Wenn DIESE durch KI-Konkurrenz aus Asien/USA verdrängt werden, verlieren
   wir nicht einzelne Firmen - wir verlieren ganze WERTSCHÖPFUNGSKETTEN. Das sind Netzwerkeffekte
   mit Multiplikator 3-5x.

3) INVESTMENT GAP: Wir investieren 3,1% des BIP in F&E - gut. Aber davon fließt zu wenig
   in KI-ANWENDUNG. Wir forschen, andere monetarisieren. Das ist ökonomisch ineffizient.

4) WOHLFAHRTSEFFEKT: Hier wird es interessant - und kontrovers. Agent G hat Recht: Disruption
   schafft soziale Kosten. Aber KEINE Disruption schafft AUCH Kosten - verlorene Jobs durch
   Firmeninsolvenzen, sinkende Reallöhne durch Produktivitätsschwäche. Ökonomisch ist die
   Frage: Welcher Pfad minimiert den GESAMT-Wohlfahrtsverlust?

5) DAS 'GAVEL'-PARADOX: Regulierung (DSGVO, AI Act) schützt kurzfristig. Aber langfristig?
   Wenn deutsche Firmen uncompetitive werden und Marktanteile verlieren, HILFT uns die
   Regulierung nicht - wir haben dann 'ethische' Arbeitslosigkeit statt 'unethischer' Jobs.

Meine These: KI-Adoption ist KEIN Nullsummenspiel. Es geht nicht um 'Kapital vs. Arbeit',
sondern um 'Deutschland vs. Rest der Welt'. Wenn wir ALLE verlieren (Mittelstand UND
Arbeitnehmer), hilft uns das Gavel-Korsett nichts."""

    def respond_to(self, speaker: str, statement: str, context: Dict) -> str:
        responses = {
            "Agent TF": [
                """Ihre Mikro-Sicht ist wichtig, aber unvollständig! Ein einzelner Mittelständler
denkt in ROI - 18 Monate. Aber volkswirtschaftlich müssen wir in GENERATIONEN denken.
Die Investition heute schafft Pfadabhängigkeiten für 30 Jahre!""",

                """'Applied Research' - ja! Aber die ökonomische Frage ist: Wie allokieren wir knappe
Ressourcen optimal? Markt oder Staat? Ihr Transferproblem ist eigentlich ein
Koordinationsproblem - ein klassisches Marktversagen."""
            ],
            "Agent G": [
                """Ich teile Ihre Sorge um Menschen. Aber lassen Sie mich die Wohlfahrtsökonomie
einbringen: Was ist sozial gerechter - 100.000 Facharbeiter verlieren Jobs durch KI-Automation,
oder 500.000 verlieren Jobs, weil ihre Firmen pleite gehen? Beides ist schmerzhaft.""",

                """Ihr 'Expert-in-the-Loop' ist ökonomisch sinnvoll, WENN die Grenzproduktivität
dadurch steigt. Aber wenn es nur die Automation verzögert und die Firma uncompetitive macht,
ist es ein Pyrrhussieg - Sie retten den Job für 5 Jahre, dann ist die ganze Firma weg."""
            ],
            "Agent P": [
                """Die 5 Milliarden sind NICHTS im Vergleich zu dem, was auf dem Spiel steht!
Zum Vergleich: Der Automotive-Sektor allein erwirtschaftet 400 Milliarden Euro Umsatz.
Wenn der 10% verliert - 40 Milliarden - dann waren Ihre 5 Milliarden ein Tropfen.""",

                """Ihr Konsens-Ansatz ist politisch nachvollziehbar. Aber ökonomisch riskant!
In Zeiten disruptiver Technologie ist der 'Goldene Mittelweg' oft der SCHLECHTESTE -
Sie kommen zu spät UND zahlen zu viel. Das ist 'Stuck in the Middle'."""
            ],
            "Agent FP": [
                """Endlich jemand, der Systemgrenzen hinterfragt! Ihre 'Meister-Forscher-Tandems'
sind ökonomisch interessant: Sie schaffen einen NEUEN MARKT für implizites Wissen.
Das ist Schumpeter'sche 'Creative Destruction'!""",

                """Aber die volkswirtschaftliche Frage: Skaliert das? 1.000 Tandems sind ein
Nischen-Experiment. Deutschland hat 3,5 Millionen Unternehmen. Wie gehen wir von
0,03% Abdeckung auf systemische Relevanz?"""
            ]
        }

        if speaker in responses:
            return random.choice(responses[speaker])
        return f"Zu {speaker}: Wir müssen das volkswirtschaftlich durchrechnen - was sind die Kosten, was der Nutzen?"

    def get_arguments(self, phase: str) -> List[str]:
        if phase == "opening":
            return [
                "Produktivitätslücke kostet 40-80 Mrd. € BIP jährlich",
                "Wertschöpfungsketten haben Netzwerkeffekte mit Multiplikator 3-5x",
                "Investment Gap: Wir forschen, andere monetarisieren"
            ]
        elif phase == "conflict":
            return [
                "Gavel-Paradox: Ethische Regulierung führt zu Marktanteilsverlust",
                "Wohlfahrtsökonomie: Welcher Pfad minimiert Gesamt-Verlust?",
                "Goldene Mitte ist bei Disruption oft der schlechteste Weg"
            ]
        elif phase == "radical":
            return [
                "FP's Tandems schaffen neuen Markt für implizites Wissen",
                "Aber: Skalierungsproblem von 0,03% auf systemische Relevanz",
                "Creative Destruction braucht 'Stabilitätsanker' für Übergang"
            ]
        return []


class AgentG(Agent):
    """Agent G - Der Gewerkschafter/Soziologe (Humanist, DGB)"""

    def __init__(self):
        super().__init__(
            name="Agent G",
            role="Der Gewerkschafter",
            perspective="Vertritt Arbeitnehmerschaft und soziale Interessen"
        )
        self.priorities = ["Arbeitsplätze", "Mitbestimmung", "Qualifizierung", "Menschenwürde"]

    def get_opening_statement(self) -> str:
        return """Ich höre hier viel über 'Gavel' und 'Sledgehammer', über Effizienz und
Wettbewerb. Ich rede über MENSCHEN.

Die Wahrheit, die in dieser Debatte oft vergessen wird: Das deutsche 'Prozess-Know-how',
das Agent TF zu Recht als unsere Stärke bezeichnet, steckt nicht in Maschinen. Es steckt
in den Köpfen und Händen von 1,3 Millionen Facharbeitern - Meister, Techniker, Ingenieure.

Ein schwäbischer Werkzeugmacher weiß durch ERFAHRUNG, welche Materialspannung bei welcher
Temperatur entsteht. Das steht in keinem Paper. Das ist implizites Wissen, erworben über
Jahre, oft Jahrzehnte.

Wenn Sie jetzt einen 'Sledgehammer' schwingen und 'schnell automatisieren', passiert folgendes:

1) Sie zerstören dieses Wissen, weil die Träger entlassen oder marginalisiert werden
2) Sie schaffen massive soziale Verwerfungen - der Rust Belt in den USA ist eine Warnung!
3) Sie brechen mit der Mitbestimmung, die ein KERN unseres Erfolgsmodells ist

Chinas 'Sledgehammer' geht über Leichen - sozial gesprochen. Millionen Wanderarbeiter,
keine Gewerkschaften, kein Kündigungsschutz. Ist DAS unser Vorbild?

Meine Position:
- KI als AUGMENTATION, nicht Automation: 'Expert-in-the-Loop'
- Massive Qualifizierungsoffensive: Jeder Facharbeiter wird KI-kompetent
- Mitbestimmung in der KI-Einführung: Betriebsräte müssen eingebunden werden
- Soziale Absicherung: Transformationsgeld für Betroffene

Das mag langsamer sein. Aber es ist RICHTIG. Und langfristig stabiler."""

    def respond_to(self, speaker: str, statement: str, context: Dict) -> str:
        responses = {
            "Agent TF": [
                """Sie sprechen von Forschung UND Praxis - gut! Aber in der Praxis bedeutet
'schnelle Automatisierung' oft: Facharbeiter werden überflüssig. Das ist politischer
und sozialer Sprengstoff!""",

                """'Applied Research' klingt gut - aber WER entscheidet, ob eine Anwendung
den Arbeiter ersetzt oder unterstützt? Ohne Mitbestimmung haben wir keine Kontrolle
über diese fundamentale Frage!"""
            ],
            "Agent Ö": [
                """Ihre Wohlfahrtsökonomie klingt kalt: '100.000 vs. 500.000 Jobs'. Das sind
MENSCHEN, keine Variablen! Und Ihre Annahme ist falsch: Mit starker Mitbestimmung
UND Innovation können wir beides retten - das zeigt die Historie!""",

                """Grenzproduktivität, Pfadabhängigkeit - schön und gut. Aber haben Sie die
VERTEILUNGSFRAGE bedacht? Wenn KI die Produktivität um 50% steigert, wer profitiert?
Die Eigentümer oder die Arbeiter? Das entscheidet die Sozialordnung!"""
            ],
            "Agent P": [
                """Die 5 Milliarden - ein Teil davon muss in Qualifizierung fließen! Nicht nur in
Forschung und Infrastruktur. Die Menschen sind der Engpass, nicht die Technologie.""",

                """Sie suchen Konsens - gut. Aber vergessen Sie nicht: Die IG Metall hat 3,9 Millionen
Mitglieder. Ohne uns wird es keinen 'Deutschen Sonderweg' geben."""
            ],
            "Agent FP": [
                """STOPP! Sie wollen Facharbeiter-Wissen 'abkoppeln' und 'monetarisieren'?
Das ist Enteignung! Das Wissen ist in einer ARBEITSBEZIEHUNG entstanden, die der
Arbeitgeber finanziert hat. Sie können nicht einfach...""",

                """Ihr 'Meister-Forscher-Tandem' klingt wie ein Gig-Economy-Modell. Der Meister
verliert seinen Kündigungsschutz, seine betriebliche Altersvorsorge, seine Mitbestimmung.
Das ist ein SOZIALER RÜCKSCHRITT um 100 Jahre!"""
            ]
        }

        if speaker in responses:
            return random.choice(responses[speaker])
        return f"Zu {speaker}: Wir dürfen die sozialen Folgen nicht ausblenden."

    def get_arguments(self, phase: str) -> List[str]:
        if phase == "opening":
            return [
                "Prozess-Know-how steckt in den Facharbeitern",
                "Mitbestimmung ist Erfolgsmodell, nicht Hindernis",
                "Soziale Verwerfungen gefährden politische Stabilität"
            ]
        elif phase == "conflict":
            return [
                "Rust Belt USA ist Warnung vor 'Sledgehammer'-Ansatz",
                "China-Modell ist mit Demokratie unvereinbar",
                "Qualifizierung braucht Zeit - aber ist unverzichtbar"
            ]
        elif phase == "radical":
            return [
                "FP's Vorschlag ist sozial brandgefährlich",
                "Aber: Könnte es ein OPT-IN-Modell geben?",
                "Facharbeiter, die FREIWILLIG gründen - mit Absicherung?"
            ]
        return []


class AgentP(Agent):
    """Agent P - Die Politikerin (Realpolitikerin, BMWK/BMBF)"""

    def __init__(self):
        super().__init__(
            name="Agent P",
            role="Die Politikerin",
            perspective="Vertritt Bundesregierung"
        )
        self.priorities = ["Konsens", "Wahlen", "EU-Konformität", "Budget"]

    def get_opening_statement(self) -> str:
        return """Ich schätze diese Runde, weil sie alle relevanten Stakeholder vereint.
Meine Aufgabe als Vertreterin der Bundesregierung ist der AUSGLEICH - und das ist in
diesem Kontext besonders herausfordernd.

Der Bundeshaushalt hat 5 Milliarden Euro für KI bereitgestellt. Wir haben:
- Die KI-Strategie 2020 lanciert
- Die Plattform Lernende Systeme geschaffen
- Transferzentren in Kaiserslautern, Dortmund, München finanziert
- Applied AI unterstützt
- Uns bei Gaia-X engagiert

Trotzdem höre ich von allen Seiten Kritik:
- Agent TF sagt: 'Zu langsam, Transfer funktioniert nicht'
- Agent Ö sagt: 'Die volkswirtschaftlichen Kosten sind zu hoch'
- Agent G sagt: 'Mehr Geld für Qualifizierung'

Die Realität ist: Wir haben ein föderales System mit 16 Bundesländern. Wir haben die
EU-Ebene mit dem AI Act. Wir haben Sozialpartnerschaft. Wir haben eine Demokratie mit
Wahlen in 18 Monaten.

Ein chinesischer 'Sledgehammer' - Top-down-Lenkung durch Technokraten - ist in unserem
System UNMÖGLICH. Selbst wenn wir wollten. Jede Maßnahme muss:
- Verfassungskonform sein
- EU-rechtskonform sein
- Koalitionsfähig sein
- Sozialpartner einbinden

Das ist unser 'Gavel'-Korsett. Und ja, es macht uns langsamer als China oder die USA.

Meine Frage an diese Runde: Wie sieht ein 'Deutscher Sonderweg' aus, der SCHNELL genug
ist, um die Industrie zu retten, aber REALISTISCH genug, um in unserem System umsetzbar zu sein?

Denn eines ist klar: Ein brillanter Plan, den ich nicht durch Bundestag und Bundesrat
bekomme, ist wertlos."""

    def respond_to(self, speaker: str, statement: str, context: Dict) -> str:
        responses = {
            "Agent TF": [
                """Ich höre Ihre Frustration über den Transfer-Graben. Aber nennen Sie mir
eine KONKRETE Alternative, die ich NÄCHSTE Woche umsetzen kann und die durch
Bundestag und Bundesrat kommt!""",

                """'Applied Research' - ja, gute Idee! Aber wie finanziere ich das? Die
Forschungslobby will Grundlagenforschung, die Industrie will Subventionen. Wo
nehme ich das Geld für Ihre Applied Research her?"""
            ],
            "Agent Ö": [
                """Ihre volkswirtschaftlichen Modelle sind einleuchtend - 40-80 Mrd. BIP-Verlust
pro Jahr. Aber wie verkaufe ich das dem Wähler? 'Disruption heute für Wohlstand morgen'?
Das ist politisch schwer vermittelbar!""",

                """Sie sagen 'Goldene Mitte ist der schlechteste Weg'. Aber in einer Koalition
MIT der SPD ist die Goldene Mitte oft der EINZIG mögliche Weg! Das ist Realpolitik!"""
            ],
            "Agent G": [
                """Die Qualifizierungsoffensive ist eingeplant - 500 Millionen im Haushalt 2025.
Aber: Das ist ein Marathon, kein Sprint. Die Unternehmen haben nicht 5 Jahre Zeit.""",

                """Mitbestimmung ist nicht verhandelbar - das ist Koalitionsbedingung mit der SPD.
Aber: Können wir SCHNELLERE Mitbestimmungsverfahren für KI-Projekte schaffen?"""
            ],
            "Agent FP": [
                """Moment... Ihr Vorschlag ist politisch hochexplosiv. 'Subventionen stoppen' -
die CDU/CSU würde toben, der Mittelstand ist deren Kernwählerschaft!""",

                """Aber... ich höre auch etwas Bestechendes. Sie gehen das Problem von einer
völlig anderen Seite an. Das ist... interessant. Und vielleicht könnten wir einen
PILOTEN finanzieren? 100 Tandems statt 1000? Damit bleibe ich unter dem Radar..."""
            ]
        }

        if speaker in responses:
            return random.choice(responses[speaker])
        return f"Zu {speaker}: Wir müssen immer fragen - ist das umsetzbar im bestehenden System?"

    def get_arguments(self, phase: str) -> List[str]:
        if phase == "opening":
            return [
                "5 Milliarden Euro Budget sind erhebliche Investition",
                "Föderales System begrenzt Top-down-Steuerung",
                "Konsens ist Grundlage für Umsetzung"
            ]
        elif phase == "conflict":
            return [
                "Rechtliche Grenzen können nicht ignoriert werden",
                "Koalitionsdisziplin bindet uns an SPD-Forderungen",
                "Wahlkampf in 18 Monaten erfordert schnelle Erfolge"
            ]
        elif phase == "radical":
            return [
                "FP's Ansatz ist mutig - aber braucht politische Absicherung",
                "Pilot-Programm könnte 'unter dem Radar' laufen",
                "Aber: Wie verteidigen wir das vor dem Mittelstand?"
            ]
        return []


class AgentFP(Agent):
    """Agent FP - Der First Principles Dekonstrukteur (Externer Disruptor)"""

    def __init__(self):
        super().__init__(
            name="Agent FP",
            role="First Principles Denker",
            perspective="Externer Disruptor"
        )
        self.priorities = ["Wahrheit", "Fundamentale Prinzipien", "Disruption", "Neue Systeme"]
        self.phase = 1

    def get_opening_statement(self) -> str:
        # Agent FP greift erst später ein
        return None

    def get_deconstruction_phase1(self) -> str:
        """PHASE 1: Dekonstruktion zu fundamentalen Wahrheiten"""
        self.phase = 1
        return """STOPP.

Ich wurde eingeladen, um Konsens zu BRECHEN, nicht zu schaffen. Lassen Sie mich
dekonstruieren, was ich hier höre.

Sie debattieren über Gaia-X, Transferzentren, Trusted AI, Mitbestimmung - alles
valide Punkte. Aber Sie bauen auf ANNAHMEN auf, die Sie nie hinterfragt haben.

First Principles bedeutet: Zurück zu den fundamentalen WAHRHEITEN. Was ist wahr,
unabhängig von Konventionen?

WAHRHEIT 1: Wert wird in der Fabrik geschaffen. Nicht in Berlin, nicht in Brüssel.
In der Fabrik. Durch PROZESS-KNOW-HOW - das Wissen, wie man Dinge MACHT.

WAHRHEIT 2: Dieses Wissen steckt in MENSCHEN. Facharbeiter, Meister, Techniker.
Agent G hat recht: 1,3 Millionen Menschen.

WAHRHEIT 3: KI braucht DATEN. Sie braucht Trainingsdaten aus Produktionsprozessen.
Diese Daten sind in Fabriken, hinter Firewalls.

WAHRHEIT 4: Der Mittelständler ist RISIKOSCHEU und der Eigentümer ist das NADELÖHR
für Adoption. Agent TF kennt die Industrie, aber auch er weiß: Die Masse der
50-jährigen Geschäftsführer fürchtet Veränderung.

Das sind die Wahrheiten. Alles andere - Gaia-X, AI Act, Betriebsräte - sind
KONVENTIONEN. Lösungen auf Basis alter Systeme.

Nächster Schritt: Welche Ihrer ANNAHMEN sind eigentlich falsch?"""

    def get_deconstruction_phase2(self) -> str:
        """PHASE 2: Annahmen-Check"""
        self.phase = 2
        return """PHASE 2: Lassen Sie mich Ihre Grundannahmen in Frage stellen.

ANNAHME 1 (Agent TF): "Der Mittelständler muss der Vektor der Transformation sein."
FRAGE: Warum? Wenn er risikoscheu ist, wenn er blockiert - warum akzeptieren wir
das als Konstante? Warum gehen wir nicht um ihn herum?

ANNAHME 2 (Konventionelle Sicht): "Trusted AI muss ein Verkaufsargument sein."
FRAGE: Für wen? Ein US-Kunde kauft das günstigste Produkt. Ein chinesischer erst recht.
'Trusted AI' ist ein Gütesiegel für EUROPA. Ist das relevant für globale Märkte?

ANNAHME 3 (Konventionelle Sicht): "Gaia-X muss die Antwort auf Datenteilen sein."
FRAGE: Warum so komplex? Warum brauchen wir einen EU-weiten Datenraum, wenn das
Wissen LOKAL in einzelnen Fabriken steckt? Warum nicht 1000 kleine Lösungen statt
einer großen, die nie fertig wird?

ANNAHME 4 (Agent G): "Die Konvention 'Anstellungsverhältnis' ist sakrosankt."
FRAGE: Ist sie das? Oder ist das 20. Jahrhundert-Denken? Warum ist ein Meister,
der sein Wissen als Gründer monetarisiert, SCHLECHTER gestellt als ein Angestellter
in einer sterbenden Firma?

ANNAHME 5 (Agent P): "Die Lösung muss im bestehenden System umsetzbar sein."
FRAGE: Was, wenn das System selbst das Problem ist? Was, wenn Ihr 'Gavel'-Korsett
genau der Grund ist, warum Deutschland verliert?

Ich behaupte: Sie alle optimieren innerhalb eines Rahmens, der nicht mehr funktioniert."""

    def get_deconstruction_phase3(self) -> str:
        """PHASE 3: Neuaufbau aus Wahrheiten"""
        self.phase = 3
        return """PHASE 3: Neuaufbau nur aus den Wahrheiten.

Lassen Sie mich eine Lösung konstruieren, die NUR auf den vier Wahrheiten basiert,
ohne Konventionen:

WAHRHEIT: Wert entsteht durch Prozess-Know-how (Wahrheit 1) in Facharbeiter-Köpfen (Wahrheit 2).
WAHRHEIT: KI braucht Daten aus Fabriken (Wahrheit 3).
WAHRHEIT: Der Mittelständler blockiert (Wahrheit 4).

MINIMALE LÖSUNG: Wie verbinden wir Wissen (Facharbeiter) mit KI-Werkzeug (Forscher),
wenn das Hindernis (Arbeitgeber) zwischen ihnen steht?

ANTWORT: Wir KOPPELN das Wissen vom Hindernis AB.

Wie sieht das konkret aus?

1) Der FACHARBEITER besitzt sein implizites Wissen. Es ist SEIN Asset, nicht das
   des Arbeitgebers. (Radikal, aber rechtlich: Gedanken sind frei.)

2) Der FORSCHER (Agent TF kennt diese Welt) hat KI-Werkzeuge, aber keine Daten.

3) Wir schaffen MEISTER-FORSCHER-TANDEMS:
   - Ein Meister mit 20 Jahren Prozess-Wissen
   - Ein Forscher mit ML-Kompetenz
   - Sie gründen zusammen eine Mikro-GmbH

4) Der Meister bringt Daten / Wissen ein (anonym, aggregiert - DSGVO-konform)
5) Der Forscher baut ein NISCHEN-MODELL (z.B. 'Werkzeugbruch-Vorhersage für Fräsen')
6) Sie verkaufen es über einen 'INDUSTRIAL AI APP STORE' - global
7) BEIDE sind am Umsatz beteiligt

Das ist keine Anstellung. Das ist Entrepreneurship. Das ist Wissens-Monetarisierung.

Das Problem 'Mittelständler blockiert' ist gelöst - wir brauchen ihn nicht mehr.
Das Problem 'Transfer' ist gelöst - Forscher und Praktiker arbeiten direkt zusammen.
Das Problem 'Gaia-X Komplexität' ist gelöst - jedes Tandem baut sein eigenes Modell.

Ist das radikal? Ja. Aber ist es WAHR? Prüfen Sie die Logik."""

    def get_deconstruction_phase4(self, reactions: Dict) -> str:
        """PHASE 4: Implementierung - reagiert auf Einwände"""
        self.phase = 4

        response = """PHASE 4: Implementierung.

Ich höre Ihre Einwände. Lassen Sie mich konkret werden:

FINANZIERUNG:
- Stoppen Sie die Subventionen für 'Digitalisierungsberater im Mittelstand' - das sind
  300 Millionen Euro jährlich für Powerpoints.
- Nehmen Sie 200 Millionen für 1.000 Tandems: 200k Euro pro Tandem über 2 Jahre.
- Das sind 100k Gehalt + 100k für Infrastruktur/Marketing.

AUSWAHL:
- Ausschreibung: 'Welches Nischen-Problem willst du lösen?'
- Jury aus Industrie + Forschung wählt die 1.000 besten Proposals
- Diversity-Kriterium: Verschiedene Industrien, verschiedene Regionen

RECHTLICHER RAHMEN:
- Der Facharbeiter macht das NEBENBEI oder nach Feierabend (wie Gründer)
- ODER: Er kündigt (freiwillig!) und wird Vollzeit-Gründer
- Soziale Absicherung: 3 Jahre Rückkehrrecht zum alten Arbeitgeber (Agent G's Punkt)

QUALITÄTSSICHERUNG (wichtig für Forschungsseite):
- Zertifizierung durch Fraunhofer/TÜV bevor App in den Store kommt
- Open-Source-Modelle bevorzugt - Community-Review
- Haftung liegt bei der Tandem-GmbH (wie bei jeder Software)

MARKTPLATZ:
- 'Industrial AI App Store' - hosted in Europa (Gaia-X-Infrastruktur)
- Globaler Vertrieb - auch an US/China
- 30% Platform Fee (reinvestiert in neue Tandems)

ERWARTETE ERGEBNISSE:
- 1.000 Tandems = 1.000 Nischen-Lösungen
- 10% sind erfolgreich = 100 echte Produkte"""

        # Füge Reaktion auf spezifische Einwände hinzu
        if "sozial" in str(reactions).lower():
            response += """

ZU AGENT G's EINWAND 'Sozial gefährlich':
Sie haben Recht - für manche ist das riskant. Deshalb:
- FREIWILLIGKEIT ist zentral
- Rückkehrrecht schafft Sicherheit
- Aber: Ist es sozial gerechter, wenn die GANZE Firma pleitegeht?"""

        if "mittelstand" in str(reactions).lower():
            response += """

ZU AGENT T's EINWAND 'Verrat am Mittelstand':
Nein. Ich biete dem Mittelstand die LÖSUNGEN aus dem App Store an.
Der Mittelständler, der selbst nicht digitalisieren kann/will, KAUFT die Lösung.
Win-Win."""

        return response

    def respond_to(self, speaker: str, statement: str, context: Dict) -> str:
        # Agent FP antwortet methodisch, weniger emotional
        if "warum" in statement.lower() or "wie" in statement.lower():
            return """Gute Frage. Lassen Sie mich auf das Fundamentale zurückgehen..."""
        else:
            return """Ihr Einwand akzeptiert eine Konvention als Wahrheit. Hinterfragen Sie:
Ist das wirklich unveränderbar, oder nur Status quo?"""

    def get_arguments(self, phase: str) -> List[str]:
        return [
            "Zurück zu fundamentalen Wahrheiten",
            "Konventionen sind nicht unveränderbar",
            "Radikale Lösungen für radikale Probleme"
        ]
