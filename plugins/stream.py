# ফাইলের আসল নাম খোঁজার সঠিক লজিক
media = message.document or message.video
file_name = "Video_File.mp4" # ডিফল্ট নাম

if media:
    file_name = getattr(media, 'file_name', "Video_File.mp4")
    if not file_name: # যদি নাম খালি থাকে
        file_name = "Video_File.mp4"
