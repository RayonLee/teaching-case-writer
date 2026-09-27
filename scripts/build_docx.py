# -*- coding: utf-8 -*-
"""按审定参考稿格式，将 Markdown 式草稿排版为教学案例/教学笔记 docx。

用法：
    python build_docx.py <draft.md> <output.docx>

草稿约定：
    第 1 个非空行："# 案例正文" 或 "# 教学笔记"（决定文档类型）
    第 2 个非空行：案例标题（居中、幼圆、16pt、加粗）
    "## 标题"   -> Word Heading 2 样式（宋体14加粗，导航窗格可用）
    "### 标题"  -> Word Heading 4 样式（宋体12加粗）
    普通行      -> 正文（TNR+宋体12pt，1.5倍行距，首行缩进2字符，两端对齐）
    以“开头的行 -> 对话/引语（楷体12pt）
    **粗体**    -> 行内粗体；整行被 ** 包裹 -> 整行粗体
    关键词：... -> "关键词："标签自动加粗
    | 管道表格  -> Table Grid（表头加粗，单元格10.5pt）
    ![图N 说明](图片路径) -> 居中插图 + 加粗居中图注（路径相对草稿目录）
    自动加粗行  ：思考题N：…、【案例分析】、关键知识点、关键能力点
    案例正文末尾自动追加"（案例正文完，全文X字）"（X 为 Word 口径字数近似值，
    最终以 Word 字数统计为准微调）。
"""
import os
import re
import sys
from docx import Document
from docx.shared import Pt, Cm, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml.ns import qn

TNR = "Times New Roman"
SONG = "宋体"
KAI = "楷体"
YOU = "幼圆"
BLUE = RGBColor(0x4F, 0x81, 0xBD)
AUTO_BOLD = [r"^思考题\d+：", r"^【案例分析】$", r"^关键知识点$", r"^关键能力点$"]


def set_font(run, ea=SONG, ascii_f=TNR, size=12, bold=False):
    run.font.name = ascii_f
    run._element.get_or_add_rPr().rFonts.set(qn("w:eastAsia"), ea)
    run.font.size = Pt(size)
    run.font.bold = bold


def add_runs(p, text, ea=SONG, size=12, bold_all=False):
    for part in re.split(r"(\*\*.+?\*\*)", text):
        if not part:
            continue
        wrapped = part.startswith("**") and part.endswith("**") and len(part) > 4
        set_font(p.add_run(part[2:-2] if wrapped else part),
                 ea=ea, size=size, bold=bold_all or wrapped)


def body_paragraph(doc, text, ea=SONG, bold=False, align=WD_ALIGN_PARAGRAPH.JUSTIFY):
    p = doc.add_paragraph()
    pf = p.paragraph_format
    pf.alignment = align
    pf.first_line_indent = Pt(24)
    pf.line_spacing = 1.5
    add_runs(p, text, ea=ea, bold_all=bold)
    return p


def setup_styles(doc):
    def fix(name, size):
        st = doc.styles[name]
        st.font.name = TNR
        st.element.get_or_add_rPr().rFonts.set(qn("w:eastAsia"), SONG)
        st.font.size = Pt(size)
        st.font.bold = True
        st.font.color.rgb = BLUE
        st.paragraph_format.space_before = Pt(10)
        st.paragraph_format.space_after = Pt(4)
    fix("Heading 2", 14)
    fix("Heading 4", 12)


def setup_page(doc):
    sec = doc.sections[0]
    sec.page_width, sec.page_height = Cm(21.0), Cm(29.7)
    sec.top_margin = sec.bottom_margin = Cm(2.54)
    sec.left_margin = sec.right_margin = Cm(2.8)


def render_table(doc, block):
    rows = []
    for line in block:
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if all(re.fullmatch(r":?-{2,}:?", c or "---") for c in cells):
            continue
        rows.append(cells)
    if not rows:
        return
    ncols = max(len(r) for r in rows)
    table = doc.add_table(rows=len(rows), cols=ncols)
    table.style = "Table Grid"
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    for ri, row in enumerate(rows):
        for ci in range(ncols):
            cell = table.cell(ri, ci)
            cell.text = ""
            p = cell.paragraphs[0]
            if ri == 0:
                p.alignment = WD_ALIGN_PARAGRAPH.CENTER
            add_runs(p, row[ci] if ci < len(row) else "", size=10.5, bold_all=(ri == 0))


