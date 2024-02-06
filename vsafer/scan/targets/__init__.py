from typing import List

from vsafer.types import ScanTarget

from vsafer.scan.targets.common import common_targets
import vsafer.scan.targets.crossexservice as crossexservice
import vsafer.scan.targets.dext5upload as dext5upload
import vsafer.scan.targets.ztransferx as ztransferx
import vsafer.scan.targets.crownix as crownix
import vsafer.scan.targets.rdviewer as rdviewer
import vsafer.scan.targets.ozweblauncher as ozweblauncher


targets: List[ScanTarget] = common_targets
if crossexservice.target is not None:
    targets.append(crossexservice.target)
targets.append(dext5upload.target)
targets += ztransferx.targets
targets.append(crownix.target)
targets.append(rdviewer.target)
targets.append(ozweblauncher.targets)
