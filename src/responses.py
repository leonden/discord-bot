import random


def handle_response(message) -> str:
    p_message = message.lower()

    # swear_words = [" isch en Vogel", " isch en Lappe", " het en Egge ab", "",
    #                "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""]

    if p_message == "$hello":
        return "Guete Daag"

    if p_message == "$Holden":
        return "aah du kennsch also de Insider? You are a true man of culture!"

    if p_message == "$roll":
        return str(random.randint(1, 6))

    # if p_message == "kidnap " + client.user.name:
    #     return "HAHAHA Jetzt hani di xD"

    if p_message == "$help":
        return "`$help` - Shows this message\n`$roll` - Rolls a dice\n`$hello` - Says hello"

    # if p_message == "offend " + client.user.name:
    #     return + str(random.choice(swear_words))

    return "Han di nid verstande du Vogel"
