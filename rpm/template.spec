Name:           ros-kinetic-cost-map-core
Version:        0.3.2
Release:        0%{?dist}
Summary:        ROS cost_map_core package

Group:          Development/Libraries
License:        BSD
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-kinetic-ecl-build
Requires:       ros-kinetic-ecl-console
Requires:       ros-kinetic-ecl-eigen
Requires:       ros-kinetic-grid-map-core
BuildRequires:  ros-kinetic-catkin
BuildRequires:  ros-kinetic-ecl-build
BuildRequires:  ros-kinetic-ecl-console
BuildRequires:  ros-kinetic-ecl-eigen
BuildRequires:  ros-kinetic-grid-map-core

%description
Cost maps, following the style of ethz-asl's grid_map library.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/kinetic/setup.sh" ]; then . "/opt/ros/kinetic/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/kinetic" \
        -DCMAKE_PREFIX_PATH="/opt/ros/kinetic" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/kinetic/setup.sh" ]; then . "/opt/ros/kinetic/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/kinetic

%changelog
* Sun Aug 06 2017 Daniel Stonier <stonier@yujinrobot.com> - 0.3.2-0
- Autogenerated by Bloom

* Thu Feb 16 2017 Daniel Stonier <stonier@yujinrobot.com> - 0.3.1-0
- Autogenerated by Bloom

* Thu Jan 26 2017 Daniel Stonier <stonier@yujinrobot.com> - 0.3.0-0
- Autogenerated by Bloom

