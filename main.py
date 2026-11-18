"""news-image-20261118: write the entry image to the harness output dir.

The image (entry.png) is a newspaper front page summarising the world
news of Wednesday 18 November 2026. This program only copies it to the
path the harness names, so both runs produce identical bytes.
"""

import os
import shutil
from pathlib import Path


def main() -> None:
    here = Path(__file__).resolve().parent
    source = here / "entry.png"
    if not source.is_file():
        raise FileNotFoundError(f"entry image missing: {source}")
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "out")
    output_dir.mkdir(parents=True, exist_ok=True)
    target = output_dir / "entry.png"
    if target.resolve() != source.resolve():
        shutil.copyfile(source, target)


if __name__ == "__main__":
    main()
