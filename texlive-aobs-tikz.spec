# revision 32662
# category Package
# catalog-ctan /graphics/pgf/contrib/aobs-tikz
# catalog-date 2014-01-13 12:12:15 +0100
# catalog-license lppl1.3
# catalog-version 1.0
Name:		texlive-aobs-tikz
Version:	1.0
Release:	2
Summary:	TikZ styles for creating overlaid pictures in beamer
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/graphics/pgf/contrib/aobs-tikz
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/aobs-tikz.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/aobs-tikz.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/aobs-tikz.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package defines auxiliary TikZ styles useful for overlaying
pictures' elements in Beamer. The TikZ styles are grouped in a
library, overlay-beamer-styles which is automatically called by
the package itself. Users may either load just aobs-tikz or the
library; the latter method necessitates TikZ manual load.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/aobs-tikz/tikzlibraryoverlay-beamer-styles.code.tex
%doc %{_texmfdistdir}/doc/latex/aobs-tikz/README
%doc %{_texmfdistdir}/doc/latex/aobs-tikz/aobs-tikz.pdf
%doc %{_texmfdistdir}/doc/latex/aobs-tikz/example.tex
#- source
%doc %{_texmfdistdir}/source/latex/aobs-tikz/aobs-tikz.dtx
%doc %{_texmfdistdir}/source/latex/aobs-tikz/aobs-tikz.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
