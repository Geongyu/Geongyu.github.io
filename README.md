<h1 align="center">Geongyu Lee · 이건규</h1>

<p align="center">
  <b>Machine Learning Researcher</b><br>
  <sub>Cross-modal learning · Reliable prediction · Computational Pathology × Multi-Omics · Seoul, KR</sub>
</p>

<p align="center">
  <a href="https://geongyu.github.io/"><img alt="Portfolio" src="https://img.shields.io/badge/Portfolio-geongyu.github.io-7d8cff?style=flat-square&logo=githubpages&logoColor=white"></a>
  <a href="https://scholar.google.com/citations?user=43BuluYAAAAJ"><img alt="Google Scholar" src="https://img.shields.io/badge/Google%20Scholar-4285F4?style=flat-square&logo=googlescholar&logoColor=white"></a>
</p>

<p align="center">
  <a href="https://geongyu.github.io/">English</a> ·
  <a href="https://geongyu.github.io/ko/">한국어</a> ·
  <a href="https://geongyu.github.io/ja/">日本語</a>
</p>

---

## About

Machine learning researcher working on **cross-modal learning** from histology to molecular data and on **predictions that stay reliable under distribution shift**, applied to oncology.

I build models that read molecular state (gene expression, receptor status, assay-based recurrence risk) from routine H&E slides, and I test when those predictions hold up across hospitals, cohorts and compounds. 5+ years of industry R&D: contributing to pre-deployment model validation and regulatory documentation for a medical-AI product submitted to Korea's **MFDS** (Deep Bio), co-authoring the G2L pathology foundation-model paper, and now running pre-registered, site-disjoint evaluations of H&E-based molecular prediction and building leave-drug-out drug-response models. At **OMIXAI** I lead multi-omics model R&D that integrates proteomics and RNA with H&E for drug-response prediction (in progress), including a Korea–Japan Pan-Sarcoma proteogenomics collaboration.

조직병리에서 분자 데이터로 이어지는 **크로스모달 학습**과, 분포가 바뀌어도 유지되는 **신뢰할 수 있는 예측**을 연구하는 머신러닝 리서처입니다. 응용 분야는 종양학입니다. 일상적인 H&E 슬라이드에서 분자 상태(유전자 발현, 수용체 상태, 유전자 검사 기반 재발 위험)를 읽어내는 모델을 만들고, 그 예측이 병원·코호트·약물이 바뀌어도 유지되는지 검증합니다. 5년 넘게 산업계 R&D를 해 왔습니다. 딥바이오에서는 WSI 파이프라인을 구축하고 식약처(MFDS) 인허가용 의료 AI 제품의 출시 전 모델 검증 및 인허가 문서 작성에 기여했습니다. 이후 병리 파운데이션 모델(G2L) 논문에 공저자로 참여했습니다. 지금은 H&E 기반 분자 예측의 기관 분리·사전등록 평가와 미학습 약물 기준(leave-drug-out) 약물 반응 예측을 하고 있으며, OMIXAI에서는 프로테오믹스·RNA와 H&E를 통합한 약물 반응 예측 멀티오믹스 모델 R&D를 주도하고 있습니다(진행 중). 한·일 Pan-Sarcoma 프로테오지노믹스 공동연구도 그 일환입니다.

## Highlights

