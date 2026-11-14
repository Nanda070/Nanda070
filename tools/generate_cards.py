"""Generates the project cards and the toolbox strip for the profile README.

Writes assets/cards/<id>-dark.svg / -light.svg and assets/toolbox-dark.svg / -light.svg.
Same look as the banner (generate_profile_assets.py): terminal panels in the adnan070.me palette.
No dependencies:  python tools/generate_cards.py
"""
from __future__ import annotations

import html
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "assets" / "cards"
OUT.mkdir(parents=True, exist_ok=True)

SANS = "Inter,Segoe UI,Helvetica,Arial,sans-serif"
MONO = "ui-monospace,SFMono-Regular,Menlo,Consolas,monospace"

THEMES = {
    "dark": dict(bg="#060913", panel="#0C1222", border="#1F2A47", text="#E9EEFC", muted="#8793B3",
                 signal="#7C9BFF", mint="#5BF5B0", flare="#FF6B9A", chip="#111A30"),
    "light": dict(bg="#F5F7FF", panel="#FFFFFF", border="#CDD5EE", text="#0C1222", muted="#4D5B85",
                  signal="#3D5BD9", mint="#0E9F6E", flare="#E0396F", chip="#EEF1FB"),
}

# (id, title, role, metric, metric label, description, stack, accent)
CARDS = [
    ("valqauym", "Val Qauym", "creator · dev team lead", "~945", "members",
     "The bot that runs discord.gg/valqauym, the largest VALORANT community in Kazakhstan: roles, economy, moderation, 700+ auto customs.",
     ["Python", "aiohttp", "React", "TypeScript"], "flare"),
    ("juniper", "Juniper", "core dev · 2019–2025", "1.29M", "servers served",
     "Multipurpose bot for large communities. p95 query time cut from 1.4 s to 18 ms.",
     ["Python", "PostgreSQL"], "signal"),
    ("cheterin", "Cheterin", "founder · open source", "518", "servers",
     "Multi-server bot with a web dashboard: modules switched on per server in the browser.",
     ["Python", "aiohttp", "React"], "mint"),
    ("quests", "Discord Quests × VALORANT", "partner dev", "Orbs", "connection",
     "Partnership work on Discord Quests for VALORANT; designed the code structure of the Orbs connection.",
     [], "signal"),
    ("chetmedia", "ChetMedia", "founder", "270k", "views a day",
     "Anime streaming in the Cheterin ecosystem: catalog and watch, peak 370k views a day.",
     ["Web"], "mint"),
    ("rp-state-mirror", "RP-State-Mirror", "author", "Gov", "in use",
     "Bot and dashboard used by the state factions of the GTA5RP Mirror server: documents, fines, registrations.",
     ["TypeScript", "discord.js", "Next.js"], "signal"),
    ("astra", "ASTRA plugins", "author", "4", "plugins",
     "Minecraft plugins for live servers: AstraSMP, AstraBuild, AstraOP and AstraIP.",
     ["Java"], "mint"),
    ("vencord", "Vencord userplugins", "author", "5+", "plugins",
     "Client-side Discord plugins such as SoundboardToVoice and vc-followUser, each in its own public repo.",
     ["TypeScript"], "signal"),
]

TOOLBOX = [
    ("primary", ["Python", "TypeScript", "Node.js", "Go", "Java", "PostgreSQL"]),
    ("familiar", ["Dart / Flutter", "C#", "C++"]),
    ("platforms", ["Linux", "nginx", "systemd", "Docker", "GitHub Actions", "React"]),
]


def esc(s: str) -> str:
    return html.escape(s, quote=True)


def wrap(text: str, max_chars: int) -> list[str]:
    lines, line = [], ""
    for word in text.split():
        if line and len(line) + 1 + len(word) > max_chars:
            lines.append(line)
            line = word
        else:
            line = f"{line} {word}".strip()
    if line:
        lines.append(line)
    return lines


def text_w(s: str, size: float, mono: bool = False) -> float:
    return len(s) * size * (0.62 if mono else 0.56)


