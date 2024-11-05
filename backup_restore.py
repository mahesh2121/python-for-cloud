import os
import tarfile
from datetime import datetime

def backup_directory(source_dir,backup_dir):
    backup_filename = f"Backup_{datetime.now().strftime('%y%m%d%H%M%S')}.tar.gz"
    print(f"{backup_filename}")

    backup_filepath = os.path.join(backup_dir,backup_filename)


    with tarfile.open(backup_filepath,"w:gz") as tar:
        tar.add(source_dir,arcname=os.path.basename(source_dir))

    print(f"Backup Completed: {backup_filepath}")


if __name__ == "main":
    source ="/home/mahesh/Desktop/python-for-cloud/ep1"
    destination = "/home/mahesh/Desktop/python-for-cloud/backupdemo"
    backup_directory(source,destination)








          
if __name__ == "__main__":
   source = "."
   destination = "."
   backup_directory(source, destination)