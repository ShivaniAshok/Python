from pymongo import MongoClient
from bson import ObjectId

#Not a good idea to include id & password in code files
#tlsAllowInvalidCertificates=True - Not a good way to handle ssl
client=MongoClient("mongodb+srv://your_userid:your_password@cluster0.j3iuaow.mongodb.net/",tlsAllowInvalidCertificates=True)
db=client["ytmanager"]
video_collection=db["videos"]

#print(video_collection)

def list_videos():
    videos=video_collection.find()
    video_list=list(videos)
    if not video_list:
        print("No videos found")
    else:
        for video in video_list:
            print(f"ID: {video['_id']}, Name: {video['name']}, Time: {video['time']}")

def add_video(name,time):
    video_collection.insert_one({"name":name,"time":time})

def update_video(video_id,new_name,new_time):
    video_collection.update_one(
            {'_id': ObjectId(video_id)},
            {"$set":{"name":new_name,"time":new_time}}
        )

def delete_video(video_id):
    video_collection.delete_one({'_id':ObjectId(video_id)})

def main():
    while True:
        print("\nYoutube Manager App")
        print("1. List all videos")
        print("2. Add a new video")
        print("3. Update a video")
        print("4. Delete a video")
        print("5. Exit the app")

        choice=input("Enter your choice: ")

        if choice=="1":
            list_videos()
        elif choice=="2":
            name=input("Enter the video name: ")
            time=input("Enter the video time: ")
            add_video(name,time)
        elif choice=="3":
            video_id=input("Enter video id to update: ")
            name=input("Enter the new video name: ")
            time=input("Enter the new video time: ")
            update_video(video_id,name,time)
        elif choice=="4":
            video_id=input("Enter video id to delete: ")
            delete_video(video_id)
        elif choice=="5":
            break
        else:
            print("Invalid Choice")

if __name__=="__main__":
    main()
