import coloredlogs
from pyupdater.client import Client
from client_config import ClientConfig

APP_NAME = 'ngalert'
APP_VERSION = '0.1'

coloredlogs.install()


def print_status_info(info):
    total = info.get(u'total')
    downloaded = info.get(u'downloaded')
    status = info.get(u'status')
    print downloaded, total, status


client = Client(ClientConfig(), refresh=True,
                        progress_hooks=[print_status_info])



app_update = client.update_check(APP_NAME, APP_VERSION)
if app_update is not None:
    app_update.download()
    
    if app_update.is_downloaded():
        app_update.extract_overwrite()
    
    if app_update.is_downloaded():
        app_update.extract_restart()
