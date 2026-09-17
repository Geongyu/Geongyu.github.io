# Conference archive

Original posters and slides for conference presentations, kept in full here even though the website shows only a summary. These files are the only surviving copies.

| Date | Venue | Title | Role | Files |
|---|---|---|---|---|
| 2026-11 | BIOINFO/GIW ISCB-Asia 2026, Seoul (Nov 17–20) | Predictability Is Not Substitutability: A cost-of-substitution framework for H&E-based molecular prediction across 5 cancers (Submission #193) | First author, presenting, poster | `GIW2026_abstract_substitutability_submission.png` |
| 2026-11 | BIOINFO/GIW ISCB-Asia 2026, Seoul (Nov 17–20) | A reliability map for per-gene multiome RNA velocity parameters in single-cell kinetics (Abstract #241) | Co-author (3rd), oral | `GIW2026_abstract_rna_velocity_reliability.png` |
| 2023-04-02 | AACR Annual Meeting 2023 | Predicting Protein Receptor Status from H&E-stained Images in Breast Cancer (Abstract #5404) | First author, poster | `AACR2023_poster_protein_receptor_HE.png` |
| 2022-04-12 | AACR Annual Meeting 2022, New Orleans | Recurrence Risk Prediction Based on Automatic Histologic Analysis of Breast Cancer Using Whole Slide Images | First author, poster | `AACR2022_breast_recurrence_slide_01..06.png` |
| 2022-04 | AACR Annual Meeting 2022, New Orleans | A Deep Learning based Pancreatic Adenocarcinoma Survival Prediction Model Applicable to Adenocarcinoma of Other Organs | Co-author, poster | `AACR2022_pancreatic_survival_slide_01..06.png` |
| 2022-03-18 | USCAP Annual Meeting 2022 | Breast Cancer Survival Analysis through the Extracted Feature from the Prostate Diagnosis Model | Co-author, poster | `USCAP2022_poster_breast_survival_prostate_feature.png` |
| 2022-03-17 | USCAP Annual Meeting 2022 | Automatic Histological Grading of Breast Cancer Resection Tissue | First author, poster | `USCAP2022_poster_histologic_grading.png` |
| 2020-11 | KIIE Fall Conference 2020 (2020년 대한산업공학회 추계학술대회) | 영역분할 모델 성능 향상을 위한 대조적 손실 함수의 활용 (Utilizing a contrastive loss to improve segmentation model performance) | First author, oral | `KIIE2020_contrastive_loss_segmentation_slides.pdf`, `KIIE2020_contrastive_loss_segmentation_arch.png` |

## GIW ISCB-Asia 2026 · Predictability Is Not Substitutability: A cost-of-substitution framework for H&E-based molecular prediction across 5 cancers

BIOINFO/GIW ISCB-Asia 2026, Seoul, November 17–20, 2026. Call for Abstracts, Submission ID 193. Poster, presenting author.
Authors: Geongyu Lee (Pseudo Lab; OmixAI Co. Ltd.), Ka-Kyung Kim (Pseudo Lab), Sejin Park (Pseudo Lab; Seegene Inc.), Jaemyun Lyu (Pseudo Lab; R&D Center, Genolution Inc.), Jeong-Han Seo (Pseudo Lab; ROKIT Genomics; Department of Medical Science, University of Ulsan College of Medicine, Asan Medical Center), Yong Gi Ji (Pseudo Lab; Qaumtum C&S)

Abstract: Deep learning predicts molecular subtypes from H&E histology accurately, but accuracy alone does not indicate what treatment a patient receives when a prediction is wrong. Predictability and substitutability are distinct claims, and replacing a molecular test requires evidence for the latter. We define substitution cost by weighting confusion-matrix errors by treatment distance, translating each error into a deviation from a prespecified treatment routing, with a distance-independent misassignment rate as the primary measure. A single pre-registered protocol was applied across five cancer types (breast, lung, colorectal, gastric, head and neck) using UNI embeddings and CLAM-SB attention-based multiple-instance learning. Evaluation used site-disjoint hold-outs with five-seed label-shuffle controls. Of approximately 15 endpoints, only one non-control endpoint met the pre-registered confirmation criterion: HPV status in head and neck cancer (AUROC 0.959; 26 hold-out positives). The highest-performing result, lung histological subtype (AUROC 0.939), was excluded after the site-confounding audit yielded V(site, label) = 1.000. In the breast anchor, anti-HER2 routing from H&E-predicted subtype misassigned every treatment-eligible patient. Most clinically actionable endpoints were undecided rather than negative, falling below the pre-registered power criterion. Reporting them as undecided is central to this framework. The framework applies to any proposed H&E-based surrogate beyond predictive performance alone.

## GIW ISCB-Asia 2026 · A reliability map for per-gene multiome RNA velocity parameters in single-cell kinetics

BIOINFO/GIW ISCB-Asia 2026, Seoul, November 17–20, 2026. Abstract #241. Oral presentation.
Authors: Ka-Kyung Kim¹, Jaemyun Lyu², Geongyu Lee³˒⁴, Sejin Park⁵, Yong Gi Ji⁶ (¹ Independent Researcher, Seoul · ² R&D Center, Genolution Inc. · ³ Omixai Co., Ltd. · ⁴ Pseudo Lab · ⁵ Seegene Inc. · ⁶ Qaumtum C&S)

Abstract: Multiome RNA-velocity methods emit several per-gene quantities, a transcription rate α, a degradation rate γ, and a chromatin-to-transcription lag, each proposed as a biological readout. A derived quantity is usable only if it is reliable: reproducible across algorithms and consistent with independent measurement. Across up to five velocity arms (an RNA-only scVelo floor plus MultiVelo, MultiVeloVAE, MoFlow and CRAK-Velo) on human hematopoietic stem and progenitor cells (10x Multiome), we tested each output on four axes: cross-method reproducibility, a causal within-lineage ATAC-shuffle control, replication in five external multiomes, and anchoring to measured synthesis and degradation rates. Only α reproduced across methods (Spearman ρ=0.88); the lag reproduced weakly in magnitude (strongest pair +0.163), only at chance in sign (54.6%), and was unchanged by ATAC shuffling, marking it model-structural. γ was fragile (ρ≈−0.1) and ran reversed against measured half-life (−0.224). Fitted α tracked measured synthesis (+0.24 to +0.29), but transcript abundance tracked it at least as strongly (+0.410 versus +0.262), consistency evidence, not α-specific accuracy. The α-over-lag ordering held in all six systems; the sixth was preregistered and passed six-of-six, sealed before fitting. Trust α against an abundance baseline; treat lag, sign, timing and γ as requiring orthogonal validation.

## AACR 2023 · Predicting Protein Receptor Status from H&E-stained Images in Breast Cancer

Abstract #5404, presented April 2, 2023.
Authors: Geongyu Lee¹, Chungyeul Kim²˒³, Tae-Yeong Kwak¹, Sun Woo Kim¹, Hyeyoon Chang¹ (¹ Deep Bio Inc. · ² Korea University Guro Hospital · ³ Korea University)

- Goal: predict ER / PR / HER2 status from H&E whole-slide images alone, without IHC staining.
- Data: TCGA-BRCA, 728 of 1,097 cases with definitive IHC status; WSI split 3:1:1 (train / tune / test), tiled into 1024×1024 patches.
- Method: multi-task model with a shared morphology feature extractor and three prediction heads (ER, PR, HER2), each with a confidence output. Patches with confidence below 70% are excluded at the WSI level. Strong augmentation (grayscale, gaussian blur, color jitter, posterization) so predictions are not driven by color alone.
- Results (test set sampled with class balance):

| Receptor | Patch acc. | Patch F1 | Slide acc. | Slide F1 |
|---|---|---|---|---|
| ER | 73.34 | 69.24 | 74.6 | 68.75 |
| PR | 64.93 | 60.45 | 66.0 | 64.25 |
| HER2 | 80.40 | 78.64 | 76.6 | 73.41 |

- Conclusion: ER and HER2 are predicted reasonably well, PR less so, indicating a correlation between H&E morphology and molecular subtype. Grad-CAM maps highlight the regions the model relies on.

## AACR 2022 · Recurrence Risk Prediction Based on Automatic Histologic Analysis of Breast Cancer Using Whole Slide Images

Presented April 12, 2022 (New Orleans, April 8–13).
Authors: Geongyu Lee¹, Chungyeul Kim²˒³, Tae-Yeong Kwak¹, Sun Woo Kim¹, Hyeyoon Chang¹ (¹ Deep Bio Inc. · ² Korea University · ³ Korea University Medicine)

- Goal: test whether automated analysis of H&E WSIs can approximate the 21-gene recurrence score (RS) for hormone-positive, node-negative, HER2-negative early-stage breast cancer.
- Data: 125 cases with RS ground truth: low risk (RS < 18) 49, intermediate (18 ≤ RS < 31) 59, high (RS > 31) 17. Invasive tumor regions annotated by an expert pathologist. WSIs tiled into 512×512 patches.
- Method: CNN classifies patches as benign / low / intermediate / high risk; majority vote assigns the WSI class. Nested cross-validation.
- Results (confusion matrix, rows = prediction, columns = 21-gene ground truth):

| | Low | Intermediate | High |
|---|---|---|---|
| Low | 42 | 14 | 0 |
| Intermediate | 5 | 44 | 8 |
| High | 2 | 1 | 9 |

| | Low | Intermediate | High |
|---|---|---|---|
| Accuracy | 0.832 | 0.776 | 0.912 |
| Sensitivity | 0.857 | 0.746 | 0.529 |
| Specificity | 0.791 | 0.797 | 0.966 |
| PPV | 0.75 | 0.772 | 0.75 |

- No low-risk case was misclassified as high-risk. Grad-CAM shows which regions drove each class.
- Conclusion: limited but promising; expected to improve with more data and additional clinical / pathological inputs. This line of work became the Scientific Reports (2025) paper.

## AACR 2022 · A Deep Learning based Pancreatic Adenocarcinoma Survival Prediction Model Applicable to Adenocarcinoma of Other Organs

New Orleans, April 8–13, 2022.
Authors: Joonho Lee¹˒², Geongyu Lee¹, Tae-Yeong Kwak¹, Sun Woo Kim¹, Hyeyoon Chang¹ (¹ Deep Bio Inc. · ² University of Waterloo)

- Goal: relate histomorphological features of adenocarcinoma to patient survival, and test whether a model trained on pancreatic adenocarcinoma transfers to other organs.
- Data (TCGA): 179 pancreatic adenocarcinoma cases for the survival model (66 uncensored; 144 train / 35 test, 256×256 patches, 5-fold CV). General adenocarcinoma feature extractor (GAFE) trained on 92 lung, 100 colon, 97 prostate and 39 stomach adenocarcinoma cases. Transfer tested on 122 rectum (TCGA-READ) and 999 breast (TCGA-BRCA) cases.
- Results: 5-fold test C-index 0.7216 / 0.7784 / 0.6959 / 0.6598 / 0.7732, mean 0.7258; log-rank p-values 0.0199 / 0.0016 / 0.0089 / 0.1081 / 0.0055 for the 50% high- vs low-risk split. Transfer: C-index 0.6941 on TCGA-READ and 0.5711 on TCGA-BRCA.
- Conclusion: adenocarcinoma histomorphology carries survival signal for pancreatic cancer, with some transferability to rectum and, to a lesser degree, breast.

## USCAP 2022 · Breast Cancer Survival Analysis through the Extracted Feature from the Prostate Diagnosis Model

Presented March 18, 2022.
Authors: Joonho Lee¹˒², Geongyu Lee¹, Tae-Yeong Kwak¹, Sun Woo Kim¹, Hyeyoon Chang¹ (¹ Deep Bio Inc. · ² University of Waterloo)

- Goal: predict breast-cancer death risk from H&E WSIs using features from a pre-trained prostate diagnosis model rather than a general-image backbone.
- Data: TCGA-BRCA, 980 H&E WSIs (×100) with survival events and periods (881 censored, 99 uncensored), 512×512 patches, 5-fold CV.
- Method: attention-guided deep multiple-instance learning (Siamese MI-FCN, Yao et al. 2020) over prostate-model features.
- Results: 5-fold C-index 0.6885 / 0.5915 / 0.5968 / 0.6359 / 0.7627, mean 0.6551. Kaplan-Meier curves for top-40% vs bottom-60% risk groups separate with log-rank p = 0.0011.
- Conclusion: morphology learned from prostate grading carries some signal for breast survival, suggesting transferability of histomorphological knowledge across organs.

## USCAP 2022 · Automatic Histological Grading of Breast Cancer Resection Tissue

Presented March 17, 2022.
Authors: Geongyu Lee¹, Chung-Yeul Kim²˒³, Tae-Yeong Kwak¹, Sun Woo Kim¹, Hyeyoon Chang¹ (¹ Deep Bio Inc. · ² Korea University · ³ Korea University Medicine)

- Goal: reduce inter-observer variability in breast histology grading (tubule formation, nuclear grade, mitotic activity) with a model learned from a specialist's grading, for hormone-positive, HER2-negative, node-negative patients.
- Data: 125 H&E WSIs with pathologist grading and region-level annotations of invasive tumor; 512×512 patches, 8:2 split (293,637 train / 69,634 test patches).
- Method: patch-level benign-vs-tumor classifier, then a ConvNet grades tumor patches (grade 1 / 2 / 3).
- Results (patch level, columns = ground-truth grade):

| | Benign | Grade 1 | Grade 2 | Grade 3 |
|---|---|---|---|---|
| Accuracy | 0.966 | 0.958 | 0.922 | 0.956 |
| Sensitivity | 0.976 | 0.722 | 0.672 | 0.696 |
| Specificity | 0.941 | 0.976 | 0.957 | 0.975 |
| PPV | 0.979 | 0.698 | 0.688 | 0.666 |

- CAM heatmaps show the regions the model attends to per grade.
- Conclusion: a consistent automatic grading system; larger data and stronger reference standards are needed for full evaluation.

## KIIE Fall Conference 2020 · 영역분할 모델 성능 향상을 위한 대조적 손실 함수의 활용

2020년 대한산업공학회 추계학술대회 (KIIE Fall Conference 2020), 논문집 수록. Oral presentation, first author.
Authors: 이건규 (Geongyu Lee), 황상흠 (Sangheum Hwang), Department of Data Science, Seoul National University of Science and Technology. Supported by NRF Basic Science Research Program (NRF2018R1D1A1A02086017).

- Motivation: encoder-decoder segmentation models give no guarantee that encoder embeddings of the same class lie close together and those of different classes lie apart. Prior medical-segmentation work improved performance by adding architectural complexity (residual / DAC blocks, cascaded U-Nets, UNet++ / UNet3+) rather than addressing embedding structure.
- Method: a feature-wise contrastive loss on the encoder's bottleneck feature vectors. The ground-truth mask is resized to the feature-map resolution, positive (target-region) feature vectors are pulled together and pushed away from negative-region vectors (cosine similarity, temperature τ), and the loss is added to the segmentation loss (CE / Dice) with weight α. m random positive samples per batch keep the cost bounded. α = 0.1 chosen on validation.
- Data: lung segmentation in CT (Kaggle "Finding and Measuring Lungs in CT", 263 images, 512×512, HU [−1000, 400]); liver segmentation in CT (LiTS2017, 19,263 liver-containing slices from 131 patients, 7:3 patient split, 330×330, HU [−200, 200]).
- Setup: U-Net and UNet++, SGD (momentum 0.9, LR 0.01, decay at [75, 100] ×0.1, weight decay 1e-4), batch 20, 120 epochs. Metrics: JSC, DSC, ACD, ASD, precision, sensitivity, specificity.
- Results (Base → Ours):

| Task | Model | JSC | DSC | ACD ↓ | ASD ↓ |
|---|---|---|---|---|---|
| Lung (Kaggle) | U-Net | 0.970 → 0.980 | 0.980 → 0.990 | 0.463 → 0.440 | 0.311 → 0.298 |
| Lung (Kaggle) | UNet++ | 0.980 → 0.982 | 0.989 → 0.991 | 0.455 → 0.391 | 0.314 → 0.273 |
| Liver (LiTS2017) | U-Net | 0.850 → 0.867 | 0.912 → 0.923 | 0.697 → 0.499 | 0.533 → 0.365 |
| Liver (LiTS2017) | UNet++ | 0.860 → 0.877 | 0.919 → 0.924 | 0.647 → 0.460 | 0.541 → 0.321 |

- Conclusion: consistent gains, largest on distance-based boundary metrics, showing that well-structured embeddings help segmentation. Limitation: the contrastive term may not apply correctly when the target region is very small. Future work: handling small targets and testing whether the learned encoder is robust to domain shift. This work led to the M.S. thesis and the IEEE Access (2021) paper.
