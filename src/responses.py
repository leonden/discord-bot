import random

VALID_COMMANDS = ["$hello", "$roll", "$help",
                  "$offend", "$kidnap", "$shut", "$holden"]

DID_NOT_UNDERSTAND = ["Han di nid verstande du Vogel", "Han di nid verstande du Lappe",
                      "Han di nid verstande du Kek", "Lern mol rede", "Lern mol schriibe",
                      "Jo red lüter", "Hämmers im Griff?", "Nid mol richtig schriibe chasch",
                      "Bechunsch nid mol en grade Satz ahne", "Lern mol Dütsch"]

SWEAR_WORDS = [" isch en Vogel", " isch en Lappe", " het en Egge ab", " het z'tief ins Glas gluegt",
               " isch en Mongo", " het au scho besser usgseh", " chönti wider emol go dusche", " stinkt bis ins nechste Abteil",
               " het wider emol ufem Behinderteparkplatz parkiert", " het nid nur ei Ischränkig", " sötti mol go pfuse",
               " isch en Süesswasserpirat", " het au kei Narrefreiheit nur will de IQ unter 50 isch", " het au scho besseri Zyyte gha"]

GREET = ["Guete Daag", "Servus", "Moin", "Moin Meister", "Guete Morge du alte Bruchpilot", "Grüezi",
         "Grüess Gott", "Sali", "Sali du alte Halunke"]

SHUT = ["Schnuure zue ", "Maul halten ", "Hoit dei Goschn ",
        "Längt jetzt au mol ", "Schnauze ", "Schnauze tief "]


def handle_response(message) -> str:

    p_message = message.lower()

    if p_message == "$hello":
        return str(random.choice(GREET))

    if p_message == "$holden":
        return "aah du kennsch also de Insider? You are a true man of culture!"

    if p_message == "$roll":
        return str(random.randint(1, 6))

    if p_message.startswith("$kidnap "):
        user = p_message[8:]
        return f"HAHAHA Jetzt hani di {user} xD"

    if p_message.startswith("$offend "):
        user = p_message[8:]
        return f"{user} {str(random.choice(SWEAR_WORDS))}"

    if p_message.startswith("$shut "):
        user = p_message[6:]
        return f"{random.choice(SHUT)} {user}"

    # Check if message is not a valid command
    if p_message.startswith("$") and p_message not in VALID_COMMANDS:
        return str(random.choice(DID_NOT_UNDERSTAND))

    # Help command
    if p_message == "$help":
        return "`$help` - Shows this message\n`$roll` - Rolls a dice\n`$hello` - Says hello\n`$offend` - Offends a user\n`$kidnap` - Kidnaps a user\n`$shut` - Tells a user to shut up\n"
