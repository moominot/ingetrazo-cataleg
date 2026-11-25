#!/usr/bin/env python3
"""Descarrega els paquets de les fitxes i genera els dos catàlegs.

    python tools/construeix.py

catalog.json         rutes relatives, per afegir aquest clon com a carpeta local
online/catalog.json  adreces https, per afegir-lo com a catàleg per URL

Per publicar una versió nova: canvia version, download i sha256 a la fitxa.
"""
import hashlib
import json
import tomllib
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
FIELDS = ("id", "version", "author", "license", "repository", "download",
          "sha256", "ingetrazo", "name", "summary", "tags")


def package(entry):
    path = ROOT / "paquets" / entry["download"].rsplit("/", 1)[-1]
    if path.is_file():
        data = path.read_bytes()
    else:
        request = urllib.request.Request(
            entry["download"], headers={"User-Agent": "catalog-builder"})
        with urllib.request.urlopen(request, timeout=60) as response:
            data = response.read()
    if hashlib.sha256(data).hexdigest() != entry["sha256"]:
        raise SystemExit(f"{entry['id']}: el sha256 no coincideix")
    path.write_bytes(data)
    return path


def write(path, entries):
    text = json.dumps({"format": 1, "extensions": entries},
                      ensure_ascii=False, indent=1)
    path.write_text(text + "\n", encoding="utf-8", newline="\n")


def main():
    local, online, used = [], [], set()
    for file in sorted((ROOT / "fitxes").glob("*.toml")):
        entry = tomllib.loads(file.read_text(encoding="utf-8"))
        path = package(entry)
        used.add(path.name)
        item = {key: entry[key] for key in FIELDS}
        online.append(item)
        local.append({**item, "download": f"paquets/{path.name}"})
    for old in (ROOT / "paquets").glob("*.zip"):
        if old.name not in used:
            old.unlink()
    write(ROOT / "catalog.json", local)
    write(ROOT / "online" / "catalog.json", online)
    print(f"{len(local)} extensions")


if __name__ == "__main__":
    main()
