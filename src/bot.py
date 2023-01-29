from decouple import config
import responses
import discord


async def send_msg(msg, user_msg, is_private):
    try:
        response = responses.handle_response(user_msg)
        await msg.author.send(response) if is_private else await msg.channel.send(response)
    except Exception as e:
        print(e)


def run():
    intents = discord.Intents.default()

    intents.msg_content = True

    client = discord.Client(intents=intents)

    @client.event
    async def on_ready():
        print(f'{client.user} has connected to Discord!')

    @client.event
    async def on_msg(msg):
        if msg.author == client.user:
            return

        username = str(msg.author)
        user_msg = str(msg.content)
        channel = str(msg.channel)

        print(f"{username} in {channel}: {user_msg}")

        if user_msg[0] == "?":
            user_msg = user_msg[1:]
            await send_msg(msg, user_msg, True)
        else:
            await send_msg(msg, user_msg, False)

    client.run(config("TOKEN"))


def terminate():
    print("Terminating bot...")
    exit()
