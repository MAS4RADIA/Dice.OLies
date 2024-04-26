import gi
gi.require_version ("Gtk", "4.0")
from gi.repository import Gtk

def set_table_for (players = 0, sign = None):
    if players < 2 or players > 8 or sign == None:
        return

    table = Gtk.Grid ()
    table.set_column_homogeneous (True)
    table.set_row_homogeneous (True)

    roller = Gtk.Button (label = "Roll")
    table.attach (roller, 0, 0, 1, 1)

    position = list ()
    position.append ({ "x": Gtk.Align.CENTER, "y": Gtk.Align.END })
    position.append ({ "x": Gtk.Align.CENTER, "y": Gtk.Align.START })
    position.append ({ "x": Gtk.Align.START, "y": Gtk.Align.CENTER })
    position.append ({ "x": Gtk.Align.END, "y": Gtk.Align.CENTER })
    position.append ({ "x": Gtk.Align.START, "y": Gtk.Align.START })
    position.append ({ "x": Gtk.Align.END, "y": Gtk.Align.END })
    position.append ({ "x": Gtk.Align.START, "y": Gtk.Align.END })
    position.append ({ "x": Gtk.Align.END, "y": Gtk.Align.START })

    for player in range (players):
        cup = Gtk.Box ()
        for slot in range (5):
            empty = Gtk.Label (label = "?")
            cup.append (empty)
        table.attach (cup, 0, 0, 1, 1)
        cup.set_halign (position [player]["x"])
        cup.set_valign (position [player]["y"])

    roller.set_halign (Gtk.Align.CENTER)
    roller.set_valign (Gtk.Align.CENTER)

    sign.set_child (table)