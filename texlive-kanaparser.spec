Name:		texlive-kanaparser
Version:	48052
Release:	2
Summary:	Kana parser for LuaTeX
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/kanaparser
License:	bsd
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/kanaparser.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/kanaparser.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package provides a kana parser for LuaTeX. It is a set of 4
macros that handle transliteration of text: from hiragana and
katakana to Latin from Latin and katakana to hiragana from
Latin and hiragana to katakana It can be used to write kana
directly using only the ASCII character set or for education
purposes. The package has support for obsolete and rarely used
syllables, some only accessible via the provided toggle macro.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/luatex/kanaparser
%doc %{_texmfdistdir}/doc/luatex/kanaparser

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
