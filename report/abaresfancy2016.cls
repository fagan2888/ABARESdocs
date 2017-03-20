%% Neal Hughes - Hack of CSRIO latex template to match ABARES style
%%
\NeedsTeXFormat{LaTeX2e}[1994/12/01] \ProvidesClass{abaresfancy2016}
              [2003/07/21, v1.3]

\newif\if@times
\newif\if@mtpro
\newif\if@colortbl
\newif\if@fleqn

\newif\if@review
\newif\if@final

\newif\if@formal
\newif\if@standard

\@formalfalse \DeclareOption{formal}{\@formaltrue}
\@standardfalse \DeclareOption{standard}{\@standardtrue}

\@reviewfalse \DeclareOption{review}{\@reviewtrue}

\@finalfalse \DeclareOption{final}{\@finaltrue}

\@timesfalse \DeclareOption{times}{\@timestrue}

\@mtprofalse \DeclareOption{mtpro}{\@mtprotrue}

\@colortblfalse \DeclareOption{colortbl}{\@colortbltrue}

\@fleqnfalse \DeclareOption{fleqn}{\@fleqntrue}

\DeclareOption*{\PassOptionsToClass{\CurrentOption}{article}} \ProcessOptions
\LoadClass{article}

\if@times \RequirePackage[scaled=0.90]{helvet} \RequirePackage{times} \fi

\if@fleqn
  \RequirePackage{fleqn}
  \setlength{\mathindent}{4em}
\fi

 \RequirePackage{wallpaper}

 \textwidth=140mm
 \textheight=240mm
 \topsep=0ex
 \headheight=15mm
 \headsep=15mm
 \topmargin=0mm
 \footskip=13mm
 \oddsidemargin=19mm
 \evensidemargin=-5mm
 \parskip=1.0ex
 \parindent=0em
 \raggedbottom
 \voffset=0mm
 \hoffset=0mm

\marginparwidth=35mm
\marginparsep=1ex

\RequirePackage{ifthen} \RequirePackage{parskip}

\if@mtpro
  \RequirePackage{mtpro}
\fi

\newcounter{pdfout}

%% latex or pdflatex?
\@ifundefined{pdfoutput}{  %latex-mode
  \setcounter{pdfout}{0}
  \RequirePackage{graphicx}
  \RequirePackage{color}
  \RequirePackage[%draft,
    pdftitle={ABARES LaTeX report class},
    pdfauthor={Neal Hughes},
    pdfsubject={Copyright ABARES},
    pdfcreator={LaTeX source to pdf},
    bookmarksnumbered,bookmarksopen,pdfstartview=Fit,breaklinks=true,
    %colorlinks=true,urlcolor=blue, citecolor = magenta, linkcolor=red]{hyperref}
    colorlinks=true,urlcolor=blue, citecolor = black, linkcolor=blue]{hyperref}
}
{  %pdflatex-mode
  \setcounter{pdfout}{1}
  \RequirePackage{graphicx}
  \RequirePackage{color}
  \RequirePackage[
    pdftitle={ABARES LaTeX report class},
    pdfauthor={Neal Hughes},
    pdfsubject={Copyright ABARES},
    pdfcreator={LaTeX source to pdf},
    bookmarksnumbered,bookmarksopen,pdfstartview=Fit,
    colorlinks=true,urlcolor=blue, citecolor = magenta, linkcolor=blue]{hyperref}
    %colorlinks=true,urlcolor=dark-colour, citecolor = black, linkcolor=black]{hyperref}
}

\if@colortbl \RequirePackage{colortbl} \fi

\newboolean{formal}
\setboolean{formal}{false}
\newboolean{standard}
\setboolean{standard}{false}

\if@formal
\setboolean{formal}{true}
\fi
\if@standard
\setboolean{standard}{true}
\fi

%\definecolor{light-colour}{rgb}{1,0.49,0.0} % ABARES Orange
%\definecolor{third-colour}{rgb}{0.89,0.0,0.13} % ABARES Red
\definecolor{dark-colour}{rgb}{0,0,0} % Black

