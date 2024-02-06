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
        TargetPath(BasePath.System32, "RDVistaSupport.dll").join()
        # TODO: add more files
    ]
    for f in files:
        try:
            os.remove(f)
        except OSError:
            pass


target = ScanTarget(
    "Report Designer / CROWNIX Report",
    "리포팅 솔루션",
    TargetPath(BasePath.System32, "RDVistaSupport.dll"),
    None,
    TargetPath(BasePath.Root, "luigi"),
    [
        Vulnerability(
            "임의 코드 실행 취약점",
            VulnSource(
                "KISA 보안공지",
                "https://www.boho.or.kr/kr/bbs/view.do?searchCnd=1&bbsId=B0000133&searchWrd=&menuNo=205020&pageIndex=74&categoryCode=&nttId=25844",
            ),
            VersionRange(None, (1, 0, 0, 22)),
            (1, 0, 0, 23),
        ),
        Vulnerability(
            "임의 코드 실행 취약점",
            VulnSource(
                "KISA 보안공지",
                "https://www.boho.or.kr/kr/bbs/view.do?searchCnd=1&bbsId=B0000133&searchWrd=&menuNo=205020&pageIndex=74&categoryCode=&nttId=24464",
            ),
            VersionRange(None, (1, 0, 0, 19)),
            (1, 0, 0, 20),
        ),
    ],
)

target.uninstall = __uninstall  # type: ignore[method-assign]
