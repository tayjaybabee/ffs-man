import PySimpleGUIQt as gui
from pathlib import Path



LABEL_SIZE = (150, 20)


class AddHostWin(object):
    def __init__(self, quick_connect=False):

        self.quick_connect = quick_connect
        if self.quick_connect:
            self.suggest_test = False
        else:
            self.suggest_test = True

        self.frame_basic = [
            # Two elements beside each-other. A label, and a text-input field.
            # Host Name:  HOST_NAME
            [
                gui.Text("Host Name: ", size=LABEL_SIZE),
                gui.InputText('', tooltip="The hostname you want to connect to", key='HOST_NAME')
            ],
            # User name:  USER_NAME
            [
                gui.Text("User name: ", size=LABEL_SIZE),
                gui.InputText('', tooltip="The account name on the host you'd like to connect to", key='USER_NAME')
            ],
            # Remote Directory:  REMOTE_DIR
            [
                gui.Text("Remote Directory: ", size=LABEL_SIZE),
                gui.InputText(
                    '',
                    tooltip="The directory on the remote host you'd like to mount",
                    key="REMOTE_DIR"
                )
            ],
        ]

        self.frame_auth_pass = [
            [
                gui.Text('SSH Password: ', size=LABEL_SIZE, key='LABEL_SSH_PASS'),
                gui.InputText('',
                              tooltip='The SSH password for the username at the host',
                              password_char='*',
                              key='SSH_PASS')
            ]
        ]

        self.frame_auth_key_upload = [
            [
                gui.Text('SSH Key File: ', key='SSH_KEY_FILE_LABEL', size=LABEL_SIZE),
                gui.InputText('', visible=False, key='SSH_KEY_FILEPATH'),
                gui.FolderBrowse('SSH Key File',
                                 tooltip='Find SSH Key File',
                                 key='SSH_KEY_BROWSE_BUTTON')
            ],
        ]

        self.frame_auth_key = [
            [
                gui.Text('Need to upload key: ', size=LABEL_SIZE, key='LABEL_UPLOAD_KEY'),
                gui.Radio('Yes', group_id='UPLOAD_KEY', key='UPLOAD_KEY_TRUE', enable_events=True),
                gui.Radio('No', group_id='UPLOAD_KEY', key='UPLOAD_KEY_FALSE', enable_events=True)
            ],
            [
                gui.Frame('Upload Key File', layout=self.frame_auth_key_upload, visible=False, key='FRAME_UPLOAD_KEY')
            ]
        ]

        self.frame_auth = [
            # A text label asking for 'AUTH_TYPE' radio button selection
            [
                gui.Text("Auth Type: ", size=LABEL_SIZE),
                gui.Radio("Password", group_id='AUTH_TYPE', key='AUTH_TYPE_PASS', enable_events=True),
                gui.Radio("SSH Key", group_id='AUTH_TYPE', key='AUTH_TYPE_KEY', enable_events=True)
            ],
            [
                gui.Frame('SSH Password Authentication', layout=self.frame_auth_pass, visible=False, key='FRAME_AUTH_PASS'),
                gui.Frame('SSH Key Authentication', layout=self.frame_auth_key, visible=False, key='FRAME_AUTH_KEY')
            ]
        ]

        self.frame_mount = [
            [
                gui.Text('Mount Point: ', size=LABEL_SIZE),
                gui.InputText('', visible=False, key='MOUNT_DIR'),
                gui.FolderBrowse(initial_folder=str(Path('~').expanduser().resolve()))
            ]
        ]

        self.frame_save = [
            [
                gui.Text("Save: ", size=LABEL_SIZE),
                gui.Radio('Yes', group_id='SAVE_HOST', key='SAVE_HOST_TRUE', enable_events=True),
                gui.Radio('No', group_id='SAVE_HOST', key='SAVE_HOST_FALSE', enable_events=True)

            ]
        ]

        self.frame_additional_opts = [
            [
                gui.Text("Mount on start: ", size=LABEL_SIZE, key='LABEL_MOUNT_ON_START'),
                gui.Radio('Yes', group_id='MOUNT_ON_START', key='MOUNT_ON_START_TRUE',),
                gui.Radio('No', group_id='MOUNT_ON_START', key='MOUNT_ON_START_FALSE')
            ]
        ]

        self.frame_test_conn = [
            [
                gui.Text("Test Connection: ", size=LABEL_SIZE),
                gui.Radio("Yes", group_id='TEST_CONN', key='TEST_CONN_TRUE'),
                gui.Radio("No", group_id='TEST_CONN', key='TEST_CONN_FALSE')
            ]
        ]

        self.main_frame = [
            [
                gui.Frame('Basic Information', layout=self.frame_basic, title_location=gui.TITLE_LOCATION_TOP)
            ],

            [
                gui.Frame('Authentication', layout=self.frame_auth)
            ],
            [
                gui.Frame('Mount Point', layout=self.frame_mount)
            ],
            [
                gui.Frame('Save Session', layout=self.frame_save)
            ],
            [
                gui.Frame('Additional Options',
                          layout=self.frame_additional_opts,
                          title_location=gui.TITLE_LOCATION_TOP,
                          visible=False,
                          key='FRAME_ADDITIONAL_OPTS')
            ],
            [
                gui.Frame('Test Connection', layout=self.frame_test_conn, title_location=gui.TITLE_LOCATION_TOP)
            ]
        ]

        self.layout = [
            [gui.Frame('', self.main_frame)],
            [
                gui.Button('OK', key='OK_BUTTON'),
                gui.Button('Connect', key='CONNECT_BUTTON', visible=self.quick_connect),
                gui.Button('Quit', key='QUIT_BUTTON')
            ]
        ]

        self.window = gui.Window(
            'Add Host',
            layout=self.layout,
            location=(775, 425),
            force_toplevel=True,
            keep_on_top=True
        )

    def run(self):
        while True:
            event, values = self.window.Read(timeout=100)

            if event is None:
                self.window.close()
                break

            if event == 'QUIT_BUTTON':
                self.window.close()
                break

            if self.quick_connect:
                if event == 'CONNECT_BUTTON':
                    print("Would connect here.")
                    self.window.close()
                    break

            if event == 'OK_BUTTON':
                print(values)

            if event == 'AUTH_TYPE_KEY':
                self.window['FRAME_AUTH_PASS'].update(visible=False)
                self.window['FRAME_AUTH_KEY'].update(visible=True)
                self.window['SSH_PASS'].update('')

            if event == 'AUTH_TYPE_PASS':
                self.window['FRAME_AUTH_KEY'].update(visible=False)
                self.window['FRAME_AUTH_PASS'].update(visible=True)

            if event == 'UPLOAD_KEY_TRUE':
                self.window['FRAME_UPLOAD_KEY'].update(visible=True)

            if event == 'UPLOAD_KEY_FALSE':
                self.window['FRAME_UPLOAD_KEY'].update(visible=False)

            if event == 'SAVE_HOST_TRUE':
                self.window['FRAME_ADDITIONAL_OPTS'].update(visible=True)

            if event == 'SAVE_HOST_FALSE':
                self.window['FRAME_ADDITIONAL_OPTS'].update(visible=False)
