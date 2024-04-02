from typing import List
from vsafer.types import (
    BasePath,
    ScanTarget,
    TargetPath,
    VersionRange,
    Vulnerability,
    VulnSource,
)

_VERAPORT_VULNS: List[Vulnerability] = [
    Vulnerability(
        "정보 노출 취약점 등",
        VulnSource(
            "KISA 보안공지",
            "https://boho.or.kr/kr/bbs/view.do?searchCnd=1&bbsId=B0000133&searchWrd=&menuNo=205020&pageIndex=1&categoryCode=&nttId=67136",
        ),
        VersionRange((3, 7, 0, 2), (3, 8, 6, 3)),
        (3, 8, 6, 4),
    ),
    Vulnerability(
        "원격 코드 실행 취약점",
        VulnSource(
            "KISA 보안공지",
            "https://boho.or.kr/kr/bbs/view.do?searchCnd=1&bbsId=B0000133&searchWrd=&menuNo=205020&pageIndex=1&categoryCode=&nttId=35794",
        ),
        VersionRange(None, (3, 8, 5, 0)),
        (3, 8, 5, 1),
    ),
    Vulnerability(
        "경쟁 상태 취약점",
        VulnSource(
            "KISA 보안공지",
            "https://boho.or.kr/kr/bbs/view.do?searchCnd=1&bbsId=B0000133&searchWrd=&menuNo=205020&pageIndex=1&categoryCode=&nttId=30109",
        ),
        VersionRange(None, (3, 7, 3, 3)),
        (3, 7, 3, 4),
    ),
    Vulnerability(
        "원격 코드 실행 취약점",
        VulnSource(
            "KISA 보안공지",
            "https://boho.or.kr/kr/bbs/view.do?searchCnd=1&bbsId=B0000133&searchWrd=&menuNo=205020&pageIndex=1&categoryCode=&nttId=30109",
        ),
        VersionRange(None, (3, 7, 3, 3)),
        (3, 7, 3, 4),
    ),
]

_XPLATFORM_EXTCOMMON_VULNS: List[Vulnerability] = [
    Vulnerability(
        "임의 코드 실행 취약점",
        VulnSource(
            "KISA 보안공지",
            "https://www.boho.or.kr/kr/bbs/view.do?searchCnd=1&bbsId=B0000133&searchWrd=&menuNo=205020&pageIndex=1&categoryCode=&nttId=30095",
        ),
        VersionRange(None, (2018, 11, 20, 0)),
        (2018, 12, 13, 1),
    ),
    Vulnerability(
        "임의 파일 생성 취약점",
        VulnSource(
            "투비소프트 매뉴얼",
            "http://docs.tobesoft.com/vulnerability_guide/e9af76d8074a59e9#c02c11092389d84b",
        ),
        VersionRange(None, (2019, 9, 6, 0)),
        (2018, 9, 6, 1),
    ),
    Vulnerability(
        "레지스트리 변조 취약점",
        VulnSource(
            "투비소프트 매뉴얼",
            "http://docs.tobesoft.com/vulnerability_guide/e9af76d8074a59e9#0735e99a839a4a24",
        ),
        VersionRange(None, (2019, 9, 6, 0)),
        (2018, 9, 6, 1),
    ),
]

_XPLATFORM_VULNS: List[Vulnerability] = [
    Vulnerability(
        "원격 코드 실행 취약점",
        VulnSource(
            "투비소프트 매뉴얼",
            "http://docs.tobesoft.com/vulnerability_guide/e9af76d8074a59e9#b4ff9a9afc95165a",
        ),
        VersionRange(None, (2019, 2, 26, 0)),
        (2019, 2, 26, 1),
    ),
    Vulnerability(
        "원격 코드 실행 취약점",
        VulnSource(
            "투비소프트 매뉴얼",
            "http://docs.tobesoft.com/vulnerability_guide/e9af76d8074a59e9#20b171be35e6fb65",
        ),
        VersionRange(None, (2019, 2, 26, 0)),
        (2019, 2, 26, 1),
    ),
    Vulnerability(
        "파일 다운로드 및 실행 취약점",
        VulnSource(
            "투비소프트 매뉴얼",
            "http://docs.tobesoft.com/vulnerability_guide/e9af76d8074a59e9#76d441b28c0f140d",
        ),
        VersionRange(None, (2019, 8, 27, 0)),
        (2019, 8, 27, 1),
    ),
    Vulnerability(
        "임의 코드 실행 취약점",
        VulnSource(
            "투비소프트 매뉴얼",
            "http://docs.tobesoft.com/vulnerability_guide/e9af76d8074a59e9#612b3abd343a18ba",
        ),
        VersionRange(None, (2019, 8, 27, 0)),
        (2019, 8, 27, 1),
    ),
]

