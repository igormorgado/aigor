"""Commom utilities"""

from pathlib import Path
from typing import Callable, TextIO, Any
import yaml
from dotenv import load_dotenv

import typer
from rich import print as rprint

from aigor import __appname__, state_get


def log_warn(message: str) -> None:
    """Print a warn message.

    Parameters
    ==========
    message : str
        The message
    """
    rprint(f"[bold yellow]WARNING[/bold yellow]: {message}")


def log_info(message: str) -> None:
    """Print a info message.

    Parameters
    ==========
    message : str
        The message
    """
    rprint(f"[bold blue]INFO[/bold blue]: {message}")


def log_debug(message: str) -> None:
    """Print a DEBUG message.

    Parameters
    ==========
    message : str
        The message
    """
    rprint(f"[bold purple]DEBUG[/bold purple]: {message}")


def log_error(message: str) -> None:
    """Print a, ERROR message.

    Parameters
    ==========
    message : str
        The message
    """
    rprint(f"[bold red]ERROR[/bold red]: {message}")


def get_app_dir() -> Path:
    """Get config dir based on platform.

    Returns
    =======
    Path
        A path pointing to config dir.
    """
    app_dir = Path(typer.get_app_dir(__appname__)).resolve()
    return app_dir


def process_stdin(
        process_func: Callable[..., Any],
        input_stream: TextIO,
        output_stream: TextIO
) -> None:
    """Apply process_function into the STDIN->STDOUT stream"""
    # We need to merge the whole input in a single stream instead call
    # multiple process_func per input_Stream
    for line in input_stream:
        result = process_func(line.strip())
        output_stream.write(result + '\n')
        output_stream.flush()


def search_and_load_dotenv() -> None:
    """Loads .env file from an hierachy of locations.

    It will search in CWD, if does not exist it will look inside ${HOME}.
    """
    loaded_dotenv = False
    locations = [Path("."), Path.home()]
    for location in locations:
        if state_get("verbose"):
            log_debug(f"Trying to read .env from {location}")
        if load_dotenv(location / ".env"):
            loaded_dotenv = True
            break

    if state_get("verbose"):
        if loaded_dotenv:
            log_info(f"Loaded `.env` from {location}")
        else:
            log_warn("Could not find .env file.")


def args_to_dict(args: list[str]) -> dict[str, str]:
    """Converts a list of strings like "key:value" into a dictionary.

    Parameters
    ==========
    args : list[str]
        List of string in formatted as "key:value". Keys and values will be
        considered as strings. Content will be stripped.

    Returns
    =======
    dict
        A dicionary of given key and values.
    """
    args_dict = {
        key.strip(): value.strip()
        for arg in args
        for key, value in [arg.split(":")]
    } if args else {}
    return args_dict


def config_read() -> dict[str, str]:
    """Read AIgor config.

    Returns
    =======
    dict[Any]
        Dictionary containing the AIgor config.
    """
    app_dir = get_app_dir()
    config_path = app_dir / "config.yaml"
    config = {}
    if config_path.exists():
        with open(config_path, "r", encoding="UTF-8") as file:
            config = yaml.safe_load(file)
    return config


def config_write(config: dict[str, Any]) -> None:
    """Writes dictionary to AIgor config file.

    Parameters
    ===========
    config : dict[str, Any]
        Dictionary containing the AIgor config.

    Returns
    =======
    None
    """
    app_dir = get_app_dir()
    config_path = app_dir / "config.yaml"
    with open(config_path, "w", encoding="UTF-8") as file:
        yaml.dump(config, file, default_flow_style=False)
