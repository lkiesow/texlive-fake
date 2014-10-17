Name:     texlive-fake
Version:  1
Release:  6%{?dist}
Summary:  Fakes the installation of the texlive packages
Epoch:    99
License:  BSD

BuildArch: noarch

Provides: dvipng
Provides: tetex-dvipost
Provides: tetex-latex
Provides: tetex-xdvi
Provides: tex(dvips)
Provides: tex(latex)
Provides: tex(tex)
Provides: tex(url.sty)
Provides: xdvi


%description
Fakes the installation of the texlive packages.
Useful if you have installed texlive from ctan.

%prep

%build


%install


%files

%changelog
* Fri Oct 17 2014 Lars Kiesow <lkiesow@uos.de> - 1-6
- Added further provides

* Fri Jul 19 2013 Lars Kiesow <lkiesow@uos.de> - 1-1
- Initial build

