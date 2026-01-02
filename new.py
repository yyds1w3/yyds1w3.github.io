import os
import datetime
import sys

# ================= 配置区域 (可自定义) =================
# 预设分类列表 (对应数字 1, 2, 3...)
PRESET_CATS = [
    "Codeforces",   # 1
    "AtCoder",      # 2
    "LeetCode",     # 3
    "算法模板",     # 4
    "杂谈",         # 5
    "C++",          # 6
]

# 文章保存路径 (Astro 标准路径)
POSTS_DIR = "src/content/posts"
# =====================================================

def main():
    # 1. 获取 Slug (文件名/URL)
    # 优先读取命令行参数，例如: python new.py cf-999
    if len(sys.argv) > 1:
        slug = sys.argv[1]
    else:
        slug = input("请输入 Slug (例如 cf-920): ").strip()
        if not slug:
            print("❌ Slug 不能为空！")
            return

    # 2. 获取标题 (如果留空则使用 Slug)
    title = input(f"请输入标题 (默认同 Slug): ").strip() or slug

    # 3. 交互式选择分类
    print("-" * 35)
    print("请选择分类 (输入数字，空格分隔; 或直接输入名称):")
    for i, cat in enumerate(PRESET_CATS):
        print(f"[{i+1}] {cat}")
    print("-" * 35)

    cat_input = input("你的选择 (默认为 Codeforces): ").strip()
    final_cats = []

    if not cat_input:
        # 如果用户直接回车，默认选第1个
        final_cats.append(PRESET_CATS[0])
    else:
        # 处理输入，支持混合模式，例如 "1 3 动态规划"
        parts = cat_input.split()
        for p in parts:
            if p.isdigit():
                idx = int(p) - 1
                if 0 <= idx < len(PRESET_CATS):
                    final_cats.append(PRESET_CATS[idx])
            else:
                # 不是数字，则视为自定义分类
                final_cats.append(p)

    # 4. 生成文件内容 (Markdown + Frontmatter)
    # 注意: pubDate 是 Typography 主题常用的字段名
    # 如果你的主题用 publishDate，请修改下方的 key
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
    
    content = f"""---
title: "{title}"
pubDate: {current_time}
categories: {str(final_cats)}
description: "{title} 题解与思路分析"
slug: "{slug}"
draft: false
---

"""
    # 5. 写入文件
    # 确保目录存在
    if not os.path.exists(POSTS_DIR):
        os.makedirs(POSTS_DIR)

    filepath = os.path.join(POSTS_DIR, f"{slug}.md")

    if os.path.exists(filepath):
        print(f"❌ 错误: 文件已存在 -> {filepath}")
    else:
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"✅ 成功创建: {filepath}")
        print(f"🏷️  分类: {final_cats}")
if __name__ == "__main__":
    main();