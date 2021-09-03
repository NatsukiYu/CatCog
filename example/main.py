from discord.ext import commands
import cat_cog

bot = commands.Bot(command_prefix='!')
cat_cog.set_config(bot, cat_cog.CatCogConfig(['🐱', '😸', '😺', '😼']))  # <1>
bot.load_extension('cat_cog')  # <2>
bot.run('<bot token>')  # <3>
