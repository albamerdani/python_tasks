import socket
import tqdm
import os
import ftplib
import requests
from decouple import config
import time
import ftputil
import json

class Client():

    SEPARATOR = "   "
    buffer_size = config('BUFFER_SIZE')
    ftp_host = config('FTP_SERVER')
    ftp_user = config('FTP_USERNAME')
    ftp_pass = config('FTP_PASS')

    def __init__(self):
        pass

    def upload_cloud(self):
        s = socket.socket()
        host = config('CLIENT_HOST')
        port = config('PORT')
        s.connect((host, port))
        print("[+] Connected to ", host)
        filename = input("File to Transfer : ")
        filesize = os.path.getsize(filename)
        s.send(f"{filename}{self.SEPARATOR}{filesize}".encode())
        #file = open(filename, 'wb')

        progress = tqdm.tqdm(range(filesize), f"Sending {filename}", unit="B", unit_scale=True, unit_divisor=1024)
        with open(filename, "rb") as f:
            while True:
                bytes_read = f.read(self.buffer_size)
                if not bytes_read:
                    break
                s.sendall(bytes_read)
                progress.update(len(bytes_read))
        s.close()


    def get_file_from_url(self, file_url):

        file_data = requests.get(file_url).content
        # create the file in write binary mode, because the data we get from net is in binary
        with open("file.txt", "wb") as file:
            file.write(file_data.decode("utf-8"))
            file.write(json.loads(file_data.decode("utf-8")))


    def upload_ftp(self, path):
        myFTP = ftplib.FTP(self.ftp_host, self.ftp_user, self.ftp_pass)
        myPath = config('PATH')

        files = os.listdir(path)
        os.join.path(path)
        for f in files:
            if os.path.isfile(path + r'\{}'.format(f)):
                fh = open(f, 'rb')
                myFTP.storbinary('STOR %s' % f, fh)
                fh.close()
            elif os.path.isdir(path + r'\{}'.format(f)):
                myFTP.mkd(f)
                myFTP.cwd(f)
                self.upload_ftp(path + r'\{}'.format(f))
                myFTP.cwd('..')
                os.chdir('..')


    def get_ftp_file(self, filename):
        ftp = ftplib.FTP(self.ftp_host, self.ftp_user, self.ftp_pass)

        with open(filename, 'wb') as f:
            ftp.retrbinary('RETR ' + filename, f.write())
            f.close()
        ftp.quit()


    def delete_file_ftp(self, ftp_dir_path):
        host = ftputil.FTPHost(self.ftp_host, self.ftp_user, self.ftp_pass)
        now = time.time()
        host.chdir(ftp_dir_path)
        names = host.listdir(host.curdir)
        for name in names:
            if host.path.getmtime(name) < (now - (7 * 86400)):
                if host.path.isfile(name):
                    host.remove(name)
        host.close()


client = Client()
client.upload_cloud()
client.upload_ftp("path")
client.get_file_from_url("file_url")
client.get_ftp_file("filename")
client.delete_file_ftp("ftp_dir_path")