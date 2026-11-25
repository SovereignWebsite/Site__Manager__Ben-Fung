import os, importlib
R = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "site")
OUT = {"d1_path": "index.html", "d2_departures": "designs/departures/index.html", "d3_plan": "designs/programme-plan/index.html",
       "d4_line": "designs/line-map/index.html", "d5_broadsheet": "designs/broadsheet/index.html", "gallery": "designs/index.html"}
for mod, path in OUT.items():
    p = os.path.join(R, path); os.makedirs(os.path.dirname(p), exist_ok=True)
    open(p, "w").write(importlib.import_module(mod).page()); print("wrote", path)

# /progress/ is written by hand (by the reporter agent); refresh its copy of the design picker too.
import re, sys
from common import switcher
p = os.path.join(R, "progress", "index.html")
if os.path.exists(p):
    t = open(p).read()
    open(p, "w").write(re.sub(r'<nav class="designs".*?</nav>', switcher(""), t, count=1, flags=re.S)); print("refreshed progress/index.html picker")
