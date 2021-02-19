import PySimpleGUIQt as gui
from pathlib import Path


def where_app_dir(app_dir=Path('~/Inspyre-Softworks/FFS-Man').expanduser().resolve()):
    app_dir = gui.PopupGetFolder("Please choose an app directory: ",
                                 title="Choose a filepath",
                                 default_path=str(app_dir),
                                 initial_folder=str(Path('~').expanduser().resolve()),
                                 size=(300,20),
                                 location=(750,450),
                                 keep_on_top=True
                                 )

    return app_dir


def confirm_del_host():
    confirm = gui.PopupOKCancel('This will delete these hosts permanently!', title='Confirm Host Deletion', keep_on_top=True)

    if confirm is None:
        return False
    else:
        if confirm.lower() == 'cancel':
            return False
        elif confirm.lower() == 'ok':
            return True

    return confirm
