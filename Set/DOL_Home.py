import gi
gi.require_version ("Gtk", "4.0")
from gi.repository import Gtk
from Set.DOL_Table import set_table_for

def check_players (button, entry, sign):
    buffer = entry.get_buffer ()
    text = buffer.get_text ()
    try:
        players = int (text)
    except:
        return
    set_table_for (players, sign)

def player_numbers (mode, sign):
    floor = Gtk.Box (orientation = "vertical", spacing = 5)
    player = Gtk.Box (orientation = "horizontal", spacing = 5)

    text = Gtk.Label (label = "Players")
    number = Gtk.Entry ()
    default_value = Gtk.EntryBuffer ()
    default_value.set_text ("2", -1)
    number.set_buffer (default_value)

    okay = Gtk.Button (label = "Play")
    okay.connect ("clicked", check_players, number, sign)

    floor.set_homogeneous (True)
    player.set_valign (Gtk.Align.END)
    player.set_halign (Gtk.Align.CENTER)
    okay.set_halign (Gtk.Align.CENTER)
    okay.set_valign (Gtk.Align.END)

    player.append (text)
    player.append (number)

    floor.append (player)
    floor.append (okay)
    sign.set_child (floor)

def select_table_mode (sign):
    mode = Gtk.Box (orientation = "vertical", spacing = 5)
    same_device = Gtk.Button (label = "Same device")
    linked = Gtk.Button (label = "LAN/Online")

    same_device.set_name ("network")
    linked.set_name ("network")

    mode.set_homogeneous (True)
    same_device.set_valign (Gtk.Align.START)
    same_device.set_halign (Gtk.Align.CENTER)
    linked.set_halign (Gtk.Align.CENTER)
    linked.set_valign (Gtk.Align.START)

    same_device.connect ("clicked", navigate, sign)
    linked.connect ("clicked", navigate, sign)

    mode.append (same_device)
    mode.append (linked)
    sign.set_child (mode)

def player_role (sign):
    mode = Gtk.Box (orientation = "vertical", spacing = 5)
    host = Gtk.Button (label = "Host")
    guest = Gtk.Button (label = "Join")

    host.set_name ("status")
    guest.set_name ("status")

    mode.set_homogeneous (True)
    host.set_valign (Gtk.Align.END)
    host.set_halign (Gtk.Align.CENTER)
    guest.set_halign (Gtk.Align.CENTER)
    guest.set_valign (Gtk.Align.START)

    host.connect ("clicked", navigate, sign)
    guest.connect ("clicked", navigate, sign)

    mode.append (host)
    mode.append (guest)
    sign.set_child (mode)

def host_panel (sign):
    floor = Gtk.Box (orientation = "vertical", spacing = 5)
    address = Gtk.Box (orientation = "horizontal", spacing = 5)
    player = Gtk.Box (orientation = "horizontal", spacing = 5)
    okay = Gtk.Button (label = "Play")

    ip = Gtk.Entry (placeholder_text = "IP Address")
    port = Gtk.Entry (placeholder_text = "Port")
    address.append (ip)
    address.append (port)

    text = Gtk.Label (label = "Players")
    number = Gtk.Label (label = "1")
    player.append (text)
    player.append (number)

    floor.set_homogeneous (True)
    address.set_valign (Gtk.Align.END)
    address.set_halign (Gtk.Align.CENTER)
    player.set_valign (Gtk.Align.CENTER)
    player.set_halign (Gtk.Align.CENTER)
    okay.set_halign (Gtk.Align.CENTER)
    okay.set_valign (Gtk.Align.END)

    floor.append (address)
    floor.append (player)
    floor.append (okay)
    sign.set_child (floor)

def guest_panel (sign):
    floor = Gtk.Box (orientation = "vertical", spacing = 5)
    address = Gtk.Box (orientation = "horizontal", spacing = 5)
    okay = Gtk.Button (label = "Join")

    ip = Gtk.Entry (placeholder_text = "IP Address")
    port = Gtk.Entry (placeholder_text = "Port")
    address.append (ip)
    address.append (port)

    floor.set_homogeneous (True)
    address.set_valign (Gtk.Align.END)
    address.set_halign (Gtk.Align.CENTER)
    okay.set_halign (Gtk.Align.CENTER)
    okay.set_valign (Gtk.Align.END)

    floor.append (address)
    floor.append (okay)
    sign.set_child (floor)

def navigate (to, sign):
    link = to.get_name ()
    content = to.get_label ()
    content = content.lower ()

    match link:
        case "mode":
            if content.find ("single") > -1:
                player_numbers (content, sign)
            elif content.find ("multi") > -1:
                select_table_mode (sign)
        case "network":
            if content.find ("same device") > -1:
                player_numbers (content, sign)
            elif content.find ("LAN") > -1 or content.find ("online"):
                player_role (sign)
        case "status":
            if content.find ("host") > -1:
                host_panel (sign)
            elif content.find ("join") > -1:
                guest_panel (sign)
        case _:
            print ("Unknown link", link)

def go_back (button, sign):
    print (sign.get_title ())

def home (dice_o_lies):
    sign = Gtk.ApplicationWindow (application = dice_o_lies)
    sign.set_default_size (400, 500)
    sign.set_title ("Dice O\'Lies")

    mode = Gtk.Box (orientation = "vertical", spacing = 5)
    single = Gtk.Button (label = "Single player")
    multi = Gtk.Button (label = "Multiplayer")

    mode.set_homogeneous (True)
    single.set_name ("mode")
    multi.set_name ("mode")

    single.set_valign (Gtk.Align.END)
    single.set_halign (Gtk.Align.CENTER)
    multi.set_valign (Gtk.Align.START)
    multi.set_halign (Gtk.Align.CENTER)

    single.connect ("clicked", navigate, sign)
    multi.connect ("clicked", navigate, sign)

    mode.append (single)
    mode.append (multi)

    sign.set_child (mode)
    sign.show ()