%global tl_name kanaparser
%global tl_revision 48052

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.0
Release:	%{tl_revision}.1
Summary:	Kana parser for LuaTeX
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/luatex/generic/kanaparser
License:	bsd
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/kanaparser.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/kanaparser.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package provides a kana parser for LuaTeX. It is a set of 4 macros
that handle transliteration of text: from hiragana and katakana to Latin
from Latin and katakana to hiragana from Latin and hiragana to katakana
It can be used to write kana directly using only the ASCII character set
or for education purposes. The package has support for obsolete and
rarely used syllables, some only accessible via the provided toggle
macro.

