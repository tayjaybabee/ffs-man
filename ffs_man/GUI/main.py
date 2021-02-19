# ----------------------------------------------------------
#  Copyright (c) 2021. Inspyre Softworks                   -
# ----------------------------------------------------------

# ****** ffs_man/GUI/main.py ****** #
# Description: A module containing a class for the main window of the GUI version of FFS-Man
# Time of Creation: 2/18/21 at 11:45 PM
# Author: Taylor-Jayde J. Blackstone <t.blackstone@inspyre.tech>
# ************************ #
import PySimpleGUIQt as qt
from time import time
import ffs_man.GUI
from ffs_man.GUI.popups import confirm_del_host
from ffs_man.GUI.add_host import AddHostWin

GUI = ffs_man.GUI

class MainWin(object):
    def __init__(self, host_list):
        self.host_list = host_list
        self.frame_hosts = [
            [
                qt.Listbox(
                    host_list,
                    select_mode=qt.LISTBOX_SELECT_MODE_MULTIPLE,
                    enable_events=True,
                    key='LISTBOX_HOSTS',
                )
            ]
        ]

        self.frame_buttons = [
            [
                qt.Button(
                    'Connect',
                    tooltip='Connect to selected hosts and mount their associated directories.',
                    key='BUTTON_CONNECT',
                    enable_events=True
                ),
                qt.Button(
                    'Edit Host',
                    tooltip="Edit the selected host.",
                    key='BUTTON_EDIT_HOST',
                    enable_events=True
                ),
                qt.Button(
                    'Clear Selection',
                    tooltip="Clear currently selected hosts.",
                    key='BUTTON_CLEAR_SELECTIONS',
                    visible=False
                ),
                qt.Button(
                    'Delete Selected',
                    tooltip="Delete the currently selected hosts.",
                    visible=False,
                    key='BUTTON_DEL_HOST'
                ),
                qt.Button(
                    'Add Host',
                    tooltip="Add a host and it's options to FFS-Man",
                    key='BUTTON_ADD_HOST',
                    enable_events=True
                ),
                qt.Button(
                    'Quick Connect',
                    tooltip="Add and quickly connect to a host and mount it's associated directory before quitting.",
                    key='BUTTON_QUICK_CONN',
                    visible=True,
                    enable_events=True
                ),
                qt.Button(
                    'Quit',
                    tooltip='Leave FFS-Man without connecting to a remote server.',
                    key='BUTTON_QUIT',
                    enable_events=True
                )
             ]
        ]

        self.layout = [
            [qt.Frame('Hosts', layout=self.frame_hosts, title_location=qt.TITLE_LOCATION_TOP, relief=qt.RELIEF_RAISED)],
            [qt.Frame('', layout=self.frame_buttons, relief=qt.RELIEF_SUNKEN)]
        ]

        self.window = qt.Window('FFS-Man', layout=self.layout)

    def run(self):
        while True:
            event, values = self.window.read(timeout=100)

            if event is None:
                self.window.close()
                break

            if event == 'BUTTON_QUIT':
                self.window.close()
                break

            if event == 'BUTTON_ADD_HOST':
                clicked_time = time()
                unlock_time = clicked_time + .3
                if 'ADD_HOST_WIN' in GUI.active_windows.keys():
                    if not GUI.active_windows['ADD_HOST_WIN']['active']:
                        if GUI.active_windows['ADD_HOST_WIN']['deactivated_time'] >= unlock_time:
                            GUI.active_windows['ADD_HOST_WIN']['active'] = True
                            GUI.active_windows['ADD_HOST_WIN']['deactivated_time'] = None
                            ah_win = AddHostWin()
                            ah_win.run()
                        else:
                            print("User attempted to load two instances of the 'Add Host' window!")
                    else:
                        print("User attempted to load two instances of the 'Add Host' window!")
                else:
                    GUI.active_windows.update(
                        {
                            'ADD_HOST_WIN': {
                                'active': True,
                                'deactivated_time': None
                            }
                        }
                    )
                    add_host_win = AddHostWin()
                    add_host_win.run()

            if len(values['LISTBOX_HOSTS']) == 0:
                self.window['BUTTON_QUICK_CONN'].update(visible=True)
                self.window['BUTTON_ADD_HOST'].update(visible=True)
            else:
                self.window['BUTTON_QUICK_CONN'].update(visible=False)
                self.window['BUTTON_ADD_HOST'].update(visible=False)

            if len(values['LISTBOX_HOSTS']) == 1:
                self.window['BUTTON_EDIT_HOST'].update(visible=True)
            else:
                self.window['BUTTON_EDIT_HOST'].update(visible=False)

            if len(values['LISTBOX_HOSTS']) >= 1:
                self.window['BUTTON_CONNECT'].update(visible=True)
                self.window['BUTTON_DEL_HOST'].update(visible=True)
                self.window['BUTTON_CLEAR_SELECTIONS'].update(visible=True)
            else:
                self.window['BUTTON_CONNECT'].update(visible=False)
                self.window['BUTTON_DEL_HOST'].update(visible=False)
                self.window['BUTTON_CLEAR_SELECTIONS'].update(visible=False)

            if event == 'BUTTON_CLEAR_SELECTIONS':
                self.window['LISTBOX_HOSTS'].update(self.host_list)

            if event == 'BUTTON_DEL_HOST':
                if not confirm_del_host():
                    pass
                else:
                    for item in values['LISTBOX_HOSTS']:
                        self.host_list.remove(item)

                self.window['LISTBOX_HOSTS'].update(self.host_list)

            #print(values['LISTBOX_HOSTS'])
            #print(len(values['LISTBOX_HOSTS']))

            self.window.refresh()


win = MainWin(['banana', 'sundae', 'and', 'fudge'])
win.run()
