import os
from dotenv import load_dotenv
from openai import OpenAI

# .env laden und API-Key setzen
load_dotenv()
# Client mit API-Key initialisieren
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_email_prompt(product, target_audience, tone, language, call_to_action, version=None):
    version_note = f"Dies ist Version {version} für einen A/B-Test.\n\n" if version else ""
    if version == "v1":
        variation_style = (
        "Nutze einen emotionalen, sanften Einstieg, Fokus auf Entschleunigung und Wohlbefinden.\n"
        if language == "Deutsch" else
        "Version 1 (v1): Start with a calm, inspirational tone that evokes mindfulness, self-care and emotional connection. "
        "Focus on the reader's aspiration for balance, wellness, and intentional living.\n"
    )
    elif version == "v2":
        variation_style = (
        "Starte mit einem konkreten Problem oder Stressmoment. Formuliere lösungsorientiert und direkt.\n"
        if language == "Deutsch" else
        "Version 2 (v2): Start with a specific, relatable stressor or pain point. Be clear and solution-driven. "
        "Speak to the reader's everyday struggles and position the product as an immediate, credible relief.\n"
    )
    else:
        variation_style = ""


    if target_audience == "Neukunden":
        zielgruppen_note = (
            "Die Zielgruppe sind Neukunden: Menschen, die sich für Yoga, Achtsamkeit und nachhaltige Produkte interessieren. "
            "Überzeuge sie von ZENLYFE und führe sie behutsam in die Markenwelt ein.\n"
        )
    elif target_audience == "Bestandskunden":
        zielgruppen_note = (
            "Die Zielgruppe sind Bestandskunden: Sie kennen die Marke bereits. "
            "Stärke die Kundenbindung und motiviere sie mit passenden Mehrwerten zum nächsten Kauf.\n"
        )
    elif target_audience == "Inaktive Nutzer":
        zielgruppen_note = (
            "Die Zielgruppe sind inaktive Nutzer: Sie haben schon einmal gekauft, aber lange nichts mehr. "
            "Gewinne sie durch gezielte Reaktivierung zurück mit einem vertrauten, aber frischen Ton.\n"
        )
    else:
        zielgruppen_note = ""
    
    language_instruction = (
    "Formuliere die gesamte E-Mail auf Englisch.\n"
    if language == "Englisch"
    else "Formuliere die gesamte E-Mail auf Deutsch.\n"
)

    {variation_style}
    ab_test_instruction = (
        "Erstelle genau eine E-Mail Version inhaltlich für die A/B-Test mit der angegebenen Tonalität."
        "Verwende eine eigene Argumentationsstruktur oder Formulierung, die sich deutlich von anderen Varianten unterscheidet.\n"
        if version else
        "Erstelle genau eine E-Mail-Version basierend auf den folgenden Vorgaben.\n"
    )

    return f"""{version_note}{variation_style}{zielgruppen_note}{language_instruction}{ab_test_instruction}
Du bist ein erfahrener Marketing-Experte und arbeitest für die ZENLYFE GmbH, ein Unternehmen aus dem Bereich Gesundheit & Lifestyle, spezialisiert auf nachhaltige Produkte für Yoga, Achtsamkeit und mentale Balance. Du hast eine Spezialisierung im Bereich digitale Kommunikation, E-Mail-Marketing und Conversion-Optimierung. Du kennst die Prinzipien der DSGVO und setzt sie konsequent um. Du verstehst, wie man Texte emotional auflädt, die Aufmerksamkeit steigert und mit wenig Worten viel Wirkung erzielt.
Verfasse eine DSGVO-konforme, kurze Marketing-E-Mail, die im Rahmen einer digitalen Produktkampagne versendet wird. Die Aufgabe ist es, sofort das Interesse der Zielgruppe zu wecken, Vertrauen aufzubauen und eine konkrete Handlung zu motivieren (die konkrete Handlung wird im Call-to-Action vom Nutzer eingegeben).
{ab_test_instruction}
Wenn Sprache = Deutsch, formuliere kulturadäquat für den DACH-Raum. Achte bei der Wortwahl auf regionale Eigenheiten, Ansprache und CTA-Konventionen. Verwende bei deutschsprachigen E-Mails je nach Tonalität konsequent entweder die Du- oder Sie-Ansprache keine Mischung.
Wenn Sprache = Englisch, formuliere für eine international englischsprachige Zielgruppe mit Fokus auf Professionalität, Klarheit und authentischer Tonalität. Achte auf idiomatische Formulierungen, vermeide kulturelle Missverständnisse und nutze passende Call-to-Action-Konventionen.

Anforderungen an den Text:

Subject Line:
- Maximal 50 Zeichen
- Emotional und aufmerksamkeitsstark
- Ohne reißerisches Spam-Vokabular
- Muss zum Öffnen animieren und Neugier wecken, ohne Clickbait-Charakter

E-Mail Body:
- Maximal 100 Wörter
- Klar strukturierter, aktivierender Fließtext
- Direkt, persönlich und zielgerichtet formuliert
- Enthält eine klare Handlungsaufforderung (Call-to-Action)
- Passt sich sprachlich der Zielgruppe an („du“ oder „Sie“)
- Starke Benefits und emotionaler Nutzen statt Funktionsbeschreibungen
- Keine typischen Werbefloskeln wie „kostenlos“, „jetzt zugreifen“, etc.
- Keine unnötigen Formatierungen (kein HTML, nur Klartext)

Kontext und Vorgaben:
- Produktname: {product["name"]}
- Produktbeschreibung: {product["description"]}
- Zielgruppe: {target_audience}
- Sprache: {language}
- Tonalität: {tone}
- Call-to-Action: {call_to_action}

Tonalitätsdefinitionen zur Klarstellung:
- Locker: Duzend, direkt, emotional und nahbar, gelegentlich humorvoll
- Neutral: Freundlich-sachlich, informativ, duzend oder gesiezt je nach Kontext
- Förmlich: Siezend, professionell, korrekt und zurückhaltend in Versprechen

Zielgruppe: 
- Neukunden: Menschen, die sich für Yoga, Achtsamkeit und nachhaltige Produkte interessieren. Das Ziel bei dieser Gruppe ist es, sie von der Marke ZENLYFE zu überzeugen und sie zum Kauf zu bewegen.
- Bestandskunden: Bestehende Kunden, die bereits Produkte von ZENLYFE gekauft haben. Das Ziel ist es, sie zu weiteren Käufen zu motivieren und die Kundenbindung zu stärken.
- Inaktive Nutzer: Frühere Kunden, die seit längerem nicht mehr aktiv sind. Ziel ist es, sie zurückzugewinnen und sie wieder für die Marke zu begeistern.

Ziel:
Erzeuge ein hochkonvertierendes E-Mail-Konzept, das auf psychologischen Triggern basiert. Die Empfänger:innen sollen sich angesprochen fühlen und auf den Call-to-Action klicken. Achte darauf, Vertrauen und Glaubwürdigkeit aufzubauen ohne Übertreibungen. Nutze maximal zwei der folgenden psychologischen Trigger, passend zur Zielgruppe: Neugier, Zugehörigkeit, Relevanz, soziale Bewährtheit (Social Proof), Verlustangst, Community-Zugehörigkeit.
"""

