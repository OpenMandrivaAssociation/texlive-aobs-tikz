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
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package defines auxiliary TikZ styles useful for overlaying
pictures' elements in Beamer. The TikZ styles are grouped in a library,
overlay-beamer-styles which is automatically called by the package
itself. Users may either load just aobs-tikz or the library; the latter
method necessitates TikZ manual load.

