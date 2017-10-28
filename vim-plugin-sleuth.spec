%define		commit	d56a4302358359ddf9845252addf637a5e6bd6d5
%define		plugin	sleuth
Summary:	Vim plugin: Heuristically set buffer options
Name:		vim-plugin-%{plugin}
Version:	0.20171028.1
Release:	1
License:	Vim
Group:		Applications/Editors/Vim
Source0:	https://github.com/tpope/vim-sleuth/archive/%{commit}.zip
# Source0-md5:	aaf96c48053eb67cd80977b84eac06c5
URL:		https://github.com/tpope/vim-sleuth
# for _vimdatadir
Requires:	vim-rt >= 4:7.2.170
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_vimdatadir	%{_datadir}/vim

%description
This plugin automatically adjusts 'shiftwidth' and 'expandtab'
heuristically based on the current file, or, in the case the current
file is new, blank, or otherwise insufficient, by looking at other
files of the same type in the current and parent directories. In lieu
of adjusting 'softtabstop', 'smarttab' is enabled.

%prep
%setup -q -n vim-sleuth-%{commit}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_vimdatadir}
cp -a doc plugin $RPM_BUILD_ROOT%{_vimdatadir}

%clean
rm -rf $RPM_BUILD_ROOT

# if packaging doc/* files
%post
echo 'helptags %{_vimdatadir}/doc' | vim -e -s -V0 -R -n --noplugin

%postun
echo 'helptags %{_vimdatadir}/doc' | vim -e -s -V0 -R -n --noplugin

%files
%defattr(644,root,root,755)
%doc %{_vimdatadir}/doc/sleuth.txt
%{_vimdatadir}/plugin/sleuth.vim
