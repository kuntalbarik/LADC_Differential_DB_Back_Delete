import os
from datetime import date,datetime,timedelta


##log path
logPath="c:\\Differential_DB_Back_Delete"
if (os.path.exists(logPath) == False):
    os.mkdir(logPath)
##creating log file
now=datetime.now()
log_date=str(now)
filepath=logPath+"\\log_"+log_date[0:11] + '.txt'
fileobject=open(filepath,"a+")
fileobject.close()

backupPath=r"d:\laxisilon.pftla.local\Clear\ifs\PRODUCTION_BACKUPS\SQLDB\Differential_Production_DB_Backup_Products"

###getting the dates in backup folder name
today = date.today()  ###will be in format YYYY-MM-DD
yesterday = today - timedelta(days = 1)
dayBeforeYesterday=today- timedelta(days = 2)
today=str(today).split('-')
yesterday=str(yesterday).split('-')
dayBeforeYesterday=str(dayBeforeYesterday).split('-')
today = today[0]+'_'+today[1] + '_' + today[2]
yesterday = yesterday[0]+'_'+yesterday[1] + '_' + yesterday[2]
dayBeforeYesterday = dayBeforeYesterday[0]+'_'+dayBeforeYesterday[1] + '_' + dayBeforeYesterday[2]

fileobject=open(filepath,"a+")
for roots, dirs, files in os.walk(backupPath):
    for dir in dirs:
        backupPath1= backupPath
        backupPath1+="\\"+dir
        filesDeleted=0
        now = datetime.now()
        message="[ "+str(now)+" ]--Deleting from : "+str(backupPath1)+"\n"
        fileobject.write(message)
        for roots,dirs,files in os.walk(backupPath1):
            for file in files:
                if (today not in file) and (yesterday not in file) and (dayBeforeYesterday not in file):
                    os.remove(backupPath1+"\\"+file)
                    filesDeleted+=1
                    now = datetime.now()
                    message="[ "+str(now)+" ]--"+str(file)+" deleted successfully\n"
                    fileobject.write(message)
        if(filesDeleted==0):
            now = datetime.now()
            message="[ "+str(now)+" ]--No files are deleted\n"
            fileobject.write(message)
        now = datetime.now()
        message="-------------------------------------------------------------------------------------------------------\n"
        fileobject.write(message)
fileobject.close()
