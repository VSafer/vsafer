from enum import Enum
from itertools import count
from typing import Dict

import winreg


class Bit(Enum):
    x64 = "64bit"
    x86 = "32bit"


def get_uninstallers(bit: Bit) -> Dict[str, str]:
    uninstallers: Dict[str, str] = dict()

    if bit == Bit.x64:
        access = winreg.KEY_WOW64_64KEY | winreg.KEY_READ
    elif bit == Bit.x86:
        access = winreg.KEY_WOW64_32KEY | winreg.KEY_READ

    key = winreg.OpenKey(
        winreg.HKEY_LOCAL_MACHINE,
        "SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Uninstall",
        0,
        access,
    )

    for i in count():
        try:
            subkey = winreg.OpenKey(key, winreg.EnumKey(key, i), 0, access)
            name = None
            uninstallcmd = None
            for j in count():
                try:
                    k, v, _ = winreg.EnumValue(subkey, j)
                    if k == "DisplayName":
                        name = v
                    elif k == "UninstallString":
                        uninstallcmd = v
                except OSError as e:
                    if "WinError 259" not in str(e):
                        raise e
                    break
            if name is not None and uninstallcmd is not None:
                uninstallers[name] = uninstallcmd
        except OSError as e:
            if "WinError 259" not in str(e):
                raise e
            break

    return uninstallers


uninstallers = {**get_uninstallers(Bit.x86), **get_uninstallers(Bit.x64)}
