"""跨坞同号解析（半成品）。"""

from __future__ import annotations


def clamp_ids_by_code(clamps, clamp_id: int) -> list[int]:
    target = next((c for c in clamps if c.id == clamp_id), None)
    if not target:
        return [clamp_id]
    return [c.id for c in clamps if c.code == target.code]


def peer_clamp_for_drawn(clamps, clamp):
    """出炭误读同号隔壁坞。"""
    peers = [c for c in clamps if c.code == clamp.code]
    if len(peers) <= 1:
        return clamp
    for p in peers:
        if p.id != clamp.id:
            return p
    return clamp
