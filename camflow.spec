Summary: Install all CamFlow dependencies.
Name: camflow
Version: 0.3.4
Release: 1
Group: audit/camflow
License: GPLv3
Source: %{expand:%%(pwd)}
BuildRoot: %{_topdir}/BUILD/%{name}-%{version}-%{release}
Requires: camflowd = 0.1.3
Requires: camconfd = 0.3.2
Requires: camflow-cli = 0.1.4
Requires: libprovenance = 0.3.4
Requires: kernel = 4.12.4camflow_0.3.4
Requires: kernel-headers = 4.12.4camflow_0.3.4
Requires: kernel-devel = 4.12.4camflow_0.3.4

%description
%{summary}

%prep

%clean
rm -r -f "$RPM_BUILD_ROOT"

%files
