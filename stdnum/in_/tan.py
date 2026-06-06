# tan.py - functions for handling Indian Tax Deduction and Collection Account Numbers
#
# Copyright (C) 2024
#
# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 2.1 of the License, or (at your option) any later version.
#
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this library; if not, see <https://www.gnu.org/licenses/>.

"""TAN (Tax Deduction and Collection Account Number, Indian tax identifier).

The Tax Deduction and Collection Account Number (TAN) is a 10-character
alphanumeric identifier issued by the Income Tax Department of India to
persons who are authorized to collect tax or deduct tax at source. It is
used for tax-related transactions such as TDS/TCS deposits.

TAN consists of 4 alphabetic letters (A-Z, excluding O, I, Q) followed by
6 numeric digits. The format validation ensures the characters are in the
correct positions and meet the specified constraints.

More information:

* https://www.incometaxindia.gov.in/pages/tan.aspx

>>> validate('ABCD123456')
'ABCD123456'
>>> validate('abcd123456')
'ABCD123456'
>>> validate('ABCD12345')
Traceback (most recent call last):
    ...
InvalidLength: ...
>>> validate('ABCD1234AB')
Traceback (most recent call last):
    ...
InvalidFormat: ...
>>> validate('OBCX123456')
Traceback (most recent call last):
    ...
InvalidComponent: ...
"""

from __future__ import annotations

import re

from stdnum.exceptions import *
from stdnum.util import clean


_tan_re = re.compile(r'^[A-Z]{4}[0-9]{6}$')


def compact(number: str) -> str:
    """Convert the number to the minimal representation. This strips the
    number of any valid separators and removes surrounding whitespace."""
    return clean(number, ' ').upper().strip()


def validate(number: str) -> str:
    """Check if the number provided is a valid TAN. This checks the length
    and formatting."""
    number = compact(number)
    if len(number) != 10:
        raise InvalidLength()
    if not _tan_re.match(number):
        raise InvalidFormat()
    # Check that first 4 characters don't contain O, I, or Q
    for char in number[:4]:
        if char in 'OIQ':
            raise InvalidComponent()
    return number


def is_valid(number: str) -> bool:
    """Check if the number provided is a valid TAN. This checks the length
    and formatting."""
    try:
        return bool(validate(number))
    except ValidationError:
        return False


def format(number: str) -> str:
    """Return the compacted, normalized representation of the TAN."""
    return compact(number)