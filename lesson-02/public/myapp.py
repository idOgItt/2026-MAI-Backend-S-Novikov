import os
import random
import string
from typing import Iterable, List, Tuple


DIGITS = string.digits
LOWER = string.ascii_lowercase
UPPER = string.ascii_uppercase
SPECIAL = "#[]().,!@&^%*"


def _generate_password(length: int) -> str:
    if length < 8 or length > 16:
        raise ValueError("password length must be between 8 and 16 characters")

    rng = random.SystemRandom()

    # Ensure at least one character from each required class
    chars: List[str] = [
        rng.choice(DIGITS),
        rng.choice(LOWER),
        rng.choice(UPPER),
        rng.choice(SPECIAL),
    ]

    all_chars = DIGITS + LOWER + UPPER + SPECIAL
    while len(chars) < length:
        chars.append(rng.choice(all_chars))

    rng.shuffle(chars)
    return "".join(chars)


def app(environ, start_response):
    """
    Minimal WSGI application that generates a single password per request.

    Password length is controlled via the PASSWORD_LENGTH environment
    variable (default is 12, always clamped to the [8, 16] range).
    """
    try:
        default_length = 12
        raw_length = os.getenv("PASSWORD_LENGTH")
        length = int(raw_length) if raw_length is not None else default_length
    except ValueError:
        length = default_length

    length = max(8, min(16, length))

    password = _generate_password(length)
    body = f"{password}\n".encode("utf-8")

    headers: List[Tuple[str, str]] = [
        ("Content-Type", "text/plain; charset=utf-8"),
        ("Content-Length", str(len(body))),
    ]

    start_response("200 OK", headers)
    return [body]


if __name__ == "__main__":
    # For local debugging without gunicorn
    from wsgiref.simple_server import make_server

    with make_server("127.0.0.1", 8000, app) as httpd:
        print("Serving on http://127.0.0.1:8000")
        httpd.serve_forever()

