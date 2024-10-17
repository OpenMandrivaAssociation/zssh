# empty debug
%define debug_package	%{nil}

Summary:	Interactive file transfers through ssh
Name:		zssh 
Version:	1.5c
Release:	9
License:	GPL
Group:		Networking/File transfer
Requires:	lrzsz
Url:		https://zssh.sourceforge.net
Source0:	http://prdownloads.sf.net/zssh/%{name}-%{version}.tgz
Patch0:		zssh-1.5a-install.patch
Patch1:		zssh-1.5a-ptmx.patch
BuildRequires:	readline-devel 
BuildRequires:	termcap-devel

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
%makeinstall

%files
%defattr(644,root,root,755)
%doc CHANGES FAQ INSTALL README VERSION
%attr(0755,root,root) %{_bindir}/zssh
%attr(0755,root,root) %{_bindir}/ztelnet
%{_mandir}/man1/zssh.1*
%{_mandir}/man1/ztelnet.1*
