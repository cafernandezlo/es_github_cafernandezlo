---
layout: page
title: RNAseq analysis
description: A Machine Learning approach
img: /assets/img/chapter.png
---

Transcriptome analysis, as a tool for the characterization and understanding of phenotypic alterations in molecular biology, plays an integral role in the understanding of complex, multi-factorial and heterogeneous diseases such as cancer. Profiling of transcriptome is used for searching the genes that show differences in their expression level associated with a particular response. RNA-seq data allows researchers to study millions of short reads derived from an RNA sample using next-generation sequencing (NGS) methods. In general terms, such amount of data is difficult to understand and there is no optimal analysis pipeline for every single analysis. Classical statistical approaches are provided in different R packages (i.e. DESeq or edgeR packages). In medicine, a Machine Learning algorithm can be used for the differential expression analysis of a particular response (i.e. sick versus healthy patients) selecting the genes that are more relevant for discriminating both health outcomes, considering biological pathway information, gene relations or using integrative approaches in order to include all the information available from different curated data-sources. The main aim of our proposal is to practically address Machine Learning based approach for gene expression analysis using RNA-seq data for cancer research within the R framework and to compare it with a classical gene expression analysis approach.

RNASeq v2 data from BRCA and LUAD cohort have been download from <a href="http://gdac.broadinstitute.org/runs/stddata__latest/" target="_blank">here</a>. TCGA2STAT package version 1.2 have been used for this issue.

This <a href="https://github.com/jlinaresb/RNAseqML/" target="_blank">repository</a> includes code based on the following <a href="https://doi.org/10.1007/978-3-030-15628-2_3" target="_blank">chapter book</a>.

<div class="img_alone">
    <img class="col three left" src="{{ site.baseurl }}/assets/img/chapter1.png" alt="" title="analysis workflow comparison"/>
</div>

<div class="col three caption">
    Comparison between differential analysis methodology using conventional statistical tech-niques and machine learning techniques. It is observed that both methodologies share the initialpart of the protocol of pre-processing of the data and they differ in the final phases.
</div>
<br/><br/>