common_targets: List[ScanTarget] = [
    ScanTarget(
        "AnySign for PC",
        "공동인증서/전자서명 솔루션",
        TargetPath(
            BasePath.ProgramFiles32,
            "C:\\Program Files (x86)\\Battle.net\\Battle.net.exe",
        ),
        None,
        TargetPath(BasePath.Root, "luigi"),
        [
            Vulnerability(
                "파일 다운로드 취약점",
                VulnSource(
                    "KISA 보안공지",
                    "https://www.boho.or.kr/kr/bbs/view.do?searchCnd=1&bbsId=B0000133&searchWrd=&menuNo=205020&pageIndex=1&categoryCode=&nttId=35011",
                ),
                VersionRange(None, (9999, 1, 1, 6)),
                (1, 1, 2, 0),
            )
        ],
    ),
    ScanTarget(
        "DEXTUploadX5",
        "파일 업/다운로드 솔루션",
        TargetPath(
            BasePath.ProgramFiles32,
            "DEVPIA\\DEXTUploadX5 ActiveX\\dextuploadx5-ax.dll",
        ),
        (
            TargetPath(
                BasePath.ProgramFiles32,
                "DEVPIA\\DEXTUploadX5 ActiveX\\DEXTUploadX5 ActiveX UnInstaller.exe",
            ).join(),
        ),
        TargetPath(BasePath.Root, "luigi"),
        [
            Vulnerability(
                "원격 코드 실행 취약점",
                VulnSource(
                    "KISA 보안공지",
                    "https://boho.or.kr/kr/bbs/view.do?searchCnd=1&bbsId=B0000133&searchWrd=&menuNo=205020&pageIndex=85&categoryCode=&nttId=30092",
                ),
                VersionRange((1, 0, 0, 0), (2, 2, 0, 0)),
                (2, 2, 1, 0),
            )
        ],
    ),
    ScanTarget(
        "Magic Line V4.0",
        "전자서명 및 웹구간 암호화 솔루션",
        TargetPath(
            BasePath.ProgramFiles32, "DreamSecurity\\MagicLine4NX\\MagicLine4NX.exe"
        ),
        (
            TargetPath(
                BasePath.ProgramFiles32,
                "DreamSecurity\\MagicLine4NX\\MagicLine4NX_Uninstall.exe",
            ).join(),
        ),
        TargetPath(BasePath.Root, "luigi"),
        [
            Vulnerability(
                "버퍼 오버플로우 취약점",
                VulnSource(
                    "KISA 보안공지",
                    "https://www.boho.or.kr/kr/bbs/view.do?searchCnd=1&bbsId=B0000133&searchWrd=&menuNo=205020&pageIndex=2&categoryCode=&nttId=71023",
                ),
                VersionRange((1, 0, 0, 1), (1, 0, 0, 26)),
                (1, 0, 0, 27),
            ),
            Vulnerability(
                "버퍼 오버플로우 취약점",
                VulnSource(
                    "KISA 보안공지",
                    "https://www.boho.or.kr/kr/bbs/view.do?searchCnd=1&bbsId=B0000133&searchWrd=&menuNo=205020&pageIndex=2&categoryCode=&nttId=36219",
                ),
                VersionRange(None, (1, 0, 0, 17)),
                (1, 0, 0, 18),
            ),
        ],
    ),
    ScanTarget(
        "TouchEn nxKey",
        "키보드 보안 프로그램",
        TargetPath(BasePath.ProgramFiles32, "RaonSecure\\TouchEn nxKey\\TKMain.dll"),
        (
            TargetPath(BasePath.System32, "CKSetup32.exe").join(),
            "/uninstall",
            "appm",
        ),
        TargetPath(BasePath.Root, "luigi"),
        [
            Vulnerability(
                "크로스 사이트 스크립팅 취약점 등",
                VulnSource(
                    "KISA 보안공지",
                    "https://boho.or.kr/kr/bbs/view.do?searchCnd=1&bbsId=B0000133&searchWrd=&menuNo=205020&pageIndex=1&categoryCode=&nttId=67136",
                ),
                VersionRange(None, (1, 0, 0, 78)),
                (1, 0, 0, 82),
            )
        ],
    ),
    ScanTarget(
        "CrossEXService",
        "웹 환경 플러그인",
        TargetPath(BasePath.ProgramFiles32, "iniLINE\\CrossEX\\crossex\\CrossEXService.exe"),
        (
            TargetPath(BasePath.ProgramFiles32, "iniLINE\\CrossEX\\crossex\\UninstallCrossEXLocal.exe").join(),
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
    ),
    ScanTarget(
        "INISAFE CrossWeb EX V3",
        "공동인증서/전자서명 솔루션",
        TargetPath(
            BasePath.ProgramFiles32,
            "INITECH\\INISAFE Web EX Client\\INIExtensionVer.dll",
        ),
        (
            TargetPath(
                BasePath.ProgramFiles32, "INITECH\\INISAFE Web EX Client\\UnINIS_EX.exe"
            ).join(),
        ),
        TargetPath(BasePath.Root, "luigi"),
        [
            Vulnerability(
                "미공개 취약점",
                VulnSource(
                    "KISA 보안공지",
                    "https://boho.or.kr/kr/bbs/view.do?searchCnd=1&bbsId=B0000133&searchWrd=&menuNo=205020&pageIndex=2&categoryCode=&nttId=71030",
                ),
                VersionRange(None, (3, 3, 2, 40)),
                (3, 3, 2, 41),
            ),
            Vulnerability(
                "무결성 검증 우회 취약점",
                VulnSource(
                    "KISA 보안공지",
                    "https://boho.or.kr/kr/bbs/view.do?searchCnd=1&bbsId=B0000133&searchWrd=&menuNo=205020&pageIndex=2&categoryCode=&nttId=24787",
                ),
                VersionRange(None, (1, 0, 0, 43)),
                (1, 0, 0, 44),
            ),
        ],
    ),
    ScanTarget(
        "INISAFE MoaSign EX v1.0",
        "공인인증서 솔루션",
        TargetPath(
            BasePath.ProgramFiles32,
            "INITECH\\INISAFE MoaSign EX\\INISAFEMoaSignEX.exe",
        ),
        (
            TargetPath(
                BasePath.ProgramFiles32, "INITECH\\INISAFE MoaSign EX\\uninst.exe"
            ).join(),
        ),
        TargetPath(BasePath.Root, "luigi"),
        [
            Vulnerability(
                "무결성 검증 우회 취약점",
                VulnSource(
                    "KISA 보안공지",
                    "https://www.boho.or.kr/kr/bbs/view.do?searchCnd=1&bbsId=B0000133&searchWrd=&menuNo=205020&pageIndex=1&categoryCode=&nttId=24787",
                ),
                VersionRange(None, (1, 0, 0, 15)),
                (1, 0, 0, 16),
            )
        ],
    ),
    ScanTarget(
        "INISAFE MoaSign S v1.0",
        "공인인증서 솔루션",
        TargetPath(
            BasePath.ProgramFiles32,
            "INITECH\\INISAFE MoaSignS\\INISAFEMoaSignS.exe",
        ),
        (
            TargetPath(
                BasePath.ProgramFiles32, "INITECH\\INISAFE MoaSignS\\uninst.exe"
            ).join(),
        ),
        TargetPath(BasePath.Root, "luigi"),
        [
            Vulnerability(
                "무결성 검증 우회 취약점",
                VulnSource(
                    "KISA 보안공지",
                    "https://www.boho.or.kr/kr/bbs/view.do?searchCnd=1&bbsId=B0000133&searchWrd=&menuNo=205020&pageIndex=1&categoryCode=&nttId=24787",
                ),
                VersionRange(None, (1, 0, 0, 44)),
                (1, 0, 0, 45),
            ),
        ],
    ),
    ScanTarget(
        "INISAFE SFilter",
        "키보드 보안 프로그램",
        TargetPath(BasePath.ProgramFiles32, "INITECH\\SHTTP\\INIUpdater.ocx"),
        (TargetPath(BasePath.ProgramFiles32, "INITECH\\SHTTP\\uninst.exe").join(),),
        TargetPath(BasePath.Root, "luigi"),
        [
            Vulnerability(
                "무결성 검증 우회 취약점",
                VulnSource(
                    "KISA 보안공지",
                    "https://www.boho.or.kr/kr/bbs/view.do?searchCnd=1&bbsId=B0000133&searchWrd=&menuNo=205020&pageIndex=1&categoryCode=&nttId=24787",
                ),
                VersionRange(None, (7, 2, 0, 13)),
                (7, 2, 0, 14),
            ),
        ],
    ),
    ScanTarget(
        "INISAFE Web V6",
        "웹 보안 솔루션",
        TargetPath(
            BasePath.ProgramFiles32,
            "INITECH\\INISAFE Web V6\\INISAFEWeb60.dll",
        ),
        (
            TargetPath(
                BasePath.ProgramFiles32, "INITECH\\INISAFE Web V6\\UnINIS61.exe"
            ).join(),
        ),
        TargetPath(BasePath.Root, "luigi"),
        [
            Vulnerability(
                "무결성 검증 우회 취약점",
                VulnSource(
                    "KISA 보안공지",
                    "https://www.boho.or.kr/kr/bbs/view.do?searchCnd=1&bbsId=B0000133&searchWrd=&menuNo=205020&pageIndex=1&categoryCode=&nttId=24787",
                ),
                VersionRange(None, (6, 4, 0, 87)),
                (6, 4, 0, 88),
            ),
        ],
    ),
    ScanTarget(
        "INISAFE Web V6.4",
        "웹 보안 솔루션",
        TargetPath(
            BasePath.ProgramFiles32,
            "INITECH\\INISAFE Web Client v6.4\\INISAFEWeb60.dll",
        ),
        (
            TargetPath(
                BasePath.ProgramFiles32,
                "INITECH\\INISAFE Web Client v6.4\\UnINIS64.exe",
            ).join(),
        ),
        TargetPath(BasePath.Root, "luigi"),
        [
            Vulnerability(
                "무결성 검증 우회 취약점",
                VulnSource(
                    "KISA 보안공지",
                    "https://www.boho.or.kr/kr/bbs/view.do?searchCnd=1&bbsId=B0000133&searchWrd=&menuNo=205020&pageIndex=1&categoryCode=&nttId=24787",
                ),
                VersionRange(None, (6, 4, 0, 87)),
                (6, 4, 0, 88),
            ),
        ],
    ),
    ScanTarget(
        "IPinside LWS",
        "PC 정보 수집 프로그램",
        TargetPath(BasePath.ProgramFiles32, "IPinside_LWS\\I3GManager.dll"),
        (
            TargetPath(
                BasePath.ProgramFiles32, "IPinside_LWS\\I3GSvcManager.exe"
            ).join(),
            "/uninstall",
        ),
        TargetPath(BasePath.Root, "luigi"),
        [
            Vulnerability(
                "서비스 거부 취약점 등",
                VulnSource(
                    "KISA 보안공지",
                    "https://boho.or.kr/kr/bbs/view.do?searchCnd=1&bbsId=B0000133&searchWrd=&menuNo=205020&pageIndex=1&categoryCode=&nttId=67136",
                ),
                VersionRange(None, (3, 0, 0, 18)),
                (3, 0, 0, 19),
            )
        ],
    ),
    ScanTarget(
        "REXPERT Viewer",
        "리포팅 솔루션",
        TargetPath(
            BasePath.ProgramFiles32,
            "clipsoft\\rexpert30\\bin\\viewer\\rexviewer30.exe",
        ),
        (
            TargetPath(
                BasePath.ProgramFiles32,
                "clipsoft\\rexpert30\\bin\\viewer\\uninstall.rexpert30viewer.exe",
            ).join(),
        ),
        TargetPath(BasePath.Root, "luigi"),
        [
            Vulnerability(
                "정보 노출 취약점",
                VulnSource(
                    "KISA 보안공지",
                    "https://www.boho.or.kr/kr/bbs/view.do?searchCnd=1&bbsId=B0000133&searchWrd=&menuNo=205020&pageIndex=74&categoryCode=&nttId=35186",
                ),
                VersionRange(None, (1, 0, 0, 527)),
                (1, 0, 0, 528),
            ),
            Vulnerability(
                "임의 파일 생성 및 실행 취약점",
                VulnSource(
                    "KISA 보안공지",
                    "https://www.boho.or.kr/kr/bbs/view.do?searchCnd=1&bbsId=B0000133&searchWrd=&menuNo=205020&pageIndex=74&categoryCode=&nttId=35186",
                ),
                VersionRange(None, (1, 0, 0, 527)),
                (1, 0, 0, 528),
            ),
            Vulnerability(
                "임의 파일 삭제 취약점",
                VulnSource(
                    "KISA 보안공지",
                    "https://www.boho.or.kr/kr/bbs/view.do?searchCnd=1&bbsId=B0000133&searchWrd=&menuNo=205020&pageIndex=74&categoryCode=&nttId=35186",
                ),
                VersionRange(None, (1, 0, 0, 527)),
                (1, 0, 0, 528),
            ),
        ],
    ),
    ScanTarget(
        "SKCertService",
        "공동인증서 솔루션",
        TargetPath(BasePath.ProgramFiles32, "SignKorea\\skcert\\SKCertService.exe"),
        (
            TargetPath(BasePath.ProgramFiles32, "SignKorea\\SetupPkg.exe").join(),
            "-us",
        ),
        TargetPath(BasePath.Root, "luigi"),
        [
            Vulnerability(
                "원격 파일 저장 취약점",
                VulnSource(
                    "KISA 보안공지",
                    "https://www.boho.or.kr/kr/bbs/view.do?searchCnd=1&bbsId=B0000133&searchWrd=&menuNo=205020&pageIndex=84&categoryCode=&nttId=30118",
                ),
                VersionRange((2, 3, 0), (2, 5, 5)),
                (2, 5, 8),
            )
        ],
    ),
    ScanTarget(
        "Veraport V3 (32비트)",
        "통합 설치 관리 프로그램",
        # TODO: Check if multiple version can coexist
        TargetPath(BasePath.ProgramFiles32, "Wizvera\\Veraport20\\veraportmain20.exe"),
        (
            TargetPath(
                BasePath.ProgramFiles32, "Wizvera\\Veraport20\\unins000.exe"
            ).join(),
        ),
        TargetPath(BasePath.Root, "luigi"),
        _VERAPORT_VULNS,
    ),
    ScanTarget(
        "Veraport V3 (64비트)",
        "통합 설치 관리 프로그램",
        TargetPath(BasePath.ProgramFiles64, "Wizvera\\Veraport20\\veraportmain20.exe"),
        (
            TargetPath(
                BasePath.ProgramFiles64, "Wizvera\\Veraport20\\unins000.exe"
            ).join(),
        ),
        TargetPath(BasePath.Root, "luigi"),
        _VERAPORT_VULNS,
    ),
    ScanTarget(
        "VestCert",
        "공동인증서/전자서명 솔루션",
        TargetPath(BasePath.ProgramFiles32, "VestCert\\VestCert.exe"),
        (
            TargetPath(BasePath.ProgramFiles32, "SetupPkg.exe").join(),
            "-uv",
        ),
        TargetPath(BasePath.Root, "luigi"),
        [
            Vulnerability(
                "원격 코드 실행 취약점",
                VulnSource(
                    "KISA 보안공지",
                    "https://www.boho.or.kr/kr/bbs/view.do?searchCnd=1&bbsId=B0000133&searchWrd=&menuNo=205020&pageIndex=1&categoryCode=&nttId=71008",
                ),
                VersionRange((2, 3, 6, 0), (2, 5, 29, 0)),
                (2, 5, 30, 0),
            )
        ],
    ),
    ScanTarget(
        "XPLATFORM 9.1 ExtCommon API",
        "프론트엔드 솔루션",
        TargetPath(
            BasePath.LocalLow, "TOBESOFT\\XPLATFORM\\9.1\\Component\\ExtCommon.dll"
        ),
        (
            TargetPath(
                BasePath.ProgramFiles32, "TOBESOFT\\XPLATFORM\\9.1\\unins000.exe"
            ).join(),
        ),
        TargetPath(BasePath.Root, "luigi"),
        _XPLATFORM_EXTCOMMON_VULNS,
    ),
    ScanTarget(
        "XPLATFORM 9.2 ExtCommon API",
        "프론트엔드 솔루션",
        TargetPath(
            BasePath.LocalLow, "TOBESOFT\\XPLATFORM\\9.2.0\\Component\\ExtCommon.dll"
        ),
        # WTF? its 9.2 below
        (
            TargetPath(
                BasePath.ProgramFiles32,
                "TOBESOFT\\XPLATFORM\\9.2\\XPEngineUninstaller.exe",
            ).join(),
        ),
        TargetPath(BasePath.Root, "luigi"),
        _XPLATFORM_EXTCOMMON_VULNS,
    ),
    ScanTarget(
        "XPLATFORM 9.2.1 ExtCommon API",
        "프론트엔드 솔루션",
        TargetPath(
            BasePath.LocalLow, "TOBESOFT\\XPLATFORM\\9.2.1\\Component\\ExtCommon.dll"
        ),
        (
            TargetPath(
                BasePath.ProgramFiles32,
                "TOBESOFT\\XPLATFORM\\9.2.1\\XPEngineUninstaller.exe",
            ).join(),
        ),
        TargetPath(BasePath.Root, "luigi"),
        _XPLATFORM_EXTCOMMON_VULNS,
    ),
    ScanTarget(
        "XPLATFORM 9.2.2 ExtCommon API",
        "프론트엔드 솔루션",
        TargetPath(
            BasePath.LocalLow, "TOBESOFT\\XPLATFORM\\9.2.2\\Component\\ExtCommon.dll"
        ),
        (
            TargetPath(
                BasePath.ProgramFiles32,
                "TOBESOFT\\XPLATFORM\\9.2.2\\XPEngineUninstaller.exe",
            ).join(),
        ),
        TargetPath(BasePath.Root, "luigi"),
        _XPLATFORM_EXTCOMMON_VULNS,
    ),
    ScanTarget(
        "XPLATFORM 9.1",
        "프론트엔드 솔루션",
        TargetPath(BasePath.ProgramFiles32, "TOBESOFT\\XPLATFORM\\9.1\\XPlatform.exe"),
        (
            TargetPath(
                BasePath.ProgramFiles32, "TOBESOFT\\XPLATFORM\\9.1\\unins000.exe"
            ).join(),
        ),
        TargetPath(BasePath.Root, "luigi"),
        _XPLATFORM_VULNS,
    ),
    ScanTarget(
        "XPLATFORM 9.2",
        "프론트엔드 솔루션",
        TargetPath(BasePath.ProgramFiles32, "TOBESOFT\\XPLATFORM\\9.2\\XPlatform.exe"),
        (
            TargetPath(
                BasePath.ProgramFiles32,
                "TOBESOFT\\XPLATFORM\\9.2\\XPEngineUninstaller.exe",
            ).join(),
        ),
        TargetPath(BasePath.Root, "luigi"),
        _XPLATFORM_VULNS,
    ),
    ScanTarget(
        "XPLATFORM 9.2.1",
        "프론트엔드 솔루션",
        TargetPath(
            BasePath.ProgramFiles32, "TOBESOFT\\XPLATFORM\\9.2.1\\XPlatform.exe"
        ),
        (
            TargetPath(
                BasePath.ProgramFiles32,
                "TOBESOFT\\XPLATFORM\\9.2.1\\XPEngineUninstaller.exe",
            ).join(),
        ),
        TargetPath(BasePath.Root, "luigi"),
        _XPLATFORM_VULNS,
    ),
    ScanTarget(
        "XPLATFORM 9.2.2",
        "프론트엔드 솔루션",
        TargetPath(
            BasePath.ProgramFiles32, "TOBESOFT\\XPLATFORM\\9.2.2\\XPlatform.exe"
        ),
        (
            TargetPath(
                BasePath.ProgramFiles32,
                "TOBESOFT\\XPLATFORM\\9.2.2\\XPEngineUninstaller.exe",
            ).join(),
        ),
        TargetPath(BasePath.Root, "luigi"),
        _XPLATFORM_VULNS,
    ),
]
