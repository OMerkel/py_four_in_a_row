#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
modules package for py-four-in-a-row game engines.
"""
import sys
import os

module_dir = os.path.dirname(os.path.abspath(__file__))
if module_dir not in sys.path:  # pragma: no cover
    sys.path.insert(0, module_dir)