def render_image(doc, alt, path, base):
    full = path if os.path.isabs(path) else os.path.join(base, path)
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    if os.path.exists(full):
        p.add_run().add_picture(full, width=Cm(12))
    cap = doc.add_paragraph()
    cap.alignment = WD_ALIGN_PARAGRAPH.CENTER
    add_runs(cap, alt, bold_all=True)


def word_count(text):
    """Word 口径近似：汉字与中文标点各计1，连续西文/数字串计1词。"""
    s = re.sub(r"\s+", "", text)
    runs = re.findall(r"[A-Za-z0-9][A-Za-z0-9._%$,\-/]*", s)
    rest = re.sub(r"[A-Za-z0-9][A-Za-z0-9._%$,\-/]*", "", s)
    return len(rest) + len(runs)


def build(draft_path, out_path):
    base = os.path.dirname(os.path.abspath(draft_path))
    with open(draft_path, encoding="utf-8") as f:
        lines = [ln.rstrip() for ln in f.read().splitlines()]
    nonempty = [i for i, ln in enumerate(lines) if ln.strip()]
    doctype = lines[nonempty[0]].lstrip("# ").strip()
    assert doctype in ("案例正文", "教学笔记"), "首行必须是 '# 案例正文' 或 '# 教学笔记'"
    title = lines[nonempty[1]].strip()
    body_start = nonempty[1] + 1

    doc = Document()
    setup_page(doc)
    setup_styles(doc)
    p0 = doc.add_paragraph()
    set_font(p0.add_run(doctype), ea=YOU, size=16)
    p1 = doc.add_paragraph()
    p1.alignment = WD_ALIGN_PARAGRAPH.CENTER
    set_font(p1.add_run(title), ea=YOU, size=16, bold=True)

    collected = [doctype, title]
    i = body_start
    while i < len(lines):
        s = lines[i].strip()
        if not s or s == "---":
            i += 1
            continue
        if s.startswith("|"):
            block = []
            while i < len(lines) and lines[i].strip().startswith("|"):
                block.append(lines[i].strip())
                i += 1
            render_table(doc, block)
            collected.extend(block)
            continue
        m = re.match(r"^!\[(.*?)\]\((.*?)\)$", s)
        if m:
            render_image(doc, m.group(1), m.group(2), base)
            collected.append(m.group(1))
            i += 1
            continue
        m = re.match(r"^(#{2,4})\s+(.*)$", s)
        if m and len(m.group(1)) in (2, 3, 4):
            level = {2: "Heading 2", 3: "Heading 4", 4: "Heading 4"}[len(m.group(1))]
            doc.add_paragraph(m.group(2).strip(), style=level)
            collected.append(m.group(2).strip())
            i += 1
            continue
        if s.startswith("关键词：") or s.startswith("**关键词：**"):
            kw = s[5:] if s.startswith("关键词：") else s
            p = body_paragraph(doc, "")
            set_font(p.add_run("关键词："), bold=True)
            add_runs(p, kw.replace("**关键词：**", "").replace("**", ""))
            collected.append("关键词：" + kw)
            i += 1
            continue
        bold = any(re.match(pat, s) for pat in AUTO_BOLD)
        if s.startswith("**") and s.endswith("**") and len(s) > 4:
            s, bold = s[2:-2], True
        ea = KAI if s.startswith("“") else SONG
        body_paragraph(doc, s, ea=ea, bold=bold)
        collected.append(s)
        i += 1

    if doctype == "案例正文":
        n = word_count("".join(collected))
        body_paragraph(doc, "（案例正文完，全文%d字）" % n)
    doc.save(out_path)
    print("OK %s（%d 段，%d 表）" % (out_path, len(doc.paragraphs), len(doc.tables)))


if __name__ == "__main__":
    if len(sys.argv) != 3:
        sys.exit("用法: python build_docx.py <draft.md> <output.docx>")
    build(sys.argv[1], sys.argv[2])
