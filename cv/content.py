# -*- coding: utf-8 -*-
"""Geongyu Lee — CV content, three languages.
Publication titles stay in English in every edition (same as the previous PDFs);
only surrounding labels and prose are localised.
"""

SCHOLAR = "https://scholar.google.com/citations?user=43BuluYAAAAJ&hl=ko"

# Shared across languages: (title, venue, extra)
PUBS = [
    ("Recurrence risk prediction in early-stage breast cancer from H&amp;E whole-slide images.",
     "Scientific Reports, 2025.",
     "First author · doi.org/10.1038/s41598-025-16679-x"),
    ("G2L: From Giga-scale to Cancer-specific Pathology Foundation Models via Knowledge Distillation.",
     "AAAI 2026 Workshop (W3PHIAI), Oral.",
     "arXiv:2510.11176"),
    ("KPIs 2024 Challenge: Advancing glomerular segmentation from patch- to slide-level.",
     "Medical Image Analysis 114, 104234, 2026.",
     "2nd place, whole-slide track · doi.org/10.1016/j.media.2026.104234"),
    ("AI-driven digital pathology in urological cancers (Review).",
     "Prostate International, 2025.",
     "Co-first author"),
    ("MurSS: Multi-Resolution Selective Segmentation for breast cancer.",
     "Bioengineering, 2024.",
     "MDPI"),
    ("Spatial proteomics guided by H&amp;E-based AI reveals recurrence-risk niches in triple-negative breast cancer.",
     "Preprint, 2026.",
     "arXiv:2608.03145"),
    ("Multi-section WSI analysis for biochemical recurrence in prostate cancer.",
     "Preprint, 2026.",
     "arXiv:2603.20273"),
    ("Supervised contrastive embedding for medical image segmentation.",
     "IEEE Access, 2021.",
     ""),
]

CONTACT = ["rjsrb365@gmail.com", "github.com/Geongyu", "Google Scholar",
           "linkedin.com/in/geongyu-lee"]

