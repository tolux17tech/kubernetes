import shutil


#variable declaration

SOURCE="/Users/dc/Library/CloudStorage/OneDrive-Personal/full_k8s/python/test.yaml"
DESTINATION="/Users/dc/Library/CloudStorage/OneDrive-Personal/full_k8s/backup"

print("The source file is %s" %(SOURCE))
print("")
print("The backup directory is %s" %(DESTINATION))

#Using the shutil module to copy a file
shutil.copy(SOURCE, DESTINATION)