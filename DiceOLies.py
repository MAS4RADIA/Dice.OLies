#!/usr/bin/python3

import gi
gi.require_version ("Gtk", "4.0")
from gi.repository import Gtk
import Set.DOL_Home as DOL_set

dice_o_lies = Gtk.Application (application_id = "mas4.dice.olies")
dice_o_lies.connect ("activate", DOL_set.home)
dice_o_lies.run ()