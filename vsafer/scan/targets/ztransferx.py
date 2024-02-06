import os

from vsafer.types import (
    BasePath,
    ScanTarget,
    TargetPath,
    VersionRange,
    Vulnerability,
    VulnSource,
)

_OZVIEWER_VULNS = [
    Vulnerability(
        "원격 코드 실행 취약점",
        VulnSource(
            "KISA 보안공지",
            "https://www.boho.or.kr/kr/bbs/view.do?searchCnd=1&bbsId=B0000133&searchWrd=&menuNo=205020&pageIndex=32&categoryCode=&nttId=36475",
        ),
        VersionRange(None, (2, 2, 6, 3)),
        (2, 2, 6, 4),
    )
]


def __uninstall_32():
    try:
        os.remove(
            TargetPath(
                BasePath.ProgramFiles32, "Forcs\\OZ Family\\OZTransferX\\ZTransferX.ocx"
            ).join()
        )
    except OSError:
        pass


def __uninstall_64():
    try:
        os.remove(
            TargetPath(
                BasePath.ProgramFiles64,
                "Forcs\\OZ Family\\OZTransferX\\ZTransferX_64.ocx",
            ).join()
        )
    except OSError:
        pass


targets = [
    ScanTarget(
        "OZ Viewer ZtransferX (32비트)",
        "웹 리포팅 솔루션",
        TargetPath(
            BasePath.ProgramFiles32, "Forcs\\OZ Family\\OZTransferX\\ZTransferX.ocx"
        ),
        None,
        TargetPath(BasePath.Root, "luigi"),
        _OZVIEWER_VULNS,
    ),
    ScanTarget(
        "OZ Viewer ZtransferX (64비트)",
        "웹 리포팅 솔루션",
        TargetPath(
            BasePath.ProgramFiles64,
            "Forcs\\OZ Family\\OZTransferX\\ZTransferX_64.ocx",
        ),
        None,
        TargetPath(BasePath.Root, "luigi"),
        _OZVIEWER_VULNS,
    ),
]

targets[0].uninstall = __uninstall_32  # type: ignore[method-assign]
targets[1].uninstall = __uninstall_64  # type: ignore[method-assign]
