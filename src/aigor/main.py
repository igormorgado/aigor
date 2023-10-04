#!/usr/bin/env python
"""Main entrypoint for AIgor CLI. No logic here."""

import sys
from typing_extensions import Annotated
import typer
from aigor import (
    __version__,
    __appname__,
    state_get,
    state_set,
)
from aigor.common import (
    log_debug,
    log_info,
    log_error,
    # process_stdin,
    search_and_load_dotenv,
    args_to_dict
)
from aigor.assistant import (
    assistant_infer,
    assistant_create,
    assistant_delete,
    assistant_list,
    assistant_flush,
    assistant_chat,
    assistant_default_set,
    assistant_default_get,
)
from aigor.provider import (
    provider_get_func
)


app = typer.Typer(
    no_args_is_help=False,
    rich_markup_mode="markdown",
    invoke_without_command=True,
)


def version_callback(value: bool) -> None:
    """Shows version and exits."""
    if value:
        print(f"{__appname__} {__version__}")
        raise typer.Exit(code=0)


@app.command()
def infer(name: str | None) -> None:
    """Makes single inference using the `name` assistant.

    If no command is given. It will start `infer` command in the default
    assistant. If no assistant is set as default. It will abort.

    Parameters
    =========
    name : str
        The name of the assistent to be used in inference. If no assistant
        name is passed it will use the default assistant.
    """
    assistant_infer(name)


@app.command()
def chat(name: str) -> None:
    """Friendly chat with `name` assistant. If `name` is a valid previous
    chat title. It will load the previous chat with the correct assistant
    and continue the conversation from there.

    If there is no conversation. It will start a new one with `name` assistant.

    Parameters
    ==========
    name : str
        Name of the assistant or a valid chat session.
    """
    assistant_chat(name)


@app.command()
def flush(name: str) -> None:
    """Flush previous conversation from `name`.

    Parameters
    ==========
    name : str
        Name of the assistant without spaces.
    """
    assistant_flush(name)


@app.command()
def create(
    name: Annotated[
        str,
        typer.Argument(
            show_default=False,
        )
    ],
    provider: Annotated[
        str,
        typer.Argument(
            show_default=False,
        )
    ],
    force: Annotated[
        bool,
        typer.Option(
            help="Overwrite existing assistant, if it exists.",
            show_default=False,
        )
    ] = False,
    default: Annotated[
        bool,
        typer.Option(
            help="Set this assistant as default.",
            show_default=False,
        )
    ] = False,
    args: Annotated[
        list[str] | None,
        typer.Option(
            "-a",
            "--args",
            help=(
                "Arguments to pass to provider. "
                "Can specify multiple times. "
                "Must be in form 'key:value'.",
            ),
            show_default=False,
        )
    ] = None
) -> None:
    """Creates an :robot: assistant with given `name` using `provider`.

    Parameters
    ==========

    name : str
        Name of the assistant without spaces.

    provider : str
        Name of the provider.

    force: bool
        Ovewrite existing assistant, it it exists.

    default: bool
        Set this assistant as the default one.

    args : list[str] | None
        Arguments to pass to the provider. Must be in form "key:value".

    """
    if args is None:
        args_dict = {}
    else:
        args_dict = args_to_dict(args)
    assistant_create(
        name=name,
        provider=provider,
        args=args_dict,
        force=force,
        default=default
    )


@app.command()
def delete(name: str) -> None:
    """Delete assistant named `name` (if it exists).

    Parameters
    ==========
    name : str
        Name of the assistant.
    """
    assistant_delete(name)


@app.command("list")
def list_assistants() -> None:
    """List available assistants.
    """
    assistant_list()


@app.command("default")
def default_set(name: str) -> None:
    """Set a given assistant as the default.

    Parameters
    ==========
    name : str
        Name of the assistant without spaces.
    """
    assistant_default_set(name)


@app.callback(invoke_without_command=True)
def main(
    ctx: typer.Context,
    verbose: Annotated[
        bool | None,
        typer.Option(
            "--verbose",
            "-v",
            help="Runs in verbose mode.",
            show_default=False,
            is_eager=True
        )
    ] = False,
    version: Annotated[
        bool | None,
        typer.Option(
            "--version",
            "-V",
            help="Shows version.",
            callback=version_callback,
            show_default=False,
            is_eager=True
        )
    ] = None,
) -> None:
    """AIgor is an old school :robot: AI assistant."""

    if version:
        version_callback(True)

    if verbose:
        log_debug("Set verbose")
        state_set("verbose", True)

    search_and_load_dotenv()

    if ctx.invoked_subcommand is None:
        assistant = assistant_default_get()

        if state_get("verbose"):
            log_debug(f"Calling default assistant {assistant}.")

        if assistant:
            provider_func = provider_get_func(assistant)
        else:
            log_error("Could not find default assistant")
            raise typer.Abort()

        if sys.stdin.isatty():
            log_info("Reading from terminal. CTRL-D to finish.")
        # process_stdin(provider_func, sys.stdin, sys.stdout)
        log_debug(f"provider_func {provider_func}")
        log_info(f"Default assistant {assistant}")
        if sys.stdin.isatty():
            log_info("Bye. :wave:")


if __name__ == "__main__":
    app()
