#!/usr/bin/python
import os
import time

#change this to read from a config
db_User_Name = 'USER'
DB_User_Password = 'PASS'
DB_Name = 'DATABASE'
backupDir = 'DIRECTORY'

datetime = time.strftime('%m%d%Y-%H%M%S')
datetimeBackupDir = backupDir + datetime

print "creating backup folder"
if not os.path.exists(datetimeBackupDir):
    os.makedirs(datetimeBackupDir)


mysqldump_cmd = "mysqldump -u " + db_User_Name + " --password='" + DB_User_Password + "' -h mysql.server --databases '" + DB_Name + "' > " + datetimeBackupDir + "/" + DB_Name + ".sql"
os.system(mysqldump_cmd)
