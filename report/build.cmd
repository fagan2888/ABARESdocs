SET filename="Report"
setlocal enabledelayedexpansion enableextensions
SET source=
for %%x in (*.md) do set source=!source! %%x
SET source=%source:~1%
pandoc --filter pandoc-crossref --filter pandoc-citeproc -s %source% --template abares_fancy.latex -o output/%filename%.pdf --default-image-extension pdf --latex-engine=xelatex
pandoc --filter pandoc-crossref --filter pandoc-citeproc -s %source%  --template abares_basic.latex -o output/%filename%_basic.pdf --default-image-extension pdf --latex-engine=xelatex
pandoc --filter pandoc-crossref --filter pandoc-citeproc -s %source%  -c github-pandoc.css -o %filename%.html --default-image-extension png --template abares.html --toc 
pandoc --filter pandoc-crossref --filter pandoc-citeproc -s %source%  -o output/%filename%.docx --reference-docx="ABARES report template.docx" --default-image-extension png --toc
pandoc --filter pandoc-crossref --filter pandoc-citeproc -s %source% -o output/%filename%.icml  --default-image-extension png --toc
PAUSE
