#!/usr/bin/env python
#-*- coding: utf-8 -*-
#
# Ailurus - make Linux easier to use
#
# Copyright (C) 2007-2010, Trusted Digital Technology Laboratory, Shanghai Jiao Tong University, China.
# Copyright (C) 2009-2010, Ailurus Developers Team
#
# Ailurus is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# Ailurus is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Ailurus; if not, write to the Free Software Foundation, Inc.,
# 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA

from __future__ import with_statement
import sys, os
import gtk, pango
from lib import *
from libu import *

def __study_linux(main_view):
    study_url_items = [ 
        # (use stock?, stock name or icon path, text, web page url, Chinese only?
#        (True, gtk.STOCK_HELP, _(u'How to use Intel® compiler & math library ?'), 
#         'http://tdt.sjtu.edu.cn/S/how_to/icc_mkl_tbb.html', False),
        (True, gtk.STOCK_HELP, _('How to compile a LaTeX file into pdf file ?'), 
         'http://ailurus.cn/?p=329', False),
        (True, gtk.STOCK_HELP, _('Check Linux device driver'),
         'http://kmuto.jp/debian/hcl/', False),
         ]

    def __get_menu(items):
        ret = []
        for item in items:
            if item == None: 
                ret.append( gtk.SeparatorMenuItem() )
                continue 
            if item[4]==False or (item[4] and Config.is_Chinese_locale()):
                if item[0]: menu_item = image_stock_menuitem(item[1], item[2])
                else: menu_item = image_file_menuitem(item[2], item[1], 16, 3)
                menu_item.url = item[3]
                menu_item.connect('activate', lambda w: open_web_page(w.url))
                ret.append( menu_item )
        return ret
    
    ret = __get_menu(study_url_items)
    study_show_tip = image_file_menuitem(_('Tip of the day'), D+'sora_icons/m_tip_of_the_day.png', 16, 3)
    def show_day_tip(*w):
        from support.tipoftheday import TipOfTheDay
        w=TipOfTheDay()
        w.run()
        w.destroy()
    study_show_tip.connect('activate', show_day_tip)
    ret.insert(0, study_show_tip)
    ret.insert(1, gtk.SeparatorMenuItem() )
    return ret

def __set_wget_options(w): # called by __preferences
    current_timeout = Config.wget_get_timeout()
    current_tries = Config.wget_get_triesnum()
    
    adjustment_timeout = gtk.Adjustment(current_timeout, 1, 60, 1, 1, 0)
    scale_timeout = gtk.HScale(adjustment_timeout)
    scale_timeout.set_digits(0)
    scale_timeout.set_value_pos(gtk.POS_BOTTOM)
    timeout_label = label_left_align(_('How long after the server does not respond, give up downloading? (in seconds)'))
    
    adjustment_tries = gtk.Adjustment(current_tries, 1, 20, 1, 1, 0)
    scale_tries = gtk.HScale(adjustment_tries)
    scale_tries.set_digits(0)
    scale_tries.set_value_pos(gtk.POS_BOTTOM)
    tries_label = label_left_align(_('How many times does Ailurus try to download the same resource?'))
    
    dialog = gtk.Dialog(
        _('Set Ailurus download parameter'), 
        None, gtk.DIALOG_MODAL|gtk.DIALOG_NO_SEPARATOR, 
        (gtk.STOCK_CANCEL, gtk.RESPONSE_CANCEL, gtk.STOCK_OK, gtk.RESPONSE_OK) )
    dialog.set_border_width(5)
#    dialog.set_size_request(500,-1)
    dialog.vbox.pack_start(timeout_label, False)
    dialog.vbox.pack_start(scale_timeout, False)
    dialog.vbox.pack_start(tries_label, False)
    dialog.vbox.pack_start(scale_tries, False)
    dialog.vbox.show_all()
    #display dialog
    ret = dialog.run()
    #get parameter
    new_timeout = int(adjustment_timeout.get_value())
    new_tries = int(adjustment_tries.get_value())
    dialog.destroy()
    #write back
    if ret == gtk.RESPONSE_OK:
        Config.wget_set_timeout(new_timeout)
        Config.wget_set_triesnum(new_tries)
        
