# -*- coding: utf-8 -*-
"""Geongyu Lee: CV content, three languages.
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
    "role": "AI Researcher · Computational Pathology × Multi-Omics",
    "contact": CONTACT + ["Seoul, Republic of Korea"],
    "summary": (
        "Five years building deep learning for computational pathology and drug discovery. "
        "First-author work on H&amp;E-based breast-cancer recurrence (Scientific Reports 2025), "
        "a contribution to large-scale pathology foundation models (G2L, AAAI 2026 oral), and "
        "MFDS-track model validation; now extending histopathology AI into proteomics and multi-omics."),
    "h_pubs": "Selected Publications",
    "scholar_note": "Google Scholar · 55 citations · h-index 5 · i10-index 2",
    "h_exp": "Experience",
    "h_proj": "Selected Projects",
    "h_edu": "Education",
    "h_skills": "Skills",
    "h_awards": "Awards &amp; Funding",
    "h_talks": "Conference Presentations",
    "jobs": [
        ("OMIXAI (fmr. RadiSen)", "Feb 2025 – Present", "AI Researcher · Seoul", [
            "Lead multi-omics foundation-model R&amp;D integrating proteomics with H&amp;E pathology for drug-response prediction; co-authored the G2L pathology foundation model.",
            "Co-authored spatial-proteomics work using H&amp;E-based AI risk scores to pinpoint recurrence-risk niches in triple-negative breast cancer (preprint, 2026).",
            "Built a proteomics drug-response model (Leave-Drug-Out Pearson ≥ 0.65) and a canine veterinary-oncology drug-recommendation algorithm (top-k ≥ 70%).",
            "Advanced ADMET prediction and self-supervised proteomic representation learning with LoRA / PEFT.",
            "Co-led the Virtual Cell Challenge: predicting CRISPR-knockdown response in pluripotent stem cells.",
        ]),
        ("Deep Bio", "Mar 2021 – Jan 2025", "AI Researcher · Seoul", [
            "First-authored the multi-center breast-cancer recurrence study (Scientific Reports 2025); built a scalable WSI pipeline handling 500+ slides.",
            "Developed lymph-node metastasis detection and the KPIs 2024 glomeruli segmentation model (2nd place, whole-slide track, MICCAI); challenge results published in Medical Image Analysis (2026).",
            "Led prostate metastasis &amp; recurrence-risk projects; presented at AACR (2022, 2023) and USCAP (2022).",
            "Contributed to MFDS regulatory documentation and validation, plus internal server-automation tooling (Docker).",
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
        ("M.S. Data Science · Seoul Nat'l University of Science and Technology (SeoulTech)", "2019 – 2021",
         "Advisor: Prof. Sangheum Hwang · Thesis: contrastive loss for segmentation under uncertain medical-image labels."),
    ],
    "skills": [
        ("Deep Learning", "PyTorch, HuggingFace, PEFT / LoRA, Accelerate, DDP / FSDP"),
        ("Pathology", "OpenSlide, QuPath, CLAM / weakly-supervised MIL, UNI · CONCH · Virchow, WSI tiling"),
        ("Bio / Omics", "scanpy · AnnData, single-cell perturbation, proteomic representation, ADMET"),
        ("MLOps &amp; Languages", "Python, R, SQL, Bash, Docker, Slurm, W&amp;B, MLflow, FastAPI, Git"),
    ],
    "awards": [
        ("KPIs Challenge 2024 · Whole-Slide Track",
         "2nd place · Glomeruli segmentation, held at MICCAI 2024 · results published in Medical Image Analysis 2026"),
        ("Pan-Sarcoma Proteogenomic Profiling for Precision Oncology",
         "Korea–US–Japan · Kyung Hee Univ. Medical Center · 2025–2028 · KRW 400M · Participating Researcher"),
        ("Virtual-Cell CDSS for Veterinary Oncology",
         "IPET / Ministry of Agriculture · 2026–2030 (awarded) · KRW 3B+ · Participating Researcher"),
        ("General-Purpose AI for Cancer Pathology Diagnosis",
         "Lead: Deep Bio · National R&amp;D · 2021–2025 · KRW 2.375B · Participating Researcher"),
    ],
    "h_service": 'Community &amp; Service',
    "service": [
        ('Research member (Runner), Pseudo Lab season 12: AutoBioX, AI Agents for End-to-End Bio Research', '2026 · 16 weeks · two outputs accepted at GIW ISCB-Asia 2026, then submitted to ML4H 2026 Findings'),
        ('Reviewer, ML4H 2026 (Machine Learning for Health Symposium)', '2026'),
        ('AI Career &amp; Project Mentor, Codeit', '2025 – present · part-time · 13 mentees 1:1, 8+ project teams across 2+ cohorts'),
    ],
    "talks": [
        ('Predictability is not substitutability: a cost-of-substitution framework for H&amp;E-based molecular prediction across 5 cancers', 'BIOINFO/GIW ISCB-Asia 2026 · Accepted poster · First &amp; presenting author'),
        ('A reliability map for per-gene multiome RNA velocity parameters in single-cell kinetics', 'BIOINFO/GIW ISCB-Asia 2026 · Accepted oral · Co-author'),
        ('Predicting protein receptor status from H&amp;E-stained images in breast cancer', 'AACR Annual Meeting 2023 · Poster · First author'),
        ('Recurrence risk prediction based on automatic histologic analysis of breast cancer using whole slide images', 'AACR Annual Meeting 2022 · Poster · First author'),
        ('A deep learning based pancreatic adenocarcinoma survival prediction model applicable to adenocarcinoma of other organs', 'AACR Annual Meeting 2022 · Poster · Co-author'),
        ('Automatic histological grading of breast cancer resection tissue', 'USCAP Annual Meeting 2022 · Poster · First author'),
        ('Breast cancer survival analysis through the extracted feature from the prostate diagnosis model', 'USCAP Annual Meeting 2022 · Poster · Co-author'),
        ('Utilizing a contrastive loss to improve segmentation model performance', 'KIIE Fall Conference 2020 · Oral · First author'),
    ],
}

KO = {
    "lang": "ko",
    "name": "이건규",
    "native": "Geongyu Lee · イ・ゴンギュ",
    "role": "AI 리서처 · Computational Pathology × 멀티오믹스",
    "contact": CONTACT + ["대한민국 서울"],
    "summary": (
        "5년간 Computational Pathology와 신약 개발을 위한 딥러닝을 연구해 왔습니다. H&amp;E 기반 유방암 재발 예측으로 "
        "Scientific Reports 제1저자 논문을 냈고, 대규모 병리 파운데이션 모델(G2L, AAAI 2026 구두 발표)에 기여했으며, "
        "식약처(MFDS) 인허가 모델 검증을 수행했습니다. 현재는 조직병리 AI를 프로테오믹스·멀티오믹스로 확장하고 있습니다."),
    "h_pubs": "주요 논문",
    "scholar_note": "Google Scholar · 인용 55 · h-index 5 · i10-index 2",
    "h_exp": "경력",
    "h_proj": "대표 프로젝트",
    "h_edu": "학력",
    "h_skills": "기술 스택",
    "h_awards": "수상 &amp; 연구과제",
    "h_talks": "학회 발표",
    "jobs": [
        ("OMIXAI (前 래디센)", "2025.02 – 현재", "AI 리서처 · 서울", [
            "약물 반응성 예측을 위해 프로테오믹스와 H&amp;E 병리를 통합하는 멀티오믹스 파운데이션 모델 R&amp;D 주도; G2L 병리 FM 공동저자.",
            "H&amp;E 기반 AI 위험도 점수로 공간 프로테오믹스를 안내해 삼중음성 유방암의 재발 위험 니치를 규명한 연구 공동저자(프리프린트, 2026).",
            "프로테오믹스 약물 반응성 모델(Leave-Drug-Out Pearson ≥ 0.65)과 반려견 수의 종양 약물 추천 알고리즘(top-k ≥ 70%) 개발.",
            "ADMET 예측과 LoRA/PEFT 기반 자기지도 프로테옴 표현 학습 고도화.",
            "Virtual Cell Challenge 공동 주도: 만능줄기세포의 CRISPR 넉다운 반응 예측.",
        ]),
        ("딥바이오", "2021.03 – 2025.01", "AI 리서처 / 머신러닝 엔지니어 · 서울", [
            "다기관 유방암 재발 연구 제1저자(Scientific Reports 2025); 500장 이상을 처리하는 확장형 WSI 파이프라인 구축.",
            "림프절 전이 검출 모델과 KPIs 2024 사구체 분할 모델 개발(전체 슬라이드 트랙 2위, MICCAI). 챌린지 결과는 Medical Image Analysis(2026)에 게재.",
            "전립선 전이·재발 위험 프로젝트 리드; AACR(2022, 2023)·USCAP(2022) 발표.",
            "식약처(MFDS) 인허가 문서·검증 기여, 사내 서버 자동화 도구(Docker) 개발.",
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
        ("데이터사이언스 석사 · 서울과학기술대학교", "2019 – 2021",
         "지도교수: 황상흠 · 논문: 불확실한 의료영상 라벨에서 분할 성능을 높이는 대조 손실."),
    ],
    "skills": [
        ("딥러닝", "PyTorch, HuggingFace, PEFT / LoRA, Accelerate, DDP / FSDP"),
        ("병리", "OpenSlide, QuPath, CLAM / weakly-supervised MIL, UNI · CONCH · Virchow, WSI 타일링"),
        ("바이오 / 오믹스", "scanpy · AnnData, 단일세포 섭동, 프로테옴 표현학습, ADMET"),
        ("MLOps &amp; 언어", "Python, R, SQL, Bash, Docker, Slurm, W&amp;B, MLflow, FastAPI, Git"),
    ],
    "awards": [
        ("KPIs 챌린지 2024 · 전체 슬라이드 트랙",
         "2위 · 사구체 분할, MICCAI 2024 개최 · 결과는 Medical Image Analysis 2026 게재"),
        ("정밀종양학을 위한 Pan-Sarcoma 프로테오지노믹 프로파일링",
         "한·미·일 · 경희대학교 의료원 · 2025–2028 · 4억 원 · 참여연구원"),
        ("수의 종양학을 위한 버추얼 셀 CDSS",
         "농림축산식품부 IPET · 2026–2030 (선정) · 30억 원+ · 참여연구원"),
        ("암 병리 진단용 범용 AI 개발·상용화",
         "주관: 딥바이오 · 국가 R&amp;D · 2021–2025 · 23.75억 원 · 참여연구원"),
    ],
    "h_service": '커뮤니티 &amp; 학술 서비스',
    "service": [
        ('연구 멤버(러너), 가짜연구소(Pseudo Lab) 시즌 12: AutoBioX, AI Agents for End-to-End Bio Research', '2026 · 16주 · 연구 2편 GIW ISCB-Asia 2026 채택, 이후 ML4H 2026 Findings 투고'),
        ('리뷰어, ML4H 2026 (Machine Learning for Health Symposium)', '2026'),
        ('AI 커리어 & 프로젝트 멘토, 코드잇', '2025 – 현재 · 파트타임 · 멘티 13명 1:1, 2개+ 기수 8개+ 프로젝트 팀'),
    ],
    "talks": [
        ('예측 가능성은 대체 가능성이 아니다: 5개 암종 H&amp;E 기반 분자 예측의 대체 비용 프레임워크', 'BIOINFO/GIW ISCB-Asia 2026 · 포스터 채택 · 1저자 · 발표 예정'),
        ('단일세포 멀티옴 RNA velocity 유전자별 파라미터의 신뢰성 지도', 'BIOINFO/GIW ISCB-Asia 2026 · 구두 발표 채택 · 공저자'),
        ('H&amp;E 기반 유방암 단백질 수용체 상태 예측', 'AACR 연례학술대회 2023 · 포스터 · 1저자'),
        ('WSI 자동 조직 분석 기반 유방암 재발 위험 예측', 'AACR 연례학술대회 2022 · 포스터 · 1저자'),
        ('다른 장기로 적용 가능한 췌장 선암 생존 예측 모델', 'AACR 연례학술대회 2022 · 포스터 · 공저자'),
        ('유방암 절제 조직의 자동 조직학적 등급 판정', 'USCAP 연례학술대회 2022 · 포스터 · 1저자'),
        ('전립선 진단 모델 특징을 이용한 유방암 생존 분석', 'USCAP 연례학술대회 2022 · 포스터 · 공저자'),
        ('영역분할 모델 성능 향상을 위한 대조적 손실 함수의 활용', '대한산업공학회 추계학술대회 2020 · 구두 · 1저자'),
    ],
}

JA = {
    "lang": "ja",
    "name": "イ・ゴンギュ",
    "native": "Geongyu Lee · 이건규",
    "role": "AIリサーチャー · Computational Pathology × マルチオミクス",
    "contact": CONTACT + ["韓国・ソウル"],
    "summary": (
        "5年間、Computational Pathologyと創薬のための深層学習を研究してきました。H&amp;Eによる乳がん再発予測で"
        "Scientific Reports筆頭著者論文を発表し、大規模病理基盤モデル(G2L、AAAI 2026 口頭発表)に貢献、"
        "食品医薬品安全処(MFDS)承認モデル検証を担当しました。現在は組織病理AIをプロテオミクス・マルチオミクスへ拡張しています。"),
    "h_pubs": "主要論文",
    "scholar_note": "Google Scholar · 被引用 55 · h-index 5 · i10-index 2",
    "h_exp": "職務経歴",
    "h_proj": "主なプロジェクト",
    "h_edu": "学歴",
    "h_skills": "スキル",
    "h_awards": "受賞 &amp; 研究プロジェクト",
    "h_talks": "学会発表",
    "jobs": [
        ("OMIXAI (前 RadiSen)", "2025.02 – 現在", "AIリサーチャー · ソウル", [
            "薬剤応答性予測のためプロテオミクスとH&amp;E病理を統合するマルチオミクス基盤モデルR&amp;Dを主導；G2L病理FM共同著者。",
            "H&amp;EベースのAIリスクスコアで空間プロテオミクスを誘導し、トリプルネガティブ乳がんの再発リスクニッチを解明した研究の共著(プレプリント、2026)。",
            "プロテオミクス薬剤応答モデル(Leave-Drug-Out Pearson ≥ 0.65)とイヌ獣医腫瘍の薬剤推薦アルゴリズム(top-k ≥ 70%)を開発。",
            "ADMET予測とLoRA/PEFTベースの自己教師ありプロテオーム表現学習を高度化。",
            "Virtual Cell Challenge共同主導: 多能性幹細胞のCRISPRノックダウン応答予測。",
        ]),
        ("Deep Bio", "2021.03 – 2025.01", "AIリサーチャー / 機械学習エンジニア · ソウル", [
            "多施設乳がん再発研究の筆頭著者(Scientific Reports 2025)；500枚以上を処理するスケーラブルなWSIパイプラインを構築。",
            "リンパ節転移検出モデルとKPIs 2024 糸球体セグメンテーションモデルを開発(全スライドトラック2位、MICCAI)。チャレンジ結果はMedical Image Analysis(2026)に掲載。",
            "前立腺の転移・再発リスクプロジェクトを主導；AACR(2022, 2023)・USCAP(2022)で発表。",
            "食品医薬品安全処(MFDS)承認文書・検証に貢献、社内サーバ自動化ツール(Docker)を開発。",
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
        ("データサイエンス修士 · ソウル科学技術大学", "2019 – 2021",
         "指導教員: ファン・サンフム · 修士論文: 不確実な医療画像ラベル下でのセグメンテーションを高めるコントラスティブ損失。"),
    ],
    "skills": [
        ("深層学習", "PyTorch, HuggingFace, PEFT / LoRA, Accelerate, DDP / FSDP"),
        ("病理", "OpenSlide, QuPath, CLAM / weakly-supervised MIL, UNI · CONCH · Virchow, WSIタイリング"),
        ("バイオ / オミクス", "scanpy · AnnData, 単一細胞摂動, プロテオーム表現学習, ADMET"),
        ("MLOps &amp; 言語", "Python, R, SQL, Bash, Docker, Slurm, W&amp;B, MLflow, FastAPI, Git"),
    ],
    "awards": [
        ("KPIsチャレンジ2024 · 全スライドトラック",
         "2位 · 糸球体セグメンテーション, MICCAI 2024 開催 · 結果はMedical Image Analysis 2026に掲載"),
        ("精密腫瘍学のためのPan-Sarcomaプロテオゲノムプロファイリング",
         "日米韓 · 慶熙大学校医療院 · 2025–2028 · 4億ウォン · 参加研究員"),
        ("獣医腫瘍学のためのバーチャルセルCDSS",
         "農林畜産食品部 IPET · 2026–2030 (採択) · 30億ウォン+ · 参加研究員"),
        ("がん病理診断向け汎用AIの開発・実用化",
         "主管: Deep Bio · 国家R&amp;D · 2021–2025 · 23.75億ウォン · 参加研究員"),
    ],
    "h_service": 'コミュニティ &amp; 学術サービス',
    "service": [
        ('研究メンバー(ランナー), Pseudo Lab シーズン12: AutoBioX, AI Agents for End-to-End Bio Research', '2026 · 16週 · 2編がGIW ISCB-Asia 2026に採択、その後ML4H 2026 Findingsへ投稿'),
        ('査読者, ML4H 2026 (Machine Learning for Health Symposium)', '2026'),
        ('AIキャリア & プロジェクトメンター, Codeit', '2025 – 現在 · パートタイム · メンティー13名1対1、2期以上・8チーム以上'),
    ],
    "talks": [
        ('予測可能性は代替可能性ではない: 5がん種H&amp;E分子予測の代替コストフレームワーク', 'BIOINFO/GIW ISCB-Asia 2026 · ポスター採択 · 筆頭・発表予定'),
        ('単一細胞マルチオームRNA velocity遺伝子別パラメータの信頼性マップ', 'BIOINFO/GIW ISCB-Asia 2026 · 口頭発表採択 · 共著者'),
        ('H&amp;Eによる乳がんタンパク質受容体ステータス予測', 'AACR年次総会 2023 · ポスター · 筆頭'),
        ('WSI自動組織解析による乳がん再発リスク予測', 'AACR年次総会 2022 · ポスター · 筆頭'),
        ('他臓器へ適用可能な膵臓腺がん生存予測モデル', 'AACR年次総会 2022 · ポスター · 共著'),
        ('乳がん切除組織の自動組織学的グレード判定', 'USCAP年次総会 2022 · ポスター · 筆頭'),
        ('前立腺診断モデルの特徴を用いた乳がん生存解析', 'USCAP年次総会 2022 · ポスター · 共著'),
        ('セグメンテーションモデル性能向上のための対照損失関数の活用', '韓国産業工学会 秋季学術大会 2020 · 口頭 · 筆頭'),
    ],
}

EDITIONS = {"EN": EN, "KO": KO, "JA": JA}