% The following commands redefine the styles for the different section headings.
\makeatletter
%\renewcommand{\section}{\resetequation\resettable\resetfigure%
%\@startsection{section}{1}{0mm}{0mm}{2mm}{\normalfont\Huge\sffamily}%
%}
%\renewcommand{\subsection}{\@startsection{subsection}{2}{0em}%
%  {-0.5\baselineskip}{0.1ex}{\normalfont\Large\bfseries\rmfamily} }
%\renewcommand{\subsubsection}{\@startsection{subsubsection}{3}{0em}%
%  {-0.1\baselineskip}{0.1ex}{\normalfont\bfseries\sffamily\color{third-colour}}}
%\renewcommand{\paragraph}{\@startsection{paragraph}{4}{0em}%
%  {-0.1\baselineskip}{0.01ex}{\normalfont\small\bfseries\sffamily}}
%\renewcommand{\subparagraph}{\@startsection{subparagraph}{5}{0em}%
%  {-0.1\baselineskip}{0.01ex}{\normalfont\small\sffamily}}


\renewcommand{\l@section}{\bigskip\bfseries\@dottedtocline{1}{1.0em}{1.2em}}
\renewcommand{\l@subsection}{\smallskip\normalfont\@dottedtocline{2}{2.2em}{2.2em}}
\renewcommand{\l@subsubsection}{\normalfont\@dottedtocline{3}{4.4em}{2.9em}}
\renewcommand{\l@paragraph}{\normalfont\@dottedtocline{3}{7.3em}{3.3em}}

