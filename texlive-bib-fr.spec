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
Requires(pre):	texlive-tlpkg
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
These files are French translations of the classical BibTeX style files.
The translations can easily be modified by simply redefining FUNCTIONs
named fr.*, at the beginning (lines 50-150) of each file.

%prep
%setup -q -c -a1
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
%dir %{_datadir}/texmf-dist/bibtex
%dir %{_datadir}/texmf-dist/doc
%dir %{_datadir}/texmf-dist/bibtex/bst
%dir %{_datadir}/texmf-dist/doc/bibtex
%dir %{_datadir}/texmf-dist/bibtex/bst/bib-fr
%dir %{_datadir}/texmf-dist/doc/bibtex/bib-fr
%{_datadir}/texmf-dist/bibtex/bst/bib-fr/abbrv-fr.bst
%{_datadir}/texmf-dist/bibtex/bst/bib-fr/abbrvnat-fr.bst
%{_datadir}/texmf-dist/bibtex/bst/bib-fr/alpha-fr.bst
%{_datadir}/texmf-dist/bibtex/bst/bib-fr/apalike-fr.bst
%{_datadir}/texmf-dist/bibtex/bst/bib-fr/ieeetr-fr.bst
%{_datadir}/texmf-dist/bibtex/bst/bib-fr/plain-fr.bst
%{_datadir}/texmf-dist/bibtex/bst/bib-fr/plainnat-fr.bst
%{_datadir}/texmf-dist/bibtex/bst/bib-fr/siam-fr.bst
%{_datadir}/texmf-dist/bibtex/bst/bib-fr/unsrt-fr.bst
%{_datadir}/texmf-dist/bibtex/bst/bib-fr/unsrtnat-fr.bst
%doc %{_datadir}/texmf-dist/doc/bibtex/bib-fr/CHANGELOG
%doc %{_datadir}/texmf-dist/doc/bibtex/bib-fr/README
