# -*- coding: utf-8 -*-
"""Geongyu Lee: CV content, three languages.
Publication titles are verbatim as published (DOI / arXiv page) and stay in English in
every edition; talk titles stay in their original language in every edition (the KIIE
talk is Korean). Only surrounding labels and prose are localised (PUBS extras are
per-language dicts: {"en": ..., "ko": ..., "ja": ...}).
"""

# Each edition links to Scholar in its own interface language ("scholar" key below).
SCHOLAR = "https://scholar.google.com/citations?user=43BuluYAAAAJ"

# Shared across languages: (title, venue, extra); extra is localised per edition.
# Order: first / co-first author first, then the rest newest first.
PUBS = [
    ("Assessing the risk of recurrence in early-stage breast cancer through H&amp;E stained whole slide images.",
     "Scientific Reports 15, 35069, 2025.",
     {"en": "First author · doi.org/10.1038/s41598-025-16679-x",
      "ko": "제1저자 · doi.org/10.1038/s41598-025-16679-x",
      "ja": "筆頭著者 · doi.org/10.1038/s41598-025-16679-x"}),
    ("MoSPR: Histology-to-Gene Expression Prediction with Morpho-Spatial Macrostates and Low-Rank Molecular Programs.",
     "Preprint, 2026.",
     {"en": "Co-first author · arXiv:2609.34280 · code released",
      "ko": "공동 제1저자 · arXiv:2609.34280 · 코드 공개",
      "ja": "共同筆頭著者 · arXiv:2609.34280 · コード公開"}),
    ("Artificial intelligence–driven digital pathology in urological cancers: current trends and future directions.",
     "Prostate International 13(4), 181–190, 2025.",
     {"en": "Review · co-first author · doi.org/10.1016/j.prnil.2025.02.002",
      "ko": "리뷰 논문 · 공동 제1저자 · doi.org/10.1016/j.prnil.2025.02.002",
      "ja": "総説 · 共同筆頭著者 · doi.org/10.1016/j.prnil.2025.02.002"}),
    ("KPIs 2024 challenge: Advancing glomerular segmentation from patch- to slide-level.",
     "Medical Image Analysis 114, 104234, 2026.",
     {"en": "Challenge report · co-author · team 2nd place, whole-slide track · doi.org/10.1016/j.media.2026.104234",
      "ko": "챌린지 결과 논문 · 공저자 · 전체 슬라이드 트랙 2위(딥바이오 팀) · doi.org/10.1016/j.media.2026.104234",
      "ja": "チャレンジ報告論文 · 共著者 · WSIレベル部門でチーム2位 · doi.org/10.1016/j.media.2026.104234"}),
    ("Spatial proteomics guided by H&amp;E-based AI reveals recurrence-risk niches in triple-negative breast cancer.",
     "Preprint, 2026.",
     {"en": "Co-author · arXiv:2608.03145",
      "ko": "공저자 · arXiv:2608.03145",
      "ja": "共著者 · arXiv:2608.03145"}),
    ("Efficient AI-Driven Multi-Section Whole Slide Image Analysis for Biochemical Recurrence Prediction in Prostate Cancer.",
     "Preprint, 2026.",
     {"en": "Co-author · arXiv:2603.20273",
      "ko": "공저자 · arXiv:2603.20273",
      "ja": "共著者 · arXiv:2603.20273"}),
    ("G2L: From Giga-Scale to Cancer-Specific Large-Scale Pathology Foundation Models via Knowledge Distillation.",
     "AAAI 2026 Workshop (W3PHIAI).",
     {"en": "Oral · co-author · arXiv:2510.11176",
      "ko": "구두 발표 · 공저자 · arXiv:2510.11176",
      "ja": "口頭発表 · 共著者 · arXiv:2510.11176"}),
    ("MurSS: A Multi-Resolution Selective Segmentation Model for Breast Cancer.",
     "Bioengineering 11(5), 463, 2024.",
     {"en": "Co-author · doi.org/10.3390/bioengineering11050463",
      "ko": "공저자 · doi.org/10.3390/bioengineering11050463",
      "ja": "共著者 · doi.org/10.3390/bioengineering11050463"}),
    ("Supervised Contrastive Embedding for Medical Image Segmentation.",
     "IEEE Access 9, 138403–138414, 2021.",
     {"en": "Co-author · doi.org/10.1109/ACCESS.2021.3118694",
      "ko": "공저자 · doi.org/10.1109/ACCESS.2021.3118694",
      "ja": "共著者 · doi.org/10.1109/ACCESS.2021.3118694"}),
]

