"""Configuration file parser of the A-Maze-ing activity.

The configuration file contains one ``KEY = VALUE`` pair per line.
Empty lines and lines that start with ``#`` are ignored.
"""

from __future__ import annotations

from dataclasses import dataclass

MANDATORY_KEYS: tuple[str, ...] = (
    "WIDTH",
    "HEIGHT",
    "ENTRY",
    "EXIT",
    "OUTPUT_FILE",
    "PERFECT",
)
KNOWN_KEYS: tuple[str, ...] = MANDATORY_KEYS + ("SEED",)


@dataclass
class Config:
    """Parsed content of one configuration file.

    Attributes:
        width: Number of cells horizontally.
        height: Number of cells vertically.
        entry: Entry of the maze as ``(x, y)``.
        exit: Exit of the maze as ``(x, y)``.
        output_file: Name of the file to write.
        perfect: ``True`` for a perfect maze, ``False`` for a board.
        seed: Seed of the random generator, ``None`` when not given.
    """

    width: int
    height: int
    entry: tuple[int, int]
    exit: tuple[int, int]
    output_file: str
    perfect: bool
    seed: int | None = None


def _parse_int(key: str, value: str) -> int:
    """Convert one configuration value to an integer.

    Args:
        key: Name of the key, used in the error message.
        value: Raw value read from the file.

    Returns:
        The integer value.

    Raises:
        ValueError: If the value is not an integer.
    """
    try:
        return int(value)
    except ValueError:
        raise ValueError(
            f"{key} must be an integer, not '{value}'"
        ) from None


def _parse_bool(key: str, value: str) -> bool:
    """Convert one configuration value to a boolean.

    Args:
        key: Name of the key, used in the error message.
        value: Raw value read from the file.

    Returns:
        ``True`` for ``true`` or ``1``, ``False`` for ``false`` or
        ``0``.

    Raises:
        ValueError: If the value is not a boolean.
    """
    lowered = value.strip().lower()
    if lowered in ("true", "1"):
        return True
    if lowered in ("false", "0"):
        return False
    raise ValueError(
        f"{key} must be 'True' or 'False', not '{value}'"
    )


def _parse_position(key: str, value: str) -> tuple[int, int]:
    """Convert an ``ENTRY`` or ``EXIT`` value to ``(x, y)``.

    Args:
        key: Name of the key, used in the error message.
        value: Raw value read from the file.

    Returns:
        The coordinates as an ``(x, y)`` tuple.

    Raises:
        ValueError: If the value is not two non-negative integers.
    """
    parts = value.split(",")
    if len(parts) != 2:
        raise ValueError(
            f"{key} must be two integers separated by a comma, "
            f"for example '0,0', not '{value}'"
        )
    try:
        x_coord = int(parts[0].strip())
        y_coord = int(parts[1].strip())
    except ValueError:
        raise ValueError(
            f"{key} must contain two integers, not '{value}'"
        ) from None
    if x_coord < 0 or y_coord < 0:
        raise ValueError(f"{key} coordinates must not be negative")
    return x_coord, y_coord


def _read_lines(file_path: str) -> list[str]:
    """Read the raw lines of the configuration file.

    Args:
        file_path: Path of the configuration file.

    Returns:
        The lines of the file without their line endings.

    Raises:
        ValueError: If the file cannot be read.
    """
    try:
        with open(file_path, "r", encoding="utf-8") as config_file:
            return config_file.read().splitlines()
    except FileNotFoundError:
        raise ValueError(
            f"the configuration file '{file_path}' was not found"
        ) from None
    except PermissionError:
        raise ValueError(
            f"permission denied when reading '{file_path}'"
        ) from None
    except OSError as error:
        raise ValueError(
            f"cannot read '{file_path}': {error}"
        ) from error


def parse_config(file_path: str) -> Config:
    """Parse a configuration file.

    Unknown keys are ignored with a warning so that extra options,
    for example a comment of the team, do not stop the program.

    Args:
        file_path: Path of the configuration file.

    Returns:
        The parsed :class:`Config`.

    Raises:
        ValueError: If the file is missing, if a line is invalid, if
            a mandatory key is missing or if a value is invalid.
    """
    raw: dict[str, str] = {}
    for line in _read_lines(file_path):
        stripped = line.strip()
        if not stripped or stripped.startswith("#"):
            continue
        if "=" not in stripped:
            raise ValueError(
                f"invalid configuration line '{line}', "
                "expected KEY = VALUE"
            )
        key, value = stripped.split("=", 1)
        key = key.strip().upper()
        if not key:
            raise ValueError(
                f"invalid configuration line '{line}', empty key"
            )
        if key not in KNOWN_KEYS:
            print(f"Warning: ignoring unknown key '{key}'")
            continue
        raw[key] = value.strip()

    missing = [key for key in MANDATORY_KEYS if key not in raw]
    if missing:
        raise ValueError(
            "missing mandatory configuration key(s): "
            + ", ".join(missing)
        )

    width = _parse_int("WIDTH", raw["WIDTH"])
    height = _parse_int("HEIGHT", raw["HEIGHT"])
    if width <= 0 or height <= 0:
        raise ValueError("WIDTH and HEIGHT must be positive")

    entry = _parse_position("ENTRY", raw["ENTRY"])
    exit_cell = _parse_position("EXIT", raw["EXIT"])
    if entry == exit_cell:
        raise ValueError("ENTRY and EXIT must be different cells")
    if not (0 <= entry[0] < width and 0 <= entry[1] < height):
        raise ValueError(
            f"ENTRY {entry} is outside a {width}x{height} maze"
        )
    if not (0 <= exit_cell[0] < width
            and 0 <= exit_cell[1] < height):
        raise ValueError(
            f"EXIT {exit_cell} is outside a {width}x{height} maze"
        )

    output_file = raw["OUTPUT_FILE"].strip()
    if not output_file:
        raise ValueError("OUTPUT_FILE cannot be empty")

    perfect = _parse_bool("PERFECT", raw["PERFECT"])

    seed: int | None = None
    if "SEED" in raw:
        seed = _parse_int("SEED", raw["SEED"])
        if seed < 0:
            print(
                "Warning: negative and positive seeds give "
                "the same maze"
            )

    return Config(
        width=width,
        height=height,
        entry=entry,
        exit=exit_cell,
        output_file=output_file,
        perfect=perfect,
        seed=seed,
    )
