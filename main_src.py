# ai-happy-01 entry: copies the bundled image to /output/entry.png.
# No network; two runs write the same bytes; the copy is guarded by the 1 MiB gate.
import os
from pathlib import Path
import shutil

OUTPUT_DIR = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

src = Path(__file__).with_name("entry.png")
size = src.stat().st_size
if size > 1024 * 1024:
    raise SystemExit("entry.png exceeds the 1 MiB gate")
shutil.copyfile(src, OUTPUT_DIR / "entry.png")