def __preferences(main_view):
    menu_query_before_exit = gtk.CheckMenuItem(_('Query before exit'))
    menu_query_before_exit.set_active(Config.get_query_before_exit())
    menu_query_before_exit.connect('toggled', 
            lambda w: Config.set_query_before_exit(w.get_active()))
    menu_hide_quick_setup_pane = gtk.CheckMenuItem(_('Hide "quickly install popular software" button'))
    menu_hide_quick_setup_pane.set_active(Config.get_hide_quick_setup_pane())
    menu_hide_quick_setup_pane.connect('toggled', 
            lambda w: notify(_('Preferences changed'), _('Your changes will take effect at the next time when the program starts up.')) 
                              or Config.set_hide_quick_setup_pane(w.get_active()))
    menu_tooltip = gtk.CheckMenuItem( _("""Don't show "tip of the day" on start up""") )
    menu_tooltip.set_active( Config.get_disable_tip() )
    menu_tooltip.connect('toggled', 
            lambda w: notify(_('Preferences changed'), _('Your changes will take effect at the next time when the program starts up.')) 
                              or Config.set_disable_tip(w.get_active()) )
    
    menu_tip_after_logging_in = gtk.CheckMenuItem( _('Show a random Linux skill after you log in to GNOME') )
    menu_tip_after_logging_in.set_active(ShowALinuxSkill.installed())
    def toggled(w):
        if w.get_active(): ShowALinuxSkill.install()
        else: ShowALinuxSkill.remove()
        notify(_('Preferences changed'), _('Your changes will take effect at the next time when you log in to GNOME.') )
    menu_tip_after_logging_in.connect('toggled', toggled)
    
    menu_set_wget_option = gtk.MenuItem(_("Set download parameters"))
    menu_set_wget_option.connect('activate', __set_wget_options)
    
    return [ menu_hide_quick_setup_pane, menu_query_before_exit, menu_tooltip, menu_tip_after_logging_in, menu_set_wget_option ]

def right_label(text):
    font = pango.FontDescription('Georgia')
    ret = gtk.Label(text)
    ret.modify_font(font)
    ret.modify_fg(gtk.STATE_NORMAL, gtk.gdk.color_parse("#667766"))
    ret.set_alignment(1, 0)
    ret.set_justify(gtk.JUSTIFY_RIGHT)
    return ret

def left_label(text):
    font = pango.FontDescription('Georgia')
    ret = gtk.Label(text)
    ret.modify_font(font)
    ret.set_alignment(0, 0.5)
    ret.set_justify(gtk.JUSTIFY_LEFT)
    ret.set_selectable(True)
    box = gtk.HBox()
    box.pack_start(ret, True, True, 6)
    return box

def url_button(url):
    import gtk
    def func(w, url): open_web_page(url)
    def enter(w, e): 
        try: w.get_window().set_cursor(gtk.gdk.Cursor(gtk.gdk.HAND2))
        except AttributeError: pass
    def leave(w, e): 
        try: w.get_window().set_cursor(gtk.gdk.Cursor(gtk.gdk.LEFT_PTR))
        except AttributeError: pass
    label = gtk.Label()
    label.set_markup("<span color='blue'><u>%s</u></span>"%url)
    font = pango.FontDescription('Georgia')
    label.modify_font(font)
    button = gtk.Button()
    button.connect('clicked', func, url)
    button.connect('enter-notify-event', enter)
    button.connect('leave-notify-event', leave)
    button.set_relief(gtk.RELIEF_NONE)
    button.add(label)
    align = gtk.Alignment(0, 0.5)
    align.add(button)
    return align

