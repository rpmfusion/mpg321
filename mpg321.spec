Name:           mpg321
Version:        0.2.10.4
Release:        3%{?dist}
Summary:        Command line MPEG audio player

Group:          Applications/Multimedia
License:        GPLv2+
URL:            http://mpg321.sourceforge.net/
Source0:        http://ftp.debian.org/debian/pool/main/m/mpg321/%{name}_%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires:  libao-devel
BuildRequires:  libmad-devel
BuildRequires:  libid3tag-devel
BuildRequires:  zlib-devel
Requires(post): /usr/sbin/update-alternatives
Requires(postun): /usr/sbin/update-alternatives
Provides:       mp3-cmdline
Obsoletes:      mpg123

%description
mpg321 is a replacement for mpg123, a very popular command-line
mp3 player. mpg123 is used for frontends, as an mp3 player and as an
mp3 to wave file decoder (primarily for use with CD-recording
software.) In all of these capacities, mpg321 can be used as a drop-in
replacement for mpg123.


%prep
%setup -q 


%build
%configure --with-default-audio=alsa09
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT
ln -s mpg321.1 $RPM_BUILD_ROOT%{_mandir}/man1/mpg123.1


%clean
rm -rf $RPM_BUILD_ROOT


%post
/usr/sbin/update-alternatives --install %{_bindir}/mp3-cmdline \
    mp3-cmdline %{_bindir}/mpg321 40

%postun
if [ $1 -eq 0 ] ; then
    /usr/sbin/update-alternatives --remove mp3-cmdline %{_bindir}/mpg321
fi


%files 
%defattr(-,root,root,-)
%doc AUTHORS BUGS ChangeLog COPYING HACKING NEWS README* THANKS TODO
%{_bindir}/mpg321
%{_bindir}/mpg123
%{_mandir}/man1/mpg321.1*
%{_mandir}/man1/mpg123.1*


%changelog
* Sun Mar 29 2009 Thorsten Leemhuis <fedora [AT] leemhuis [DOT] info> - 0.2.10.4-3
- rebuild for new F11 features

* Sun Sep 14 2008 Thorsten Leemhuis <fedora [AT] leemhuis [DOT] info - 0.2.10.4-2
- rebuild

* Sat Oct 13 2007 Adrian Reber <adrian@lisas.de> - 0.2.10.4-1
- updated to debian's 0.2.10.4
- updated License
- adapted %%description, to make it not sound like mpg123 is non-free
- rebuilt for rpmfusion

* Fri Oct 06 2006 Thorsten Leemhuis <fedora [AT] leemhuis [DOT] info> 0.2.10.3-3
 - rebuilt for unwind info generation, broken in gcc-4.1.1-21

* Wed Sep 20 2006 Ville Skyttä <ville.skytta at iki.fi> - 0.2.10.3-2
- Avoid broken Requires(foo,bar) syntax.
- Specfile cleanups.
- Improve summary.

* Thu Mar 09 2006 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
- switch to new release field
- drop Epoch

* Tue Feb 28 2006 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
- add dist

* Fri Jan  9 2004 Ville Skyttä <ville.skytta at iki.fi> - 0:0.2.10.3-0.lvn.1
- Update to 0.2.10.3 (from Debian), fixes CAN-2003-0969.
- Make alsa09 the default output device.
- Install mpg123 manpage symlink.

* Sun Apr 20 2003 Ville Skyttä <ville.skytta at iki.fi> - 0:0.2.10.1-0.fdr.1
- Update to 0.2.10.1 (from Debian).
- Rebuild using reorganized libmad.
- Provide mp3-cmdline virtual package and alternative.
- Save .spec in UTF-8.

* Fri Apr  4 2003 Ville Skyttä <ville.skytta at iki.fi> - 0:0.2.10-0.fdr.1
- Update to current Fedora guidelines.

* Thu Feb 20 2003 Ville Skyttä <ville.skytta at iki.fi> - 0.2.10-1.fedora.1
- First Fedora release, based on Matthias Saou's work.
- Added zlib-devel build requirement.

* Mon Sep 30 2002 Matthias Saou <matthias.saou@est.une.marmotte.net>
- Update to 0.2.10.
- Spec file cleanup.

* Tue Apr  9 2002 Bill Nottingham <notting@redhat.com> 0.2.9-3
- add patch from author to fix id3 segfaults (#62714)
- fix audio device fallback to match upstream behavior

* Thu Mar 14 2002 Bill Nottingham <notting@redhat.com> 0.2.9-2
- fix possible format string exploit
- add simple audio device fallback

* Tue Mar 12 2002 Bill Nottingham <notting@redhat.com> 0.2.9-1
- update to 0.2.9

* Thu Feb 21 2002 Bill Nottingham <notting@redhat.com>
- rebuild

* Mon Jan 28 2002 Bill Nottingham <notting@redhat.com>
- update to 0.2.3, libmad is now separate

* Mon Aug 13 2001 Bill Nottingham <notting@redhat.com>
- update to 0.1.5
- fix build with new libao

* Fri Jul 20 2001 Bill Nottingham <notting@redhat.com>
- initial build
