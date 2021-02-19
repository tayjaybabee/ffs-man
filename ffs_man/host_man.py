# ****** ffs_man/host_man.py ****** #
# Description:
# Time of Creation: 2/7/21 at 6:30 PM
# Author: Taylor-Jayde J. Blackstone <t.blackstone@inspyre.tech>
# ************************ #

class Host(object):
    def __init__(self,
                 host,
                 username,
                 remote_dir,
                 auth_type='PASS',
                 password=None,
                 mount_point=None,
                 mount_on_start=False,
                 save=True,
                 test_conn=False):
        self.host = host
        self.username = username
        self.remote_dir = remote_dir
        self.auth_type = auth_type
        self.password = password
        self.mount_point = mount_point
        self.mount_on_start = mount_on_start
        self.save = save
        self.test_conn = test_conn