\renewcommand{\contentsline}[4]{\sffamily\color{dark-colour}\csname l@#1\endcsname{\sffamily #2}{\color{dark-colour}\sffamily#3}{}}


\makeatother

%\renewcommand{\theequation}{\thesection.\arabic{equation}}
%\newcommand{\resetequation}{\setcounter{equation}{0}}
%\renewcommand{\thetable}{\thesection.\arabic{table}}
%\newcommand{\resettable}{\setcounter{table}{0}}
%\renewcommand{\thefigure}{\thesection.\arabic{figure}}
%\newcommand{\resetfigure}{\setcounter{figure}{0}}

\setcounter{secnumdepth}{4} \setcounter{tocdepth}{4}

  \newcommand{\thedoctitle}{}
  \newcommand{\doctitle}[1][]{\renewcommand{\thedoctitle}{#1}}

  \newcommand{\thedocsubtitle}{}
  \newcommand{\docsubtitle}[1][]{\renewcommand{\thedocsubtitle}{#1}}


  \newcommand{\thecommercial}{}
  \newcommand{\docinconfidence}[1][]{\renewcommand{\thecommercial}{#1}}

  \newcommand{\theabstract}{}
  \newcommand{\docabstract}[1][]{\renewcommand{\theabstract}{#1}}

  \newcommand{\thedivision}{}
  \newcommand{\docdivision}[1][]{\renewcommand{\thedivision}{#1}}

  \newcommand{\theauthors}{}
  \newcommand{\docauthors}[1][]{\renewcommand{\theauthors}{#1}}

  \newcommand{\thereportnum}{}
  \newcommand{\docreportnum}[1][]{\renewcommand{\thereportnum}{#1}}

  \newcommand{\thenumclientcopy}{0}
  \newcommand{\numclientcopy}[1][]{\renewcommand{\thenumclientcopy}{#1}}

  \newcommand{\thenumlibcopy}{0}
  \newcommand{\numlibcopy}[1][]{\renewcommand{\thenumlibcopy}{#1}}

  \newcommand{\thenumslcopy}{0}
  \newcommand{\numslcopy}[1][]{\renewcommand{\thenumslcopy}{#1}}

  \newcommand{\thenumauthorcopy}{0}
  \newcommand{\numauthorcopy}[1][]{\renewcommand{\thenumauthorcopy}{#1}}

  \newcommand{\thereportdate}{}
  \newcommand{\docreportdate}[1][]{\renewcommand{\thereportdate}{#1}}

  \newcommand{\thecopyrightyear}{}
  \newcommand{\doccopyrightyear}[1][]{\renewcommand{\thecopyrightyear}{#1}}

  \newcommand{\thefootertitle}{}
  \newcommand{\docfootertitle}[1][]{\renewcommand{\thefootertitle}{#1}}

  \newcommand{\thereportday}{}
  \newcommand{\docreportday}[1][]{\renewcommand{\thereportday}{#1\ }{}}

  \newcommand{\thereportmonth}{}
  \newcommand{\docreportmonth}[1][]{\renewcommand{\thereportmonth}{#1\ }}

  \newcommand{\thereportyear}{}
  \newcommand{\docreportyear}[1][]{\renewcommand{\thereportyear}{#1}}

  \newcommand{\theclient}{}
  \newcommand{\docclient}[1][]{\renewcommand{\theclient}{#1}}

  \newcommand{\theclientcontact}{}
  \newcommand{\docclientcontact}[1][]{\renewcommand{\theclientcontact}{#1}}

  \newcommand{\thebusinessunit}{}
  \newcommand{\docbusinessunit}[1][]{\renewcommand{\thebusinessunit}{#1}}


  \newcommand{\thefurtherinfoA}{}
  \newcommand{\docfurtherinfoA}[6][]{\renewcommand{\thefurtherinfoA}{%

   \vspace{1ex}

  \textbf{#1}\\
  #2\\
  \begin{tabular}{ll}
  \textbf{t} & #3 \\
  \textbf{e} &  \href{mailto: #4}{\ifthenelse{\boolean{formal}}{#4}
  {\ifthenelse{\boolean{standard}}{\color{white}#4}{#4}}}\\
  \textbf{w} &  \href{#5}{\ifthenelse{\boolean{formal}}{#6}
  {\ifthenelse{\boolean{standard}}{\color{white}#6}{#6}}}\\
  \end{tabular}}}

  \newcommand{\thefurtherinfoB}{}
  \newcommand{\docfurtherinfoB}[6][]{\renewcommand{\thefurtherinfoB}{%
  \textbf{#1}\\
  #2\\
  \begin{tabular}{ll}
  \textbf{t} & #3 \\
  \textbf{e} &  \href{mailto: #4}{\ifthenelse{\boolean{formal}}{#4}
  {\ifthenelse{\boolean{standard}}{\color{white}#4}{#4}}}\\
  \textbf{w} &  \href{#5}{\ifthenelse{\boolean{formal}}{#6}
  {\ifthenelse{\boolean{standard}}{\color{white}#6}{#6}}}\\
  \end{tabular}}}

  \newcommand{\thefurtherinfoC}{}
  \newcommand{\docfurtherinfoC}[6][]{\renewcommand{\thefurtherinfoC}{%
  \textbf{#1}\\
  #2\\
  \begin{tabular}{ll}
  \textbf{t} & #3 \\
  \textbf{e} &  \href{mailto: #4}{\ifthenelse{\boolean{formal}}{#4}
  {\ifthenelse{\boolean{standard}}{\color{white}#4}{#4}}}\\
  \textbf{w} &  \href{#5}{\ifthenelse{\boolean{formal}}{#6}
  {\ifthenelse{\boolean{standard}}{\color{white}#6}{#6}}}\\
  \end{tabular}}}




\newcommand{\thefrontpicture}{}
\newcommand{\docfrontpicture}[2][scale=1.0]{\renewcommand{\thefrontpicture}{%
\AddToShipoutPicture*{%
\AtPageLowerLeft{%
\parbox[b][\paperheight]{\paperwidth}{%
\hspace{-28.5mm}\raisebox{150.7mm}[0mm][0mm]{%
\begin{minipage}[c]{300mm}%
\centering%
%\includegraphics[#1]{#2}%
\end{minipage}}%
}}}}}


\newcounter{partcount}
\setcounter{partcount}{1}

%\newcommand{\partpage}[1]{
%\clearpage

%\thispagestyle{empty}

%\mbox{}\ClearWallPaper\ThisCenterWallPaper{1.005}{figures/reportpart-formal}

%\vspace{20mm}

%{\Huge\color{light-colour}\sffamily\bfseries Part \Roman{partcount}\quad \color{dark-colour} #1}

%\addcontentsline{toc}{part}{Part \Roman{partcount}\quad
%#1}

%\refstepcounter{partcount}

%\clearpage

%}


\newcommand{\thelogoA}{}
\newcommand{\doclogoA}[4]{\renewcommand{\thelogoA}{%
\AddToShipoutPicture*{%
\AtPageLowerLeft{%
\parbox[b][\paperheight]{\paperwidth}{%
\raisebox{#2}[0mm][0mm]{%
\hspace{#1}\includegraphics[#3]{#4}%
} }}}}}

\newcommand{\thelogoB}{}
\newcommand{\doclogoB}[4]{\renewcommand{\thelogoB}{%
\AddToShipoutPicture*{%
\AtPageLowerLeft{%
\parbox[b][\paperheight]{\paperwidth}{%
\raisebox{#2}[0mm][0mm]{%
\hspace{#1}\includegraphics[#3]{#4}%
} }}}}}


\newcommand{\thelogoC}{}
\newcommand{\doclogoC}[4]{\renewcommand{\thelogoC}{%
\AddToShipoutPicture*{%
\AtPageLowerLeft{%
\parbox[b][\paperheight]{\paperwidth}{%
\raisebox{#2}[0mm][0mm]{%
\hspace{#1}\includegraphics[#3]{#4}%
} }}}}}


\newcommand{\setreportfront}[1]{
       %\thispagestyle{empty}
       %\vspace*{-20pt}%
       %\enlargethispage{40pt}%
       %\ClearWallPaper\thefrontpicture\ThisCenterWallPaper{1.005}{figures/reportfront-formal.pdf}

}

\newcommand{\setfronttext}{
 \AtPageLowerLeft{
  \parbox[b][\paperheight]{\paperwidth}{
  \vspace{60mm}%
  \hspace{60mm}\begin{minipage}[t]{135mm}
 %  \raggedright\color{white}
 %
 %  \sffamily\bfseries

 %  \thedivision

 %  \ifthenelse{\boolean{standard}}{
 %  \color{light-colour}}{\color{dark-colour}}

   \end{minipage}
  }
 }

 \AtPageLowerLeft{
  \parbox[b][\paperheight]{\paperwidth}{
   \vspace{45mm}%
   \hspace{38mm}\begin{minipage}[t]{150mm}
   \raggedright

   \color{black}

   \sffamily\bfseries\Huge\thedoctitle

   \normalfont\Huge\sffamily\thedocsubtitle

   \vspace{4mm}
   \normalfont\Large\sffamily\theauthors

   \vspace{7mm}%

   \footnotesize\normalfont\sffamily \begin{flushright}Research by the Australian Bureau of Agricultural  \end{flushright}
   \footnotesize\normalfont\sffamily \begin{flushright}and Resource Economics and Sciences \end{flushright}
   %\vspace*{-0.1\baselineskip}
   \textcolor{orange}{\rule{15.05cm}{0.75pt}}

   \vspace*{-1.6\baselineskip}
   \textcolor{orange}{\Large\normalfont\sffamily\begin{flushright}\thereportdate \end{flushright}}

   %\normalsize \begin{flushright}\thereportdate \kern 10.6pc   \end{flushright}

  \vspace{10mm}

   %\restoregeometry
   \end{minipage} \vfill
  }
 }

}


\makeatletter
%\renewcommand{\@evenhead}{\noindent \hfill \textit{\thefootertitle} \hspace{10mm} ABARES \hfill }
%\renewcommand{\@oddhead}{\noindent \hfill \textit{\thefootertitle} \hspace{10mm} ABARES \hfill }
%\renewcommand{\@evenfoot}{\noindent \thepage \hfill }
%\renewcommand{\@oddfoot}{\noindent \hfill \thepage }

\makeatother


%\renewcommand{\familydefault}{\sfdefault}
\renewcommand\listfigurename{Figures}
\renewcommand\listtablename{Tables}
%=================================================

\AtBeginDocument{

  \pagenumbering{alph}

  \thispagestyle{empty}


  \ifthenelse{\boolean{formal}}{
    \setreportfront{formal}

    \mbox{}

    \AddToShipoutPicture*{
      \setfronttext
    }
  }
  {\ifthenelse{\boolean{standard}}{
    \setreportfront{standard}

    \mbox{}

    \AddToShipoutPicture*{
      \setfronttext
    }
  }
  {% Make the default front the same as formal
    \setreportfront{formal}

    \mbox{}

    \AddToShipoutPicture*{
      \setfronttext
    }
  }
  }

  \renewcommand{\thefrontpicture}{}
  \thelogoA  \renewcommand{\thelogoA}{}
  \thelogoB  \renewcommand{\thelogoB}{}
  \thelogoC  \renewcommand{\thelogoC}{}


}

%=================================================

\AtEndDocument{}

%=================================================

\endinput