EN = {
    "lang": "en",
    "name": "Geongyu Lee",
    "native": "이건규 · イ・ゴンギュ",
    "role": "AI Researcher — Computational Pathology × Multi-Omics",
    "contact": CONTACT + ["Seoul, Republic of Korea"],
    "summary": (
        "Five years building deep learning for computational pathology and drug discovery. "
        "First-author work on H&amp;E-based breast-cancer recurrence (Scientific Reports 2025), "
        "a contribution to large-scale pathology foundation models (G2L, AAAI 2026 oral), and "
        "KFDA-track model validation; now extending histopathology AI into proteomics and multi-omics. "
        "Coming from information security into medical AI, I take a robustness-first approach — "
        "calibration, uncertainty, and out-of-distribution behavior matter as much as accuracy once "
        "a model reaches the clinic."),
    "h_pubs": "Selected Publications",
    "scholar_note": "Google Scholar · 55 citations · h-index 5 · i10-index 2",
    "h_exp": "Experience",
    "h_proj": "Selected Projects",
    "h_edu": "Education",
    "h_skills": "Skills",
    "h_awards": "Awards &amp; Funding",
    "h_talks": "Talks &amp; Abstracts",
    "jobs": [
        ("OMIXAI (fmr. RadiSen)", "Feb 2025 – Present", "AI Researcher · Seoul", [
            "Lead multi-omics foundation-model R&amp;D integrating proteomics with H&amp;E pathology for drug-response prediction; co-authored the G2L pathology foundation model.",
            "Co-authored spatial-proteomics work using H&amp;E-based AI risk scores to pinpoint recurrence-risk niches in triple-negative breast cancer (preprint, 2026).",
            "Built a proteomics drug-response model (Leave-Drug-Out Pearson ≥ 0.65) and a canine veterinary-oncology drug-recommendation algorithm (top-k ≥ 70%).",
            "Advanced ADMET prediction and self-supervised proteomic representation learning with LoRA / PEFT.",
            "Co-led the Virtual Cell Challenge — predicting CRISPR-knockdown response in pluripotent stem cells.",
        ]),
        ("Deep Bio", "Mar 2021 – Jan 2025", "AI Researcher · Seoul", [
            "First-authored the multi-center breast-cancer recurrence study (Scientific Reports 2025); built a scalable WSI pipeline handling 500+ slides.",
            "Developed lymph-node metastasis detection and the KPIs 2024 glomeruli segmentation model (2nd place, whole-slide track, MICCAI) — challenge results published in Medical Image Analysis (2026).",
            "Led prostate metastasis &amp; recurrence-risk projects; presented at AACR (2022, 2023) and USCAP (2022).",
            "Contributed to KFDA regulatory documentation and validation, plus internal server-automation tooling (Docker).",
        ]),
        ("Nuricon", "2021", "Intern · Pangyo", [
            "Built a parking-lot fire-detection AI system.",
        ]),
    ],
    "projects": [
        ("Proteomics drug-response prediction", "OMIXAI",
         "Self-supervised proteomic representation with LoRA/PEFT and cell-line IC50 prediction; leave-drug-out validation (Pearson ≥ 0.65)."),
        ("Veterinary oncology CDSS &amp; Virtual Cell", "OMIXAI",
         "Canine drug-recommendation (top-k ≥ 70%) and CRISPR-knockdown response prediction in pluripotent stem cells."),
        ("Oncotype DX recurrence prediction", "Deep Bio",
         "Breast-cancer prognosis from H&amp;E WSIs only; confidence-aware selection + majority voting into GHI-RS risk groups (high-risk acc 91.2%)."),
        ("Brain-hemorrhage detection on CT", "SK / Ajou Univ. Hospital",
         "2D &amp; 3D hemorrhage segmentation, slice-level classification, domain-generalization validation with class-activation-map auditing."),
    ],
    "education": [
        ("M.S. Data Science — Seoul Nat'l University of Science and Technology (SeoulTech)", "2019 – 2021",
         "Advisor: Prof. Sangheum Hwang · Thesis: contrastive loss for segmentation under uncertain medical-image labels."),
        ("B.S. Information Security — Daejeon University", "2012 – 2019",
         "Cross-domain foundation behind a robustness-first approach."),
    ],
    "skills": [
        ("Deep Learning", "PyTorch, HuggingFace, PEFT / LoRA, Accelerate, DDP / FSDP"),
        ("Pathology", "OpenSlide, QuPath, CLAM / weakly-supervised MIL, UNI · CONCH · Virchow, WSI tiling"),
        ("Bio / Omics", "scanpy · AnnData, single-cell perturbation, proteomic representation, ADMET"),
        ("MLOps &amp; Languages", "Python, R, SQL, Bash, Docker, Slurm, W&amp;B, MLflow, FastAPI, Git"),
    ],
    "awards": [
        ("KPIs Challenge 2024 — Whole-Slide Track",
         "2nd place · Glomeruli segmentation, held at MICCAI 2024 · results published in Medical Image Analysis 2026"),
        ("Pan-Sarcoma Proteogenomic Profiling for Precision Oncology",
         "Korea–US–Japan · Kyung Hee Univ. Medical Center · 2025–2028 · KRW 400M · Participating Researcher"),
        ("Virtual-Cell CDSS for Veterinary Oncology",
         "IPET / Ministry of Agriculture · 2026–2030 (awarded) · KRW 3B+ · Participating Researcher"),
        ("General-Purpose AI for Cancer Pathology Diagnosis",
         "Lead: Deep Bio · National R&amp;D · 2021–2025 · KRW 2.375B · Participating Researcher"),
    ],
    "talks": ("AACR Annual Meeting (2022, 2023) · USCAP Annual Meeting (2022) · KIIE Fall Conference (2020) — "
              "breast-cancer recurrence, protein-receptor status from H&amp;E, cross-organ adenocarcinoma survival, "
              "and histological grading."),
}

