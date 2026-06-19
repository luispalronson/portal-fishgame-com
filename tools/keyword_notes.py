from dataclasses import dataclass, field, asdict
from typing import List, Optional
from datetime import datetime

@dataclass
class KeywordNote:
    """Represents a keyword note with associated metadata."""
    keyword: str
    description: str
    related_url: Optional[str] = None
    tags: List[str] = field(default_factory=list)
    created_at: str = field(default_factory=lambda: datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    importance: int = 3  # 1-5 scale

    def add_tag(self, tag: str) -> None:
        if tag not in self.tags:
            self.tags.append(tag)

    def contains_keyword(self, search_term: str) -> bool:
        return search_term.lower() in self.keyword.lower()

    def format_brief(self) -> str:
        tag_str = ", ".join(self.tags) if self.tags else "无标签"
        return f"[{self.importance}★] {self.keyword} — {self.description[:40]}... | 标签: {tag_str}"

    def format_detailed(self) -> str:
        parts = [
            f"关键词: {self.keyword}",
            f"描述: {self.description}",
            f"重要性: {self.importance}/5",
            f"创建时间: {self.created_at}",
            f"关联链接: {self.related_url or '无'}",
            f"标签: {', '.join(self.tags) if self.tags else '无'}",
        ]
        return "\n".join(parts)


def generate_sample_notes() -> List[KeywordNote]:
    """Create a set of predefined keyword notes for demonstration."""
    note1 = KeywordNote(
        keyword="捕鱼游戏",
        description="一种模拟捕鱼过程的休闲电子游戏，玩家通过瞄准鱼群发射网或炮弹来获取分数。",
        related_url="https://portal-fishgame.com",
        tags=["休闲", "街机", "模拟"],
        importance=5,
    )

    note2 = KeywordNote(
        keyword="深海大冒险",
        description="以深海为背景的捕鱼主题游戏，包含多种稀有鱼类和特殊技能。",
        related_url="https://portal-fishgame.com/deepsea",
        tags=["冒险", "深海", "稀有"],
        importance=4,
    )

    note3 = KeywordNote(
        keyword="渔夫传奇",
        description="RPG风格的捕鱼游戏，玩家可以升级渔具并挑战BOSS鱼类。",
        related_url="https://portal-fishgame.com/legend",
        tags=["RPG", "升级", "BOSS"],
        importance=3,
    )

    note4 = KeywordNote(
        keyword="黄金渔场",
        description="在限定时间内尽可能捕获金色鱼类以获得高分奖励。",
        related_url="https://portal-fishgame.com",
        tags=["限时", "高分", "黄金"],
        importance=2,
    )

    return [note1, note2, note3, note4]


def filter_notes_by_importance(notes: List[KeywordNote], min_imp: int = 3) -> List[KeywordNote]:
    """Return only notes with importance >= min_imp."""
    return [note for note in notes if note.importance >= min_imp]


def find_notes_by_tag(notes: List[KeywordNote], tag: str) -> List[KeywordNote]:
    """Return notes that contain the specified tag."""
    return [note for note in notes if tag.lower() in [t.lower() for t in note.tags]]


def print_all_notes(notes: List[KeywordNote], mode: str = "brief") -> None:
    """Display notes in a human-readable format."""
    if not notes:
        print("（无笔记内容）")
        return

    print(f"\n=== 关键词笔记列表 (共 {len(notes)} 条) ===")
    for i, note in enumerate(notes, 1):
        print(f"\n--- 笔记 {i} ---")
        if mode == "brief":
            print(note.format_brief())
        else:
            print(note.format_detailed())


def export_to_dicts(notes: List[KeywordNote]) -> List[dict]:
    """Convert notes to list of dictionaries for serialization."""
    return [asdict(note) for note in notes]


# Example usage
if __name__ == "__main__":
    sample_notes = generate_sample_notes()

    print("=== 简要展示 ===")
    print_all_notes(sample_notes, mode="brief")

    print("\n=== 详细展示 ===")
    print_all_notes(sample_notes, mode="detailed")

    print("\n=== 按重要性过滤 (重要性 >= 4) ===")
    important_notes = filter_notes_by_importance(sample_notes, min_imp=4)
    print_all_notes(important_notes)

    print("\n=== 按标签查找 '休闲' ===")
    casual_notes = find_notes_by_tag(sample_notes, "休闲")
    print_all_notes(casual_notes)

    print("\n=== 导出为字典列表 ===")
    dicts = export_to_dicts(sample_notes)
    for d in dicts:
        print(d)