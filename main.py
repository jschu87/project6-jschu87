import os
from dnd import Spell, Equipment, Monster, Races, Class, Magic_Item
import discord
#from keep_alive import keep_alive

my_secret = os.environ['token']

site_url = 'https://www.dnd5eapi.co/api/'

client = discord.Client()


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    msg = message.content.lower()

    if message.author == client.user:
        return

    if msg.startswith('!help'):
        help_input = msg.split('!help')
        await message.channel.send("!spell, !magic, !class, !race, !equip, !mon")
        await message.channel.send("are the acceptable commands")
        await message.channel.send('Magic armor or weapons should use the !magic to look up')

    if msg.startswith('!spell'):
        spell_input = Spell(name='{}'.format(msg.split('!spell ', 1)[1]))

        embed = discord.Embed(
            title=spell_input.name,
            description=spell_input.desc,
            color=discord.Colour.red()
        )
        # embed.set_footer('This is a footer')
        embed.set_thumbnail(url='{}'.format(spell_input.url))
        embed.add_field(name='Range', value=spell_input.range)
        embed.add_field(name='Cast', value=spell_input.cast)
        embed.add_field(name='Damage', value=spell_input.damage_type),
        embed.add_field(name='Damage', value=spell_input.damage)

        await message.channel.send(embed=embed)
        # await message.channel.send(spell_input.url)

    if msg.startswith('!equip'):
        equip_input = Equipment(name='{}'.format(msg.split('!equip ', 1)[1]))

        embed = discord.Embed(
            title=equip_input.name,
            description=equip_input.equipment_category,
            color=discord.Colour.red()
        )
        # embed.set_footer('This is a footer')

        if equip_input.equipment_category == 'Armor':
            embed.add_field(name='Armor Category', value=equip_input.armor_category)
            embed.add_field(name='Stealth Disadvantage', value=equip_input.stealth_disadvantage)
            embed.add_field(name='Str Requirement', value=equip_input.str_minimum),
            embed.add_field(name='Weight', value=equip_input.weight)

            await message.channel.send(embed=embed)
        # await message.channel.send(spell_input.url)

        if equip_input.equipment_category == 'Weapon':
            embed.add_field(name='Weapon Range', value=equip_input.weapon_range)
            embed.add_field(name='Damage', value=equip_input.damage)
            embed.add_field(name='Damage', value=equip_input.damage_type)

        await message.channel.send(embed=embed)

    if msg.startswith('!mon'):
        mon_input = Monster(name='{}'.format(msg.split('!mon ', 1)[1]))

        embed = discord.Embed(
            title=mon_input.name,
            description='',
            color=discord.Colour.red()
        )
        # embed.set_footer('This is a footer')
        embed.add_field(name='Hit Points', value=mon_input.hit_points),
        embed.add_field(name='Challenge Rating', value=mon_input.rating),
        embed.add_field(name='Armor Class', value=mon_input.armor_class)
        embed.add_field(name='Size', value=mon_input.size)
        embed.add_field(name='Type', value=mon_input.type),
        embed.add_field(name='Speed', value=mon_input.speed)

        await message.channel.send(embed=embed)
        # await message.channel.send(spell_input.url)

    if msg.startswith('!race'):
        race_input = Races(name='{}'.format(msg.split('!race ', 1)[1]))

        embed = discord.Embed(
            title=race_input.name,
            description='{}'.format(race_input.lang),
            color=discord.Colour.red()
        )
        # embed.set_footer('This is a footer')
        embed.add_field(name='Alignment', value=race_input.alignment)
        embed.add_field(name='Speed', value=race_input.speed, inline=False)
        embed.add_field(name='Ability Bonus',
                        value='+{} to {}'.format(race_input.ability_bonus_1, race_input.ability_bonuses_1), inline=True)
        embed.add_field(name='Ability Bonus',
                        value='+{} to {}'.format(race_input.ability_bonus_2, race_input.ability_bonuses_2), inline=True)

        await message.channel.send(embed=embed)

    if msg.startswith('!class'):
        class_input = Class(name='{}'.format(msg.split('!class ', 1)[1]))
        starting_items = []
        proficiency_choices = []
        saving_throws = []
        proficiencies = []

        for item in class_input.starting_equipment:
            starting_items.append(item['equipment']['index'])

        proficiency_list = class_input.proficiency_choices[0]['from']

        for prof in proficiency_list:
            proficiency_choices.append(prof['index'])

        for save in class_input.saving_throws:
            saving_throws.append(save['index'])

        for skill in class_input.proficiencies:
            proficiencies.append(skill['index'])

        embed = discord.Embed(
            title=class_input.name,
            description='Starting items: {}'.format(*starting_items, sep=','),
            color=discord.Colour.red()
        )
        # embed.set_footer('This is a footer')

        embed.add_field(name='Proficiency Choice',
                        value='\n'.join('{}: {}   '.format(*k) for k in enumerate(proficiency_choices)))

        embed.add_field(name='Skills', value='\n'.join('{}: {}'.format(*k) for k in enumerate(proficiencies)))

        embed.add_field(name='Hit Dice', value=class_input.hit, inline=False)
        embed.add_field(name='Saving Throw', value='\n'.join('{}:{}   '.format(*k) for k in enumerate(saving_throws)),
                        inline=True)

        await message.channel.send(embed=embed)

    if msg.startswith('!magic'):
        magic_input = Magic_Item(name='{}'.format(msg.split('!magic ', 1)[1]))

        embed = discord.Embed(
            title=magic_input.name,
            description='\n'.join('{}:{}'.format(*k) for k in enumerate(magic_input.desc)),
            color=discord.Colour.red()
        )
        # embed.set_footer('This is a footer')
        # embed.set_thumbnail(url = '{}'.format(magic_input.url))

        await message.channel.send(embed=embed)
        # await message.channel.send(spell_input.url)



client.run(my_secret)



