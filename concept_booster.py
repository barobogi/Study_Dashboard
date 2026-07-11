# concept_booster.py — 개념노트 자동 보충 (최소 6개 유지)
import json, requests, datetime

FIREBASE_URL = "https://remote-claude-358d6-default-rtdb.asia-southeast1.firebasedatabase.app"
TASKS_PATH   = r"D:\AI\AI_hub\shared\tasks.json"
MIN_COUNT    = 6

CATEGORY_MAP = {
    41: "도구/자동화", 42: "도구/자동화",
    51: "학습", 52: "학습",
    61: "실전/주식", 62: "실전",
    71: "생활",
}

def get_concepts():
    r = requests.get(f"{FIREBASE_URL}/study_all/concepts.json")
    return r.json() or {}

def add_concept(name, body, category):
    now = datetime.datetime.now().isoformat()
    payload = {"name": name, "body": body, "category": category,
               "projects": [], "created": now, "updated": now}
    r = requests.post(f"{FIREBASE_URL}/study_all/concepts.json", json=payload)
    return r.status_code == 200

def load_candidates():
    with open(TASKS_PATH, encoding="utf-8") as f:
        tasks = json.load(f)["tasks"]
    result = []
    for t in tasks:
        if t["상태"] in ("completed", "in_progress") and t.get("설명") and t.get("title"):
            cat = CATEGORY_MAP.get(t["뿌리"], "기타")
            result.append({"name": t["title"], "body": t["설명"], "category": cat})
    return result

def main():
    concepts = get_concepts()
    count = len(concepts) if concepts else 0
    print(f"현재 개념노트: {count}개")

    if count >= MIN_COUNT:
        print("✅ 이미 6개 이상 — 보충 불필요")
        return

    needed = MIN_COUNT - count
    existing_names = {v["name"] for v in concepts.values()} if concepts else set()
    candidates = [c for c in load_candidates() if c["name"] not in existing_names]

    added = 0
    for c in candidates[:needed]:
        ok = add_concept(c["name"], c["body"], c["category"])
        status = "✅" if ok else "❌"
        print(f"{status} {c['name']}")
        if ok:
            added += 1

    print(f"\n{added}개 추가 → 현재 {count + added}개")

if __name__ == "__main__":
    main()