def chips(items: list[str], x: float, y: float, t: dict) -> str:
    out = []
    for item in items:
        w = text_w(item, 11, mono=True) + 18
        out.append(f'<rect x="{x:.1f}" y="{y}" width="{w:.1f}" height="22" rx="6" fill="{t["chip"]}" stroke="{t["border"]}"/>'
                   f'<text x="{x + w / 2:.1f}" y="{y + 15}" text-anchor="middle" fill="{t["muted"]}" font-size="11" font-family="{MONO}">{esc(item)}</text>')
        x += w + 6
    return "".join(out)


def frame(w: int, h: int, t: dict, accent: str, label: str) -> str:
    return (f'<rect x="1" y="1" width="{w - 2}" height="{h - 2}" rx="14" fill="{t["panel"]}" stroke="{t["border"]}" stroke-width="2"/>'
            f'<rect x="1" y="1" width="{w - 2}" height="32" rx="14" fill="{t["border"]}" opacity=".35"/>'
            f'<rect x="1" y="20" width="{w - 2}" height="13" fill="{t["panel"]}" opacity="0"/>'
            f'<circle cx="20" cy="17" r="4.5" fill="#EF4444"/><circle cx="35" cy="17" r="4.5" fill="#F59E0B"/><circle cx="50" cy="17" r="4.5" fill="#10B981"/>'
            f'<text x="{w / 2}" y="21" text-anchor="middle" fill="{t["muted"]}" font-size="11" font-family="{MONO}">{esc(label)}</text>'
            f'<rect x="1" y="33" width="4" height="{h - 48}" fill="{t[accent]}"/>')


def card(c: tuple, t: dict, w: int, h: int, max_chars: int, title_size: int) -> str:
    cid, title, role, metric, mlabel, desc, stack, accent = c
    lines = wrap(desc, max_chars)
    body = "".join(
        f'<text x="24" y="{106 + i * 19}" fill="{t["muted"]}" font-size="13.5" font-family="{SANS}">{esc(l)}</text>'
        for i, l in enumerate(lines)
    )
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}">
{frame(w, h, t, accent, f"~/projects/{cid}")}
<text x="24" y="58" fill="{t[accent]}" font-size="11" font-weight="700" letter-spacing="1.4" font-family="{MONO}">{esc(role.upper())}</text>
<text x="24" y="{58 + title_size + 6}" fill="{t["text"]}" font-size="{title_size}" font-weight="750" letter-spacing="-.4" font-family="{SANS}">{esc(title)}</text>
<text x="{w - 24}" y="66" text-anchor="end" fill="{t[accent]}" font-size="{title_size + 6}" font-weight="750" font-family="{SANS}">{esc(metric)}</text>
<text x="{w - 24}" y="84" text-anchor="end" fill="{t["muted"]}" font-size="10.5" letter-spacing="1" font-family="{MONO}">{esc(mlabel.upper())}</text>
{body}
{chips(stack, 24, h - 38, t)}
</svg>'''


def toolbox(t: dict) -> str:
    w, row_h = 840, 40
    h = 50 + row_h * len(TOOLBOX) + 10
    rows = []
    for i, (name, items) in enumerate(TOOLBOX):
        y = 50 + i * row_h
        rows.append(f'<text x="24" y="{y + 16}" fill="{[t["signal"], t["mint"], t["flare"]][i]}" font-size="11" font-weight="700" letter-spacing="1.4" font-family="{MONO}">{name.upper()}</text>')
        x = 130
        for item in items:
            iw = text_w(item, 12.5) + 26
            rows.append(f'<rect x="{x:.1f}" y="{y}" width="{iw:.1f}" height="26" rx="7" fill="{t["chip"]}" stroke="{t["border"]}"/>'
                        f'<text x="{x + iw / 2:.1f}" y="{y + 17.5}" text-anchor="middle" fill="{t["text"]}" font-size="12.5" font-weight="600" font-family="{SANS}">{esc(item)}</text>')
            x += iw + 8
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}">
{frame(w, h, t, "signal", "~/toolbox --list")}
{"".join(rows)}
</svg>'''


def main() -> None:
    for mode, t in THEMES.items():
        for c in CARDS:
            (OUT / f"{c[0]}-{mode}.svg").write_text(card(c, t, 410, 200, 46, 20), encoding="utf-8")
        (ROOT / "assets" / f"toolbox-{mode}.svg").write_text(toolbox(t), encoding="utf-8")
    print("Generated", len(CARDS), "cards and the toolbox strip in", OUT.parent)


if __name__ == "__main__":
    main()
