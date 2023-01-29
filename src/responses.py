import random
import discord

VALID_COMMANDS = ["$hello", "$roll", "$help", "$offend", "$Holden"]

DID_NOT_UNDERSTAND = ["Han di nid verstande du Vogel", "Han di nid verstande du Lappe",
                      "Han di nid verstande du Kek", "Lern mol rede", "Lern mol schriibe",
                      "Jo red lüter", "Hämmers im Griff?", "Nid mol richtig schriibe chasch",
                      "Bechunsch nid mol en grade Satz ahne", "Lern mol Dütsch"]

SWEAR_WORDS = [" isch en Vogel", " isch en Lappe", " het en Egge ab", " het z'tief ins Glas gluegt",
               " isch en Mongo", " het au scho besser usgseh", " chönti wider emol go dusche", " stinkt bis ins nechste Abteil",
               " het wider emol ufem Behinderteparkplatz parkiert", " het nid nur ei Ischränkig", "", "", "", "", "", "", "", "", "", "", "", ""]

GREET = ["Guete Daag", "Servus", "Moin", "Moin Meister",
         "Guete Morge du alte Bruchpilot", "Grüezi", "Grüess Gott", "Sali", "Sali du alte Halunke"]


def handle_response(message) -> str:

    p_message = message.lower()

    if p_message == "$hello":
        return str(random.choice(GREET))

    if p_message == "$Holden":
        return "aah du kennsch also de Insider? You are a true man of culture!"

    if p_message == "$roll":
        return str(random.randint(1, 6))

    # if p_message == "kidnap " + client.user.name:
    #     return "HAHAHA Jetzt hani di xD"

    if p_message == f"$offend ":
        return f" {str(random.choice(SWEAR_WORDS))}"

    if p_message.startswith("$") and p_message not in VALID_COMMANDS:
        return str(random.choice(DID_NOT_UNDERSTAND))

    if p_message == "$help":
        return "`$help` - Shows this message\n`$roll` - Rolls a dice\n`$hello` - Says hello\n`$offend` - Offends people\`$kidnap` - Kidnaps a user\n"
