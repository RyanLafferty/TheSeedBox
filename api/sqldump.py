import os, subprocess
import time
from ConfigParser import SafeConfigParser

def sql_dump():
    #parse config file
    parser = SafeConfigParser()
    parser.read('config.ini')
    host =  parser.get('mysql', 'host')
    database =  parser.get('mysql', 'database')
    user =  parser.get('mysql', 'user')
    password =  parser.get('mysql', 'password')
    upload =  parser.get('directories', 'upload')

    #setup parameters
    db_User_Name = user
    DB_User_Password = password
    DB_Name = database
    backupDir = upload

    #create backup path
    datetime = time.strftime('%m%d%Y-%H%M%S')
    datetimeBackupDir = backupDir + datetime

    #print "creating backup folder"
    #if not os.path.exists(datetimeBackupDir):
    #    os.makedirs(datetimeBackupDir)

    #mysqldump_cmd = "mysqldump -u " + db_User_Name + " --password='" + DB_User_Password + "' -h mysql.server --databases '" + DB_Name + "' > " + datetimeBackupDir + "/" + DB_Name + ".sql"
    mysqldump_cmd = "mysqldump -u " + db_User_Name + " --password='" + DB_User_Password + "' --all-databases > " + backupDir + "/" + DB_Name + ".sql"

    subprocess.call(mysqldump_cmd)
    #os.system(mysqldump_cmd)
