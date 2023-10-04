"""Defines the anthropic provider."""

from anthropic import Anthropic
from anthropic.types import TextBlock, ToolUseBlock

from aigor.common import logging


def claude_api_request(
    user_prompt: str,
    system_prompt: str = "",
    temperature: float = 0.7,
    max_tokens: int = 4096,
    model: str = "claude-3-sonnet-20240229"
) -> str:
    """Makes request o Anthropic API given parameters

    Parameters
    ==========
    user_prompt : str
        The user prompt. Normaly is what is sent from STDIN.
    system_prompt: str = "",
        Prompt that prepares the model for some task.
    temperature: float = 0.7,
        How wild the model is behave. Greater values more wilder in vocabulary.
    max_tokens: int = 4096,
        Limt the tokens from the output.
    model: str = "claude-3-sonnet-20240229"
        Model name to request from.
    """

    client = Anthropic()

    message = client.messages.create(
        model=model,
        max_tokens=max_tokens,
        temperature=temperature,
        system=system_prompt,
        messages=[
            {"role": "user", "content": user_prompt},
        ]
    )

    content: str = ""
    if message.content:
        first_block = message.content[0]
        if isinstance(first_block, TextBlock):
            content = first_block.text
        elif isinstance(first_block, ToolUseBlock):
            logging.debug("First block {dir(first_block)}")

    return content


def run(data: str) -> str:
    """Executes the anthropic provider."""
    result = claude_api_request(data)
    return result
