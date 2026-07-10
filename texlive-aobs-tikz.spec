%global tl_name aobs-tikz
%global tl_revision 70952

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.01
Release:	%{tl_revision}.1
Summary:	TikZ styles for creating overlaid pictures in beamer
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/graphics/pgf/contrib/aobs-tikz
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/aobs-tikz.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/aobs-tikz.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/aobs-tikz.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
Requires(pre):	texlive-tlpkg
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package defines auxiliary TikZ styles useful for overlaying
pictures' elements in Beamer. The TikZ styles are grouped in a library,
overlay-beamer-styles which is automatically called by the package
itself. Users may either load just aobs-tikz or the library; the latter
method necessitates TikZ manual load.

%prep
%setup -q -c -a1 -a2
rm -rf tlpkg
if [ -d RELOC ]; then
	cp -a RELOC/. .
	rm -rf RELOC
fi

%build

%install
mkdir -p %{buildroot}%{_datadir}/texmf-dist
# Flat tlnet layout: tex/ doc/ source/ fonts/ ... -> texmf-dist/
if [ -d texmf-dist ]; then
	cp -a texmf-dist/. %{buildroot}%{_datadir}/texmf-dist/
elif [ -d texmf ]; then
	mkdir -p %{buildroot}%{_datadir}/texmf
	cp -a texmf/. %{buildroot}%{_datadir}/texmf/
else
	for d in * .[!.]* ..?*; do
		[ -e "$d" ] || continue
		case "$d" in tlpkg|RELOC) continue ;; esac
		cp -a "$d" %{buildroot}%{_datadir}/texmf-dist/
	done
fi
rm -rf %{buildroot}%{_datadir}/texmf-dist/tlpkg

%files
%dir %{_datadir}/texmf-dist
%dir %{_datadir}/texmf-dist/doc
%dir %{_datadir}/texmf-dist/source
%dir %{_datadir}/texmf-dist/tex
%dir %{_datadir}/texmf-dist/doc/latex
%dir %{_datadir}/texmf-dist/source/latex
%dir %{_datadir}/texmf-dist/tex/latex
%dir %{_datadir}/texmf-dist/doc/latex/aobs-tikz
%dir %{_datadir}/texmf-dist/source/latex/aobs-tikz
%dir %{_datadir}/texmf-dist/tex/latex/aobs-tikz
%doc %{_datadir}/texmf-dist/doc/latex/aobs-tikz/README.txt
%doc %{_datadir}/texmf-dist/doc/latex/aobs-tikz/aobs-tikz.pdf
%doc %{_datadir}/texmf-dist/doc/latex/aobs-tikz/example.tex
%doc %{_datadir}/texmf-dist/source/latex/aobs-tikz/aobs-tikz.dtx
%doc %{_datadir}/texmf-dist/source/latex/aobs-tikz/aobs-tikz.ins
%{_datadir}/texmf-dist/tex/latex/aobs-tikz/tikzlibraryoverlay-beamer-styles.code.tex
