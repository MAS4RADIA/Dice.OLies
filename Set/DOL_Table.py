import gi
gi.require_version ("Gtk", "4.0")
from gi.repository import Gtk
from random import random
import math

random_hand = list ()
def lone_in (container = None, element = None):
    if container is None or element is None:
        return (False)

    try:
        child = container.get_first_child ()
    except:
        return (False)

    while child is not None:
        if type (child) is type (element):
            try:
                if child.get_label () == element.get_label ():
                    return (False)
                else:
                    return (True)
            except:
                return (False)
        child = child.get_next_sibling ()
    return (True)

def start_rolling (rolling, players, table):
    if type (players) is not int:
        return

    random_hand.clear ()
    for player in range (players):
        cup = list ()
        for die in range (6):
            play = math.ceil (random () * 6)
            cup.append (play)
        random_hand.append (cup)
    first = math.floor (random () * players)
    seat = table.get_first_child ()

    stool = 0
    while seat is not None:
        if type (seat) is not Gtk.Box:
            seat = seat.get_next_sibling ()
            continue

        button = Gtk.Button (label = "Show")
        if stool == first and lone_in (seat, button):
           button.connect ("clicked", show_hand, table)
           seat.append (button)
        if stool != first and lone_in (seat, button) is False:
           child = seat.get_first_child ()
           while child is not None:
               if type (child) is type (button):
                   seat.remove (child)
               child = child.get_next_sibling ()
           child = None
        seat = seat.get_next_sibling ()
        stool += 1

def next_player (previous):
    print (previous.get_parent ())

def show_hand (button, table):
    if len (random_hand) == 0:
        return

    seat = table.get_first_child ()
    point = 0
    while seat is not None:
        if type (seat) is not Gtk.Box:
            seat = seat.get_next_sibling ()
            continue
        if button.get_parent () is seat:
            child = seat.get_first_child ()
            cupped = 0
            while child is not None:
                if child.get_name () == "bidding":
                    bid = child.get_first_child ()
                    while bid is not None:
                        if type (bid) is not Gtk.Entry:
                            bid = bid.get_next_sibling ()
                            continue
                        if bid.get_text_length () < 1:
                            return
                        bid = bid.get_next_sibling ()

                    bid = child.get_first_child ()
                    while bid is not None:
                        if type (bid) is not Gtk.Entry:
                            bid = bid.get_next_sibling ()
                            continue
                        raw = bid.get_buffer ()
                        number = raw.get_text ()
                        label = Gtk.Label (label = number)
                        child.append (label)

                        husk = bid
                        bid = bid.get_next_sibling ()
                        if husk is not None:
                            child.remove (husk)
                if child.get_name () != "cup":
                    child = child.get_next_sibling ()
                    continue

                face = child.get_first_child ()
                while face is not None:
                    if type (face) is not Gtk.Label:
                        face = face.get_next_sibling ()
                        continue
                    if button.get_name () == "bid":
                        face.set_label ("?")
                    else:
                        face.set_label (str (random_hand [point][cupped]))
                    face = face.get_next_sibling ()
                    cupped += 1
                child = child.get_next_sibling ()

            if button.get_name () == "bid":
                next_player (seat)
                seat.remove (button)
            else:
                button.set_name ("bid")
                button.set_label ("Bid")
                bid = Gtk.Box (orientation = "horizontal")
                bid.set_name ("bidding")
                number = Gtk.Entry ()
                faces = Gtk.Entry ()
                number.set_placeholder_text ("Numbers")
                faces.set_placeholder_text ("Faces")

                bid.append (number)
                bid.append (faces)
                seat.prepend (bid)
        seat = seat.get_next_sibling ()
        point += 1

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
        seat = Gtk.Box (orientation = "vertical", spacing = 5)
        cup = Gtk.Box (orientation = "horizontal")
        cup.set_name ("cup")
        for slot in range (5):
            empty = Gtk.Label (label = "?")
            cup.append (empty)
        seat.append (cup)

        table.attach (seat, 0, 0, 1, 1)
        seat.set_halign (position [player]["x"])
        seat.set_valign (position [player]["y"])

    roller.connect ("clicked", start_rolling, players, table)
    roller.set_halign (Gtk.Align.CENTER)
    roller.set_valign (Gtk.Align.CENTER)

    sign.set_child (table)