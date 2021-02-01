import discord

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as', self.user)

    async def on_message(self, message):
        # don't respond to ourselves
        if message.author == self.user:
            return

        if message.content.startswith( '!auth' ):
            # user requested to be authenticated
            await message.channel.send('Check your email address...')

client = MyClient()
client.run('token')
