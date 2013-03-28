#!/usr/bin/python
# Copyright 2013, Big Switch Networks, Inc.
#
# LoxiGen is licensed under the Eclipse Public License, version 1.0 (EPL), with
# the following special exception:
#
# LOXI Exception
#
# As a special exception to the terms of the EPL, you may distribute libraries
# generated by LoxiGen (LoxiGen Libraries) under the terms of your choice, provided
# that copyright and licensing notices generated by LoxiGen are not altered or removed
# from the LoxiGen Libraries and the notice provided below is (i) included in
# the LoxiGen Libraries, if distributed in source code form and (ii) included in any
# documentation for the LoxiGen Libraries, if distributed in binary form.
#
# Notice: "Copyright 2013, Big Switch Networks, Inc. This library was generated by the LoxiGen Compiler."
#
# You may not use this file except in compliance with the EPL or LOXI Exception. You may obtain
# a copy of the EPL at:
#
# http://www.eclipse.org/legal/epl-v10.html
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# EPL for the specific language governing permissions and limitations
# under the EPL.

#
# Some test code for of_h_utils.py
#

import sys
sys.path.append("..")
sys.path.append("../loxi_front_end")
sys.path.append("../loxi_utils")

from of_h_utils import *

for filename, version in [
    ('../canonical/openflow.h-1.0', 1),
    ('../canonical/openflow.h-1.1', 2),
    ('../canonical/openflow.h-1.2', 3),
    ('../canonical/openflow.h-1.3', 4)]:

    f = open(filename, 'r')
    all_lines = f.readlines()
    contents = " ".join(all_lines)

    enum_dict = get_enum_dict(version, contents)
    print "Got %d LOXI entries %s" % (len(enum_dict), filename)
    for name, entry in enum_dict.items():
        print "Enum %s:\n  ofp_name: %s.\n  ofp_group: %s.\n  value: %s" % (
            name, entry.ofp_name, entry.ofp_group, str(entry.value))