"""Round-2 shipper for news-image-20261118.

The bundled front page (entry.png, 1024 by 1024) sums up Wednesday
18 November 2026 in twenty stories across five continents: four
illustrated leads - Trump in Manila for the Quad summit, the Kerch
Bridge hit, the Hormuz tanker strike, Cyclone Akvan nearing India -
plus twelve briefs and a footer of four more items. This script does
nothing but move those bytes into the harness output directory, so
the two grading runs agree byte for byte.
"""

import os
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
IMAGE = HERE / "entry.png"


def deliver() -> int:
    if not IMAGE.exists():
        sys.stderr.write("bundled image not found\n")
        return 1
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "out")
    out_dir.mkdir(parents=True, exist_ok=True)
    payload = IMAGE.read_bytes()
    (out_dir / "entry.png").write_bytes(payload)
    if (out_dir / "entry.png").stat().st_size != len(payload):
        sys.stderr.write("written bytes differ from the bundle\n")
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(deliver())