def generate_email(product, target_audience, tone, language, call_to_action, version=None):
    prompt = generate_email_prompt(product, target_audience, tone, language, call_to_action, version)

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7,
        max_tokens=700
    )

    return response.choices[0].message.content
    

def generate_image_prompt(product, target_audience):
    product_context = {
        "ZENLYFE Eco Yoga Mat": "ausgerollt auf einem hellen Holzfußboden in einem modernen Wohnzimmer oder Yoga-Studio mit Pflanzen im Hintergrund",
        "MindfulFocus Aroma Spray": "stehend auf einem schlichten Nachttisch oder Meditationsaltar aus Holz, umgeben von Leinen, Kerze und Buch",
        "ZENLYFE Glas Trinkflasche": "stehend auf einem Schreibtisch mit Notizbuch und Laptop oder in einer Yoga-Tasche neben der Matte, natürliche Szene"
    }

    product_scene = product_context.get(product["name"], "natürliche Szene mit authentischem Anwendungskontext")

    return f"""
Generiere ein fotorealistisches Produktfoto von {product['name']} basierend auf dieser Beschreibung: {product['description']}. 

Das Bild soll im Stil moderner Lifestyle-Fotografie gestaltet sein und folgende Kriterien erfüllen:

Ziel: Hochwertige Darstellung im realistischen Nutzungskontext für die Zielgruppe: {target_audience}

Stilrichtlinien (ZENLYFE Marke):
Minimalistisch, achtsam, ruhig
Farbpalette: Naturtöne (weiß, beige, salbei, terracotta)
Materialität: Holz, Leinen, Keramik, Glas, keine Plastik-Elemente
Keine Texte, keine Logos, keine Menschen

Bildkomposition:
Perspektive: Eye-Level oder leicht erhöht
Kamera: DSLR, natürliche Unschärfe im Hintergrund
Licht: Tageslicht
Format: Vertikal (4:5)  

Anwendungskontext:
{product_scene}
""".strip()