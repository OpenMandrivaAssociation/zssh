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



%changelog
* Mon Sep 21 2009 Thierry Vignaud <tvignaud@mandriva.com> 1.5c-7mdv2010.0
+ Revision: 446353
- rebuild

* Tue Mar 03 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.5c-6mdv2009.1
+ Revision: 347883
- rebuild for latest readline

* Mon Aug 04 2008 Thierry Vignaud <tvignaud@mandriva.com> 1.5c-5mdv2009.0
+ Revision: 263229
- rebuild

* Mon Aug 04 2008 Thierry Vignaud <tvignaud@mandriva.com> 1.5c-4mdv2009.0
+ Revision: 262912
- rebuild

* Fri Dec 21 2007 Olivier Blin <oblin@mandriva.com> 1.5c-2mdv2008.1
+ Revision: 136634
- restore BuildRoot

  + Thierry Vignaud <tvignaud@mandriva.com>
    - kill re-definition of %%buildroot on Pixel's request


* Sun Aug 13 2006 Luca Berra <bluca@comedia.it>
+ 08/13/06 06:10:06 (55788)
rebuild

* Sun Aug 13 2006 Luca Berra <bluca@comedia.it>
+ 08/13/06 05:49:18 (55784)
import zssh-1.5c-1mdk

* Thu Jun 02 2005 Sebastien Savarin <plouf@mandriva.org> 1.5c-1mdk
- New release 1.5c

* Thu Jan 20 2005 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 1.5a-8mdk
- rebuild for new readline
- fix summary-ended-with-dot
- cosmetics

* Sun Feb 15 2004 Luca Berra <bluca@vodka.it> 1.5a-7mdk
- fix detection of /dev/ptmx
- remove configure patch, we run autoconf

* Tue Nov 25 2003 Marcel Pol <mpol@mandrake.org> 1.5a-6mdk
- buildrequires

