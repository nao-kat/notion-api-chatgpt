
import os
from openai import OpenAI
from md2notionpage import md2notionpage
from dotenv import load_dotenv



load_dotenv()
# openai_api_key=os.environ["OPENAI_API_KEY"]
# # notion_token = os.environ["NOTION_TOKEN"]
# parent_page_id = os.environ["PARENT_PAGE_ID"]
import os, re
from notion_client import Client

NOTION_SECRET = os.environ["NOTION_SECRET"]
PARENT_PAGE_ID = os.environ["PARENT_PAGE_ID"]
notion = Client(auth=NOTION_SECRET)

# def md_to_notion_blocks(md: str):
#     blocks = []
#     for raw in md.splitlines():
#         line = raw.strip()
#         if not line:
#             continue
#         # - [ ] / - [x] を to_do に
#         m = re.match(r"- \[( |x|X)\] (.+)", line)
#         if m:
#             checked = m.group(1).lower() == "x"
#             text = m.group(2)
#             blocks.append({
#                 "object": "block",
#                 "type": "to_do",
#                 "to_do": {
#                     "rich_text": [{"type": "text", "text": {"content": text}}],
#                     "checked": checked
#                 }
#             })
#             continue
#         # 見出し（例: "Monday 朝:" → heading_2）
#         if line.endswith(":"):
#             blocks.append({
#                 "object": "block",
#                 "type": "heading_2",
#                 "heading_2": {
#                     "rich_text": [{"type": "text", "text": {"content": line[:-1]}}]
#                 }
#             })
#         else:
#             blocks.append({
#                 "object": "block",
#                 "type": "paragraph",
#                 "paragraph": {
#                     "rich_text": [{"type": "text", "text": {"content": line}}]
#                 }
#             })
#     return blocks

# def create_todo_page(title: str, md: str):
#     # 親ページ配下にページを作成（子ページは title プロパティのみ有効）
#     page = notion.pages.create(
#         parent={"page_id": PARENT_PAGE_ID},
#         properties={
#             "title": [{"type": "text", "text": {"content": title}}]
#         }
#     )
#     blocks = md_to_notion_blocks(md)
#     notion.blocks.children.append(page["id"], children=blocks)
#     return page["url"]

# if __name__ == "__main__":
#     md = """Monday 朝:
# - [ ] 体重を測る
# - [ ] ストレッチ
# - [ ] 散歩
# """
#     url = create_todo_page("週次 To‑Do", md)
#     print("✅ Notionページを作成しました:", url)




CHILD_PAGE_ID = os.environ["CHILD_PAGE_ID"]







import os, re
from notion_client import Client
from openai import OpenAI
from dotenv import load_dotenv

# load_dotenv()
openai_api_key = os.environ["OPENAI_API_KEY"]
# PARENT_PAGE_ID = os.environ["PARENT_PAGE_ID"]
# NOTION_SECRET = os.environ["NOTION_SECRET"]

# Notion & OpenAI clients
# notion = Client(auth=NOTION_SECRET)
# client = OpenAI(api_key=openai_api_key)

# def generate_markdown(plan_text: str) -> str:
#     resp = client.chat.completions.create(
#         model="gpt-4o",
#         messages=[
#             {"role": "system", "content": "あなたはMarkdown形式のチェックリストTo‑Doを生成するAIです。"},
#             {"role": "user", "content": plan_text}
#         ],
#         temperature=0.2
#     )
#     return resp.choices[0].message.content.strip()

# def md_to_blocks(md: str):
#     blocks = []
#     for raw in md.splitlines():
#         line = raw.strip()
#         if not line:
#             continue
#         m = re.match(r"- \[( |x|X)\] (.+)", line)
#         if m:
#             checked = m.group(1).lower() == "x"
#             text = m.group(2)
#             blocks.append({
#                 "object": "block",
#                 "type": "to_do",
#                 "to_do": {
#                     "rich_text": [{"type": "text", "text": {"content": text}}],
#                     "checked": checked
#                 }
#             })
#         elif line.endswith(":"):
#             blocks.append({
#                 "object": "block",
#                 "type": "heading_2",
#                 "heading_2": {"rich_text": [{"type": "text", "text": {"content": line[:-1]}}]}
#             })
#         else:
#             blocks.append({
#                 "object": "block",
#                 "type": "paragraph",
#                 "paragraph": {"rich_text": [{"type": "text", "text": {"content": line}}]}
#             })
#     return blocks