# Contact line: (label, url) tuples render as links; plain strings render as text.
# For now the CV lists only the portfolio, GitHub and Google Scholar (owner's request).
def contact(scholar_url):
    return [
        ("geongyu.github.io", "https://geongyu.github.io"),
        ("github.com/Geongyu", "https://github.com/Geongyu"),
        ("Google Scholar", scholar_url),
    ]

EN = {
    "lang": "en",
    "name": "Geongyu Lee",
    "native": "이건규 · イ・ゴンギュ",
    "role": "Machine Learning Researcher · Computational Pathology × Multi-Omics",
    "scholar": SCHOLAR + "&hl=en",
    "contact": contact(SCHOLAR + "&hl=en") + ["Seoul, Republic of Korea"],
    "summary": (
        "I develop machine learning models that predict molecular measurements from pathology slides and, in my "
        "current industry work, drug response from proteomics. I focus on whether these predictions remain valid "
        "at new hospitals and for drugs not seen in training. I have 5+ years of industry R&amp;D experience, and "
        "at Deep Bio I contributed to pre-deployment model validation for a medical-AI product submitted to "
        "Korea's Ministry of Food and Drug Safety (MFDS)."),
    "h_pubs": "Selected Publications",
    "scholar_note": "Google Scholar · 58 citations · h-index 5 · i10-index 3 · as of Sep 2026",
    "h_exp": "Experience",
    "h_proj": "Selected Projects",
    "h_edu": "Education",
    "h_skills": "Skills",
    "h_awards": "Awards &amp; Funded Research",
    "h_talks": "Conference Presentations",
    "jobs": [
        ("OMIXAI (formerly RadiSen)", "Feb 2025 – Present", "AI Researcher · Seoul", [
            "Lead R&amp;D on a multi-omics model that combines proteomics and RNA with H&amp;E pathology to predict drug response (in progress).",
            "Built a proteomics-based model of cell-line drug response (IC50) and evaluated it with leave-drug-out splits, so test drugs were never seen in training (Pearson ≥ 0.65; internal R&amp;D, unpublished). Also worked on self-supervised representation learning for proteomics with LoRA/PEFT.",
            "Developed ADMET prediction models and a drug-recommendation algorithm for canine cancer (top-k ≥ 70% on an in-house cohort; internal R&amp;D, unpublished).",
            "Co-led OMIXAI's team entry in the Arc Institute Virtual Cell Challenge (predicting CRISPR-knockdown response in pluripotent stem cells).",
            "Co-first author of the MoSPR preprint on gene-expression prediction from H&amp;E (code released). The method ranked 1st of 15 in the paper's benchmark on three TCGA cancers (gene-wise PCC).",
        ]),
        ("Deep Bio", "Mar 2021 – Jan 2025", "AI Researcher · Seoul", [
            "First-authored a two-hospital study (n=125) predicting Oncotype DX recurrence-score risk groups from H&amp;E slides alone (Scientific Reports 2025; sensitivity 0.86 / 0.75 / 0.53 for low / intermediate / high risk). Built a WSI pipeline that processed 500+ slides.",
            "Developed a lymph-node metastasis detection model and, with the Deep Bio team, the glomerular segmentation model for the KPIs 2024 Challenge at MICCAI 2024 (2nd place, whole-slide track). Co-authored the challenge report (Medical Image Analysis, 2026).",
            "Led prostate metastasis and recurrence-risk modeling projects.",
            "Presented first-author breast-cancer pathology posters at AACR (2022, 2023) and USCAP (2022).",
            "Contributed to pre-deployment model validation and regulatory documentation for a medical-AI product submitted to Korea's MFDS. Built internal server-automation tools with Docker.",
        ]),
        ("Nuricon", "2021", "Intern · Pangyo", [
            "Built a parking-lot fire-detection AI system.",
        ]),
    ],
    "projects": [
        ("Brain-hemorrhage detection on CT", "SK / Ajou Univ. Hospital",
         "2D and 3D hemorrhage segmentation and slice-level classification. Validated domain generalization on external data and checked classification reliability with class-activation maps."),
        ("FlyGate: agent for drug discovery and pharmacovigilance", "NVIDIA Korea Agentic AI Hackathon 2026",
         "Side project with a team of 5. Built the FlyDiscovery module and its UI on BioNeMo NIM (off-the-shelf model checks: OpenFold3 RMSD&nbsp;1.0&nbsp;Å, Boltz-2 affinity ρ&nbsp;0.767)."),
    ],
    "education": [
        ("M.S. Data Science · Seoul National University of Science and Technology (SeoulTech)", "2019 – 2021",
         "Advisor: Prof. Sangheum Hwang · Thesis: contrastive loss for segmentation under uncertain medical-image labels."),
        ("B.S. Information Security · Daejeon University", "2012 – 2019", ""),
    ],
    "skills": [
        ("Deep Learning", "PyTorch, HuggingFace, PEFT / LoRA, Accelerate, DDP / FSDP"),
        ("Pathology", "OpenSlide, QuPath, CLAM / weakly-supervised MIL, UNI · CONCH · Virchow, WSI tiling"),
        ("Bio / Omics", "scanpy · AnnData, single-cell perturbation, proteomic representation learning, ADMET"),
        ("MLOps &amp; Languages", "Python, R, SQL, Bash, Docker, Slurm, W&amp;B, MLflow, FastAPI, Git"),
    ],
    "awards": [
        ("KPIs 2024 Challenge · Whole-Slide Track",
         "2nd place · glomerular segmentation, held in conjunction with MICCAI 2024 · results published in Medical Image Analysis 2026"),
        ("Pan-Sarcoma Proteogenomic Profiling for Precision Oncology",
         "Korea–Japan · Kyung Hee Univ. Medical Center · 2025–2028 · Participating Researcher"),
        ("Virtual-Cell CDSS for Veterinary Oncology",
         "IPET / Ministry of Agriculture · 2026–2030 (awarded) · Participating Researcher"),
        ("General-Purpose AI for Cancer Pathology Diagnosis",
         "Lead: Deep Bio · National R&amp;D · program 2021–2025 · Participating Researcher, Apr 2021 – Jan 2025"),
    ],
    "h_service": 'Community &amp; Service',
    "service": [
        ('Research member (Runner), AutoBioX: AI Agents for End-to-End Bio Research, Pseudo Lab Season 12', '2026 · completed · two studies accepted at BIOINFO/GIW ISCB-Asia 2026, then submitted to ML4H 2026 Findings (under review)'),
        ('Reviewer, ML4H 2026 (Machine Learning for Health Symposium)', '2026'),
        ('AI Career &amp; Project Mentor, Codeit', '2025 – Present · part-time · 30+ mentees 1:1, 8+ project teams across 3 cohorts'),
    ],
    "talks": [
        ('Predictability is not substitutability: a cost-of-substitution framework for H&amp;E-based molecular prediction across 5 cancers', 'BIOINFO/GIW ISCB-Asia 2026 · Accepted poster · First author'),
        ('A reliability map for per-gene multiome RNA velocity parameters in single-cell kinetics', 'BIOINFO/GIW ISCB-Asia 2026 · Accepted oral · Co-author'),
        ('Predicting Protein Receptor Status from H&amp;E-stained Images in Breast Cancer', 'AACR Annual Meeting 2023 · Poster · First author'),
        ('Recurrence Risk Prediction Based on Automatic Histologic Analysis of Breast Cancer Using Whole Slide Images', 'AACR Annual Meeting 2022 · Poster · First author'),
        ('A Deep Learning based Pancreatic Adenocarcinoma Survival Prediction Model Applicable to Adenocarcinoma of Other Organs', 'AACR Annual Meeting 2022 · Poster · Co-author'),
        ('Automatic Histological Grading of Breast Cancer Resection Tissue', 'USCAP Annual Meeting 2022 · Poster · First author'),
        ('Breast Cancer Survival Analysis through the Extracted Feature from the Prostate Diagnosis Model', 'USCAP Annual Meeting 2022 · Poster · Co-author'),
        ('영역분할 모델 성능 향상을 위한 대조적 손실 함수의 활용 (Utilizing a contrastive loss to improve segmentation model performance)', 'KIIE Fall Conference 2020 · Oral · First author'),
    ],
}

