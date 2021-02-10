import discord
from UTILS import *
import random


class DiscordBottoClient(discord.Client):
    async def on_ready(self):
        print(f'{self.user} has connected to Discord!')
    async def on_member_join(self, member):
        await member.create_dm()
        await member.dm_channel.send(f'Great! Now this server reeks of {member.name}!')
    async def on_message(self, message : discord.Message):
        if message.author == self.user:
            return
        
        command = self.find_command(message_content=message.content)


        # Check if MESSAGE_TYPE and run command
        if command[1] == MESSAGE_TYPE:
            response = command[0](message=message)
            await message.channel.send(response)
        # Check if RESPONSE_TYPE and run command
        elif command[1] == RESPONSE_TYPE:
            try:
                response = command[0](message=message)
            except NoResponseError:
                pass
            else:
                await message.channel.send(response)
        
        elif command[1] == HTML_TYPE:
            embed = command[0](message=message)
            await message.channel.send(embed=embed)
        
        elif command[1] == FILE_TYPE:
            file = command[0](message=message)
            await message.channel.send(file=file)
        

        pass
    
    

    def find_command(self, message_content):
        
        commands = {'!help':(self.help, HTML_TYPE), '!Yoda':(self.yoda_command, MESSAGE_TYPE), '!important':(self.important_file_send, FILE_TYPE)}

        for key, value in commands.items():
            key_length = len(key)

            if key == message_content[:key_length]:
                return value
        
        return (self.check_if_myles_talking, RESPONSE_TYPE)
        


    def help(self, message) -> discord.Embed:
        embed=discord.Embed(title="Help", description="List of Commands")
        embed.add_field(name="!Yoda", value="Yoda quotes", inline=True)
        embed.add_field(name="!help", value="You just issued this command, you dingus!", inline=True)
        embed.add_field(name='!important', value="Very important", inline=True)

        return embed
        
    def yoda_command(self, message):
        list_of_responses = ["Crush my cock with a rock", "Bend over, you will", "!play https://www.youtube.com/watch?v=LzxCJzM4xLo", "!play https://youtu.be/VZFCXYFWYso"]
        return random.choice(list_of_responses)

    def check_if_myles_talking(self, message):
        print("Name - ", message.author, "Class - ", str(type(message.author)))

        if str(message.author) == "BorisLoveHammer#1118":
            return self.myles_talking(message=message)
        else:
            raise NoResponseError()

    def myles_talking(self, message):
        list_of_responses = ['\nSpongeBob: "Hey Patrick, what am I know?\nPatrick:"Uhhhh, stupid?"\nSpongeBob:"No, I\'m Myles!"\nPatrick: "What\'s the difference!!!"', 
        'Hey Buddy, did you just blow in from Stupidtown?', "My wish is that the people of this server will stop paying any attention to the innane dribble that is constantly streaming out of this dunderhead's mouth.",
        "Shut your mouth, you mediocre clarinet player", "Hey Buddy, you need a ride? I was just on my way to the big doofus convention!"]

        response = random.choice(list_of_responses)

        return response
    
    def important_file_send(self, message):
        return discord.File(fp="./files/important.txt", filename='important.txt')
