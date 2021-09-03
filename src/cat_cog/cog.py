import random
import re
from logging import getLogger
from typing import Sequence

import discord
from discord.ext import commands

logger = getLogger(__name__)


class CatCogConfig:
    @staticmethod
    def repeat_regex(pattern: str, num: int) -> re.Pattern:
        """
        パターンを繰り返す正規表現を作成
        :param pattern: 繰り返すパターン
        :param num: 繰り返す回数
        :return: 正規表現
        """
        return re.compile(f'({pattern})\\1{{{num-1},}}')

    def __init__(self, reactions: Sequence[str] = ..., pattern: re.Pattern = ...):
        """
        :param reactions: リアクションで送信する絵文字の一覧
        :param pattern: 猫が送信したと判定する条件
        """
        if reactions is ...:
            reactions = ['🐱', '🐈']
        if pattern is ...:
            pattern = self.repeat_regex('.', 20)

        self.reactions = reactions
        self.pattern = pattern


class CatCog(commands.Cog):
    """猫がキーボードの上を歩いたらリアクションを送信するCog"""

    def __init__(self, bot: commands.Bot):
        config: CatCogConfig = getattr(bot, __name__, CatCogConfig())

        self.bot = bot
        self.reactions = config.reactions
        self.pattern = config.pattern

    @commands.Cog.listener()
    async def on_ready(self):
        pass  # confirm permission

    @commands.Cog.listener('on_message')
    async def on_message(self, message: discord.Message):
        text = message.content
        if not self.pattern.search(text):
            return

        logger.debug('Received an message which cat wrote.')
        reaction = random.choice(self.reactions)
        await message.add_reaction(reaction)


def set_config(bot: commands.Bot, config: CatCogConfig):
    setattr(bot, __name__, config)


def setup(bot):
    return bot.add_cog(CatCog(bot))
