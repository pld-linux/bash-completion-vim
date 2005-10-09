Summary:	bash-completion for vim
Name:		bash-completion-vim
Version:	0.20051009
Release:	0.2
License:	GPL
Group:		Applications/Shells
Source0:	ftp://ftp.linux.ee/pub/gentoo/portage/app-editors/vim/files/vim-completion
# Source0-md5:	87fe7821e180647f3bf48ed099a22b83
Patch0:		vim-completion-vi.patch
BuildArch:	noarch
Requires:	bash-completion
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sysconfdir /etc/bash_completion.d

%description
bash-completion for vim.

%prep
%setup -q -T -c
cp %{SOURCE0} .
%patch0 -p1

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_sysconfdir}
install vim-completion $RPM_BUILD_ROOT%{_sysconfdir}/vim

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_sysconfdir}/*
