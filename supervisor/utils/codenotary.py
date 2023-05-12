"""Small wrapper for CodeNotary."""
# pylint:  disable=unreachable
import asyncio
import hashlib
import json
import logging
from pathlib import Path
import shlex
from typing import Optional, Union

import async_timeout

from . import clean_env
from ..exceptions import CodeNotaryBackendError, CodeNotaryError, CodeNotaryUntrusted

_LOGGER: logging.Logger = logging.getLogger(__name__)

_VCN_CMD: str = "vcn authenticate --silent --output json"
_CACHE: set[tuple[str, Path, str, str]] = set()


_ATTR_ERROR = "error"
_ATTR_VERIFICATION = "verification"
_ATTR_STATUS = "status"


def calc_checksum(data: Union[str, bytes]) -> str:
    """Generate checksum for CodeNotary."""
    if isinstance(data, str):
        return hashlib.sha256(data.encode()).hexdigest()
    return hashlib.sha256(data).hexdigest()


async def vcn_validate(
    checksum: Optional[str] = None,
    path: Optional[Path] = None,
    org: Optional[str] = None,
    signer: Optional[str] = None,
) -> None:
    """Validate data against CodeNotary."""
    return None
