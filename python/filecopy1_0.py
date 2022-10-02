import sys
import shutil

#ASSIGNING COMMAND LINE VARIABLES
SOURCE=sys.argv[1]
DESTINATION=sys.argv[2]
SOURCE_TYPE=sys.argv[3]

def backup(arg1, arg2, arg3):
    print ("The file or directory to backup is %s" %arg1)
    print ("The backup location is %s" %arg2)
    print ("The type of source is %s" %arg3)
    print("")
    print("Backuping up %s to the backup location %s" %(arg1, arg2))
    if SOURCE_TYPE == "file":
        shutil.copy(arg1, arg2, arg3)
    elif SOURCE_TYPE == "directory":
        shutil.copytree(arg1, arg2, arg3)
    else:
        print ("Invalid file type")
    
    print("")
    print ("END OF BACKUP PROCESS")
    
backup (SOURCE, DESTINATION, SOURCE_TYPE)