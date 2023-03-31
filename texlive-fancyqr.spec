Name:		texlive-fancyqr
Version:	64182
Release:	2
Summary:	Fancy QR-Codes with TikZ
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/fancyqr
License:	gpl3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/fancyqr.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/fancyqr.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
A simple package to create fancy QR-codes with the help of the
qrcode package.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/fancyqr
%doc %{_texmfdistdir}/doc/latex/fancyqr

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