def show_contribution_to_ailurus():
    titlelabel = gtk.Label()
    titlelabel.set_markup(_('Contributing to <i>Ailurus</i>'))
    titlelabel.modify_font(pango.FontDescription('Georgia 20'))
    
    table = gtk.Table()
    
    table.set_border_width(15)
    table.set_col_spacings(20)
    table.set_row_spacings(15)
    
    table.attach(titlelabel, 0, 2, 0, 1, gtk.FILL, gtk.FILL)
    
    table.attach(right_label(_('Project homepage:')), 0, 1, 1, 2, gtk.FILL, gtk.FILL)
    table.attach(url_button('http://ailurus.googlecode.com/'), 1, 2, 1, 2, gtk.FILL, gtk.FILL)
    
    table.attach(right_label(_('Project news:')), 0, 1, 2, 3, gtk.FILL, gtk.FILL)
    table.attach(url_button('http://ailurus.cn/'), 1, 2, 2, 3, gtk.FILL, gtk.FILL)
    
    table.attach(right_label(_('Code repository:')), 0, 1, 3, 4, gtk.FILL, gtk.FILL)
    table.attach(url_button('http://github.com/homerxing/Ailurus'), 1, 2, 3, 4, gtk.FILL, gtk.FILL)
    
    table.attach(right_label(_('Bug Tracker:')), 0, 1, 4, 5, gtk.FILL, gtk.FILL)
    table.attach(url_button('http://code.google.com/p/ailurus/issues/list'), 1, 2, 4, 5, gtk.FILL, gtk.FILL)
    
    table.attach(right_label(_('How to submit' '\n' 'patches:')), 0, 1, 5, 6, gtk.FILL, gtk.FILL)
    text = left_label(_('Send me patches on github. No mailing list (yet?) but feel \n'
                      'free to email me about possible features or whatever: \n'
                      'homer.xing@gmail.com'))
    text2 = left_label(_('How to use github? Please read:'))
    box = gtk.VBox(False, 0)
    box.pack_start(text, False)
    box.pack_start(gtk.Label(), False)
    box.pack_start(text2, False)
    box.pack_start(url_button('http://wiki.github.com/homerxing/Ailurus/join-ailurus-development'))
    table.attach(box, 1, 2, 5, 6, gtk.FILL, gtk.FILL)
    
    table.attach(right_label(_('Maintainer of this' '\n' 'metadata page:')), 0, 1, 6, 7, gtk.FILL, gtk.FILL)
    table.attach(left_label('Homer Xing'), 1, 2, 6, 7, gtk.FILL, gtk.FILL)
    
    table.attach(right_label(_('Last modified:')), 0, 1, 7, 8, gtk.FILL, gtk.FILL)
    table.attach(left_label('2010-4-17'), 1, 2, 7, 8, gtk.FILL, gtk.FILL)
    
    dialog = gtk.Dialog(title = _('Contributing to Ailurus'),
                        flags = gtk.DIALOG_NO_SEPARATOR, 
                        buttons = (gtk.STOCK_OK, gtk.RESPONSE_OK))
    dialog.vbox.pack_start(table)
    dialog.vbox.show_all()
    dialog.run()
    dialog.destroy()

def __others(main_view):
    help_contribute = gtk.MenuItem(_('Contributing to Ailurus'))
    help_contribute.connect('activate', lambda w: show_contribution_to_ailurus())
    
    help_blog = image_stock_menuitem(gtk.STOCK_HOME, _('Ailurus blog'))
    help_blog.connect('activate', 
        lambda w: open_web_page('http://ailurus.cn/' ) )
    
    help_update = image_file_menuitem(_('Check for updates'), D+'suyun_icons/m_check_update.png', 16, 3) 
    def callback(*w):
        while gtk.events_pending(): gtk.main_iteration()
        check_update()
    help_update.connect('activate', callback)

    help_report_bug = image_file_menuitem(_('Propose suggestion and report bugs'), D+'umut_icons/m_propose_suggestion.png', 16, 3) 
    help_report_bug.connect('activate', 
        lambda w: report_bug() )
    
    help_translate = image_stock_menuitem(gtk.STOCK_CONVERT, _('Translate this application'))
    help_translate.connect('activate', 
        lambda w: open_web_page('https://translations.launchpad.net/ailurus/trunk' ) )
    
    special_thank = gtk.MenuItem( _('Special thanks') )
    special_thank.connect('activate', lambda *w: show_special_thank_dialog())
    
    about = gtk.MenuItem( _('About') )
    about.connect('activate', lambda *w: show_about_dialog())
    
    changelog = gtk.MenuItem( _('Read changelog') )
    changelog.connect('activate', lambda *w: show_changelog())
    
    return [ changelog, help_contribute, help_blog, help_update, help_report_bug, help_translate, special_thank, about ] 

def get_study_linux_menu(main_view):
    return __study_linux(main_view)

def get_preferences_menu(main_view):
    return __preferences(main_view)

def get_others_menu(main_view):
    return __others(main_view)
