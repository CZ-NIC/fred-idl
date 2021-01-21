#!/usr/bin/python3
# -*- coding: utf-8 -*-
#
# Copyright (C) 2018-2019  CZ.NIC, z. s. p. o.
#
# This file is part of FRED.
#
# FRED is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# FRED is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with FRED.  If not, see <https://www.gnu.org/licenses/>.

"""Setup script for fred-idl."""
import subprocess
from distutils.command.build import build
from distutils.command.sdist import sdist
from glob import glob

from setuptools import Command, setup, find_packages
from setuptools.command.build_py import build_py


class BuildIdl(Command):
    """Command to generate python modules from IDL files."""

    user_options = [
        ('build-lib=', 'd', 'directory to "build" (copy) to'),
    ]

    def initialize_options(self):
        self.build_lib = None
        self.output_path = '.'
        self.idl_files = ''
        self.modules = ''

    def finalize_options(self):
        self.set_undefined_options('build', ('build_lib', 'build_lib'))

    def run(self):
        args = ['omniidl', '-bpython', '-Wbmodules=' + self.modules, '-Wbstubs=' + self.modules + '._stubs'
                ] + glob(self.idl_files)

        # Running omniidl
        self.execute(subprocess.check_call, [args], 'running omniidl')


class CustomBuildPy(build_py):
    """Custom build_py command which collects compiled idl packages."""

    def initialize_options(self):
        super().initialize_options()
        self.idl_modules = None

    def finalize_options(self):
        super().finalize_options()
        self.set_undefined_options('build_idl', ('modules', 'idl_modules'))

    def collect_idl_packages(self):
        for package in find_packages(self.idl_modules):
            package = self.idl_modules + '.' + package
            if package not in self.packages:
                self.packages.append(package)

    def find_all_modules(self):
        self.collect_idl_packages()
        return super().find_all_modules()

    def run(self):
        self.collect_idl_packages()
        super().run()


class CustomBuild(build):
    sub_commands = [('build_idl', None)] + build.sub_commands


class CustomSdist(sdist):
    sub_commands = [('build_idl', None)] + sdist.sub_commands


setup(
    author='Vlastimil Zíma',
    cmdclass={
        'sdist': CustomSdist,
        'build': CustomBuild,
        'build_idl': BuildIdl,
        'build_py': CustomBuildPy,
    },
)
