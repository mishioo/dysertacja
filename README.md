# Reductive activation of amides as a method of obtaining functionalized amies: computer-aided synthetic investigations
This is a doctoral dissertation in the field of Chemical Sciences written by Michał M. Więcław
(ORCID: [0000-0001-7884-8982](https://orcid.org/0000-0001-7884-8982)) and supervised by
prof. Bartłomiej Furman (ORCID: [0000-0001-5459-8026](https://orcid.org/0000-0001-5459-8026)).
Investigations here described were conducted in Furman Research Group,
Institute of Organic Chemistry, Polish Academy of Sciences
([link to the group's website](http://ichopan2.pl/)).

## Contents
Title of the first section section is a direct translation of the original title of the
dissertation, which reads: "Reduktywna aktywacja amidów jako metoda otrzymywania
sfunkcjonalizowanych amin: badania syntetyczne wspomagane metodami komputerowymi".
The document is written in polish, so it is
rather not accessible for non-polish speakers. However, most of its contents was published
in peer-reviewed international journals. Appropriate articles are cited below:

- M. M. Więcław, S. Stecko, , _Hydrozirconation of C=X Functionalities with Schwartz's Reagent_,
European Journal of Organic Chemistry, **2018**, 6601-6623,
DOI: [10.1002/ejoc.201701537](https://doi.org/10.1002/ejoc.201701537);
- M. M. Więcław, B. Furman, _Direct synthesis of anomeric tetrazolyl iminosugars from sugar-derived lactams_,
Beilstein Journal of Organic Chemistry, **2021**, 17, 115-123,
DOI: [10.3762/bjoc.17.12](https://doi.org/10.3762/bjoc.17.12).
- M. M. Więcław, _tesliper: a theoretical spectroscopist's little helper_,
Journal of Open Source Software, **2022**, 7(72), 4164, DOI:
[10.21105/joss.04164](https://doi.org/10.21105/joss.04164)

## Source code compilation
This document is prepared using LaTeX. It's source code can be compiled to the .pdf file
with use of the following commands:

    pdflatex --shell-escape main
    biber main
    makeglossaries main
    pdflatex main
    pdflatex main

## Requirements
This document uses a number of CTAN packages and requires a TeX Live version at least 2020.
The easiest way to get all needed packages is to get a latest full installation of TeX Live
form [TeX Users Group](http://www.tug.org/texlive/).
Document also requires Inkscape to be installed and available in `PATH`.

    TeX Live 2020 or later (full installation)
    Inkscape