# -*- coding: utf-8 -*-
"""Geongyu Lee: CV content, three languages.
Publication titles are verbatim as published (DOI / arXiv page) and stay in English in
every edition; talk titles stay in their original language in every edition (the KIIE
talk is Korean). Only surrounding labels and prose are localised (PUBS extras are
per-language dicts: {"en": ..., "ko": ..., "ja": ...}).
"""

SCHOLAR = "https://scholar.google.com/citations?user=43BuluYAAAAJ&hl=ko"

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
     {"en": "Co-first author † · arXiv:2609.34280 · code released",
      "ko": "공동 제1저자 † · arXiv:2609.34280 · 코드 공개",
      "ja": "共同筆頭著者 † · arXiv:2609.34280 · コード公開"}),
    ("Artificial intelligence–driven digital pathology in urological cancers: current trends and future directions.",
     "Prostate International 13(4), 181–190, 2025. Review.",
     {"en": "Co-first author † · doi.org/10.1016/j.prnil.2025.02.002",
      "ko": "공동 제1저자 † · doi.org/10.1016/j.prnil.2025.02.002",
      "ja": "共同筆頭著者 † · doi.org/10.1016/j.prnil.2025.02.002"}),
    ("KPIs 2024 challenge: Advancing glomerular segmentation from patch- to slide-level.",
     "Medical Image Analysis 114, 104234, 2026.",
     {"en": "Challenge report · co-author · team 2nd place, whole-slide track · doi.org/10.1016/j.media.2026.104234",
      "ko": "챌린지 결과 논문 · 공저자 · 팀으로 전체 슬라이드 트랙 2위 · doi.org/10.1016/j.media.2026.104234",
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
     "AAAI 2026 Workshop (W3PHIAI), Oral.",
     {"en": "Co-author · arXiv:2510.11176",
      "ko": "공저자 · arXiv:2510.11176",
      "ja": "共著者 · arXiv:2510.11176"}),
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

CONTACT = ["geongyu.github.io", "github.com/Geongyu", "Google Scholar"]

EN = {
    "lang": "en",
    "name": "Geongyu Lee",
    "native": "이건규 · イ・ゴンギュ",
    "role": "Machine Learning Researcher · Cross-modal learning / Reliable prediction / Computational Pathology × Multi-Omics",
    "contact": CONTACT + ["Seoul, Republic of Korea"],
    "summary": (
        "I am a machine learning researcher in computational pathology and multi-omics for oncology. I work on "
        "predicting molecular measurements such as gene expression, receptor status and assay-based recurrence "
        "risk groups from routine H&amp;E slides, and on testing whether these predictions are reliable across "
        "sites, cohorts and unseen drugs. I have 5+ years of industry R&amp;D experience. At Deep Bio I was first "
        "author of a breast-cancer recurrence study (Scientific Reports 2025) and contributed to pre-deployment "
        "model validation for a medical-AI product submitted to Korea's MFDS. I also co-authored the G2L "
        "pathology foundation-model paper (AAAI 2026 Workshop, oral). My current work is pre-registered, "
        "site-disjoint evaluation of H&amp;E-based molecular prediction and leave-drug-out drug-response modeling."),
    "h_pubs": "Selected Publications",
    "scholar_note": "Google Scholar · 58 citations · h-index 5 · i10-index 3 · as of Sep 2026",
    "h_exp": "Experience",
    "h_proj": "Selected Projects",
    "h_edu": "Education",
    "h_skills": "Skills",
    "h_awards": "Awards &amp; Research Projects",
    "h_talks": "Conference Presentations",
    "jobs": [
        ("OMIXAI (fmr. RadiSen)", "Feb 2025 – Present", "AI Researcher · Seoul", [
            "Lead R&amp;D on a multi-omics model that combines proteomics and RNA with H&amp;E pathology to predict drug response (in progress).",
            "Built a proteomics-based drug-response (IC50) model for cell lines and evaluated it with leave-drug-out splits, so no test compound appeared in training (Pearson ≥ 0.65). Also developed self-supervised proteomic representation learning with LoRA/PEFT.",
            "Developed a drug-recommendation algorithm for canine cancer and ADMET prediction models.",
            "Co-led OMIXAI's team entry in the Arc Institute Virtual Cell Challenge (predicting CRISPR-knockdown response in pluripotent stem cells).",
            "Co-first author of MoSPR, which predicts gene expression from histology and was best of 15 methods on three TCGA cancers (preprint, code released).",
            "Co-authored the G2L paper (AAAI 2026 Workshop W3PHIAI, oral) and an H&amp;E-guided spatial-proteomics study of recurrence-risk niches in triple-negative breast cancer (preprint, 2026).",
        ]),
        ("Deep Bio", "Mar 2021 – Jan 2025", "AI Researcher · Seoul", [
            "First-authored a two-hospital breast-cancer recurrence study (Scientific Reports 2025). Built a WSI pipeline that processed 500+ slides.",
            "Developed a lymph-node metastasis detection model and the glomerular segmentation model for the KPIs 2024 Challenge at MICCAI 2024 (2nd place, whole-slide track). Co-authored the challenge report (Medical Image Analysis, 2026).",
            "Led prostate metastasis and recurrence-risk modeling projects.",
            "Presented breast-cancer pathology AI work as first author at AACR (2022, 2023) and USCAP (2022). Co-authored posters on survival prediction in pancreatic and breast cancer.",
            "Contributed to pre-deployment model validation and regulatory documentation for a medical-AI product submitted to Korea's MFDS. Built internal server-automation tools with Docker.",
        ]),
        ("Nuricon", "2021", "Intern · Pangyo", [
            "Built a parking-lot fire-detection AI system.",
        ]),
    ],
    "projects": [
        ("Proteomics drug-response prediction", "OMIXAI",
         "Cell-line drug-response (IC50) prediction from proteomics, evaluated leave-drug-out so that no test compound is seen in training (Pearson ≥ 0.65). Separate work covers self-supervised proteomic representation learning with LoRA/PEFT."),
        ("Veterinary oncology CDSS &amp; Virtual Cell", "OMIXAI",
         "Drug-recommendation algorithm for canine cancer (top-k ≥ 70% on a canine oncology cohort). Co-led OMIXAI's team entry in the Arc Institute Virtual Cell Challenge (CRISPR-knockdown response in pluripotent stem cells)."),
        ("Oncotype DX recurrence prediction", "Deep Bio",
         "Prediction of 21-gene recurrence-score risk groups from H&amp;E WSIs alone, using confidence-aware patch selection and majority voting. Scientific Reports 2025 · first author · n=125, 2 hospitals · sensitivity L / I / H 0.86 / 0.75 / 0.53, specificity L / I / H 0.82 / 0.80 / 0.97."),
        ("Brain-hemorrhage detection on CT", "SK / Ajou Univ. Hospital",
         "2D and 3D hemorrhage segmentation and slice-level classification. Validated domain generalization on external data and checked classification reliability with class-activation maps."),
        ("FlyGate: drug-discovery → pharmacovigilance agent", "NVIDIA Agentic AI Hackathon 2026",
         "Side project with a team of 5. Built the FlyDiscovery module on BioNeMo NIM (OpenFold3 1.0 Å, Boltz-2 ρ 0.767) and its UI."),
    ],
    "education": [
        ("M.S. Data Science · Seoul National University of Science and Technology (SeoulTech)", "2019 – 2021",
         "Advisor: Prof. Sangheum Hwang · Thesis: contrastive loss for segmentation under uncertain medical-image labels."),
        ("B.S. Information Security · Daejeon University", "2012 – 2019", ""),
    ],
    "skills": [
        ("Deep Learning", "PyTorch, HuggingFace, PEFT / LoRA, Accelerate, DDP / FSDP"),
        ("Pathology", "OpenSlide, QuPath, CLAM / weakly-supervised MIL, UNI · CONCH · Virchow, WSI tiling"),
        ("Bio / Omics", "scanpy · AnnData, single-cell perturbation, proteomic representation, ADMET"),
        ("MLOps &amp; Languages", "Python, R, SQL, Bash, Docker, Slurm, W&amp;B, MLflow, FastAPI, Git"),
    ],
    "awards": [
        ("KPIs 2024 Challenge · Whole-Slide Track",
         "2nd place · glomerular segmentation, held in conjunction with MICCAI 2024 · results published in Medical Image Analysis 2026"),
        ("Pan-Sarcoma Proteogenomic Profiling for Precision Oncology",
         "Korea–Japan · Kyung Hee Univ. Medical Center · 2025–2028 · total program budget KRW 400M · Participating Researcher"),
        ("Virtual-Cell CDSS for Veterinary Oncology",
         "IPET / Ministry of Agriculture · 2026–2030 (awarded) · total program budget KRW 3B+ · Participating Researcher"),
        ("General-Purpose AI for Cancer Pathology Diagnosis",
         "Lead: Deep Bio · National R&amp;D · program 2021–2025 · total program budget KRW 2.375B · Participating Researcher, Apr 2021 – Jan 2025"),
    ],
    "h_service": 'Community &amp; Service',
    "service": [
        ('Research member (Runner), Pseudo Lab season 12: AutoBioX, AI Agents for End-to-End Bio Research', '2026 · 16 weeks · two outputs accepted at GIW ISCB-Asia 2026, then submitted to ML4H 2026 Findings'),
        ('Reviewer, ML4H 2026 (Machine Learning for Health Symposium)', '2026'),
        ('AI Career &amp; Project Mentor, Codeit', '2025 – present · part-time · 30+ mentees 1:1, 8+ project teams across 3 cohorts'),
    ],
    "talks": [
        ('Predictability Is Not Substitutability: A cost-of-substitution framework for H&amp;E-based molecular prediction across 5 cancers', 'BIOINFO/GIW ISCB-Asia 2026 · Accepted poster · First &amp; presenting author'),
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
    "native": "Geongyu Lee · イ・ゴンギュ",
    "role": "머신러닝 리서처 · 크로스모달 학습 / 신뢰할 수 있는 예측 / Computational Pathology × 멀티오믹스",
    "contact": CONTACT + ["대한민국 서울"],
    "summary": (
        "종양학 분야에서 조직병리와 분자 데이터를 잇는 크로스모달 학습, 분포 변화에도 신뢰할 수 있는 예측을 연구하는 "
        "머신러닝 리서처입니다. 일상 진료에서 쓰는 H&amp;E 슬라이드로 유전자 발현, 수용체 상태, 유전자 검사 기반 재발 위험 "
        "같은 분자 정보를 예측하는 모델을 개발합니다. 병원·코호트·약물이 달라질 때 예측이 어디까지 유효한지도 검증합니다. "
        "산업계 R&amp;D 경력은 5년 이상입니다. 딥바이오에서는 유방암 재발 예측 연구(Scientific Reports 2025)를 제1저자로 "
        "수행했고, 식약처(MFDS)에 인허가를 신청한 의료 AI 제품의 출시 전 모델 검증에 기여했습니다. 병리 파운데이션 모델 "
        "G2L 논문(AAAI 2026 워크숍 구두 발표)에는 공저자로 참여했습니다. 현재는 사전 등록한 기관 분리 검증으로 H&amp;E 기반 "
        "분자 예측을 평가하고 있습니다. 학습에 없던 약물로 평가하는(leave-drug-out) 약물 반응 예측 모델도 개발 중입니다."),
    "h_pubs": "주요 논문",
    "scholar_note": "Google Scholar · 인용 58회 · h-index 5 · i10-index 3 · 2026년 9월 기준",
    "h_exp": "경력",
    "h_proj": "대표 프로젝트",
    "h_edu": "학력",
    "h_skills": "기술 스택",
    "h_awards": "수상 및 연구과제",
    "h_talks": "학회 발표",
    "jobs": [
        ("OMIXAI (구 래디센)", "2025.02 – 현재", "AI 리서처 · 서울", [
            "프로테오믹스·RNA와 H&amp;E 병리를 통합한 약물 반응 예측 멀티오믹스 모델 R&amp;D 주도(진행 중)",
            "프로테오믹스 기반 세포주 약물 반응(IC50) 예측 모델 개발 및 leave-drug-out 평가(학습에 없던 약물로만 테스트, Pearson ≥ 0.65), LoRA/PEFT 기반 자기지도 프로테옴 표현 학습 별도 수행",
            "반려견 종양 약물 추천 알고리즘 및 ADMET 예측 모델 개발",
            "Arc Institute Virtual Cell Challenge OMIXAI 참가팀 공동 주도(만능줄기세포 CRISPR 넉다운 반응 예측)",
            "H&amp;E 기반 유전자 발현 예측 모델 MoSPR 논문 공동 제1저자(TCGA 3개 암종에서 15개 방법 중 1위, 프리프린트·코드 공개)",
            "G2L 논문 공저자(AAAI 2026 워크숍 W3PHIAI 구두 발표), 삼중음성 유방암 재발 위험 니치를 다룬 H&amp;E 기반 공간 프로테오믹스 연구 공저자(프리프린트, 2026)",
        ]),
        ("딥바이오", "2021.03 – 2025.01", "AI 리서처 · 서울", [
            "2개 병원 유방암 재발 예측 연구 제1저자(Scientific Reports 2025), WSI 500장 이상을 처리한 파이프라인 구축",
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
        ("프로테오믹스 기반 약물 반응 예측", "OMIXAI",
         "프로테오믹스 기반 세포주 약물 반응(IC50) 예측 모델 개발 및 leave-drug-out 평가(학습에 없던 약물로만 테스트, Pearson ≥ 0.65), LoRA/PEFT 기반 자기지도 프로테옴 표현 학습 별도 수행"),
        ("수의 종양 CDSS &amp; 버추얼 셀", "OMIXAI",
         "반려견 종양 약물 추천 알고리즘 개발(반려견 종양 코호트에서 top-k ≥ 70%), Arc Institute Virtual Cell Challenge 참가팀 공동 주도(만능줄기세포 CRISPR 넉다운 반응 예측)"),
        ("Oncotype DX 재발 예측", "딥바이오",
         "H&amp;E WSI만으로 21-유전자 재발 점수 위험군 예측(신뢰도 기반 패치 선택, 다수결로 슬라이드 단위 판정) · Scientific Reports 2025 · 제1저자 · n=125, 2개 병원 · 민감도 저 / 중 / 고 0.86 / 0.75 / 0.53, 특이도 저 / 중 / 고 0.82 / 0.80 / 0.97"),
        ("CT 뇌출혈 검출", "SK / 아주대병원",
         "뇌출혈 2D·3D 분할, 슬라이스 단위 분류, class-activation map 점검을 포함한 도메인 일반화 검증"),
        ("FlyGate: 신약 탐색 → 약물감시 에이전트", "NVIDIA Agentic AI 해커톤 2026",
         "5인 팀 사이드 프로젝트로 BioNeMo NIM 기반 FlyDiscovery(OpenFold3 1.0 Å, Boltz-2 ρ 0.767)와 UI 개발"),
    ],
    "education": [
        ("데이터사이언스 석사 · 서울과학기술대학교(SeoulTech)", "2019 – 2021",
         "지도교수 황상흠 · 석사 논문: 라벨이 불확실한 의료영상에서 분할 성능을 높이는 대조 손실"),
        ("정보보안학과 학사 · 대전대학교", "2012 – 2019", ""),
    ],
    "skills": [
        ("딥러닝", "PyTorch, HuggingFace, PEFT / LoRA, Accelerate, DDP / FSDP"),
        ("병리", "OpenSlide, QuPath, CLAM / weakly-supervised MIL, UNI · CONCH · Virchow, WSI 타일링"),
        ("바이오 / 오믹스", "scanpy · AnnData, 단일세포 섭동, 프로테옴 표현 학습, ADMET"),
        ("MLOps &amp; 언어", "Python, R, SQL, Bash, Docker, Slurm, W&amp;B, MLflow, FastAPI, Git"),
    ],
    "awards": [
        ("KPIs 2024 챌린지 · 전체 슬라이드 트랙",
         "2위 · 사구체 분할 · MICCAI 2024 연계 개최 · 결과 논문 Medical Image Analysis 2026 게재"),
        ("정밀종양학을 위한 Pan-Sarcoma 프로테오지노믹스 프로파일링",
         "한·일 공동연구 · 경희대학교 의료원 · 2025–2028 · 총 연구비 4억 원 · 참여연구원"),
        ("수의 종양학을 위한 버추얼 셀 CDSS",
         "농림축산식품부 IPET · 2026–2030(선정) · 총 연구비 30억 원 이상 · 참여연구원"),
        ("암 병리 진단용 범용 AI 개발·상용화",
         "딥바이오 주관 · 국가 R&amp;D · 과제 기간 2021–2025 · 총 연구비 23.75억 원 · 참여연구원(2021.04 – 2025.01)"),
    ],
    "h_service": '학술·커뮤니티 활동',
    "service": [
        ('가짜연구소(Pseudo Lab) 12기 연구 멤버(러너), AutoBioX: AI Agents for End-to-End Bio Research', '2026 · 16주 · 연구 2편 GIW ISCB-Asia 2026 채택 후 ML4H 2026 Findings 투고'),
        ('ML4H 2026(Machine Learning for Health Symposium) 리뷰어', '2026'),
        ('코드잇 AI 커리어·프로젝트 멘토', '2025 – 현재 · 파트타임 · 멘티 30명 이상 1:1 멘토링, 3개 기수 프로젝트 팀 8개 이상'),
    ],
    "talks": [
        ('Predictability Is Not Substitutability: A cost-of-substitution framework for H&amp;E-based molecular prediction across 5 cancers', 'BIOINFO/GIW ISCB-Asia 2026 · 포스터 발표 채택 · 제1저자·발표자'),
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
    "contact": CONTACT + ["韓国・ソウル"],
    "summary": (
        "機械学習リサーチャーとして、組織病理から分子データへとつなぐクロスモーダル学習と、分布シフト下でも信頼できる予測を研究しています。"
        "応用分野は腫瘍学です。日常診療のH&amp;E染色スライドから分子状態(遺伝子発現、受容体ステータス、遺伝子検査に基づく再発リスク)を"
        "推定するモデルを開発し、施設・コホート・薬剤が変わっても予測がどこまで通用するかを検証しています。企業でのR&amp;D経験は5年以上です。"
        "Deep Bioでは乳がん再発予測研究(Scientific Reports 2025)を筆頭著者として発表し、韓国食品医薬品安全処(MFDS)に承認申請された"
        "医療AI製品の出荷前モデル検証に貢献しました。病理基盤モデルG2Lの論文(AAAI 2026 ワークショップ口頭発表)にも共著者として参加しました。"
        "現在はH&amp;Eによる分子予測の事前登録・施設分離検証と、未学習薬剤(leave-drug-out)での薬剤応答予測に取り組んでいます。"),
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
            "プロテオミクスに基づく細胞株の薬剤応答(IC50)予測モデルを開発し、テスト薬剤をすべて学習から除外したleave-drug-out方式で評価(Pearson ≥ 0.65)。別途、LoRA/PEFTによる自己教師ありプロテオーム表現学習も実施",
            "犬の腫瘍に対する薬剤推薦アルゴリズムとADMET予測モデルの開発",
            "Arc Institute Virtual Cell ChallengeでのOMIXAI参加チームの共同主導(多能性幹細胞のCRISPRノックダウン応答予測)",
            "MoSPR(H&amp;E画像からの遺伝子発現予測)の共同筆頭著者。TCGA 3がん種で15手法中1位、プレプリント・コード公開",
            "G2L論文(AAAI 2026 ワークショップ W3PHIAI 口頭発表)の共著者。H&amp;EベースのAIリスクスコアで空間プロテオミクスの解析領域を選定し、トリプルネガティブ乳がんの再発リスクニッチを解析した研究(プレプリント、2026)の共著者",
        ]),
        ("Deep Bio", "2021.03 – 2025.01", "AIリサーチャー · ソウル", [
            "2施設の乳がん再発研究(Scientific Reports 2025)の筆頭著者。WSIパイプラインを構築し、500枚以上のスライドを処理",
            "リンパ節転移検出モデルとKPIs 2024チャレンジ向け糸球体セグメンテーションモデルの開発(WSIレベル部門2位、MICCAI 2024)。チャレンジ報告論文(Medical Image Analysis、2026)の共著者",
            "前立腺がんの転移・再発リスクモデリングのプロジェクトを主導",
            "AACR(2022、2023)・USCAP(2022)で乳がん病理AI研究を筆頭著者として発表。膵臓がん・乳がんの生存予測に関するポスター発表の共著者",
            "MFDSに承認申請された医療AI製品の出荷前モデル検証および申請文書作成に貢献。社内サーバー自動化ツール(Docker)の開発",
        ]),
        ("Nuricon", "2021", "インターン · 板橋(パンギョ)", [
            "駐車場向け火災検知AIシステムの開発",
        ]),
    ],
    "projects": [
        ("プロテオミクスによる薬剤応答予測", "OMIXAI",
         "プロテオミクスに基づく細胞株の薬剤応答(IC50)予測モデルを開発し、テスト薬剤をすべて学習から除外したleave-drug-out方式で評価(Pearson ≥ 0.65)。別途、LoRA/PEFTによる自己教師ありプロテオーム表現学習も実施"),
        ("獣医腫瘍CDSS・バーチャルセル", "OMIXAI",
         "犬の腫瘍に対する薬剤推薦アルゴリズムの開発(犬の腫瘍コホートでtop-k ≥ 70%)。Arc Institute Virtual Cell Challenge参加チームの共同主導(多能性幹細胞のCRISPRノックダウン応答予測)"),
        ("Oncotype DX 再発予測", "Deep Bio",
         "H&amp;E WSIのみによる21遺伝子再発スコアのリスク群予測。信頼度に基づくパッチ選択と多数決でスライド単位に判定。Scientific Reports 2025 · 筆頭著者 · n=125、2施設 · 感度 L / I / H 0.86 / 0.75 / 0.53、特異度 L / I / H 0.82 / 0.80 / 0.97"),
        ("CT脳出血検出", "SK / 亜洲大学病院",
         "脳出血の2D・3Dセグメンテーションとスライス単位の分類。class-activation mapによる点検を含むドメイン汎化の検証"),
        ("FlyGate: 創薬探索 → 医薬品安全性監視エージェント", "NVIDIA Agentic AI ハッカソン 2026",
         "5人チームでのサイドプロジェクト。BioNeMo NIMを用いたFlyDiscovery(OpenFold3 1.0 Å、Boltz-2 ρ 0.767)とそのUIを開発"),
    ],
    "education": [
        ("修士(データサイエンス) · ソウル科学技術大学(SeoulTech)", "2019 – 2021",
         "指導教員: ファン・サンフム教授 · 修士論文: ラベルが不確実な医療画像のセグメンテーションに向けた対照損失"),
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
         "2位 · 糸球体セグメンテーション、MICCAI 2024 併催 · 結果はMedical Image Analysis 2026に掲載"),
        ("精密腫瘍学に向けたPan-Sarcomaプロテオゲノムプロファイリング",
         "日韓共同 · 慶熙大学校医療院 · 2025–2028 · 総事業費 4億ウォン · 参加研究員"),
        ("獣医腫瘍学に向けたバーチャルセルCDSS",
         "農林畜産食品部 IPET · 2026–2030(採択) · 総事業費 30億ウォン以上 · 参加研究員"),
        ("がん病理診断向け汎用AIの開発・実用化",
         "代表機関: Deep Bio · 国家R&amp;D · 事業期間 2021–2025 · 総事業費 23.75億ウォン · 参加研究員(2021.04 – 2025.01)"),
    ],
    "h_service": 'コミュニティ・学術貢献',
    "service": [
        ('Pseudo Lab シーズン12「AutoBioX, AI Agents for End-to-End Bio Research」研究メンバー(ランナー)', '2026 · 16週間 · 成果2編がGIW ISCB-Asia 2026に採択、その後ML4H 2026 Findingsへ投稿'),
        ('ML4H 2026(Machine Learning for Health Symposium)査読者', '2026'),
        ('AIキャリア・プロジェクトメンター(Codeit)', '2025 – 現在 · 非常勤 · メンティー30名以上を1対1で指導、3期で8チーム以上を担当'),
    ],
    "talks": [
        ('Predictability Is Not Substitutability: A cost-of-substitution framework for H&amp;E-based molecular prediction across 5 cancers', 'BIOINFO/GIW ISCB-Asia 2026 · ポスター発表(採択) · 筆頭著者・発表者'),
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
