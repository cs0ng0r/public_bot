import discord
from discord.ext import commands
import random


class Minigames(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print('Minigames sikeresen betöltve!')

    # Kő, papír, olló
    @commands.command()
    async def rockpaperscissors(self, ctx):
        await ctx.send('Kő, papír, olló! Válassz egyet!')

        def check(m):
            return m.author == ctx.author and m.channel == ctx.channel

        user_choice = await self.bot.wait_for('message', check=check)
        user_choice = user_choice.content.lower()
        if user_choice not in ['kő', 'papír', 'olló']:
            return await ctx.send('Csak kő, papír, olló közül választhatsz!')
        import random
        bot_choice = random.choice(['kő', 'papír', 'olló'])
        await ctx.send(f'A bot választása: {bot_choice}')
        if user_choice == bot_choice:
            return await ctx.send('Döntetlen!')
        if user_choice == 'kő':
            if bot_choice == 'papír':
                return await ctx.send('Bot nyert!')
            return await ctx.send('Te nyertél!')
        if user_choice == 'papír':
            if bot_choice == 'olló':
                return await ctx.send('Bot nyert!')
            return await ctx.send('Te nyertél!')
        if user_choice == 'olló':
            if bot_choice == 'kő':
                return await ctx.send('Bot nyert!')
            return await ctx.send('Te nyertél!')

    # BlackJack
    @commands.command(aliases=['bj'])
    async def blackjack(self, ctx):
        await ctx.send('Blackjack! Jó játékot!')

        def check(m):
            return m.author == ctx.author and m.channel == ctx.channel

        cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11] * 4
        random.shuffle(cards)
        user_hand = [cards.pop(), cards.pop()]
        bot_hand = [cards.pop(), cards.pop()]

        def create_embed(user_hand,
                         bot_hand,
                         result=None,
                         color=discord.Color.blue()):
            embed = discord.Embed(title="Blackjack", color=color)
            embed.add_field(name="Te kártyáid",
                            value=f'{user_hand} (Összeg: {sum(user_hand)})',
                            inline=True)
            embed.add_field(name="Bot kártyái",
                            value=f'{bot_hand} (Összeg: {sum(bot_hand)})',
                            inline=True)
            if result:
                embed.add_field(name="Eredmény", value=result, inline=False)
            return embed

        while sum(user_hand) < 21:
            await ctx.send(embed=create_embed(
                user_hand, bot_hand, 'Kérsz még egy kártyát? (igen/nem)'))
            hit = await self.bot.wait_for('message', check=check)
            if hit.content.lower() == 'igen':
                user_hand.append(cards.pop())
            else:
                break

        if sum(user_hand) > 21:
            embed = create_embed(user_hand,
                                 bot_hand,
                                 'Túllépted a 21-et! Bot nyert!',
                                 color=discord.Color.red())
            return await ctx.send(embed=embed)

        while sum(bot_hand) < 17:
            bot_hand.append(cards.pop())

        if sum(bot_hand) > 21:
            embed = create_embed(user_hand,
                                 bot_hand,
                                 'A bot túllépte a 21-et! Te nyertél!',
                                 color=discord.Color.green())
            return await ctx.send(embed=embed)

        if sum(user_hand) > sum(bot_hand):
            result = 'Te nyertél!'
            color = discord.Color.green()
        elif sum(user_hand) < sum(bot_hand):
            result = 'Bot nyert!'
            color = discord.Color.red()
        else:
            result = 'Döntetlen!'
            color = discord.Color.gray()

        embed = create_embed(user_hand, bot_hand, result, color=color)
        await ctx.send(embed=embed)


async def setup(bot):
    await bot.add_cog(Minigames(bot))
