
import pygtk
pygtk.require("2.0")
import gtk

def setup_menu():
    None

def setup_main_win(win):
    win.set_title("The Calculator")
    win.set_position(gtk.WIN_POS_CENTER)
    win.connect("delete_event", lambda w,e: gtk.main_quit())
    win.set_size_request(600 ,400)
def hello(e=None):
    print "Hello"
def gui_show():
    main_window = gtk.Window()
    setup_main_win(main_window)
###############
    menu_open = gtk.Menu()
    items=["open1","open2","open3"]
    for i in items:
        menu_items = gtk.MenuItem(i)
        menu_open.append(menu_items)
        menu_items.show()
        menu_items.set_size_request(95,25)
        menu_items.connect("activate", hello)

    root_menu = gtk.MenuItem("OOPPEENN")
    root_menu.show()
    root_menu.set_submenu(menu_open)


    menu_bar = gtk.MenuBar()

    menu_bar.show()
    menu_bar.append(root_menu)
    fixed = gtk.Fixed()
    fixed.put(menu_bar,0,0)

    main_window.add(fixed)
    fixed.show()
#############
    main_window.show_all()
    gtk.main()

gui_show()
