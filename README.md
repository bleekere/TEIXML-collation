# Automated collation of TEI-compliant XML documents

This repository contains early work on a collation tool that deals with TEI-compliant XML transcriptions of literary drafts. 
## Rationale

Literary works are dynamic entities: they go through different stages of development before publication, and often continue to change even after their first publication. The early versions of a work, such as notes, draft manuscripts and typescripts, still show the traces of this dynamic development in the form of deletions, additions or substitutions. Today, these documents are carefully transcribed, annotated and encoded in a machine-readable language. Using text comparison tools, scholars can automatically compare the encoded text versions and examine the different stages in the work’s development. So far, however, it is not possible to include the annotations in the comparison process. This means that relevant scholarly information is lost.  

## Outputs 

### Software
The collation software *HyperCollate* is designed to interpret the TEI markup elements indicating internal variation, such as `subst`, `del`, and `add`. The HyperCollate software is open source; see the [website](https://huygensing.github.io/hyper-collate/) for more information and tutorials.

### Articles
- Bleeker, Elli, Bram Buitendijk and Ronald Haentjens Dekker. 2020. “Marking up microrevisions with major implications: Non-linear text in TAG.” Presented at Balisage: The Markup Conference 2020, Washington, DC, July 27 - 31, 2020. In *Proceedings of Balisage: The Markup Conference 2020. Balisage Series on Markup Technologies*, vol. 25. [DOI](https://doi.org/10.4242/BalisageVol25.Bleeker01). 
- Bleeker, Elli, Bram Buitendijk, Ronald Haentjens Dekker, Vincent Neyt, and Dirk Van Hulle. 2022. “Layers of Variation: a Computational Approach to Collating Texts with Revisions.” In *Digital Humanities Quarterly*, vol. 16, no. 1.

### Conference papers
- Bleeker, Elli, Bram Buitendijk, Ronald Haentjens Dekker, and Astrid Kulsdom. 2018. “Including XML markup in the automated collation of literary text.” Presented at the XML Prague conference, Prague, February 8-10, 2018. In *Conference Proceedings*, pp. 77-96, available [here](https://archive.xmlprague.cz/2018/files/xmlprague-2018-proceedings.pdf).  


### PhD thesis
- Bleeker, Elli. 2017. *Mapping invention in writing: Digital infrastructure and the role of the genetic editor.* Ph.D. dissertation, University of Antwerp. Available [here](https://repository.uantwerpen.be/docman/irua/e959d6/155676.pdf).


## Ongoing developments  

April 2022 saw the start of the project “COLLaiTE”, a collaboration between researchers at the Huygens Institute of the History of the Netherlands and the Dutch eScience Center.  COLLaiTE proposes to employ machine learning technologies to develop a comparison tool that can take into account text as well as annotations. As a result, it will allow scholars to analyze the textual development at unprecedented levels of detail. See the GitHub repository of the project [here](https://github.com/collaite).