KO = {
    "lang": "ko",
    "name": "이건규",
    "native": "Geongyu Lee",
    "role": "머신러닝 리서처 · 크로스모달 학습 / 신뢰할 수 있는 예측 / Computational Pathology × 멀티오믹스",
    "scholar": SCHOLAR + "&hl=ko",
    "contact": contact(SCHOLAR + "&hl=ko") + ["대한민국 서울"],
    "summary": (
        "병리 슬라이드로 분자 정보를 예측하는 머신러닝 모델을 연구하며, 현 직장에서는 프로테오믹스로 약물 반응을 "
        "예측하는 모델도 개발합니다. 새로운 병원의 데이터나 학습에 없던 약물에서도 예측이 유효한지 검증하는 데 집중합니다. "
        "산업계 R&amp;D 경력은 5년 이상이며, 딥바이오에서는 식약처에 인허가를 신청한 의료 AI 제품의 출시 전 모델 "
        "검증에 기여했습니다."),
    "h_pubs": "주요 논문",
    "scholar_note": "Google Scholar · 인용 58회 · h-index 5 · i10-index 3 · 2026년 9월 기준",
    "h_exp": "경력",
    "h_proj": "대표 프로젝트",
    "h_edu": "학력",
    "h_skills": "기술 스택",
    "h_awards": "수상 및 연구과제",
    "h_talks": "학회 발표",
    "jobs": [
        ("OMIXAI(구 래디센)", "2025.02 – 현재", "AI 리서처 · 서울", [
            "프로테오믹스·RNA와 H&amp;E 병리를 통합한 약물 반응 예측 멀티오믹스 모델 R&amp;D 주도(진행 중)",
            "프로테오믹스 기반 세포주 약물 반응(IC50) 예측 모델 개발 및 leave-drug-out 평가(학습에 없던 약물로만 테스트, Pearson ≥ 0.65, 사내 R&amp;D, 미공개), LoRA/PEFT 기반 자기지도 프로테옴 표현 학습 별도 수행",
            "반려견 종양 약물 추천 알고리즘(자체 코호트 top-k ≥ 70%, 사내 R&amp;D, 미공개) 및 ADMET 예측 모델 개발",
            "Arc Institute Virtual Cell Challenge OMIXAI 참가팀 공동 주도(만능줄기세포 CRISPR 녹다운 반응 예측)",
            "H&amp;E 기반 유전자 발현 예측 모델 MoSPR 공동 제1저자(논문 벤치마크 15개 방법 중 유전자별 PCC 1위, TCGA 3개 암종, 프리프린트·코드 공개)",
            "G2L 논문(AAAI 2026 워크숍 W3PHIAI 구두 발표) 및 삼중음성 유방암 공간 프로테오믹스 프리프린트(2026) 공저자",
        ]),
        ("딥바이오", "2021.03 – 2025.01", "AI 리서처 · 서울", [
            "H&amp;E 슬라이드만으로 Oncotype DX 재발 점수 위험군을 예측한 2개 병원 125례 연구 제1저자(Scientific Reports 2025, 저·중·고위험군 민감도 0.86 / 0.75 / 0.53), WSI 500장 이상을 처리한 파이프라인 구축",
            "림프절 전이 검출 모델 및 KPIs 2024 챌린지 사구체 분할 모델 개발(전체 슬라이드 트랙 2위, MICCAI 2024), 챌린지 결과 논문(Medical Image Analysis, 2026) 공저자",
            "전립선암 전이·재발 위험 모델링 프로젝트 주도",
            "AACR(2022, 2023)·USCAP(2022)에서 유방암 병리 AI 연구 제1저자 발표, 췌장암·유방암 생존 예측 포스터 공저자",
            "식약처(MFDS)에 인허가를 신청한 의료 AI 제품의 출시 전 모델 검증 및 인허가 문서 작성 기여, Docker 기반 사내 서버 자동화 도구 개발",
        ]),
        ("누리콘", "2021", "인턴 · 판교", [
            "주차장 화재 감지 AI 시스템 개발",
        ]),
    ],
    "projects": [
        ("CT 뇌출혈 검출", "SK / 아주대병원",
         "뇌출혈 2D·3D 분할 및 슬라이스 단위 분류, 외부 데이터 기반 도메인 일반화 검증, class-activation map 기반 분류 신뢰성 점검"),
        ("FlyGate: 신약 탐색 → 약물감시 에이전트", "NVIDIA Korea Agentic AI 해커톤 2026",
         "5인 팀 사이드 프로젝트, BioNeMo NIM 기반 FlyDiscovery 모듈 및 UI 개발(기성 모델 점검: OpenFold3 RMSD&nbsp;1.0&nbsp;Å, Boltz-2 친화도 ρ&nbsp;0.767)"),
    ],
    "education": [
        ("서울과학기술대학교(SeoulTech) · 데이터사이언스 석사", "2019 – 2021",
         "지도교수: 황상흠 · 석사 논문: 라벨이 불확실한 의료영상에서 분할 성능을 높이는 대조 손실"),
        ("대전대학교 · 정보보안학과 학사", "2012 – 2019", ""),
    ],
    "skills": [
        ("딥러닝", "PyTorch, HuggingFace, PEFT / LoRA, Accelerate, DDP / FSDP"),
        ("디지털 병리", "OpenSlide, QuPath, CLAM / weakly-supervised MIL, UNI · CONCH · Virchow, WSI 타일링"),
        ("바이오 / 오믹스", "scanpy · AnnData, 단일세포 섭동, 프로테옴 표현 학습, ADMET"),
        ("MLOps &amp; 언어", "Python, R, SQL, Bash, Docker, Slurm, W&amp;B, MLflow, FastAPI, Git"),
    ],
    "awards": [
        ("KPIs 2024 챌린지 · 전체 슬라이드 트랙",
         "2위 · 사구체 분할 · MICCAI 2024 연계 개최 · 결과 논문 Medical Image Analysis 2026 게재"),
        ("정밀종양학을 위한 Pan-Sarcoma 프로테오지노믹스 프로파일링",
         "한·일 공동연구 · 경희대학교 의료원 · 2025 – 2028 · 참여연구원"),
        ("수의 종양학을 위한 버추얼 셀 CDSS",
         "농림축산식품부 IPET · 2026 – 2030(선정) · 참여연구원"),
        ("암 병리 진단용 범용 AI 개발·상용화",
         "딥바이오 주관 · 국가 R&amp;D · 과제 기간 2021 – 2025 · 참여연구원(2021.04 – 2025.01)"),
    ],
    "h_service": '학술·커뮤니티 활동',
    "service": [
        ('가짜연구소(Pseudo Lab) 12기 AutoBioX(AI Agents for End-to-End Bio Research) 연구 멤버(러너)', '2026 · 수료 · 연구 2편 <span class="nw">BIOINFO/GIW ISCB-Asia 2026</span> 채택, 이후 ML4H 2026 Findings 투고(심사 중)'),
        ('ML4H(Machine Learning for Health Symposium) 리뷰어', '2026'),
        ('코드잇 AI 커리어·프로젝트 멘토', '2025 – 현재 · 파트타임 · 멘티 30명 이상 1:1 멘토링, 3개 기수 프로젝트 팀 8개 이상 지도'),
    ],
    "talks": [
        ('Predictability is not substitutability: a cost-of-substitution framework for H&amp;E-based molecular prediction across 5 cancers', 'BIOINFO/GIW ISCB-Asia 2026 · 포스터 발표 채택 · 제1저자'),
        ('A reliability map for per-gene multiome RNA velocity parameters in single-cell kinetics', 'BIOINFO/GIW ISCB-Asia 2026 · 구두 발표 채택 · 공저자'),
        ('Predicting Protein Receptor Status from H&amp;E-stained Images in Breast Cancer', 'AACR 연례학술대회 2023 · 포스터 발표 · 제1저자'),
        ('Recurrence Risk Prediction Based on Automatic Histologic Analysis of Breast Cancer Using Whole Slide Images', 'AACR 연례학술대회 2022 · 포스터 발표 · 제1저자'),
        ('A Deep Learning based Pancreatic Adenocarcinoma Survival Prediction Model Applicable to Adenocarcinoma of Other Organs', 'AACR 연례학술대회 2022 · 포스터 발표 · 공저자'),
        ('Automatic Histological Grading of Breast Cancer Resection Tissue', 'USCAP 연례학술대회 2022 · 포스터 발표 · 제1저자'),
        ('Breast Cancer Survival Analysis through the Extracted Feature from the Prostate Diagnosis Model', 'USCAP 연례학술대회 2022 · 포스터 발표 · 공저자'),
        ('영역분할 모델 성능 향상을 위한 대조적 손실 함수의 활용', '대한산업공학회 추계학술대회 2020 · 구두 발표 · 제1저자'),
    ],
}