KO = {
    "lang": "ko",
    "name": "이건규",
    "native": "Geongyu Lee · イ・ゴンギュ",
    "role": "AI 리서처 — Computational Pathology × 멀티오믹스",
    "contact": CONTACT + ["대한민국 서울"],
    "summary": (
        "5년간 Computational Pathology와 신약 개발을 위한 딥러닝을 연구해 왔습니다. H&amp;E 기반 유방암 재발 예측으로 "
        "Scientific Reports 제1저자 논문을 냈고, 대규모 병리 파운데이션 모델(G2L, AAAI 2026 구두 발표)에 기여했으며, "
        "식약처(KFDA) 인허가 모델 검증을 수행했습니다. 현재는 조직병리 AI를 프로테오믹스·멀티오믹스로 확장하고 있습니다. "
        "정보보안에서 의료 AI로 넘어온 이력 덕분에 견고함을 먼저 생각합니다 — 모델이 실제 임상에 쓰이는 순간, "
        "정확도만큼이나 보정·불확실성·분포 밖(OOD) 동작이 중요하기 때문입니다."),
    "h_pubs": "주요 논문",
    "scholar_note": "Google Scholar · 인용 55 · h-index 5 · i10-index 2",
    "h_exp": "경력",
    "h_proj": "대표 프로젝트",
    "h_edu": "학력",
    "h_skills": "기술 스택",
    "h_awards": "수상 &amp; 연구과제",
    "h_talks": "학회 발표 &amp; 초록",
    "jobs": [
        ("OMIXAI (前 래디센)", "2025.02 – 현재", "AI 리서처 · 서울", [
            "약물 반응성 예측을 위해 프로테오믹스와 H&amp;E 병리를 통합하는 멀티오믹스 파운데이션 모델 R&amp;D 주도; G2L 병리 FM 공동저자.",
            "H&amp;E 기반 AI 위험도 점수로 공간 프로테오믹스를 안내해 삼중음성 유방암의 재발 위험 니치를 규명한 연구 공동저자(프리프린트, 2026).",
            "프로테오믹스 약물 반응성 모델(Leave-Drug-Out Pearson ≥ 0.65)과 반려견 수의 종양 약물 추천 알고리즘(top-k ≥ 70%) 개발.",
            "ADMET 예측과 LoRA/PEFT 기반 자기지도 프로테옴 표현 학습 고도화.",
            "Virtual Cell Challenge 공동 주도 — 만능줄기세포의 CRISPR 넉다운 반응 예측.",
        ]),
        ("딥바이오", "2021.03 – 2025.01", "AI 리서처 / 머신러닝 엔지니어 · 서울", [
            "다기관 유방암 재발 연구 제1저자(Scientific Reports 2025); 500장 이상을 처리하는 확장형 WSI 파이프라인 구축.",
            "림프절 전이 검출 모델과 KPIs 2024 사구체 분할 모델 개발(전체 슬라이드 트랙 2위, MICCAI) — 챌린지 결과는 Medical Image Analysis(2026)에 게재.",
            "전립선 전이·재발 위험 프로젝트 리드; AACR(2022, 2023)·USCAP(2022) 발표.",
            "식약처(KFDA) 인허가 문서·검증 기여, 사내 서버 자동화 도구(Docker) 개발.",
        ]),
        ("누리콘", "2021", "인턴 · 판교", [
            "주차장 화재 감지 AI 시스템 개발.",
        ]),
    ],
    "projects": [
        ("프로테오믹스 기반 약물 반응성 예측", "OMIXAI",
         "LoRA/PEFT 기반 자기지도 프로테옴 표현 학습과 세포주 IC50 예측; leave-drug-out 검증(Pearson ≥ 0.65)."),
        ("수의 종양 CDSS &amp; 버추얼 셀", "OMIXAI",
         "반려견 약물 추천(top-k ≥ 70%)과 만능줄기세포 CRISPR 넉다운 반응 예측."),
        ("Oncotype DX 재발 예측", "딥바이오",
         "H&amp;E WSI만으로 유방암 예후 예측; 신뢰도 기반 선택 + 다수결로 GHI-RS 위험군 분류(고위험군 정확도 91.2%)."),
        ("CT 뇌출혈 검출", "SK / 아주대병원",
         "뇌출혈 2D·3D 분할, 슬라이스 단위 분류, class-activation map 기반 도메인 일반화 검증."),
    ],
    "education": [
        ("데이터사이언스 석사 — 서울과학기술대학교", "2019 – 2021",
         "지도교수: 황상흠 · 논문: 불확실한 의료영상 라벨에서 분할 성능을 높이는 대조 손실."),
        ("정보보안학 학사 — 대전대학교", "2012 – 2019",
         "견고함을 우선하는 접근의 밑바탕이 된 교차 분야 경험."),
    ],
    "skills": [
        ("딥러닝", "PyTorch, HuggingFace, PEFT / LoRA, Accelerate, DDP / FSDP"),
        ("병리", "OpenSlide, QuPath, CLAM / weakly-supervised MIL, UNI · CONCH · Virchow, WSI 타일링"),
        ("바이오 / 오믹스", "scanpy · AnnData, 단일세포 섭동, 프로테옴 표현학습, ADMET"),
        ("MLOps &amp; 언어", "Python, R, SQL, Bash, Docker, Slurm, W&amp;B, MLflow, FastAPI, Git"),
    ],
    "awards": [
        ("KPIs 챌린지 2024 — 전체 슬라이드 트랙",
         "2위 · 사구체 분할, MICCAI 2024 개최 · 결과는 Medical Image Analysis 2026 게재"),
        ("정밀종양학을 위한 Pan-Sarcoma 프로테오지노믹 프로파일링",
         "한·미·일 · 경희대학교 의료원 · 2025–2028 · 4억 원 · 참여연구원"),
        ("수의 종양학을 위한 버추얼 셀 CDSS",
         "농림축산식품부 IPET · 2026–2030 (선정) · 30억 원+ · 참여연구원"),
        ("암 병리 진단용 범용 AI 개발·상용화",
         "주관: 딥바이오 · 국가 R&amp;D · 2021–2025 · 23.75억 원 · 참여연구원"),
    ],
    "talks": ("AACR 연례학술대회(2022, 2023) · USCAP 연례학술대회(2022) · 대한산업공학회 추계학술대회(2020) — "
              "유방암 재발, H&amp;E 기반 단백질 수용체 상태, 여러 장기의 선암 생존, 조직학적 등급 예측."),
}