# def create_page(title: str, parent_page_id: str) -> str:
#     page = notion.pages.create(
#         parent={"page_id": parent_page_id},
#         properties={"title": {"title": [{"type": "text", "text": {"content": title}}]}}
#     )
#     return page["id"], page["url"]

# def append_blocks(page_id: str, blocks: list):
#     notion.blocks.children.append(block_id=page_id, children=blocks)

# def main():
#     # まず親ページ直下にサブページを作成
#     sub_title = "週次 To‑Do 親サブページ"
#     sub_id, sub_url = create_page(sub_title, PARENT_PAGE_ID)
#     print("✅ 子ページ作成", sub_url)

#     # さらにそのサブページ直下に孫ページを作成
#     grand_title = "週次 To‑Do 孫ページ"
#     grand_id, grand_url = create_page(grand_title, sub_id)
#     print("✅ 孫ページ作成", grand_url)

#     # GPTでチェックリストMarkdown生成
#     plan_text = """
# Monday 朝:
# - [ ] 体重を測る
# - [ ] ストレッチ
# - [ ] 散歩
# """
#     md = generate_markdown(plan_text)
#     print("Generated Markdown:\n", md)

#     # Markdown → to_do 等の Notionブロックへ
#     blocks = md_to_blocks(md)

#     # 孫ページ直下にブロックを挿入
#     append_blocks(grand_id, blocks)
#     print("✅ 孫ページに to_do ブロックを追加しました")

# if __name__ == "__main__":
#     main()






import os, re
from notion_client import Client
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
# openai_api_key = os.environ["OPENAI_API_KEY"]
# NOTION_SECRET = os.environ["NOTION_SECRET"]
child_page_id = os.environ["CHILD_PAGE_ID"]  # 既存の子ページID

notion = Client(auth=NOTION_SECRET)
client = OpenAI(api_key=openai_api_key)

def generate_markdown(plan_text: str) -> str:
    resp = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "あなたはMarkdown形式のチェックリストTo‑Doを生成するAIです。"},
            {"role": "user", "content": plan_text}
        ],
        temperature=0.2
    )
    return resp.choices[0].message.content.strip()

def md_to_blocks(md: str):
    blocks = []
    for raw in md.splitlines():
        line = raw.strip()
        if not line: continue
        m = re.match(r"- \[( |x|X)\] (.+)", line)
        if m:
            checked = m.group(1).lower() == "x"
            text = m.group(2)
            blocks.append({
                "object": "block",
                "type": "to_do",
                "to_do": {"rich_text":[{"type":"text","text":{"content":text}}], "checked":checked}
            })
        elif line.endswith(":"):
            blocks.append({
                "object": "block", "type": "heading_2",
                "heading_2": {"rich_text":[{"type":"text","text":{"content":line[:-1]}}]}
            })
        else:
            blocks.append({
                "object": "block", "type": "paragraph",
                "paragraph": {"rich_text":[{"type":"text","text":{"content":line}}]}
            })
    return blocks

def create_subpage_under(child_id: str, title: str, initial_children=None):
    payload = {
        "parent": {"page_id": child_id},
        "properties": {
            "title": {"title":[{"type":"text","text":{"content": title}}]}
        }
    }
    if initial_children:
        payload["children"] = initial_children
    page = notion.pages.create(**payload)
    return page["id"], page.get("url")

def append_blocks(page_id: str, blocks: list):
    notion.blocks.children.append(block_id=page_id, children=blocks)

def main():
    title_grand = "孫ページのタイトル"
    initial = [
        {"object":"block", "type":"paragraph",
         "paragraph":{"rich_text":[{"type":"text","text":{"content":"孫ページを作成しました。"}}]}}
    ]
    grand_id, grand_url = create_subpage_under(child_page_id, title_grand, initial)
    print("✅ 孫ページ作成:", grand_url)

    plan_text = """
Today:
- [ ] Task A
- [ ] Task B
"""
    md = generate_markdown(plan_text)
    print("生成Markdown:\n", md)

    blocks = md_to_blocks(md)
    append_blocks(grand_id, blocks)
    print("✅ 孫ページにチェックリストを追加しました")

if __name__ == "__main__":
    main()
