# Catàleg d'extensions d'IngeTrazo (moominot)

| Extensió | Codi |
|---|---|
| Render Studio | https://github.com/moominot/ingetrazo-render-studio |
| Render Studio Library | https://github.com/moominot/ingetrazo-skp-dc-import |
| Components paramètrics des de .skp | https://github.com/moominot/ingetrazo-skp-dc-import |
| Components dinàmics: opcions i fórmules | https://github.com/moominot/ingetrazo-skp-dc-import |

## Afegir-lo al gestor (IngeTrazo 0.6.3 o posterior)

**Extensions ▸ Gestiona les extensions… ▸ Sources…**

- **Per URL** (*Add catalog URL*), si el repositori és públic:
  `https://raw.githubusercontent.com/moominot/ingetrazo-cataleg/main/online/catalog.json`
- **Carpeta local** (*Add local folder*): tria la carpeta d'aquest clon.

> **Limitació del gestor:** si un `id` ja surt al catàleg oficial, la fitxa
> d'una font afegida s'ignora, encara que la versió sigui més nova. Les quatre
> extensions són al catàleg oficial, de manera que, mentre aquest es pugui
> carregar (en línia o des de la memòria cau), es veuen les versions oficials.

## Estructura

- `fitxes/<id>.toml`: les dades de cada extensió (l'única cosa que s'edita).
- `paquets/`: els ZIP exactes de cada publicació.
- `catalog.json`: catàleg per a la carpeta local (rutes relatives).
- `online/catalog.json`: catàleg per URL (adreces https).

## Publicar una versió nova

Canvia `version`, `download` i `sha256` a la fitxa i executa
(Python 3.11 o posterior):

    python tools/construeix.py

Cada extensió manté la seva llicència (GPL-3.0-or-later).
