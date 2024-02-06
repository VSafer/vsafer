import os
import subprocess

from vsafer.types import (
    BasePath,
    ScanTarget,
    TargetPath,
    VersionRange,
    Vulnerability,
    VulnSource,
)
from vsafer.scan.uninstallers import uninstallers


def __uninstall():
    args = uninstallers["OZWebLauncher"]
    subprocess.run(args)


targets = ScanTarget(
    "OZ Web Launcher",
    "웹 리포팅 솔루션",
    TargetPath(BasePath.ProgramFiles32, "Forcs\\OZWebLauncher\\OZWebLauncher.exe"),
    None,
    TargetPath(BasePath.Root, "luigi"),
    [
        Vulnerability(
            "원격 코드 실행 취약점",
            VulnSource(
                "KISA 보안공지",
                "https://www.boho.or.kr/kr/bbs/view.do?searchCnd=1&bbsId=B0000133&searchWrd=&menuNo=205020&pageIndex=32&categoryCode=&nttId=36475",
            ),
            VersionRange(None, (80, 2022, 304, 99)),
            (80, 2022, 304, 100),
        )
    ],
)

targets.uninstall = __uninstall  # type: ignore[method-assign]
