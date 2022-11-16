import json
import pathlib
from dataclasses import dataclass

__all__ = (
    'BotConfig',
    'Config',
    'load_config',
)


@dataclass(frozen=True, slots=True)
class BotConfig:
    token: str
    admin_ids: set[int]


@dataclass(frozen=True, slots=True)
class Config:
    bot: BotConfig


def load_config(config_file_path: pathlib.Path | str) -> Config:
    with open(config_file_path, encoding='utf-8') as file:
        config = json.load(file)

    try:
        bot_config: dict = config['telegram_bot']
    except KeyError as error:
        raise KeyError(f'Missing {error} section in config.json')

    try:
        return Config(
            bot=BotConfig(
                token=bot_config['token'],
                admin_ids=set(bot_config['admin_ids']),
            )
        )
    except KeyError as error:
        raise KeyError(f'Missing {error} field in config.json')
