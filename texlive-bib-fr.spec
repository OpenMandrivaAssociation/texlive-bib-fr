%global tl_name bib-fr
%global tl_revision 76790

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.5
Release:	%{tl_revision}.1
Summary:	French translation of classical BibTeX styles
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/biblio/bibtex/contrib/bib-fr
License:	lppl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/bib-fr.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/bib-fr.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
These files are French translations of the classical BibTeX style files.
The translations can easily be modified by simply redefining FUNCTIONs
named fr.*, at the beginning (lines 50-150) of each file.

