Name:           oopr
Version:        0.1.0
Release:        1%{?dist}
Summary:        Text paginator formatting files into columns, headers, and form-feed pages.
License:        ASL 2.0
URL:            https://github.com/openOODA-tools/oopr
Source0:        oopr-linux-x86_64
Source1:        uninstall.sh
BuildArch:      x86_64
Requires:       glibc

%description
oopr is a sovereign, capability-bounded PAGINATED PRINT written
in pure openOODA, featuring zero ambient authority, oote color themes,
and an MCP stdio server.

%install
mkdir -p %{buildroot}/usr/bin
install -m 0755 %{SOURCE0} %{buildroot}/usr/bin/oopr
install -m 0755 %{SOURCE1} %{buildroot}/usr/bin/oopr-uninstall

%files
/usr/bin/oopr
/usr/bin/oopr-uninstall

%changelog
* Wed Oct 07 2026 openOODA-tools <ops@openooda.org> - 0.1.0-1
- Initial sovereign blueprint scaffolding
