import os

from vsafer.types import (
    BasePath,
    ScanTarget,
    TargetPath,
    VersionRange,
    Vulnerability,
    VulnSource,
)


def __uninstall():
    print("rdviewer")
    files = [
        TargetPath(BasePath.System32, "rdviewer50.ocx").join(),
        # TODO: add more files
    ]
    for f in files:
        try:
            os.remove(f)
        except OSError:
            pass


target = ScanTarget(
    "Report Designer Viewer",
    "문서 열람 솔루션",
    TargetPath(BasePath.System32, "rdviewer50.ocx"),
    None,
    TargetPath(BasePath.Root, "luigi"),
    [
        Vulnerability(
            "메모리 커럽션 취약점",
            VulnSource(
                "KISA 보안공지",
                "https://www.boho.or.kr/kr/bbs/view.do?searchCnd=1&bbsId=B0000133&searchWrd=&menuNo=205020&pageIndex=74&categoryCode=&nttId=27684",
            ),
            VersionRange(None, (5, 0, 0, 604)),
            (5, 0, 0, 605),
        )
    ],
)

target.uninstall = __uninstall  # type: ignore[method-assign]
