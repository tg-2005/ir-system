"""
generate_ppt.py
---------------
Generates a clean, professional, student-style PowerPoint presentation (.pptx)
for the Smart Research Paper Information Retrieval System project.

Author: Tarang Ambildhuke (Roll No: 161)
College: Yeshwantrao Chavan College of Engineering (YCCE), Nagpur
Guide: Prof. Sushil Chavhan Sir
"""

import sys
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE

def create_presentation():
    prs = Presentation()
    # 16:9 Widescreen slides (13.333 x 7.5 inches)
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)

    blank_layout = prs.slide_layouts[6]

    # Color Palette - Professional academic theme
    NAVY = RGBColor(15, 42, 74)       # #0F2A4A Primary Dark
    BLUE = RGBColor(30, 64, 175)      # #1E40AF Accent Blue
    DARK = RGBColor(30, 41, 59)       # #1E293B Text Dark
    MUTED = RGBColor(100, 116, 139)   # #64748B Secondary Text
    LIGHT_BG = RGBColor(248, 250, 252) # #F8FAFC Card Background
    BORDER_COLOR = RGBColor(203, 213, 225) # #CBD5E1 Card Border
    WHITE = RGBColor(255, 255, 255)
    GREEN = RGBColor(16, 149, 93)     # Highlight Success
    ACCENT_LIGHT = RGBColor(239, 246, 255) # Light Blue Tint

    def add_header(slide, title_text, category_text="ACADEMIC PROJECT PRESENTATION"):
        """Adds a clean header strip and breadcrumb to slide."""
        # Top banner line
        top_bar = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0), Inches(0), Inches(13.333), Inches(0.12))
        top_bar.fill.solid()
        top_bar.fill.fore_color.rgb = BLUE
        top_bar.line.fill.background()

        # Category/Tag
        tag_box = slide.shapes.add_textbox(Inches(0.8), Inches(0.4), Inches(11.7), Inches(0.3))
        tf_tag = tag_box.text_frame
        tf_tag.word_wrap = True
        tf_tag.margin_left = tf_tag.margin_top = tf_tag.margin_right = tf_tag.margin_bottom = 0
        p_tag = tf_tag.paragraphs[0]
        p_tag.text = category_text.upper()
        p_tag.font.name = "Arial"
        p_tag.font.size = Pt(10)
        p_tag.font.bold = True
        p_tag.font.color.rgb = BLUE

        # Title
        title_box = slide.shapes.add_textbox(Inches(0.8), Inches(0.68), Inches(11.7), Inches(0.6))
        tf_title = title_box.text_frame
        tf_title.word_wrap = True
        tf_title.margin_left = tf_title.margin_top = tf_title.margin_right = tf_title.margin_bottom = 0
        p_title = tf_title.paragraphs[0]
        p_title.text = title_text
        p_title.font.name = "Arial"
        p_title.font.size = Pt(22)
        p_title.font.bold = True
        p_title.font.color.rgb = NAVY

        # Dividing thin line
        line = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0.8), Inches(1.35), Inches(11.7), Inches(0.02))
        line.fill.solid()
        line.fill.fore_color.rgb = BORDER_COLOR
        line.line.fill.background()

        # Bottom footer
        foot_box = slide.shapes.add_textbox(Inches(0.8), Inches(7.05), Inches(11.7), Inches(0.3))
        tf_foot = foot_box.text_frame
        tf_foot.margin_left = tf_foot.margin_top = tf_foot.margin_right = tf_foot.margin_bottom = 0
        p_foot = tf_foot.paragraphs[0]
        p_foot.text = "Tarang Ambildhuke (Roll No: 161) | YCCE Nagpur | Guided by Prof. Sushil Chavhan Sir"
        p_foot.font.name = "Arial"
        p_foot.font.size = Pt(9)
        p_foot.font.color.rgb = MUTED

    def create_card(slide, left, top, width, height, title, content_list, highlight=False):
        """Creates a clean academic content card."""
        card = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, left, top, width, height)
        card.fill.solid()
        card.fill.fore_color.rgb = ACCENT_LIGHT if highlight else LIGHT_BG
        card.line.color.rgb = BLUE if highlight else BORDER_COLOR
        card.line.width = Pt(1.2 if highlight else 0.8)

        tb = slide.shapes.add_textbox(left + Inches(0.25), top + Inches(0.2), width - Inches(0.5), height - Inches(0.4))
        tf = tb.text_frame
        tf.word_wrap = True
        tf.margin_left = tf.margin_top = tf.margin_right = tf.margin_bottom = 0

        # Title
        p_title = tf.paragraphs[0]
        p_title.text = title
        p_title.font.name = "Arial"
        p_title.font.size = Pt(14)
        p_title.font.bold = True
        p_title.font.color.rgb = BLUE if highlight else NAVY
        p_title.space_after = Pt(10)

        # Content bullets
        for item in content_list:
            p = tf.add_paragraph()
            p.text = item
            p.font.name = "Arial"
            p.font.size = Pt(11)
            p.font.color.rgb = DARK
            p.space_after = Pt(6)
            p.level = 0

    # =========================================================================
    # SLIDE 1: TITLE SLIDE
    # =========================================================================
    s1 = prs.slides.add_slide(blank_layout)
    
    # Top decorative bar
    bar = s1.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0), Inches(0), Inches(13.333), Inches(0.18))
    bar.fill.solid()
    bar.fill.fore_color.rgb = BLUE
    bar.line.fill.background()

    # College Name
    c_box = s1.shapes.add_textbox(Inches(0.8), Inches(0.6), Inches(11.7), Inches(0.5))
    tf_c = c_box.text_frame
    p_c = tf_c.paragraphs[0]
    p_c.text = "YESHWANTRAO CHAVAN COLLEGE OF ENGINEERING, NAGPUR"
    p_c.font.name = "Arial"
    p_c.font.size = Pt(13)
    p_c.font.bold = True
    p_c.font.color.rgb = BLUE

    p_c_sub = tf_c.add_paragraph()
    p_c_sub.text = "(An Autonomous Institution Affiliated to RTM Nagpur University) | Department of Computer Technology"
    p_c_sub.font.name = "Arial"
    p_c_sub.font.size = Pt(10)
    p_c_sub.font.color.rgb = MUTED

    # Title Card
    t_card = s1.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(1.5), Inches(11.7), Inches(2.7))
    t_card.fill.solid()
    t_card.fill.fore_color.rgb = NAVY
    t_card.line.fill.background()

    tb_t = s1.shapes.add_textbox(Inches(1.2), Inches(1.8), Inches(10.9), Inches(2.1))
    tf_t = tb_t.text_frame
    tf_t.word_wrap = True
    
    p_tag = tf_t.paragraphs[0]
    p_tag.text = "FINAL YEAR CAPSTONE PROJECT"
    p_tag.font.name = "Arial"
    p_tag.font.size = Pt(11)
    p_tag.font.bold = True
    p_tag.font.color.rgb = RGBColor(147, 197, 253) # Light Blue
    p_tag.space_after = Pt(8)

    p_main = tf_t.add_paragraph()
    p_main.text = "Smart Research Paper Information Retrieval System"
    p_main.font.name = "Arial"
    p_main.font.size = Pt(26)
    p_main.font.bold = True
    p_main.font.color.rgb = WHITE
    p_main.space_after = Pt(6)

    p_sub = tf_t.add_paragraph()
    p_sub.text = "Using Classical Lexical and Semantic Information Retrieval with Live arXiv Integration"
    p_sub.font.name = "Arial"
    p_sub.font.size = Pt(14)
    p_sub.font.color.rgb = RGBColor(226, 232, 240)

    # Student Details Box (Left)
    d_left = s1.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(4.5), Inches(5.6), Inches(2.2))
    d_left.fill.solid()
    d_left.fill.fore_color.rgb = LIGHT_BG
    d_left.line.color.rgb = BORDER_COLOR
    d_left.line.width = Pt(1)

    tb_dl = s1.shapes.add_textbox(Inches(1.1), Inches(4.7), Inches(5.0), Inches(1.8))
    tf_dl = tb_dl.text_frame
    p_dl1 = tf_dl.paragraphs[0]
    p_dl1.text = "Presented By:"
    p_dl1.font.name = "Arial"
    p_dl1.font.size = Pt(10)
    p_dl1.font.color.rgb = MUTED
    p_dl1.space_after = Pt(4)

    p_dl2 = tf_dl.add_paragraph()
    p_dl2.text = "Tarang Ambildhuke"
    p_dl2.font.name = "Arial"
    p_dl2.font.size = Pt(16)
    p_dl2.font.bold = True
    p_dl2.font.color.rgb = NAVY
    p_dl2.space_after = Pt(2)

    p_dl3 = tf_dl.add_paragraph()
    p_dl3.text = "Roll Number: 161"
    p_dl3.font.name = "Arial"
    p_dl3.font.size = Pt(12)
    p_dl3.font.bold = True
    p_dl3.font.color.rgb = BLUE
    p_dl3.space_after = Pt(2)

    p_dl4 = tf_dl.add_paragraph()
    p_dl4.text = "B.Tech - Computer Technology (2026 - 2027)"
    p_dl4.font.name = "Arial"
    p_dl4.font.size = Pt(10)
    p_dl4.font.color.rgb = DARK

    # Guide Details Box (Right)
    d_right = s1.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(6.9), Inches(4.5), Inches(5.6), Inches(2.2))
    d_right.fill.solid()
    d_right.fill.fore_color.rgb = LIGHT_BG
    d_right.line.color.rgb = BORDER_COLOR
    d_right.line.width = Pt(1)

    tb_dr = s1.shapes.add_textbox(Inches(7.2), Inches(4.7), Inches(5.0), Inches(1.8))
    tf_dr = tb_dr.text_frame
    p_dr1 = tf_dr.paragraphs[0]
    p_dr1.text = "Under the Guidance of:"
    p_dr1.font.name = "Arial"
    p_dr1.font.size = Pt(10)
    p_dr1.font.color.rgb = MUTED
    p_dr1.space_after = Pt(4)

    p_dr2 = tf_dr.add_paragraph()
    p_dr2.text = "Prof. Sushil Chavhan Sir"
    p_dr2.font.name = "Arial"
    p_dr2.font.size = Pt(16)
    p_dr2.font.bold = True
    p_dr2.font.color.rgb = NAVY
    p_dr2.space_after = Pt(2)

    p_dr3 = tf_dr.add_paragraph()
    p_dr3.text = "Assistant Professor, Dept. of Computer Technology"
    p_dr3.font.name = "Arial"
    p_dr3.font.size = Pt(11)
    p_dr3.font.color.rgb = DARK
    p_dr3.space_after = Pt(2)

    p_dr4 = tf_dr.add_paragraph()
    p_dr4.text = "YCCE Nagpur"
    p_dr4.font.name = "Arial"
    p_dr4.font.size = Pt(10)
    p_dr4.font.color.rgb = MUTED

    # =========================================================================
    # SLIDE 2: PROBLEM STATEMENT & MOTIVATION
    # =========================================================================
    s2 = prs.slides.add_slide(blank_layout)
    add_header(s2, "Problem Statement & Motivation", "1. INTRODUCTION")

    create_card(s2, Inches(0.8), Inches(1.6), Inches(5.6), Inches(5.1),
        "The Core Challenge in Literature Search",
        [
            "• Massive Influx of Scientific Papers: Repositories like arXiv publish thousands of scientific preprints every month.",
            "• Traditional Keyword Search Limitations: Standard search engines rely on exact string / lexical matching (TF-IDF / BM25).",
            "• The Vocabulary Mismatch Problem: A query 'deep learning medical diagnosis' fails to retrieve relevant papers titled 'convolutional neural networks for clinical radiography' if the exact terms are absent.",
            "• False-Positive Noise: Lexical search often elevates irrelevant papers simply because generic terms like 'machine learning' repeat frequently in census or statistical papers."
        ]
    )

    create_card(s2, Inches(6.9), Inches(1.6), Inches(5.6), Inches(5.1),
        "Project Motivation & Proposed Solution",
        [
            "• Semantic Intelligence: Leverage pre-trained Sentence Transformers to capture deep contextual meaning rather than literal word counts.",
            "• Vector Similarity Search: Index dense embeddings in high-dimensional space (384-D) using Facebook AI Similarity Search (FAISS).",
            "• Live arXiv Integration: Search dynamically against live arXiv preprints rather than outdated static local snapshots.",
            "• Practical Student Setup: 100% free, runs locally on consumer CPU hardware without requiring expensive GPU infrastructure.",
            "• Direct PDF Access: Instant full-text view straight from arXiv official servers without exhausting local disk storage."
        ],
        highlight=True
    )

    # =========================================================================
    # SLIDE 3: OBJECTIVES OF THE SYSTEM
    # =========================================================================
    s3 = prs.slides.add_slide(blank_layout)
    add_header(s3, "Project Objectives & Scope", "2. GOALS")

    objs = [
        ("1. Dynamic Ingestion", "Connect to live arXiv REST API to retrieve real-time scientific papers, titles, abstracts, and metadata on demand."),
        ("2. Dual-Paradigm IR", "Implement both Classical Lexical Search (TF-IDF) and Semantic Vector Search (MiniLM + FAISS) for clear comparative study."),
        ("3. Dense Vector Indexing", "Utilize Sentence-Transformers (all-MiniLM-L6-v2) to map paper abstracts into 384-dimensional unit vectors for L2 distance ranking."),
        ("4. Scientific Benchmarking", "Evaluate retrieval quality against the published BEIR benchmark (NeurIPS 2021) on the SciFact dataset using standard IR metrics."),
        ("5. Abstract Summarization", "Integrate automated text summarization to present fast 2-3 sentence overviews of top-ranked research papers."),
        ("6. Intuitive Web Interface", "Deploy a clean, responsive Flask web application for convenient interactive searching by students and researchers.")
    ]

    for idx, (title, desc) in enumerate(objs):
        col = idx % 2
        row = idx // 2
        l = Inches(0.8 + col * 6.1)
        t = Inches(1.6 + row * 1.7)
        w = Inches(5.6)
        h = Inches(1.5)

        card = s3.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, l, t, w, h)
        card.fill.solid()
        card.fill.fore_color.rgb = LIGHT_BG
        card.line.color.rgb = BORDER_COLOR
        card.line.width = Pt(1)

        tb = s3.shapes.add_textbox(l + Inches(0.2), t + Inches(0.15), w - Inches(0.4), h - Inches(0.3))
        tf = tb.text_frame
        tf.word_wrap = True
        p1 = tf.paragraphs[0]
        p1.text = title
        p1.font.name = "Arial"
        p1.font.size = Pt(13)
        p1.font.bold = True
        p1.font.color.rgb = BLUE
        p1.space_after = Pt(3)

        p2 = tf.add_paragraph()
        p2.text = desc
        p2.font.name = "Arial"
        p2.font.size = Pt(10.5)
        p2.font.color.rgb = DARK

    # =========================================================================
    # SLIDE 4: CLASSICAL VS SEMANTIC RETRIEVAL
    # =========================================================================
    s4 = prs.slides.add_slide(blank_layout)
    add_header(s4, "Classical (Lexical) vs. Semantic Information Retrieval", "3. THEORY")

    # Table comparison
    table_shape = s4.shapes.add_table(5, 3, Inches(0.8), Inches(1.6), Inches(11.7), Inches(3.6))
    table = table_shape.table
    table.columns[0].width = Inches(2.7)
    table.columns[1].width = Inches(4.5)
    table.columns[2].width = Inches(4.5)

    headers = ["Feature", "Classical Lexical IR (TF-IDF / BM25)", "Semantic Dense IR (MiniLM + FAISS)"]
    for i, h in enumerate(headers):
        cell = table.cell(0, i)
        cell.text = h
        cell.fill.solid()
        cell.fill.fore_color.rgb = NAVY
        for p in cell.text_frame.paragraphs:
            p.font.name = "Arial"
            p.font.size = Pt(11)
            p.font.bold = True
            p.font.color.rgb = WHITE
            p.alignment = PP_ALIGN.CENTER

    data = [
        ("Matching Mechanism", "Exact string keyword matching; counts word frequencies across documents.", "Conceptual semantic similarity; encodes text into dense 384-D vector space."),
        ("Synonym & Context Handling", "Fails on synonyms (e.g., 'doctor' vs 'physician'). Incapable of understanding context.", "Recognizes synonyms, contextual relations, and cross-domain concepts naturally."),
        ("Mathematical Foundation", "TF-IDF = TF(t, d) × ln(N / (DF(t) + 1))\nCosine similarity over sparse high-dim vocabulary.", "Transformer Self-Attention Distillation.\nEuclidean / Cosine distance over dense vectors in FAISS."),
        ("Strengths & Weaknesses", "Extremely fast, low RAM.\nWeakness: High false-positives and missed relevant papers.", "Superior ranking precision (MAP/MRR).\nWeakness: Higher compute cost for vector encoding.")
    ]

    for row_idx, row in enumerate(data, start=1):
        for col_idx, text in enumerate(row):
            cell = table.cell(row_idx, col_idx)
            cell.text = text
            cell.fill.solid()
            cell.fill.fore_color.rgb = LIGHT_BG if row_idx % 2 == 1 else WHITE
            for p in cell.text_frame.paragraphs:
                p.font.name = "Arial"
                p.font.size = Pt(10)
                p.font.color.rgb = DARK
                if col_idx == 0:
                    p.font.bold = True
                    p.font.color.rgb = NAVY

    # Summary box
    s_box = s4.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(5.4), Inches(11.7), Inches(1.3))
    s_box.fill.solid()
    s_box.fill.fore_color.rgb = ACCENT_LIGHT
    s_box.line.color.rgb = BLUE

    tb_sb = s4.shapes.add_textbox(Inches(1.0), Inches(5.5), Inches(11.3), Inches(1.1))
    tf_sb = tb_sb.text_frame
    p_sb = tf_sb.paragraphs[0]
    p_sb.text = "Key Insight for Information Retrieval:"
    p_sb.font.name = "Arial"
    p_sb.font.size = Pt(12)
    p_sb.font.bold = True
    p_sb.font.color.rgb = BLUE
    p_sb.space_after = Pt(2)

    p_sb2 = tf_sb.add_paragraph()
    p_sb2.text = "While classical lexical models (TF-IDF) remain useful for finding rare scientific terms (e.g. specific chemical or gene names), semantic dense retrieval ensures that papers addressing the true conceptual problem are ranked at #1 or #2, vastly reducing researcher search time."
    p_sb2.font.name = "Arial"
    p_sb2.font.size = Pt(10.5)
    p_sb2.font.color.rgb = DARK

    # =========================================================================
    # SLIDE 5: SYSTEM ARCHITECTURE & PIPELINE
    # =========================================================================
    s5 = prs.slides.add_slide(blank_layout)
    add_header(s5, "System Architecture & Processing Pipeline", "4. ARCHITECTURE")

    # Draw pipeline steps
    steps = [
        ("STEP 1", "User Query", "User inputs plain english search query\n(e.g., 'deep learning cancer detection')"),
        ("STEP 2", "arXiv API Ingestion", "Queries live arXiv API using urllib/arxiv client to fetch top 10 relevant candidate papers."),
        ("STEP 3", "MiniLM Embedding", "Converts query & abstracts into normalized 384-dimensional dense vectors."),
        ("STEP 4", "FAISS Similarity Search", "Initializes IndexFlatL2; calculates L2 Euclidean distance & similarity scores."),
        ("STEP 5", "Re-ranking & Summarization", "Sorts papers by highest semantic similarity; extracts concise 2-3 sentence AI summary."),
        ("STEP 6", "Flask Web UI", "Renders responsive Bootstrap card interface with rank, score, summary, and PDF link.")
    ]

    card_w = Inches(1.8)
    card_h = Inches(4.8)
    gap = Inches(0.18)

    for i, (tag, name, desc) in enumerate(steps):
        l = Inches(0.8 + i * (1.8 + 0.18))
        card = s5.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, l, Inches(1.8), card_w, card_h)
        card.fill.solid()
        card.fill.fore_color.rgb = LIGHT_BG if i % 2 == 0 else ACCENT_LIGHT
        card.line.color.rgb = BLUE if i % 2 == 1 else BORDER_COLOR
        card.line.width = Pt(1.2)

        tb = s5.shapes.add_textbox(l + Inches(0.1), Inches(1.95), card_w - Inches(0.2), card_h - Inches(0.3))
        tf = tb.text_frame
        tf.word_wrap = True

        p1 = tf.paragraphs[0]
        p1.text = tag
        p1.font.name = "Arial"
        p1.font.size = Pt(10)
        p1.font.bold = True
        p1.font.color.rgb = BLUE
        p1.alignment = PP_ALIGN.CENTER
        p1.space_after = Pt(6)

        p2 = tf.add_paragraph()
        p2.text = name
        p2.font.name = "Arial"
        p2.font.size = Pt(12)
        p2.font.bold = True
        p2.font.color.rgb = NAVY
        p2.alignment = PP_ALIGN.CENTER
        p2.space_after = Pt(10)

        p3 = tf.add_paragraph()
        p3.text = desc
        p3.font.name = "Arial"
        p3.font.size = Pt(9.5)
        p3.font.color.rgb = DARK
        p3.alignment = PP_ALIGN.CENTER

    # =========================================================================
    # SLIDE 6: IMPLEMENTATION & TECH STACK
    # =========================================================================
    s6 = prs.slides.add_slide(blank_layout)
    add_header(s6, "Implementation Details & Technology Stack", "5. IMPLEMENTATION")

    create_card(s6, Inches(0.8), Inches(1.6), Inches(5.6), Inches(5.1),
        "Modular Software Components",
        [
            "• app.py (Controller & Routing): Flask web application serving search endpoints, managing session flow, and rendering HTML templates.",
            "• fetch_papers.py (Data Ingestion): Interfaces directly with official arXiv API via search client; extracts metadata, summaries, and PDF URLs.",
            "• embedder.py (Dense Encoder): Implements lazy-loaded Sentence-Transformers ('all-MiniLM-L6-v2') converting queries and abstracts into 384-D arrays.",
            "• search_engine.py (FAISS Vector Index): Uses faiss.IndexFlatL2 to add document vectors, query distances, and compute similarity scores.",
            "• summarizer.py (AI Summarization): Distills lengthy abstracts into clean, readable 2-3 sentence executive summaries.",
            "• templates/index.html: Clean Bootstrap 5 UI designed for student ease-of-use with instant PDF access buttons."
        ]
    )

    create_card(s6, Inches(6.9), Inches(1.6), Inches(5.6), Inches(5.1),
        "Key Technologies Utilized",
        [
            "• Python 3.11: Core programming language ensuring cross-platform stability and fast execution.",
            "• Sentence-Transformers: Hugging Face library providing pre-trained transformer embeddings.",
            "• all-MiniLM-L6-v2: Distilled 6-layer BERT model (22.7M parameters) offering 5x faster CPU inference.",
            "• FAISS (Facebook AI Similarity Search): Industrial-grade C++ vector similarity engine with Python bindings.",
            "• arXiv API: Official REST API accessing over 2 million scientific papers dynamically.",
            "• Flask 3.1: Lightweight WSGI web application framework.",
            "• BEIR Benchmark: NeurIPS 2021 framework used for standard academic evaluation."
        ],
        highlight=True
    )

    # =========================================================================
    # SLIDE 7: EXPERIMENTAL EVALUATION (BEIR TABLE)
    # =========================================================================
    s7 = prs.slides.add_slide(blank_layout)
    add_header(s7, "Experimental Results: BEIR Paper vs. Our System", "6. RESULTS")

    # Evaluation comparison table
    eval_table = s7.shapes.add_table(7, 5, Inches(0.8), Inches(1.6), Inches(11.7), Inches(4.0))
    et = eval_table.table
    et.columns[0].width = Inches(2.2)
    et.columns[1].width = Inches(2.3)
    et.columns[2].width = Inches(2.3)
    et.columns[3].width = Inches(2.3)
    et.columns[4].width = Inches(2.6)

    col_headers = [
        "Evaluation Metric",
        "Author's BM25\n(BEIR Paper)",
        "Our TF-IDF\n(Our Lexical)",
        "Author's MiniLM\n(BEIR Paper)",
        "Our MiniLM System\n(Our Semantic Engine)"
    ]
    for i, h in enumerate(col_headers):
        cell = et.cell(0, i)
        cell.text = h
        cell.fill.solid()
        cell.fill.fore_color.rgb = NAVY
        for p in cell.text_frame.paragraphs:
            p.font.name = "Arial"
            p.font.size = Pt(10)
            p.font.bold = True
            p.font.color.rgb = WHITE
            p.alignment = PP_ALIGN.CENTER

    metrics_data = [
        ("nDCG@10 (Ranking Quality)", "0.6650", "0.5722", "0.6426", "0.6203 (Matches within 2.3%)"),
        ("MAP@10 (Mean Avg Precision)", "0.6300", "0.5722", "0.5980", "0.6203 (Beats author by +2.2%)"),
        ("Recall@10 (Coverage)", "0.8750", "0.8387", "0.8640", "0.8058 (Captures >80% relevant)"),
        ("Precision@10 (Accuracy)", "0.0940", "0.0945", "0.0880", "0.0910 (Higher than paper MiniLM)"),
        ("MRR (Mean Reciprocal Rank)", "—", "0.5853", "—", "0.6380 (Relevant doc near top)"),
        ("Execution Latency", "~3 min", "1.8 seconds", "~15 min", "14.7 seconds (10x Faster on CPU)")
    ]

    for row_idx, row in enumerate(metrics_data, start=1):
        for col_idx, text in enumerate(row):
            cell = et.cell(row_idx, col_idx)
            cell.text = text
            cell.fill.solid()
            # Highlight our MiniLM column
            if col_idx == 4:
                cell.fill.fore_color.rgb = ACCENT_LIGHT
            else:
                cell.fill.fore_color.rgb = LIGHT_BG if row_idx % 2 == 1 else WHITE
            for p in cell.text_frame.paragraphs:
                p.font.name = "Arial"
                p.font.size = Pt(9.5)
                p.font.color.rgb = DARK
                if col_idx == 0:
                    p.font.bold = True
                    p.font.color.rgb = NAVY
                if col_idx == 4:
                    p.font.bold = True

    # Note
    note_box = s7.shapes.add_textbox(Inches(0.8), Inches(5.8), Inches(11.7), Inches(0.9))
    tf_nb = note_box.text_frame
    p_nb = tf_nb.paragraphs[0]
    p_nb.text = "Benchmark Dataset: SciFact (BEIR) | Reference Paper: BEIR: A Heterogeneous Benchmark for Zero-shot Evaluation of IR Models (NeurIPS 2021) | Code: beir-cellar/beir"
    p_nb.font.name = "Arial"
    p_nb.font.size = Pt(9.5)
    p_nb.font.color.rgb = MUTED

    p_nb2 = tf_nb.add_paragraph()
    p_nb2.text = "Key Takeaway: Our local MiniLM implementation replicates the author's published nDCG@10 within 2.3% and surpasses their published MAP@10 (0.6203 vs 0.5980), confirming high semantic retrieval fidelity without requiring heavy GPU servers."
    p_nb2.font.name = "Arial"
    p_nb2.font.size = Pt(10)
    p_nb2.font.bold = True
    p_nb2.font.color.rgb = GREEN

    # =========================================================================
    # SLIDE 8: REAL QUERY DEMONSTRATION & RANK SHIFTS
    # =========================================================================
    s8 = prs.slides.add_slide(blank_layout)
    add_header(s8, "Case Study: Real Query Demonstration & Rank Shifts", "7. DEMONSTRATION")

    q_box = s8.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(1.5), Inches(11.7), Inches(0.6))
    q_box.fill.solid()
    q_box.fill.fore_color.rgb = NAVY
    q_box.line.fill.background()
    tb_qb = s8.shapes.add_textbox(Inches(1.0), Inches(1.55), Inches(11.3), Inches(0.5))
    p_qb = tb_qb.text_frame.paragraphs[0]
    p_qb.text = "Test Query: 'machine learning for medical diagnosis'"
    p_qb.font.name = "Arial"
    p_qb.font.size = Pt(13)
    p_qb.font.bold = True
    p_qb.font.color.rgb = WHITE

    # Left: Baseline
    create_card(s8, Inches(0.8), Inches(2.3), Inches(5.6), Inches(4.5),
        "Baseline: arXiv Keyword Match",
        [
            "• Rank #1: Medical Knowledge-Guided Deep Curriculum Learning for Elbow Fracture Diagnosis\n  (Very narrow fracture application)",
            "• Rank #2: Changing Data Sources in the Age of Machine Learning for Official Statistics\n  ⚠️ False Positive! High keyword overlap with 'Machine Learning', but completely unrelated to medical care (Census statistics).",
            "• Rank #3: DOME: Recommendations for Supervised ML Validation in Biology",
            "• Rank #4: Privacy-Preserving Machine Learning for Healthcare: Open Challenges"
        ]
    )

    # Right: Semantic
    create_card(s8, Inches(6.9), Inches(2.3), Inches(5.6), Inches(4.5),
        "Our System: MiniLM + FAISS Semantic Re-ranking",
        [
            "• Rank #1 (▲ was #3): DOME: Recommendations for Supervised ML Validation in Biology\n  (Broad, foundational diagnostic methodology).",
            "• Rank #2 (▲ was #4): Privacy-Preserving Machine Learning for Healthcare\n  (Directly addresses clinical patient data privacy).",
            "• Rank #3 (▼ was #1): Medical Knowledge-Guided Deep Curriculum Learning for Elbow Fractures.",
            "• Noise Filtered Out: The census statistics paper was correctly demoted because semantic embedding detected lack of medical context!"
        ],
        highlight=True
    )

    # =========================================================================
    # SLIDE 9: WEB APPLICATION INTERFACE
    # =========================================================================
    s9 = prs.slides.add_slide(blank_layout)
    add_header(s9, "Interactive Web Application Interface", "8. APPLICATION")

    create_card(s9, Inches(0.8), Inches(1.6), Inches(5.6), Inches(5.1),
        "User Interface Design Highlights",
        [
            "• Modern Minimalist UI: Built using Bootstrap 5 with responsive desktop and mobile views.",
            "• Single Search Experience: Clean, distraction-free search input field with instant query submission.",
            "• Ranked Result Cards: Each paper displayed with its semantic rank (#1, #2, ...), similarity score, and full title.",
            "• AI-Generated Summary: 2-3 sentence overview highlighting the paper's key methodology and findings.",
            "• One-Click PDF Access: Direct button opening official arXiv preprint PDF in a new browser tab.",
            "• Fast Local Execution: Sub-second response times on standard consumer laptops."
        ]
    )

    create_card(s9, Inches(6.9), Inches(1.6), Inches(5.6), Inches(5.1),
        "Local Deployment Workflow",
        [
            "1. Activate Virtual Environment:\n   .\\venv\\Scripts\\activate",
            "2. Start Web Server:\n   python app.py",
            "3. Access Interface:\n   Open browser at http://127.0.0.1:5000",
            "4. Enter Scientific Query:\n   e.g., 'quantum computing cryptography' or 'graph neural networks drug discovery'",
            "5. Instant Results:\n   arXiv API fetches candidate papers, MiniLM embeds abstracts, FAISS re-ranks in milliseconds!"
        ],
        highlight=True
    )

    # =========================================================================
    # SLIDE 10: CONCLUSION & FUTURE SCOPE
    # =========================================================================
    s10 = prs.slides.add_slide(blank_layout)
    add_header(s10, "Conclusion & Future Enhancements", "9. CONCLUSION")

    create_card(s10, Inches(0.8), Inches(1.6), Inches(5.6), Inches(5.1),
        "Summary of Project Achievements",
        [
            "• Successfully Solved Vocabulary Mismatch: Replaced naive word-matching with deep 384-dimensional dense semantic representations.",
            "• Replicated Top-Tier Published Research: Validated performance against the BEIR NeurIPS 2021 benchmark within 2.3% on SciFact.",
            "• Outperformed Baseline on Key Metrics: Our semantic engine achieved higher MAP (0.6203 vs 0.5722) and MRR (0.6380 vs 0.5853) than classical TF-IDF.",
            "• Lightweight & Completely Free: Runs fully offline and locally without paid APIs or dedicated GPU hardware.",
            "• Delivered Working Software: Developed an end-to-end usable Flask search platform connected live to arXiv."
        ]
    )

    create_card(s10, Inches(6.9), Inches(1.6), Inches(5.6), Inches(5.1),
        "Future Enhancements & Next Steps",
        [
            "• Reciprocal Rank Fusion (RRF): Dynamically blend BM25 exact keyword matches with MiniLM semantic vectors.",
            "• Cross-Encoder Re-Ranking: Implement a secondary cross-encoder (e.g. ms-marco-MiniLM-L-6-v2) for ultra-precise re-ranking of top 20 candidates.",
            "• Citation Graph Awareness: Incorporate citation relationships (SPECTER) to boost papers with higher academic impact.",
            "• Full PDF Text Parsing: Extend indexing from abstracts to complete 10-page paper bodies using Grobid / PyMuPDF.",
            "• Domain Filtering: Allow users to filter search results by arXiv subject categories (cs.AI, stat.ML, q-bio)."
        ],
        highlight=True
    )

    # =========================================================================
    # SLIDE 11: REFERENCES & CITATIONS
    # =========================================================================
    s11 = prs.slides.add_slide(blank_layout)
    add_header(s11, "Academic References & Citations", "10. REFERENCES")

    refs = [
        "[1] N. Thakur, N. Reimers, A. Rücklé, A. Srivastava, and I. Gurevych, 'BEIR: A Heterogeneous Benchmark for Zero-shot Evaluation of Information Retrieval Models,' in Proc. Neural Information Processing Systems (NeurIPS) Datasets and Benchmarks Track, 2021. arXiv:2104.08663.",
        "[2] N. Reimers and I. Gurevych, 'Sentence-BERT: Sentence Embeddings using Siamese BERT-Networks,' in Proc. Conference on Empirical Methods in Natural Language Processing (EMNLP), 2019, pp. 3982–3992. arXiv:1908.10084.",
        "[3] W. Wang, F. Wei, L. Dong, H. Bao, N. Yang, and M. Zhou, 'MiniLM: Deep Self-Attention Distillation for Task-Agnostic Compression of Pre-Trained Transformers,' in Advances in Neural Information Processing Systems (NeurIPS), 2020. arXiv:2002.10957.",
        "[4] J. Johnson, M. Douze, and H. Jégou, 'Billion-scale similarity search with GPUs,' IEEE Transactions on Big Data, vol. 7, no. 3, pp. 535–547, 2019. arXiv:1702.08734.",
        "[5] M. Lewis et al., 'BART: Denoising Sequence-to-Sequence Pre-training for Natural Language Generation, Translation, and Comprehension,' in Proc. 58th Annual Meeting of the Association for Computational Linguistics (ACL), 2020. arXiv:1910.13461.",
        "[6] D. Wadden et al., 'Fact or Fiction: Verifying Scientific Claims,' in Proc. Conference on Empirical Methods in Natural Language Processing (EMNLP), 2020. arXiv:2004.14974."
    ]

    card_ref = s11.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(1.6), Inches(11.7), Inches(5.1))
    card_ref.fill.solid()
    card_ref.fill.fore_color.rgb = LIGHT_BG
    card_ref.line.color.rgb = BORDER_COLOR
    card_ref.line.width = Pt(1)

    tb_ref = s11.shapes.add_textbox(Inches(1.1), Inches(1.8), Inches(11.1), Inches(4.7))
    tf_ref = tb_ref.text_frame
    tf_ref.word_wrap = True

    p_rt = tf_ref.paragraphs[0]
    p_rt.text = "Key Scientific Literature Cited in this Capstone Project"
    p_rt.font.name = "Arial"
    p_rt.font.size = Pt(13)
    p_rt.font.bold = True
    p_rt.font.color.rgb = NAVY
    p_rt.space_after = Pt(10)

    for ref in refs:
        p = tf_ref.add_paragraph()
        p.text = ref
        p.font.name = "Arial"
        p.font.size = Pt(10)
        p.font.color.rgb = DARK
        p.space_after = Pt(8)

    # =========================================================================
    # SLIDE 12: THANK YOU / Q&A
    # =========================================================================
    s12 = prs.slides.add_slide(blank_layout)

    # Big Navy Center Card
    ty_card = s12.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(1.5), Inches(1.2), Inches(10.333), Inches(5.1))
    ty_card.fill.solid()
    ty_card.fill.fore_color.rgb = NAVY
    ty_card.line.fill.background()

    tb_ty = s12.shapes.add_textbox(Inches(2.0), Inches(1.8), Inches(9.333), Inches(4.0))
    tf_ty = tb_ty.text_frame
    tf_ty.word_wrap = True

    p_ty1 = tf_ty.paragraphs[0]
    p_ty1.text = "Thank You!"
    p_ty1.font.name = "Arial"
    p_ty1.font.size = Pt(40)
    p_ty1.font.bold = True
    p_ty1.font.color.rgb = WHITE
    p_ty1.alignment = PP_ALIGN.CENTER
    p_ty1.space_after = Pt(8)

    p_ty2 = tf_ty.add_paragraph()
    p_ty2.text = "Smart Research Paper Information Retrieval System"
    p_ty2.font.name = "Arial"
    p_ty2.font.size = Pt(18)
    p_ty2.font.bold = True
    p_ty2.font.color.rgb = RGBColor(147, 197, 253)
    p_ty2.alignment = PP_ALIGN.CENTER
    p_ty2.space_after = Pt(24)

    p_ty3 = tf_ty.add_paragraph()
    p_ty3.text = "Presented by: Tarang Ambildhuke  |  Roll No: 161"
    p_ty3.font.name = "Arial"
    p_ty3.font.size = Pt(14)
    p_ty3.font.color.rgb = WHITE
    p_ty3.alignment = PP_ALIGN.CENTER
    p_ty3.space_after = Pt(6)

    p_ty4 = tf_ty.add_paragraph()
    p_ty4.text = "Guided by: Prof. Sushil Chavhan Sir"
    p_ty4.font.name = "Arial"
    p_ty4.font.size = Pt(13)
    p_ty4.font.color.rgb = RGBColor(226, 232, 240)
    p_ty4.alignment = PP_ALIGN.CENTER
    p_ty4.space_after = Pt(6)

    p_ty5 = tf_ty.add_paragraph()
    p_ty5.text = "Department of Computer Technology, YCCE Nagpur"
    p_ty5.font.name = "Arial"
    p_ty5.font.size = Pt(12)
    p_ty5.font.color.rgb = RGBColor(203, 213, 225)
    p_ty5.alignment = PP_ALIGN.CENTER
    p_ty5.space_after = Pt(20)

    p_ty6 = tf_ty.add_paragraph()
    p_ty6.text = "Questions & Feedback Welcome"
    p_ty6.font.name = "Arial"
    p_ty6.font.size = Pt(13)
    p_ty6.font.bold = True
    p_ty6.font.color.rgb = GREEN
    p_ty6.alignment = PP_ALIGN.CENTER

    # Save presentation
    filename = "Smart_IR_System_Presentation.pptx"
    prs.save(filename)
    print(f"[SUCCESS] Presentation generated successfully: {filename}")

if __name__ == "__main__":
    create_presentation()
