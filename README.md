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

I develop machine learning models that predict molecular measurements from pathology slides and, in my current industry work, drug response from proteomics. I focus on whether these predictions remain valid at new hospitals and for drugs not seen in training.

I have 5+ years of industry R&D experience. At **OMIXAI** I lead R&D on a multi-omics model that combines proteomics, RNA and H&E to predict drug response (in progress). At **Deep Bio** I built the WSI pipeline and contributed to pre-deployment model validation and regulatory documentation for a medical-AI product submitted to Korea's **MFDS**.

병리 슬라이드로 분자 정보를 예측하는 머신러닝 모델을 연구하며, 현 직장에서는 프로테오믹스로 약물 반응을 예측하는 모델도 개발합니다. 새로운 병원의 데이터나 학습에 없던 약물에서도 예측이 유효한지 검증하는 데 집중합니다. 산업계 R&D 경력은 5년 이상입니다. **OMIXAI**에서는 프로테오믹스·RNA·H&E를 통합해 약물 반응을 예측하는 멀티오믹스 모델 R&D를 주도하고 있습니다(진행 중). **딥바이오**에서는 WSI 파이프라인을 구축했고, 식약처(MFDS)에 인허가를 신청한 의료 AI 제품의 출시 전 모델 검증과 인허가 문서 작성에 기여했습니다.

## Highlights

| | |
|---|---|
| **Co-first author** † | *MoSPR* (preprint, 2026). Predicts gene expression from H&E using morpho-spatial macrostates and low-rank molecular programs. Ranked 1st of 15 methods in the paper's benchmark on three TCGA cancers (gene-wise PCC, BRCA 0.413) · [code](https://github.com/Radisen-Panthera/MoSPR) |
| **First author** | *BIOINFO/GIW ISCB-Asia 2026* (accepted poster). "Predictability is not substitutability" applied one pre-registered protocol with site-disjoint hold-outs and label-shuffle controls to 5 cancers. Of ~15 endpoints, only HNSC HPV status (AUROC 0.959) met the pre-registered confirmation criterion. Most of the others were reported as inconclusive. |
| **First author** | *Scientific Reports* (2025). Prediction of 21-gene recurrence-assay risk groups in early-stage breast cancer from H&E alone · n=125, 2 hospitals · sensitivity L / I / H 0.86 / 0.75 / 0.53, specificity L / I / H 0.82 / 0.80 / 0.97 |
| **Co-author** | *G2L* (AAAI 2026 Workshop W3PHIAI, oral). Distillation of giga-scale pathology foundation models into cancer-specific models. |
| **Challenge** | 2nd place in the KPIs 2024 Challenge whole-slide track, glomerular segmentation (MICCAI 2024, Deep Bio team) · co-author of the challenge report in *Medical Image Analysis* (2026) |
| **Regulatory** | Contributed to pre-deployment model validation and regulatory documentation for a medical-AI product submitted to Korea's MFDS (Deep Bio) |
| **Service** | Reviewer, ML4H 2026 · AI career & project mentor, Codeit (30+ mentees, 8+ project teams) |

## Research interests

Cross-modal learning from histology to gene expression, receptor status and proteomics · Representation learning & pathology foundation models · Reliability across sites, cohorts and unseen drugs · Selective prediction & shortcut audits · Multimodal drug-response prediction from proteomics, H&E and RNA (ongoing) · Virtual-cell & perturbation prediction

## Publications

<sub>† equal contribution (co-first) · full list on <a href="https://scholar.google.com/citations?user=43BuluYAAAAJ">Google Scholar</a></sub>

