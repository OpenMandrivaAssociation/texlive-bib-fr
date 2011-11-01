Name:		texlive-bib-fr
Version:	1.5
Release:	1
Summary:	French translation of classical BibTeX styles
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/biblio/bibtex/contrib/bib-fr
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/bib-fr.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/bib-fr.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
These files are French translations of the classical BibTeX
style files. The translations can easily be modified by simply
redefining FUNCTIONs named fr.*, at the beginning (lines 50-
150) of each file.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    %_texmf_mktexlsr_preun

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mltexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/bibtex/bst/bib-fr/abbrv-fr.bst
%{_texmfdistdir}/bibtex/bst/bib-fr/abbrvnat-fr.bst
%{_texmfdistdir}/bibtex/bst/bib-fr/alpha-fr.bst
%{_texmfdistdir}/bibtex/bst/bib-fr/apalike-fr.bst
%{_texmfdistdir}/bibtex/bst/bib-fr/ieeetr-fr.bst
%{_texmfdistdir}/bibtex/bst/bib-fr/plain-fr.bst
%{_texmfdistdir}/bibtex/bst/bib-fr/plainnat-fr.bst
%{_texmfdistdir}/bibtex/bst/bib-fr/siam-fr.bst
%{_texmfdistdir}/bibtex/bst/bib-fr/unsrt-fr.bst
%{_texmfdistdir}/bibtex/bst/bib-fr/unsrtnat-fr.bst
%doc %{_texmfdistdir}/doc/bibtex/bib-fr/CHANGELOG
%doc %{_texmfdistdir}/doc/bibtex/bib-fr/README

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar bibtex doc %{buildroot}%{_texmfdistdir}