JA = {
    "lang": "ja",
    "name": "イ・ゴンギュ",
    "native": "Geongyu Lee · 이건규",
    "role": "AIリサーチャー — Computational Pathology × マルチオミクス",
    "contact": CONTACT + ["韓国・ソウル"],
    "summary": (
        "5年間、Computational Pathologyと創薬のための深層学習を研究してきました。H&amp;Eによる乳がん再発予測で"
        "Scientific Reports筆頭著者論文を発表し、大規模病理基盤モデル(G2L、AAAI 2026 口頭発表)に貢献、"
        "食品医薬品安全処(KFDA)承認モデル検証を担当しました。現在は組織病理AIをプロテオミクス・マルチオミクスへ拡張しています。"
        "情報セキュリティから医療AIへ移ってきた経歴から、まず頑健性を重視します — モデルが実際の臨床で使われる瞬間、"
        "精度と同じくらいキャリブレーション・不確実性・分布外(OOD)挙動が重要になるからです。"),
    "h_pubs": "主要論文",
    "scholar_note": "Google Scholar · 被引用 55 · h-index 5 · i10-index 2",
    "h_exp": "職務経歴",
    "h_proj": "主なプロジェクト",
    "h_edu": "学歴",
    "h_skills": "スキル",
    "h_awards": "受賞 &amp; 研究プロジェクト",
    "h_talks": "学会発表 &amp; 抄録",
    "jobs": [
        ("OMIXAI (前 RadiSen)", "2025.02 – 現在", "AIリサーチャー · ソウル", [
            "薬剤応答性予測のためプロテオミクスとH&amp;E病理を統合するマルチオミクス基盤モデルR&amp;Dを主導；G2L病理FM共同著者。",
            "H&amp;EベースのAIリスクスコアで空間プロテオミクスを誘導し、トリプルネガティブ乳がんの再発リスクニッチを解明した研究の共著(プレプリント、2026)。",
            "プロテオミクス薬剤応答モデル(Leave-Drug-Out Pearson ≥ 0.65)とイヌ獣医腫瘍の薬剤推薦アルゴリズム(top-k ≥ 70%)を開発。",
            "ADMET予測とLoRA/PEFTベースの自己教師ありプロテオーム表現学習を高度化。",
            "Virtual Cell Challenge共同主導 — 多能性幹細胞のCRISPRノックダウン応答予測。",
        ]),
        ("Deep Bio", "2021.03 – 2025.01", "AIリサーチャー / 機械学習エンジニア · ソウル", [
            "多施設乳がん再発研究の筆頭著者(Scientific Reports 2025)；500枚以上を処理するスケーラブルなWSIパイプラインを構築。",
            "リンパ節転移検出モデルとKPIs 2024 糸球体セグメンテーションモデルを開発(全スライドトラック2位、MICCAI) — チャレンジ結果はMedical Image Analysis(2026)に掲載。",
            "前立腺の転移・再発リスクプロジェクトを主導；AACR(2022, 2023)・USCAP(2022)で発表。",
            "食品医薬品安全処(KFDA)承認文書・検証に貢献、社内サーバ自動化ツール(Docker)を開発。",
        ]),
        ("Nuricon", "2021", "インターン · パンギョ", [
            "駐車場の火災検知AIシステムを開発。",
        ]),
    ],
    "projects": [
        ("プロテオミクスによる薬剤応答性予測", "OMIXAI",
         "LoRA/PEFTによる自己教師ありプロテオーム表現学習と細胞株IC50予測；leave-drug-out検証(Pearson ≥ 0.65)。"),
        ("獣医腫瘍CDSS &amp; バーチャルセル", "OMIXAI",
         "イヌ薬剤推薦(top-k ≥ 70%)と多能性幹細胞のCRISPRノックダウン応答予測。"),
        ("Oncotype DX 再発予測", "Deep Bio",
         "H&amp;E WSIのみで乳がん予後を予測；信頼度ベースの選択 + 多数決でGHI-RSリスク群へ分類(高リスク群精度91.2%)。"),
        ("CT脳出血検出", "SK / 亜洲大学病院",
         "脳出血の2D・3Dセグメンテーション、スライス単位分類、class-activation mapによるドメイン汎化検証。"),
    ],
    "education": [
        ("データサイエンス修士 — ソウル科学技術大学", "2019 – 2021",
         "指導教員: ファン・サンフム · 修士論文: 不確実な医療画像ラベル下でのセグメンテーションを高めるコントラスティブ損失。"),
        ("情報セキュリティ学士 — 大田大学校", "2012 – 2019",
         "頑健性を優先する姿勢の土台となった分野横断的な経験。"),
    ],
    "skills": [
        ("深層学習", "PyTorch, HuggingFace, PEFT / LoRA, Accelerate, DDP / FSDP"),
        ("病理", "OpenSlide, QuPath, CLAM / weakly-supervised MIL, UNI · CONCH · Virchow, WSIタイリング"),
        ("バイオ / オミクス", "scanpy · AnnData, 単一細胞摂動, プロテオーム表現学習, ADMET"),
        ("MLOps &amp; 言語", "Python, R, SQL, Bash, Docker, Slurm, W&amp;B, MLflow, FastAPI, Git"),
    ],
    "awards": [
        ("KPIsチャレンジ2024 — 全スライドトラック",
         "2位 · 糸球体セグメンテーション, MICCAI 2024 開催 · 結果はMedical Image Analysis 2026に掲載"),
        ("精密腫瘍学のためのPan-Sarcomaプロテオゲノムプロファイリング",
         "日米韓 · 慶熙大学校医療院 · 2025–2028 · 4億ウォン · 参加研究員"),
        ("獣医腫瘍学のためのバーチャルセルCDSS",
         "農林畜産食品部 IPET · 2026–2030 (採択) · 30億ウォン+ · 参加研究員"),
        ("がん病理診断向け汎用AIの開発・実用化",
         "主管: Deep Bio · 国家R&amp;D · 2021–2025 · 23.75億ウォン · 参加研究員"),
    ],
    "talks": ("AACR年次総会(2022, 2023) · USCAP年次総会(2022) · 韓国産業工学会 秋季学術大会(2020) — "
              "乳がん再発、H&amp;Eによるタンパク質受容体ステータス、複数臓器の腺がん生存、組織学的グレード予測。"),
}

EDITIONS = {"EN": EN, "KO": KO, "JA": JA}