| Year | Venue | Title | Authorship |
|:--|:--|:--|:--|
| 2026 | Preprint (arXiv) | [MoSPR: Histology-to-Gene Expression Prediction with Morpho-Spatial Macrostates and Low-Rank Molecular Programs](https://arxiv.org/abs/2609.34280) · [code](https://github.com/Radisen-Panthera/MoSPR) | **Co-first** † |
| 2026 | **Medical Image Analysis** | [KPIs 2024 challenge: Advancing glomerular segmentation from patch- to slide-level](https://doi.org/10.1016/j.media.2026.104234) | Co-author (challenge report) |
| 2026 | **AAAI 2026 Workshop** (W3PHIAI) · oral | [G2L: From Giga-Scale to Cancer-Specific Large-Scale Pathology Foundation Models via Knowledge Distillation](https://arxiv.org/abs/2510.11176) | Co-author |
| 2026 | Preprint (arXiv) | [Spatial proteomics guided by H&E-based AI reveals recurrence-risk niches in triple-negative breast cancer](https://arxiv.org/abs/2608.03145) | Co-author |
| 2026 | Preprint (arXiv) | [Efficient AI-Driven Multi-Section Whole Slide Image Analysis for Biochemical Recurrence Prediction in Prostate Cancer](https://arxiv.org/abs/2603.20273) | Co-author |
| 2025 | **Scientific Reports** | [Assessing the risk of recurrence in early-stage breast cancer through H&E stained whole slide images](https://www.nature.com/articles/s41598-025-16679-x) | **First** |
| 2025 | **Prostate International** · review | [Artificial intelligence–driven digital pathology in urological cancers: current trends and future directions](https://doi.org/10.1016/j.prnil.2025.02.002) | **Co-first** † |
| 2024 | **Bioengineering** | [MurSS: A Multi-Resolution Selective Segmentation Model for Breast Cancer](https://www.mdpi.com/2306-5354/11/5/463) | Co-author |
| 2021 | **IEEE Access** | [Supervised Contrastive Embedding for Medical Image Segmentation](https://ieeexplore.ieee.org/document/9564042) | Co-author |

**Conferences.** Original posters and slides are in [`archive/conferences/`](archive/conferences/).

- BIOINFO/GIW ISCB-Asia 2026 · *Predictability is not substitutability: a cost-of-substitution framework for H&E-based molecular prediction across 5 cancers* · accepted poster, first & presenting author (later submitted to ML4H 2026 Findings, under review)
- BIOINFO/GIW ISCB-Asia 2026 · *A reliability map for per-gene multiome RNA velocity parameters in single-cell kinetics* · accepted oral, co-author
- AACR 2023 · *Predicting protein receptor status from H&E-stained images in breast cancer* · poster, first author
- AACR 2022 · *Recurrence risk prediction based on automatic histologic analysis of breast cancer using whole slide images* · poster, first author
- AACR 2022 · *A deep learning based pancreatic adenocarcinoma survival prediction model applicable to adenocarcinoma of other organs* · poster, co-author
- USCAP 2022 · *Automatic histological grading of breast cancer resection tissue* · poster, first author
- USCAP 2022 · *Breast cancer survival analysis through the extracted feature from the prostate diagnosis model* · poster, co-author
- KIIE Fall Conference 2020 · *Utilizing a contrastive loss to improve segmentation model performance* · oral, first author

## Experience

| | | |
|:--|:--|:--|
| **OMIXAI** (fmr. RadiSen) | AI Researcher | Feb 2025 – present · lead multi-omics model R&D that combines proteomics and RNA with H&E for drug-response prediction (in progress) · proteomics drug-response model evaluated leave-drug-out, so no test compound is seen in training (Pearson ≥ 0.65; internal R&D, unpublished) · veterinary oncology CDSS · co-authored G2L and the TNBC spatial-proteomics preprint · co-led OMIXAI's team entry in the Arc Institute Virtual Cell Challenge |
| **Deep Bio** | AI Researcher | Mar 2021 – Jan 2025 · computational pathology · built a WSI pipeline (500+ slides) · contributed to pre-deployment model validation and regulatory documentation for a medical-AI product submitted to Korea's MFDS · led prostate metastasis & recurrence-risk projects · KPIs 2024 Challenge (2nd, whole-slide track) · first-author presentations on breast-cancer pathology AI at AACR (2022, 2023) and USCAP (2022) |
| **Nuricon** | Intern | 2021 · parking-lot fire-detection AI |

**Side project:** [FlyGate](https://github.com/Team-FlyGate/Project-FlyGate) ([live](https://flygate.kr)) is an evidence-based agent for drug discovery and pharmacovigilance, made by a team of 5 at the NVIDIA Korea Agentic AI Hackathon 2026. I built the FlyDiscovery module on BioNeMo NIM (OpenFold3, DiffDock, Boltz-2) and its workbench UI.

**Leadership & community:** Research member (Runner), **Pseudo Lab** season 12 "AutoBioX: AI Agents for End-to-End Bio Research" (2026, completed). Two studies were accepted at BIOINFO/GIW ISCB-Asia 2026 and later submitted to ML4H 2026 Findings (under review) · Reviewer, **ML4H 2026** · AI Career & Project Mentor, **Codeit** (2025 – present, part-time), with 1:1 résumé, portfolio and career mentoring for 30+ mentees and help with project scoping, methods and troubleshooting for 8+ teams across 3 cohorts.

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
assets/             images, favicons and CV PDFs (EN / KO / JA)
cv/                 CV source (content.py + cv.css) rendered to PDF with WeasyPrint
```

### Editing the site

The homepage uses short descriptive labels for three selected studies. Keep the
official paper titles, authorship, publication status, figures and evaluation
conditions in Publications and Conferences. Paper figures stay visible beside
their titles; longer study summaries use native `<details>` elements. Projects
use rows that size to their content, with one visible description and optional
figures. Avoid equal-height cards and repeated per-project disclosure controls.
Group each metric label with its value in `.meta-unit`. Keep short compound
terms together with `.term`, while allowing whole titles and paragraphs to wrap
at the available width; avoid fixed line breaks in running text.
The light theme uses Noto Sans, readable body text and restrained link colors; avoid adding
duplicate headline metrics or hiding page content behind entrance animations.

1. Edit `index.html` only. For any user-visible text, keep the Korean and Japanese versions in the element's `data-ko` / `data-ja` attributes.
2. Rebuild the language pages and commit them together with `index.html`:

   ```bash
   python3 build_i18n.py        # → ko/index.html, ja/index.html
   ```

3. `build_i18n.py` stamps today's date into the footer (EN/KO/JA) and into every `<lastmod>` in `sitemap.xml`, so run it, and commit, only when content actually changes (or revert those dates).

### CV PDFs

The CV source lives in `cv/` (`content.py` for text, `cv.css` for layout). `build_cv.py` uses WeasyPrint when it is installed and otherwise prints with headless Chrome or Edge (set `CHROME` to point at a specific browser). Fonts load from the web, so build with internet access. The CV lists GitHub, Google Scholar and the portfolio; email is intentionally left out.

```bash
python3 cv/build_cv.py assets   # → assets/Geongyu_Lee_CV_{EN,KO,JA}.pdf
```

### SEO checklist

- `robots.txt` and `sitemap.xml` are served from the site root.
- Every page declares `canonical`, `hreflang` (en / ko / ja / x-default), Open Graph + Twitter cards, and a `schema.org/Person` JSON-LD block.
- Submit `sitemap.xml` in Google Search Console and Bing Webmaster Tools after each structural change.

<p align="center"><sub>© Geongyu Lee · Seoul, Republic of Korea</sub></p>
