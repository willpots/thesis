%%
%% This is file `thesis.cls',
%% generated with the docstrip utility.
%%

\NeedsTeXFormat{LaTeX2e}[1995/12/01]
\ProvidesClass{thesis}
[2008/4/17 v2.9
  Middlebury College thesis class]
\usepackage{ifpdf}
\newif\ifphd
\DeclareOption{phd}{\phdtrue}
\DeclareOption{master}{\phdfalse}
\DeclareOption{midd}{\phdfalse}
\ExecuteOptions{phd}
\newif\ifthesisheadings
\newif\ifhalfthesisheadings
\newif\ifsmallerheadings
\DeclareOption{latexheadings}{\thesisheadingsfalse \halfthesisheadingsfalse}
\DeclareOption{thesisheadings}{\thesisheadingstrue \halfthesisheadingsfalse}
\DeclareOption{halfthesisheadings}{\halfthesisheadingstrue \thesisheadingsfalse}
\DeclareOption{normalsizeheadings}{\smallerheadingsfalse}
\DeclareOption{smallerheadings}{\smallerheadingstrue}
\ExecuteOptions{thesisheadings}
\ExecuteOptions{smallerheadings}
\DeclareOption{10pt}{%
 \iffinal%
  \OptionNotUsed%
  \ClassWarningNoLine{thesis}{Font size 10pt not allowed; using 12pt}%
 \else%
  \PassOptionsToClass{10pt}{report}%
 \fi%
}
\DeclareOption{11pt}{%
 \final%
  \OptionNotUsed%
  \ClassWarningNoLine{thesis}{Font size 11pt not allowed; using 12pt}%
 \else%
  \PassOptionsToClass{11pt}{report}%
 \fi
}
\newcommand{\prelim@contents}[1]{}
\DeclareOption{tocprelim}{%
  \renewcommand{\prelim@contents}[1]{\addcontentsline{toc}{section}{#1}}
}
\DeclareOption{draft}{%
  \let\ifdraft\iftrue%
  \let\iffinal\iffalse%
  \PassOptionsToClass{final}{report}%
}
\DeclareOption{final}{%
  \let\ifdraft\iffalse%
  \let\iffinal\iftrue%
  \PassOptionsToClass{final}{report}%
}
\DeclareOption{semifinal}{%
  \let\ifdraft\iffalse%
  \let\iffinal\iftrue%
  \PassOptionsToClass{draft}{report}%
}
\DeclareOption*{%
  \PassOptionsToClass{\CurrentOption}{report}%
}
\ExecuteOptions{final}
\ProcessOptions

\iffinal\LoadClass[12pt]{report}[1994/06/01]\else\LoadClass{report}[1994/06/01]\fi
\ifpdf
  \setlength{\pdfpagewidth}{8.5in}
  \setlength{\pdfpageheight}{11in}
\fi
\ifthesisheadings
  \def\@makechapterhead#1{%
    \begin{center}%
      \MakeUppercase{\@chapapp\space \thechapter} \\
      \MakeUppercase{\bfseries #1}
    \end{center}%
    }
  \def\@makeschapterhead#1{%
    \begin{center}%
      \MakeUppercase{\bfseries #1}
    \end{center}%
    }
\fi
\ifhalfthesisheadings
  \def\@makeschapterhead#1{%
    \begin{center}%
      \MakeUppercase{\bfseries #1}
    \end{center}%
    }
  \def\@makechapterhead#1{%
    \vspace*{50\p@}%
    {\parindent \z@ \raggedright \normalfont
      \ifnum \c@secnumdepth >\m@ne
          \huge\bfseries \@chapapp\space \thechapter
          \par\nobreak
          \vskip 20\p@
      \fi
      \interlinepenalty\@M
      \singlespacing \Huge \bfseries #1\par\nobreak
      \vskip 40\p@
    }}
  \ifsmallerheadings
    \def\@makechapterhead#1{%
      {\parindent \z@ \raggedright \normalfont
        \ifnum \c@secnumdepth >\m@ne
            \LARGE\bfseries \@chapapp\space \thechapter
            \par\nobreak
        \fi
        \interlinepenalty\@M
        \singlespacing \LARGE \bfseries #1\par\nobreak
      }}
  \fi
\fi

\ifsmallerheadings
\renewcommand\section{\@startsection {section}{1}{\z@}%
                                   {-3.5ex \@plus -1ex \@minus -.2ex}%
                                   {2.3ex \@plus.2ex}%
                                   {\normalfont\large\bfseries}}
\fi

\renewcommand{\footnotesize}{\normalsize}
\renewcommand{\@makefntext}[1]{%
  \parindent 1em%
  \noindent
  \footnotespacing
  \hbox to 1.8em{\hss\@makefnmark}#1
  \par\normalspacing
}
\renewcommand{\defaultscriptratio}{.75}
\renewcommand{\defaultscriptscriptratio}{.6}
\setlength\headsep{25\p@}
\if@twocolumn
\else
  \setlength\topmargin{-0.4in}
  \setlength\headheight{0.16667in}
  \setlength\headsep{0.33333in}
  \setlength\textheight{8.8in}
  \setlength\footskip{0.5in}
  \setlength\oddsidemargin{.6in}
  \setlength\evensidemargin{.6in}
  \setlength\textwidth{5.80in}
  \setlength\marginparsep{0.1in}
  \setlength\marginparwidth{0.8in}
\fi
\if@compatibility
  \setlength\topmargin{0\p@}
\else
\fi
\newcommand{\ps@thesis}{%
\def\@oddhead{}
\def\@oddfoot{\hfil\thepage\hfil}%
\def\@evenhead{}%
\def\@evenfoot{\@oddfoot}%
\def\chaptermark##1{}%
\def\sectionmark##1{}%
}
\newcommand{\ps@oldthesis}{%
\def\@oddhead{{\slshape\rightmark}\hfil\thepage}%
\def\@oddfoot{}%
\def\@evenhead{\thepage\hfil{\slshape\leftmark}}%
\def\@evenfoot{}%
\def\chaptermark##1{}%
\def\sectionmark##1{}%
}
\newcommand{\ps@thesisc}{%
\def\@oddhead{\hfil\thepage\hfil}%
\def\@oddfoot{}%
\def\@evenhead{\@oddhead}%
\def\@evenfoot{}%
\def\chaptermark##1{}%
\def\sectionmark##1{}%
}
\raggedbottom
\renewcommand{\contentsname}{Table of Contents}
\renewcommand{\l@figure}{\@dottedtocline{1}{1.5em}{2.6em}}
\let\l@table\l@figure

\renewenvironment{thebibliography}[1]
     {\chapter*{\bibname
        \@mkboth{\uppercase{\bibname}}{\uppercase{\bibname}}}%
      \list{\@biblabel{\arabic{enumiv}}}%
           {\settowidth\labelwidth{\@biblabel{#1}}%
            \leftmargin\labelwidth
            \advance\leftmargin\labelsep
    \itemsep=12pt
            \@openbib@code
            \usecounter{enumiv}%
            \let\p@enumiv\@empty
            \renewcommand\theenumiv{\arabic{enumiv}}}%
      \sloppy\clubpenalty4000\widowpenalty4000%
      \sfcode`\.=\@m\relax
      \addcontentsline{toc}{chapter}{\bibname}
      \listspacing{bib}}
     {\def\@noitemerr
       {\@latex@warning{Empty `thebibliography' environment}}%
      \normalspacing
      \endlist}

\newcommand{\@titlesize}{\fontsize{18}{24}\selectfont}
\newcommand{\@subtitlesize}{\fontsize{12}{24}\selectfont}
\newcommand{\@authorsize}{\normalsize\doublespacing} % No Pharaoh he.
\newcommand{\@conferralmonth}{May}
\newcommand{\@conferralyear}{2014}
\newcommand{\@adviser}{Professor XYZ}

\newcommand{\titlesize}[1]{\renewcommand{\@titlesize}{#1}}
\newcommand{\subtitlesize}[1]{\renewcommand{\@subtitlesize}{#1}}
\newcommand{\authorsize}[1]{\renewcommand{\@authorsize}{#1}}
\newcommand{\conferraldate}[2]{%
  \renewcommand{\@conferralmonth}{#1}
  \renewcommand{\@conferralyear}{#2}
}
\newcommand{\adviser}[1]{\renewcommand{\@adviser}{#1}}
\newcommand{\advisor}[1]{\renewcommand{\@adviser}{#1}}

\renewcommand{\maketitle}{%
  \begin{titlepage}%
    \realsinglespacing
    \begin{center}%
      \hrule height 0.5in width 0pt % force vertical space at top
      \@titlesize \expandafter\uppercase\expandafter{\@title}
    \end{center}
    \vfill
    \begin{center}
      \@authorsize
      \@author \\
      ~ \\  
      Adviser: \@adviser
    \end{center}
    \vfill
    \begin{center}
      \@subtitlesize
      A Thesis \\
      Presented to the Faculty of the Computer Science Department \\
      of Middlebury College \\
      in Partial Fulfillment of the Requirements for the Degree of \\
      Bachelor of Arts
    \vfill
      \@conferralmonth\ \@conferralyear
    \end{center}
    \vspace{0.25in}
  \end{titlepage}
}

\renewenvironment{titlepage}{%
  \typeout{Title page}
  \pagestyle{empty}
  \doublespacing
}{%
  \normalspacing\clearpage
}


\newenvironment{copyrightpage}{%
  \typeout{Copyleft page}
  \pagestyle{empty}
  \null\vfill
  \begin{center}
}{%
  \end{center}
  \vfill\null
  \newpage
  \clearpage%
}

\newcommand{\makecopyright}{%
  \begin{copyrightpage}
  \copyright\ \@copyrightyear{} \@copyrightholder \\
  ALL RIGHTS RESERVED
  \end{copyrightpage}%
}
\newcommand{\@copyrightholder}{\@author}
\newcommand{\@copyrightyear}{\@conferralyear}

\newcommand{\copyrightholder}[1]{\renewcommand{\@copyrightholder}{#1}}
\newcommand{\copyrightyear}[1]{\renewcommand{\@copyrightyear}{#1}}

\newcommand{\makepublicdomain}{%
  \begin{copyrightpage}
  This document is in the public domain.
  \end{copyrightpage}%
}


\newlength{\@abhdskip}%
\renewenvironment{abstract}{
  \typeout{Abstract}
  \setlength{\@abhdskip}{.6in}
  \addtolength{\@abhdskip}{-\topmargin}
  \addtolength{\@abhdskip}{-\headheight}
  \addtolength{\@abhdskip}{-\headsep}
  \addtolength{\@abhdskip}{-\baselineskip}
  \begin{center}%
    \vspace*{\@abhdskip}%
    \ifphd%
      {\def\\{\noexpand\\} \xdef\@abstracttitle{\@abstracttitle}}
      \expandafter\uppercase\expandafter{\@abstracttitle} \\
      \@author,\ Ph.D. \\
      Thesis University\ \@conferralyear%
    \else
      \normalsize \bfseries\selectfont
      ABSTRACT
    \fi%
    \vspace{0.5\baselineskip}
  \end{center}%
  \pagestyle{empty}
  \thispagestyle{empty}
}{%
  \clearpage
}

\newcommand{\@abstracttitle}{\@title}
\newcommand{\abstracttitle}[1]{\renewcommand{\@abstracttitle}{#1}}


\newenvironment{biosketch}{%
  \typeout{Vita}
  \pagestyle{plain}
  \pagenumbering{roman}
  \setcounter{page}{3}
  \prelim@contents{Biographical Sketch}
  \chapter*{Biographical Sketch}
}{%
  \clearpage
}

\newenvironment{dedication}{%
  \prelim@contents{Dedication}
  \null\vfill
  \begin{center}
}{
  \end{center}
  \vfill\null
  \clearpage
}

\newenvironment{acknowledgements}{%
  \prelim@contents{Acknowledgements}
  \chapter*{Acknowledgements}
}{%
  \cleardoublepage
}

\newcommand{\contentspage}{%
  \listspacing{toc}
  \label{toc}
  \prelim@contents{\contentsname}
  \tableofcontents
  \normalspacing
  \clearpage
}

\newcommand{\tablelistpage}{%
  \listspacing{tab}
  \label{lot}
  \prelim@contents{\listtablename}
  \listoftables
  \normalspacing
  \clearpage
}

\newcommand{\figurelistpage}{%
  \listspacing{fig}
  \label{lof}
  \prelim@contents{\listfigurename}
  \listoffigures
  \normalspacing
  \clearpage
}
\newcommand{\abbrlist}{%
  \listspacing{abbr}
  \prelim@contents{List of Abbreviations}
  \chapter*{List of Abbreviations}
}

\newcommand{\symlist}{%
  \listspacing{sym}
  \prelim@contents{List of Symbols}
  \chapter*{List of Symbols}
}

\newcommand{\preface}{%
  \listspacing{pref}
  \prelim@contents{Preface}
  \chapter*{Preface}
}

\renewcommand\normalsize{%
   \@setfontsize\normalsize\@xiipt{12}%
   \abovedisplayskip 12\p@ \@plus3\p@ \@minus7\p@
   \abovedisplayshortskip \z@ \@plus3\p@
   \belowdisplayshortskip 6.5\p@ \@plus3.5\p@ \@minus3\p@
   \def\@listi{\leftmargin\leftmargini
               \parsep 5\p@  \@plus2.5\p@ \@minus\p@
               \topsep 10\p@ \@plus4\p@   \@minus6\p@
               \itemsep \z@  \@plus2.5\p@ \@minus\p@}%
   \belowdisplayskip \abovedisplayskip
}
\renewcommand\small{%
   \@setfontsize\small\@xipt{11}%
   \abovedisplayskip 11\p@ \@plus3\p@ \@minus6\p@
   \abovedisplayshortskip \z@ \@plus3\p@
   \belowdisplayshortskip 6.5\p@ \@plus3.5\p@ \@minus3\p@
   \def\@listi{\leftmargin\leftmargini
               \topsep 9\p@ \@plus3\p@ \@minus5\p@
               \parsep 4.5\p@ \@plus2\p@ \@minus\p@
               \itemsep \z@  \@plus2\p@ \@minus\p@}%
   \belowdisplayskip \abovedisplayskip
}
\renewcommand\footnotesize{%
   \@setfontsize\footnotesize\@xpt\@xpt
   \abovedisplayskip 10\p@ \@plus2\p@ \@minus5\p@
   \abovedisplayshortskip \z@ \@plus3\p@
   \belowdisplayshortskip 6\p@ \@plus3\p@ \@minus3\p@
   \def\@listi{\leftmargin\leftmargini
               \topsep 6\p@ \@plus2\p@ \@minus2\p@
               \parsep 3\p@ \@plus2\p@ \@minus\p@
               \itemsep \parsep}%
   \belowdisplayskip \abovedisplayskip
}

\newcommand{\realsinglespacing}{%
  \let\CS=\@currsize\renewcommand{\baselinestretch}{1.0}\CS}
\newcommand{\singlespacing}{%
  \let\CS=\@currsize\renewcommand{\baselinestretch}{1.208333}\CS}
\newcommand{\singlespacingplus}{%
  \let\CS=\@currsize\renewcommand{\baselinestretch}{1.5}\CS}
\newcommand{\doublespacing}{%
  \let\CS=\@currsize\renewcommand{\baselinestretch}{2}\CS}
\newcommand{\realdoublespacing}{%
  \let\CS=\@currsize\renewcommand{\baselinestretch}{2}\CS}
\newcommand{\normalspacing}{\doublespacing}
\newcommand{\footnotespacing}{\singlespacing}
\newcommand{\listspacing}[1]{\singlespacing} % extra arg is extensibility hook
\newcommand{\changespacing}[2]{%
  \renewcommand{#1}{%
    \let\CS=\@currsize\renewcommand{\baselinestretch}{#2}\CS}%
}
\ifdraft\changespacing{\normalspacing}{1}\fi
\newcommand{\changenormalspacing}[1]{\renewcommand{\normalspacing}{#1}}
\normalspacing

\def \@floatboxreset {%
        \reset@font
        \normalsize
        \singlespacing
        \@setminipage
}

\endinput
%%
%% End of file `thesis.cls'.
