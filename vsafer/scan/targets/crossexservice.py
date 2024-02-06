import os
import re

from vsafer.types import (
    BasePath,
    ScanTarget,
    TargetPath,
    Uninstaller,
    VersionRange,
    Vulnerability,
    VulnSource,
)


def __get_path():
    rel_path = "RaonSecure\\bridge\\CrossEX\\touchenex"
    p = TargetPath(BasePath.ProgramFiles32, rel_path)
    outer_path = p.join()
    dir_regex = re.compile("[0-9]+.[0-9]+.[0-9]+.[0-9]+")
    if not os.path.exists(outer_path):
        return None
    inner_dir = re.search(dir_regex, os.listdir(outer_path)[0])
    if inner_dir is None:
        return None
    inner_dir = inner_dir.group(0)
    filename = "npraontouchenex.dll"
    inner_path = os.path.join(rel_path, inner_dir, filename)
    p = TargetPath(BasePath.ProgramFiles32, inner_path)
    if not os.path.exists(p.join()):
        return None
    return inner_path


__path = __get_path()
if __path is None:
    target = None
else:
    target = ScanTarget(
        "CrossEXService",
        "키보드 보안 프로그램",
        TargetPath(BasePath.ProgramFiles32, __path),
        (
            TargetPath(
                BasePath.ProgramFiles32,
                "RaonSecure\\bridge\\CrossEX\\touchenex\\UninstallCrossEX.exe",
            ).join()
        ),
        TargetPath(BasePath.Root, "luigi"),
        [
            Vulnerability(
                "크로스 사이트 스크립팅 취약점 등",
                VulnSource(
                    "KISA 보안공지",
                    "https://boho.or.kr/kr/bbs/view.do?searchCnd=1&bbsId=B0000133&searchWrd=&menuNo=205020&pageIndex=1&categoryCode=&nttId=67136",
                ),
                VersionRange(None, (1, 0, 2, 9)),
                (1, 0, 2, 10),
            )
        ],
    )
