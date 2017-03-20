%% Neal Hughes - Hack of CSRIO latex template to match ABARES style
%%
\NeedsTeXFormat{LaTeX2e}[1994/12/01] \ProvidesClass{abaresbasic2016}
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

 \textwidth=150mm
 \textheight=240mm
 \topsep=0ex
 \headheight=0mm
 \headsep=16mm
 \topmargin=0mm
 \footskip=13mm
 \oddsidemargin=3pt
 \evensidemargin=3pt\parskip=1.0ex
 \parindent=0em
 \raggedbottom
 \voffset=-12mm
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
    colorlinks=true,urlcolor=dark-colour, citecolor = black, linkcolor=blue]{hyperref}
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
    colorlinks=true,urlcolor=blue, citecolor = magenta, linkcolor=dark-colour]{hyperref}
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

\definecolor{abares-orange}{rgb}{1,0.49,0.0} % ABARES Orange
\definecolor{abares-red}{rgb}{0.59,0.0,0.09} % ABARES Red
\definecolor{dark-colour}{rgb}{0,0,0} % Black

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

\newcommand{\partpage}[1]{
\thispagestyle{empty}
%\mbox{}\ClearWallPaper\ThisCenterWallPaper{1.005}{figures/reportpart-standard}
\vspace{20mm}
{\Huge\sffamily\bfseries Part \Roman{partcount}\quad \color{dark-colour} #1}
\addcontentsline{toc}{part}{Part \Roman{partcount}\quad
#1}

\refstepcounter{partcount}
}


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
      % \ClearWallPaper\thefrontpicture\ThisCenterWallPaper{1.005}{figures/reportfront-standard}
}

\newcommand{\setfronttext}{
 \AtPageLowerLeft{
  \parbox[b][\paperheight]{\paperwidth}{
   \vspace{19mm}%
   \hspace{21mm}

   \begin{minipage}[t]{135mm}
   \raggedright\color{white}

   \end{minipage} \vfill
  }
 }

 \AtPageLowerLeft{
  \parbox[b][\paperheight]{\paperwidth}{
   \vspace{65mm}%
   \hspace{50mm}\begin{minipage}[t]{150mm}
   \raggedright


   \ifthenelse{\boolean{standard}}{
   \color{dark-colour}}{}

   \Huge\normalfont\bfseries\thedoctitle

   \ifthenelse{\boolean{standard}}{
   \color{dark-colour}}{\color{dark-colour}}

   \normalfont\huge\sffamily\thedocsubtitle

   \vspace{5mm}
   \ifthenelse{\boolean{standard}}{
   \color{dark-colour}}{\color{dark-colour}}

   \Large\normalfont\theauthors

   \vspace{13mm}%

   \small\sffamily\bfseries \begin{flushright}Research by the Australian Bureau of Agricultural    \end{flushright}
   \small\sffamily\bfseries \begin{flushright}and Resource Economics and Sciences  \end{flushright}
   \vspace*{-0.4\baselineskip}
   \rule{\textwidth}{0.75pt}

   \large\normalfont\sffamily\begin{flushright}\thereportnum \end{flushright}

   \normalsize \begin{flushright}\thereportdate   \end{flushright}

  \vspace{10mm}

   \end{minipage} \vfill
  }
 }

}


\makeatletter
\renewcommand{\@evenhead}{\noindent \hfill \textit{\thefootertitle} \hspace{10mm} ABARES \hfill }
\renewcommand{\@oddhead}{\noindent \hfill \textit{\thefootertitle} \hspace{10mm} ABARES \hfill }
\renewcommand{\@evenfoot}{\noindent \hfill \thepage \hfill }
\renewcommand{\@oddfoot}{\noindent \hfill \thepage \hfill }

\makeatother


%\renewcommand{\familydefault}{\sfdefault}
\renewcommand\listfigurename{Figures\vspace{4mm}}
\renewcommand\listtablename{Tables\vspace{4mm}}
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
