import sys
sys.path.insert(1, "../")  # to import mongodbCommon (which is in another folder)

from mongodbCommon import MongodbCommon

metadata = MongodbCommon("metadata", "metadata")
metadata.dropDb()
print("Doneski")
