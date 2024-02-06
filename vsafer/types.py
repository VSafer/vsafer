import os
import subprocess

from dataclasses import dataclass
from enum import Enum, auto
from typing import Optional, List, Tuple

from vsafer.utils import python_bits


class BasePath(Enum):
    ProgramFiles64 = auto()
    ProgramFiles32 = auto()
    System64 = auto()
    System32 = auto()
    AppData = auto()
    LocalAppData = auto()
    LocalLow = auto()
    Root = auto()


@dataclass
class TargetPath:
    base: BasePath
    rel: str

    def join(self):
        if self.base == BasePath.ProgramFiles64:
            if python_bits() == "32bit":
                # raise ValueError(
                #     f"Can't look up {self.rel} in 64bit Program Files directory on 32bit machine"
                # )
                # this error gets handled on gui/main.py. need to tidy up code later.
                dirname = os.environ["PROGRAMFILES"]
            else:
                dirname = os.environ["PROGRAMFILES"]
        elif self.base == BasePath.ProgramFiles32:
            if python_bits() == "64bit":
                dirname = os.environ["PROGRAMFILES(X86)"]
            else:
                dirname = os.environ["PROGRAMFILES"]
        elif self.base == BasePath.System64:
            if python_bits() == "32bit":
                # raise ValueError(
                #     f"Can't look up {self.rel} in 64bit System directory on 32bit machine"
                # )
                # this error gets handled on gui/main.py. need to tidy up code later.
                dirname = os.environ["PROGRAMFILES"]
            windir = os.environ["WINDIR"]
            dirname = os.path.join(windir, "System32")
        elif self.base == BasePath.System32:
            windir = os.environ["WINDIR"]
            if python_bits() == "32bit":
                dirname = os.path.join(windir, "System32")
            else:
                dirname = os.path.join(windir, "SysWOW64")
        elif self.base == BasePath.AppData:
            dirname = os.environ["APPDATA"]
        elif self.base == BasePath.LocalAppData:
            dirname = os.environ["LOCALAPPDATA"]
        elif self.base == BasePath.LocalLow:
            dirname = os.environ["LOCALAPPDATA"] + "Low"
        elif self.base == BasePath.Root:
            dirname = os.path.abspath(os.sep)

        return os.path.join(dirname, self.rel)


@dataclass
class Uninstaller:
    executable: TargetPath
    args: Tuple[str, ...]


@dataclass
class VulnSource:
    name: str
    url: str


Version = Tuple[int, ...]


@dataclass
class VersionRange:
    low: Optional[Version]
    high: Version


@dataclass
class Vulnerability:
    name: str
    source: VulnSource
    affected_range: VersionRange
    resolved_version: Version


@dataclass
class ScanTarget:
    name: str
    description: str
    scan_path: TargetPath
    uninstaller: Optional[Tuple[str, ...]]
    quarantine_path: TargetPath
    vulnerabilities: List[Vulnerability]

    def uninstall(self) -> None:
        if self.uninstaller is None:
            raise FileNotFoundError("uninstaller is not defined")
        # TODO: xplatform extcommon api identical exe
        if not os.path.exists(self.uninstaller[0]):
            return
        subprocess.run(self.uninstaller)


@dataclass
class ScanResult:
    target: ScanTarget
    system_ver: Version
    vulns_found: List[Vulnerability]
