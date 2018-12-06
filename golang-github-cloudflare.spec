%global goipath github.com/cloudflare/cloudflare-go
Version:        0.8.5
%gometa

Name:           %{goname}
Release:        1%{?dist}
Summary:        A Go library for interacting with Cloudflare's API v4
License:        BSD
URL:            %{gourl}
Source0:        %{gosource}
# https://github.com/cloudflare/cloudflare-go/pull/231
Patch0:         Rename-TestClient_Auth-to-TestClient_IPs-and-mock-properly.patch

BuildRequires:  golang(github.com/codegangsta/cli)
BuildRequires:  golang(github.com/olekukonko/tablewriter)
BuildRequires:  golang(github.com/pkg/errors)
BuildRequires:  golang(github.com/stretchr/testify/assert)
BuildRequires:  golang(golang.org/x/time/rate)


%description
%{summary}.


%package devel
Summary:        %{summary}
BuildArch:      noarch


%description devel
%{summary}.

This package contains the source code needed for building packages that import
the %{goipath} Go namespace.


%package -n flarectl
Summary:        A CLI application for interacting with a Cloudflare account


%description -n flarectl
%{summary}.


%prep
%forgeautosetup -p 1
rm -rf vendor


%build
%gobuildroot
%gobuild -o _bin/flarectl %{goipath}/cmd/flarectl


%install
%goinstall -t cmd
install -D -p -m 0755 _bin/flarectl %{buildroot}%{_bindir}/flarectl


%check
%gochecks


%files devel -f devel.file-list
%license LICENSE
%doc README.md


%files -n flarectl
%license LICENSE
%doc cmd/flarectl/README.md
%{_bindir}/flarectl


%changelog
* Tue Nov 13 2018 Carl George <carl@george.computer> - 0.8.5-1
- Initial package
