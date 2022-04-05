import os
import dropbox
from dropbox.files import WriteMode

class TransferData:
    def __init__(self, accessToken):
        self.accessToken = accessToken

    def uploadFile(self, fileFrom, fileTo):
        dbx = dropbox.Dropbox(self.accessToken)
        for root, dirs, files in os.walk(fileFrom):
            for filename in files:
                localPath = os.path.join(root, filename)
                relativePath = os.path.relpath(localPath, fileFrom)
                dropboxPath = os.path.join(fileTo, relativePath)
                with open(localPath, 'rb') as f:
                    dbx.files_upload(f.read(), dropbox_path, mode=WriteMode('overwrite'))
# I looked up some examples on how to write the code above.

def main():
    accessToken = 'sl.FH12ssjaj_HWztexIk5oUv3rvTJGSYWKWNSGYSUAKUIOP_37423859tfsGGUJWSyJJ-8scib8fert77523rvTtn_IUSHefbhsfe8fw68yuTk5oUv3rvT-7-0TPelU2y81msjhsjah823eu8eTRY5oQiJYOWI9CST6AY_ycJB5uYYhTtz_bKOYshsnrshajaHGAHHSGSgs'
    transferData = TransferData(accessToken)
    fileFrom = str(input("Please enter where you want to transfer this folder (folder path): "))
    fileTo = input("Please enter the access token or path to upload to Dropbox: ")
    transferData.uploadFile(fileFrom, fileTo)
    print("Yay! File has successfully been transferred.")
# I looked up some examples from previous class code.

main()