JA = {
    "lang": "ja",
    "name": "イ・ゴンギュ",
    "native": "Geongyu Lee · 이건규",
    "role": "機械学習リサーチャー · クロスモーダル学習 / 信頼できる予測 / Computational Pathology × マルチオミクス",
    "scholar": SCHOLAR + "&hl=ja",
    "contact": contact(SCHOLAR + "&hl=ja") + ["韓国・ソウル"],
    "summary": (
        "病理画像から分子情報を予測する機械学習モデルを研究し、現職ではプロテオミクスから薬剤応答を予測するモデルも開発しています。"
        "学習データに含まれない施設や薬剤でも予測が有効かどうかの検証に力を入れています。"
        "企業でのR&amp;D経験は5年以上で、Deep Bioでは韓国食品医薬品安全処(MFDS)に承認申請された医療AI製品の"
        "実運用前モデル検証に貢献しました。"),
    "h_pubs": "主要論文",
    "scholar_note": "Google Scholar · 被引用数 58 · h-index 5 · i10-index 3 · 2026年9月時点",
    "h_exp": "職務経歴",
    "h_proj": "主なプロジェクト",
    "h_edu": "学歴",
    "h_skills": "スキル",
    "h_awards": "受賞・研究課題",
    "h_talks": "学会発表",
    "jobs": [
        ("OMIXAI (旧RadiSen)", "2025.02 – 現在", "AIリサーチャー · ソウル", [
            "プロテオミクス・RNAとH&amp;E病理画像を統合して薬剤応答を予測するマルチオミクスモデルの研究開発を主導(進行中)",
            "プロテオミクスに基づく細胞株の薬剤応答(IC50)予測モデルを開発し、テスト薬剤を学習から完全に除いた<span class=\"nw\">leave-drug-out方式</span>で評価(Pearson ≥ 0.65、社内R&amp;D・未発表)。LoRA/PEFTによる自己教師ありプロテオーム表現学習も実施",
            "犬の腫瘍に対する薬剤推薦アルゴリズム(自社コホートでtop-k ≥ 70%、社内R&amp;D・未発表)とADMET予測モデルの開発",
            "OMIXAIチームの共同リーダーとしてArc Institute Virtual Cell Challengeに参加(多能性幹細胞のCRISPRノックダウン応答予測)",
            "H&amp;E画像から遺伝子発現を予測するMoSPR論文の共同筆頭著者(TCGA 3がん種での論文内比較で遺伝子別PCCが15手法中1位)",
            "G2L論文(AAAI 2026 ワークショップ W3PHIAI 口頭発表)およびトリプルネガティブ乳がんの空間プロテオミクス研究(プレプリント、2026)の共著者",
        ]),
        ("Deep Bio", "2021.03 – 2025.01", "AIリサーチャー · ソウル", [
            "H&amp;E画像のみからOncotype DX再発スコアのリスク群を予測した2施設・125例の研究の筆頭著者(Scientific Reports 2025、<span class=\"nw\">低・中・高リスクの感度</span> 0.86 / 0.75 / 0.53)。WSIパイプラインを構築し、500枚以上のスライドを処理",
            "リンパ節転移検出モデルとKPIs 2024チャレンジ向け糸球体セグメンテーションモデルの開発(WSIレベル部門2位、MICCAI&nbsp;2024)。チャレンジ報告論文(Medical Image Analysis、2026)の共著者",
            "前立腺がんの転移・再発リスクモデリングのプロジェクトを主導",
            "AACR(2022、2023)・USCAP(2022)で乳がん病理AI研究を筆頭著者として発表。膵臓がん・乳がん生存予測ポスターの共著者",
            "MFDSに承認申請された医療AI製品の実運用前モデル検証と申請文書作成に貢献。Dockerによる社内サーバー自動化ツールの開発",
        ]),
        ("Nuricon", "2021", "インターン · 板橋(パンギョ)", [
            "駐車場向け火災検知AIシステムの開発",
        ]),
    ],
    "projects": [
        ("CT脳出血検出", "SK / 亜洲大学校病院",
         "脳出血の2D・3Dセグメンテーションとスライス単位の分類。外部データでのドメイン汎化の検証と、class-activation mapによる分類根拠の点検"),
        ("FlyGate: 創薬探索 → 医薬品安全性監視エージェント", "NVIDIA Korea Agentic AI ハッカソン 2026",
         "5人チームでのサイドプロジェクト。BioNeMo NIMを用いたFlyDiscoveryモジュールとそのUIを担当(既製NIMの検証でOpenFold3&nbsp;RMSD&nbsp;1.0&nbsp;Å、Boltz-2 親和性 ρ&nbsp;0.767)"),
    ],
    "education": [
        ("修士(データサイエンス) · ソウル科学技術大学校(SeoulTech)", "2019 – 2021",
         "指導教員：ファン・サンフム教授 · 修士論文：ラベルが不確実な医療画像のセグメンテーション性能を高める対照損失"),
        ("学士(情報セキュリティ) · 大田大学校", "2012 – 2019", ""),
    ],
    "skills": [
        ("深層学習", "PyTorch, HuggingFace, PEFT / LoRA, Accelerate, DDP / FSDP"),
        ("病理", "OpenSlide, QuPath, CLAM / weakly-supervised MIL, UNI · CONCH · Virchow, WSIタイリング"),
        ("バイオ / オミクス", "scanpy · AnnData, シングルセル摂動, プロテオーム表現学習, ADMET"),
        ("MLOps・言語", "Python, R, SQL, Bash, Docker, Slurm, W&amp;B, MLflow, FastAPI, Git"),
    ],
    "awards": [
        ("KPIs 2024チャレンジ · WSIレベル部門",
         "2位 · 糸球体セグメンテーション · MICCAI 2024 併催 · Medical Image Analysis 2026 掲載"),
        ("精密腫瘍学に向けたPan-Sarcomaプロテオゲノムプロファイリング",
         "日韓共同 · 慶熙大学校医療院 · 2025–2028 · 研究員として参画"),
        ("獣医腫瘍学に向けたバーチャルセルCDSS",
         "農林畜産食品部 IPET · 2026–2030(採択) · 研究員として参画"),
        ("がん病理診断向け汎用AIの開発・実用化",
         "代表機関：Deep Bio · 国家R&amp;D · 事業期間 2021–2025 · 研究員として参画(2021.04 – 2025.01)"),
    ],
    "h_service": 'コミュニティ・学術貢献',
    "service": [
        ('Pseudo Lab シーズン12「AutoBioX: AI Agents for End-to-End Bio Research」研究メンバー(ランナー)', '2026 · 修了 · 研究2件が<span class="nw">BIOINFO/GIW ISCB-Asia 2026</span>に採択、その後ML4H 2026 Findingsへ投稿(査読中)'),
        ('ML4H 2026(Machine Learning for Health Symposium)査読者', '2026'),
        ('AIキャリア・プロジェクトメンター(Codeit)', '2025 – 現在 · 非常勤 · メンティー30名以上への1対1メンタリング、3期にわたり8チーム以上のプロジェクトを指導'),
    ],
    "talks": [
        ('Predictability is not substitutability: a cost-of-substitution framework for H&amp;E-based molecular prediction across 5 cancers', 'BIOINFO/GIW ISCB-Asia 2026 · ポスター発表(採択) · 筆頭著者'),
        ('A reliability map for per-gene multiome RNA velocity parameters in single-cell kinetics', 'BIOINFO/GIW ISCB-Asia 2026 · 口頭発表(採択) · 共著者'),
        ('Predicting Protein Receptor Status from H&amp;E-stained Images in Breast Cancer', 'AACR年次総会 2023 · ポスター発表 · 筆頭著者'),
        ('Recurrence Risk Prediction Based on Automatic Histologic Analysis of Breast Cancer Using Whole Slide Images', 'AACR年次総会 2022 · ポスター発表 · 筆頭著者'),
        ('A Deep Learning based Pancreatic Adenocarcinoma Survival Prediction Model Applicable to Adenocarcinoma of Other Organs', 'AACR年次総会 2022 · ポスター発表 · 共著者'),
        ('Automatic Histological Grading of Breast Cancer Resection Tissue', 'USCAP年次総会 2022 · ポスター発表 · 筆頭著者'),
        ('Breast Cancer Survival Analysis through the Extracted Feature from the Prostate Diagnosis Model', 'USCAP年次総会 2022 · ポスター発表 · 共著者'),
        ('영역분할 모델 성능 향상을 위한 대조적 손실 함수의 활용 (セグメンテーションモデルの性能向上に向けた対照損失関数の活用)', '韓国産業工学会 秋季学術大会 2020 · 口頭発表 · 筆頭著者'),
    ],
}

EDITIONS = {"EN": EN, "KO": KO, "JA": JA}
