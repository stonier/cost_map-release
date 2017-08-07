Name:           ros-indigo-cost-map-visualisations
Version:        0.3.2
Release:        0%{?dist}
Summary:        ROS cost_map_visualisations package

Group:          Development/Libraries
License:        BSD
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-indigo-cost-map-core
Requires:       ros-indigo-cost-map-msgs
Requires:       ros-indigo-cost-map-ros
Requires:       ros-indigo-ecl-build
Requires:       ros-indigo-ecl-command-line
Requires:       ros-indigo-ecl-console
Requires:       ros-indigo-nav-msgs
Requires:       ros-indigo-roscpp
BuildRequires:  ros-indigo-catkin
BuildRequires:  ros-indigo-cost-map-core
BuildRequires:  ros-indigo-cost-map-msgs
BuildRequires:  ros-indigo-cost-map-ros
BuildRequires:  ros-indigo-ecl-build
BuildRequires:  ros-indigo-ecl-command-line
BuildRequires:  ros-indigo-ecl-console
BuildRequires:  ros-indigo-nav-msgs
BuildRequires:  ros-indigo-roscpp

%description
Visualisation tools for cost maps.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/indigo" \
        -DCMAKE_PREFIX_PATH="/opt/ros/indigo" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/indigo

%changelog
* Mon Aug 07 2017 Daniel Stonier <stonier@yujinrobot.com> - 0.3.2-0
- Autogenerated by Bloom

* Thu Feb 16 2017 Daniel Stonier <stonier@yujinrobot.com> - 0.3.1-0
- Autogenerated by Bloom

* Tue Dec 27 2016 Daniel Stonier <stonier@yujinrobot.com> - 0.3.0-0
- Autogenerated by Bloom

