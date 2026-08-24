#!/usr/bin/env python3
"""Check QUG language runtimes against the master specification."""

from __future__ import annotations

import hashlib
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parent
MASTER = ROOT / "sg-qug-agent-master.md"
RUNTIMES = {
    "English": ROOT / "sg-qug-agent-en.md",
    "Japanese": ROOT / "sg-qug-agent-ja.md",
}
SOURCE_PATTERN = re.compile(r"source-sha256: ([0-9a-f]{64})")
JAPANESE_PATTERN = re.compile(r"[\u3040-\u30ff\u3400-\u9fff]")

COMMON_REQUIREMENTS = (
    "Extract",
    "Transform",
    "Enact",
    "Return",
    "ACTIVE_MODE",
    "ENTRY_TYPE",
    "FRAME_BASIS",
    "CONFIRMED_UNCERTAINTY_FRAME",
    "CONFIRMED_EXPLORATION_FRAME",
    "CURRENT_STAGE",
    "SCENE_3_CHOICE",
    "SIDE_QUEST_TYPE_SELECTION",
    "FINAL_REFLECTION",
    "Normal Mode",
    "Demo Mode",
)

LANGUAGE_REQUIREMENTS = {
    "English": (
        "Evidence Constraint",
        "Transformation Integrity",
        "Choice Design",
        "Safety",
        "Stage Barrier",
        "Return Integrity",
        "Broad-Topic Bridge",
        "Sample starting point",
        "4. Another action -- write your own",
        "More samples",
        "Demo quest complete",
    ),
    "Japanese": (
        "Extractの証拠制約",
        "変換の整合性",
        "選択肢設計",
        "安全境界",
        "Stage barrier",
        "Returnの整合性",
        "広いテーマへの橋渡し",
        "サンプルの出発点",
        "4. 別の行動を自分で書く",
        "他のサンプル",
        "デモクエスト完了",
    ),
}


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def fail(message: str, errors: list[str]) -> None:
    errors.append(f"ERROR: {message}")


def main() -> int:
    errors: list[str] = []
    paths = (MASTER, *RUNTIMES.values())
    for path in paths:
        if not path.is_file():
            fail(f"missing file: {path.name}", errors)

    if errors:
        print("\n".join(errors))
        return 1

    master_hash = sha256(MASTER)
    master_text = MASTER.read_text(encoding="utf-8")
    if "enabled: false" not in master_text:
        fail("master must remain disabled and non-runtime", errors)

    for language, path in RUNTIMES.items():
        text = path.read_text(encoding="utf-8")
        match = SOURCE_PATTERN.search(text)
        if not match:
            fail(f"{path.name} has no source hash marker", errors)
        elif match.group(1) != master_hash:
            fail(
                f"{path.name} is out of sync with {MASTER.name}: "
                f"marker={match.group(1)}, current={master_hash}",
                errors,
            )

        if "enabled: true" not in text:
            fail(f"{path.name} is not enabled", errors)
        if "SESSION_LANGUAGE" in text:
            fail(f"{path.name} reintroduces SESSION_LANGUAGE", errors)

        for phrase in (*COMMON_REQUIREMENTS, *LANGUAGE_REQUIREMENTS[language]):
            if phrase not in text:
                fail(f"{path.name} is missing required phrase: {phrase}", errors)

        if language == "English" and JAPANESE_PATTERN.search(text):
            fail(f"{path.name} contains Japanese characters", errors)

    if errors:
        print("\n".join(errors))
        return 1

    print(f"OK: master hash {master_hash}")
    print("OK: English and Japanese runtimes pass structural sync checks")
    return 0


if __name__ == "__main__":
    sys.exit(main())