| | |
|---|---|
| **Co-first author** | *MoSPR* (preprint, 2026; †, 2nd of 4): H&E → gene expression via morpho-spatial macrostates and low-rank molecular programs; best of 15 methods on three TCGA cancers (gene-wise PCC, BRCA 0.413) · [code](https://github.com/Radisen-Panthera/MoSPR) |
| **First author** | *BIOINFO/GIW ISCB-Asia 2026* (accepted poster): "Predictability is not substitutability". One pre-registered protocol (site-disjoint hold-outs, label-shuffle controls) across 5 cancers; of ~15 endpoints only HNSC HPV status (AUROC 0.959) met the confirmation criterion |
| **First author** | *Scientific Reports* (2025): H&E-only prediction of 21-gene recurrence-assay risk groups in early-stage breast cancer · n=125, 2 hospitals · sensitivity L / I / H 0.86 / 0.75 / 0.53, specificity L / I / H 0.82 / 0.80 / 0.97 |
| **Co-author** | *G2L* (AAAI 2026 Workshop W3PHIAI, oral; 3rd of 6 authors): distilling giga-scale pathology foundation models into cancer-specific ones |
| **Challenge** | 2nd place, KPIs 2024 Challenge whole-slide track, glomerular segmentation (MICCAI 2024; Deep Bio team) · challenge report in *Medical Image Analysis* (2026) |
| **Regulatory** | Contributed to pre-deployment model validation and regulatory documentation for a medical-AI product submitted to Korea's MFDS (Deep Bio) |
| **Service** | Reviewer, ML4H 2026 · AI career & project mentor, Codeit (30+ mentees, 8+ project teams) |

## Research interests

Cross-modal learning: histology → gene expression, receptor status, proteomics · Representation learning & pathology foundation models · Reliability under distribution shift (sites, cohorts, unseen drugs) · Selective prediction & shortcut audits · Multimodal integration for drug response (proteomics × H&E × RNA, ongoing) · Virtual-cell & perturbation prediction

## Publications

<sub>† equal contribution (co-first) · author position shown for every paper · full list on <a href="https://scholar.google.com/citations?user=43BuluYAAAAJ">Google Scholar</a></sub>

| Year | Venue | Title | Author position |
|:--|:--|:--|:--|
| 2026 | Preprint (arXiv) | [MoSPR: Histology-to-Gene Expression Prediction with Morpho-Spatial Macrostates and Low-Rank Molecular Programs](https://arxiv.org/abs/2609.34280) · [code](https://github.com/Radisen-Panthera/MoSPR) | **Co-first** (†, 2nd of 4) |
| 2026 | **Medical Image Analysis** | [KPIs 2024 challenge: Advancing glomerular segmentation from patch- to slide-level](https://doi.org/10.1016/j.media.2026.104234) | 18th of 47 (challenge report) |
| 2026 | **AAAI 2026 Workshop** (W3PHIAI) · oral | [G2L: From Giga-Scale to Cancer-Specific Large-Scale Pathology Foundation Models via Knowledge Distillation](https://arxiv.org/abs/2510.11176) | 3rd of 6 |
| 2026 | Preprint (arXiv) | [Spatial proteomics guided by H&E-based AI reveals recurrence-risk niches in triple-negative breast cancer](https://arxiv.org/abs/2608.03145) | 7th of 30 |
| 2026 | Preprint (arXiv) | [Efficient AI-Driven Multi-Section Whole Slide Image Analysis for Biochemical Recurrence Prediction in Prostate Cancer](https://arxiv.org/abs/2603.20273) | 6th of 8 |
| 2025 | **Scientific Reports** | [Assessing the risk of recurrence in early-stage breast cancer through H&E stained whole slide images](https://www.nature.com/articles/s41598-025-16679-x) | **First** (1st of 7) |
| 2025 | **Prostate International** · review | [Artificial intelligence–driven digital pathology in urological cancers: current trends and future directions](https://doi.org/10.1016/j.prnil.2025.02.002) | **Co-first** (†, 2nd of 5) |
| 2024 | **Bioengineering** | [MurSS: A Multi-Resolution Selective Segmentation Model for Breast Cancer](https://www.mdpi.com/2306-5354/11/5/463) | 2nd of 7 |
| 2021 | **IEEE Access** | [Supervised Contrastive Embedding for Medical Image Segmentation](https://ieeexplore.ieee.org/document/9564042) | 3rd of 4 |

**Conferences** (original posters and slides: [`archive/conferences/`](archive/conferences/)):

- BIOINFO/GIW ISCB-Asia 2026 · *Predictability is not substitutability: a cost-of-substitution framework for H&E-based molecular prediction across 5 cancers* · accepted poster, first & presenting author (later submitted to ML4H 2026 Findings, under review)
- BIOINFO/GIW ISCB-Asia 2026 · *A reliability map for per-gene multiome RNA velocity parameters in single-cell kinetics* · accepted oral, co-author (3rd of 5)
- AACR 2023 · *Predicting protein receptor status from H&E-stained images in breast cancer* · poster, first author
- AACR 2022 · *Recurrence risk prediction based on automatic histologic analysis of breast cancer using whole slide images* · poster, first author
- AACR 2022 · *A deep learning based pancreatic adenocarcinoma survival prediction model applicable to adenocarcinoma of other organs* · poster, co-author
- USCAP 2022 · *Automatic histological grading of breast cancer resection tissue* · poster, first author
- USCAP 2022 · *Breast cancer survival analysis through the extracted feature from the prostate diagnosis model* · poster, co-author
- KIIE Fall Conference 2020 · *Utilizing a contrastive loss to improve segmentation model performance* · oral, first author

## Experience

| | | |
|:--|:--|:--|
| **OMIXAI** (fmr. RadiSen) | AI Researcher | Feb 2025 – present · lead multi-omics model R&D integrating proteomics and RNA with H&E for drug-response prediction (in progress) · proteomics drug-response prediction evaluated leave-drug-out, so every test compound is unseen in training (Pearson ≥ 0.65) · veterinary oncology CDSS · co-authored G2L (3rd of 6) and the TNBC spatial-proteomics preprint (7th of 30) · co-led OMIXAI's team entry in the Arc Institute Virtual Cell Challenge |
| **Deep Bio** | AI Researcher | Mar 2021 – Jan 2025 · computational pathology · built a WSI pipeline (500+ slides) · contributed to pre-deployment model validation and regulatory documentation for a medical-AI product submitted to Korea's MFDS · led prostate metastasis & recurrence-risk projects · KPIs 2024 Challenge (2nd, whole-slide track) · separately, first-author breast-cancer pathology AI presentations at AACR (2022, 2023) and USCAP (2022) |
| **Nuricon** | Intern | 2021 · parking-lot fire-detection AI |

**Side project:** [FlyGate](https://github.com/Team-FlyGate/Project-FlyGate) ([live](https://flygate.kr)), NVIDIA Korea Agentic AI Hackathon 2026 (team of 5): an evidence-first agent linking drug discovery and pharmacovigilance; built the FlyDiscovery module on BioNeMo NIM (OpenFold3 · DiffDock · Boltz-2) and its workbench UI.

**Leadership & community:** Research member (Runner), **Pseudo Lab** season 12 "AutoBioX: AI Agents for End-to-End Bio Research" (2026, 16 weeks, completed; two outputs accepted at BIOINFO/GIW ISCB-Asia 2026, subsequently submitted to ML4H 2026 Findings, under review) · Reviewer, **ML4H 2026** · AI Career & Project Mentor, **Codeit** (2025 – present, part-time): 1:1 résumé / portfolio / career programs for 30+ mentees; project scoping, methodology and troubleshooting for 8+ teams across 3 cohorts.

**Education:** M.S. Data Science · Seoul National University of Science and Technology (SeoulTech), 2019 – 2021 (advisor: Prof. Sangheum Hwang) · B.S. Information Security · Daejeon University, 2012 – 2019

## Funded research programs <sub>(participating researcher)</sub>

- **Pan-Sarcoma Proteogenomic Profiling for Precision Oncology** · Korea–Japan · Kyung Hee Univ. Medical Center · 2025 – 2028 · in progress, no public results yet
- **Virtual-Cell CDSS for Veterinary Oncology** · IPET / Ministry of Agriculture, national R&D · 2026 – 2030 (awarded)
- **General-Purpose AI for Cancer Pathology Diagnosis** · lead: Deep Bio, national R&D · program 2021 – 2025 · my participation Apr 2021 – Jan 2025

## Toolkit

![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)
![PyTorch](https://img.shields.io/badge/PyTorch-EE4C2C?style=flat-square&logo=pytorch&logoColor=white)
![HuggingFace](https://img.shields.io/badge/HuggingFace-FFD21E?style=flat-square&logo=huggingface&logoColor=black)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker&logoColor=white)
![Linux](https://img.shields.io/badge/Linux-FCC624?style=flat-square&logo=linux&logoColor=black)
![W&B](https://img.shields.io/badge/W%26B-FFBE00?style=flat-square&logo=weightsandbiases&logoColor=black)

`PEFT / LoRA` · `DDP / FSDP` · `CLAM / weakly-supervised MIL` · `UNI · CONCH · Virchow` · `OpenSlide` · `QuPath` · `scanpy / AnnData` · `Slurm` · `MLflow` · `FastAPI`

---

## This repository

Source of the portfolio site at **[geongyu.github.io](https://geongyu.github.io/)**: a single static page served by GitHub Pages, with independent language versions for search indexing.

```
index.html          English page: the single source of truth (translations live in data-ko / data-ja attributes)
archive/conferences  original posters and slides (source of truth for the Conferences section)
ko/index.html       Korean page:   generated
ja/index.html       Japanese page: generated
build_i18n.py       generates ko/ and ja/ from index.html (localised <head>, hreflang, og:locale, CV link); also stamps today's date into the footer and every sitemap <lastmod>
robots.txt
sitemap.xml         /, /ko/, /ja/ with hreflang alternates
assets/             images and favicons (CV PDFs are currently unpublished, see below)
cv/                 CV source (content.py + cv.css) rendered to PDF with WeasyPrint
```

### Editing the site

1. Edit `index.html` only. For any user-visible text, keep the Korean and Japanese versions in the element's `data-ko` / `data-ja` attributes.
2. Rebuild the language pages and commit them together with `index.html`:

   ```bash
   python3 build_i18n.py        # → ko/index.html, ja/index.html
   ```

3. `build_i18n.py` stamps today's date into the footer (EN/KO/JA) and into every `<lastmod>` in `sitemap.xml`, so run it, and commit, only when content actually changes (or revert those dates).

### CV PDFs

The CV PDFs (EN / KO / JA) are currently unpublished: they are not in the repository and the site's download button is hidden. The source stays in `cv/`, and the PDFs can be rebuilt locally:

```bash
pip install weasyprint
python3 cv/build_cv.py assets   # → assets/Geongyu_Lee_CV_{EN,KO,JA}.pdf (local only until the CV is republished)
```

### SEO checklist

- `robots.txt` and `sitemap.xml` are served from the site root.
- Every page declares `canonical`, `hreflang` (en / ko / ja / x-default), Open Graph + Twitter cards, and a `schema.org/Person` JSON-LD block.
- Submit `sitemap.xml` in Google Search Console and Bing Webmaster Tools after each structural change.

<p align="center"><sub>© Geongyu Lee · Seoul, Republic of Korea</sub></p>
