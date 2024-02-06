import os
from typing import Dict, List, Tuple

from win32api import GetFileVersionInfo, LOWORD, HIWORD

import vsafer.scan.targets as scantargets
from vsafer.utils import python_bits
from vsafer.types import BasePath, TargetPath, Version, Vulnerability, ScanResult


def __get_installed_ver(path: TargetPath) -> Version:
    filepath = path.join()
    version = GetFileVersionInfo(filepath, "\\")
    ms = version["FileVersionMS"]
    ls = version["FileVersionLS"]
    return (HIWORD(ms), LOWORD(ms), HIWORD(ls), LOWORD(ls))


def __is_vulnerable(system_ver: Version, vuln: Vulnerability) -> bool:
    for i, v in enumerate(system_ver):
        if v < vuln.affected_range.high[i]:
            if vuln.affected_range.low is None:
                return True
            elif v > vuln.affected_range.low[i]:
                return True
            elif v < vuln.affected_range.low[i]:
                return False
        elif v > vuln.affected_range.high[i]:
            return False
    return True


def __is_installed(path: TargetPath) -> bool:
    filepath = path.join()
    return os.path.exists(filepath)


def scan_all() -> List[ScanResult]:
    detected: List[ScanResult] = list()
    for target in scantargets.targets:
        path = target.scan_path
        if path.base == BasePath.ProgramFiles64 and python_bits() == "32bit":
            continue
        if not __is_installed(path):
            continue
        system_ver = __get_installed_ver(path)
        vulns_found: List[Vulnerability] = list()
        for vuln in target.vulnerabilities:
            if __is_vulnerable(system_ver, vuln):
                vulns_found.append(vuln)
        if len(vulns_found) > 0:
            res = ScanResult(target, system_ver, vulns_found)
            detected.append(res)
    return detected
