Name:		texlive-aobs-tikz
Version:	32662
Release:	1
Summary:	TikZ styles for creating overlaid pictures in beamer
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/graphics/pgf/contrib/aobs-tikz
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/aobs-tikz.r32662.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/aobs-tikz.doc.r32662.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/aobs-tikz.source.r32662.tar.xz
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
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
