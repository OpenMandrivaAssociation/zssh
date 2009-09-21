%define	name	zssh 
%define	version	1.5c
%define	release	%mkrel 7

Summary:	Interactive file transfers through ssh
Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	GPL
Group:		Networking/File transfer
Requires:	lrzsz
Url:		http://zssh.sourceforge.net/		
Source0:	%{name}-%{version}.tar.bz2
Patch0:		zssh-1.5a-install.patch
Patch1:		zssh-1.5a-ptmx.patch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	readline-devel termcap-devel

%description
zssh (Zmodem SSH) is a program for interactively transferring files to/from
a remote machine while using the secure shell (ssh). It is intended to be a
convenient alternative to scp, allowing to transfer files without having to
open another  session and re-authenticate  oneself. zssh is  an interactive
wrapper for ssh used to switch  the ssh connection between the remote shell
and  file transfers.  Files are  transferred through  the  zmodem protocol,
using the rz and sz commands.

%prep
%setup -q
%patch0 -p1 -b .install
%patch1 -p1 -b .ptmx

%build
%__autoconf
%configure
%make

%install
rm -rf $RPM_BUILD_ROOT
%{makeinstall}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES FAQ INSTALL README VERSION
%attr(0755,root,root) %{_bindir}/zssh
%attr(0755,root,root) %{_bindir}/ztelnet
%{_mandir}/man1/zssh.1*
%{_mandir}/man1/ztelnet.1*

