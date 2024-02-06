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
    files = [
        TargetPath(BasePath.System32, "dext5.ocx").join(),
        TargetPath(BasePath.System32, "dext5broker.exe").join(),
    ]
    for f in files:
        try:
            os.remove(f)
        except OSError:
            pass


target = ScanTarget(
    "DEXT5 Upload",
    "대용량 파일 전송 솔루션",
    TargetPath(BasePath.System32, "dext5.ocx"),
    None,
    TargetPath(BasePath.Root, "luigi"),
    [
        Vulnerability(
            "원격 코드 실행 취약점",
            VulnSource(
                "KISA 보안공지",
                "https://boho.or.kr/kr/bbs/view.do?searchCnd=1&bbsId=B0000133&searchWrd=&menuNo=205020&pageIndex=85&categoryCode=&nttId=30080",
            ),
            VersionRange(None, (5, 0, 0, 104)),
            (5, 0, 0, 105),
        ),
    ],
)

target.uninstall = __uninstall  # type: ignore[method-assign]
