from django.shortcuts import render
from django.http import HttpResponse
import sys
import time
sys.path.append("..")
from v5 import webDetect
import os
from django_redis import get_redis_connection

JOBTYPES = ['od', 'helmet', 'poppy', 'fire']
URLTYPE = ['folder', 'stream']

# define job type
def jobHandler(url, job_type='od', url_type='folder'):
    if job_type.lower() not in JOBTYPES:
        ################################
        #
        # redis publish error message job type error
        #
        ################################
        msg = f"Job type error! Name '{job_type}' invalid."
        print(msg)
        return msg
    if url_type.lower() not in URLTYPE:
        ################################
        #
        # redis publish error message url type error
        #
        ################################
        msg = f"Url type error! Name '{url_type}' invalid."
        print(msg)
        return msg
    if url_type.lower() == 'folder' and not os.path.exists(path):
        ################################
        #
        # redis publish error message folder not exist error
        #
        ################################
        msg = f"Folder not exist! Path '{url}' invalid."
        print(msg)
        return msg
    if url_type.lower() == 'folder':
        ################################
        #
        # redis publish processing message
        #
        ################################
        if job_type.lower() == 'od':
            pass
        elif job_type.lower() == 'poppy':
            # url = '/data/ftp/yingsu/广城村'
            cmd = r'python3 detect_folder.py --device 0 --weights ./weights/RY_POPPY_YV5_2048.pt --imgsz 2048 --conf-thres 0.25 --iou-thres 0.45 --hide-conf --source ' + url
            os.system(cmd)
            pass
        elif job_type.lower() == 'helmet':
            pass
        elif job_type.lower() == 'fire':
            pass
        else:
            pass
        msg = f"Job {job_type} finished! Result saved at '{url}'."
        print(msg)
        return msg
    elif url_type.lower() == 'stream':
        ################################
        #
        # redis publish processing message
        #
        ################################
        if job_type.lower() == 'od':
            pass
        elif job_type.lower() == 'poppy':
            pass
        elif job_type.lower() == 'helmet':
            pass
        elif job_type.lower() == 'fire':
            pass
        else:
            pass
    else:
        msg = "Url type unknown error."
        print(msg)
        return msg
        

# initial redis connection
redis = get_redis_connection("default")

# publish
# push(channel, message)
# redis.publish("channel", "hahahaha")
# push2somewhere(channel, msg)

# subscription
ps = redis.pubsub()
ps.subscribe('detection')
    
# listening
while True:
    try:
        for item in ps.listen():
            print(item)
            if item['type'] == 'message':
                message = item['data']
                url = ''
                job_type = ''
                url_type = ''
                result = jobHandler(url, job_type, url_type)
                print(f'Result {result}, 111')
            else:
                print(item['type'], item['data'])
    except Exception:
        print("Got disconnected! Establish reconnection!")           
    time.sleep(0.1)

# while True:
#     try:
#         item = ps.get_message()
#     except Exception:
#         print("Got disconnected! Establish reconnection!")
#     if item:
#         print(item)          
#     time.sleep(0.1)



# def push_service():
#     redis = get_redis_connection("default")
    
#     rc = redis.StrictRedis(host="172.17.7.31", port="1987", db=1, password="q1M2IOKrz6CunZXyt58V")
#     # rc = redis.Redis(host="172.17.7.31", port="1987", db=1, password="q1M2IOKrz6CunZXyt58V", decode_responses=True)
#     ps = rc.pubsub()
#     ps.subscribe('detection')

#     rc.publish("channel", "hahahaha")
    
#     def push(channel, msg):
#         push2somewhere(channel, msg)
	
#     for item in ps.listen():
#         print(item)
#         if item['type'] == 'message':
#             channel = item['channel'].decode()
#             message = item['data'].decode()
#             push(channel, message)


# def index(request):
#     return HttpResponse(f"Object Detection platform by Zit!")

# def detect(request):
#     taskid = request.GET.get('taskid')
#     streamurl = request.GET.get('streamurl')
#     # -------------------------------------- detect here ----------------------------------------
#     # IP:Port/objectDetection/detect?taskid=1&streamurl=https://abc.yeah
#     #
#     cmd = r'python3 /data/ai/RyAI/AIDevOps/v5/webDetect.py --weights ./weights/RY_OD_YV5_640.pt --imgsz 640 --vid-stride 30 --conf-thres 0.25 --iou-thres 0.45 --project runs/od --hide-conf --source ' + streamurl + ' --exist-ok --name TaskID_' + taskid 
#     os.system(cmd)
#     # 
#     return HttpResponse(f"Task {taskid}: infer {streamurl} Success! Result saved at: '/data/ai/RyAI/AIDevOps/v5/runs/od/TaskID_{taskid}'")

# def poppy(request):
#     taskid = request.GET.get('taskid')
#     streamurl = request.GET.get('streamurl')
#     # -------------------------------------- detect here ----------------------------------------
#     # IP:Port/objectDetection/poppy?taskid=1&streamurl=https://abc.yeah
#     #
#     if not streamurl.endswith('/'):
#         cmd = r'python3 /data/ai/RyAI/AIDevOps/v5/webDetect.py --weights ./weights/RY_POPPY_YV5_2048.pt --imgsz 2048 --vid-stride 30 --conf-thres 0.25 --iou-thres 0.45 --project runs/poppy --hide-conf --source ' + streamurl + ' --exist-ok --name TaskID_' + taskid 
#     else:
#         cmd = r'python3 /data/ai/RyAI/AIDevOps/v5/detect.py --weights ./weights/RY_POPPY_YV5_2048.pt --imgsz 2048 --conf-thres 0.25 --iou-thres 0.45 --project runs/poppy --hide-conf --source ' + streamurl + ' --exist-ok --name TaskID_' + taskid 
#     os.system(cmd)
#     # 
#     return HttpResponse(f"Task {taskid}: infer {streamurl} Success! Result saved at: '/data/ai/RyAI/AIDevOps/v5/runs/poppy/TaskID_{taskid}'")

# def helmet(request):
#     taskid = request.GET.get('taskid')
#     streamurl = request.GET.get('streamurl')
#     # -------------------------------------- detect here ----------------------------------------
#     # IP:Port/objectDetection/helmet?taskid=1&streamurl=https://abc.yeah
#     #
#     cmd = r'python3 /data/ai/RyAI/AIDevOps/v5/webDetect.py --weights ./weights/RY_HELM_YV5_1024.pt --imgsz 1024 --vid-stride 30 --conf-thres 0.25 --iou-thres 0.45 --project runs/helmet --hide-conf --source ' + streamurl + ' --exist-ok --name TaskID_' + taskid 
#     os.system(cmd)
#     # 
#     return HttpResponse(f"Task {taskid}: infer {streamurl} Success! Result saved at: '/data/ai/RyAI/AIDevOps/v5/runs/helmet/TaskID_{taskid}'")

# def fire(request):
#     taskid = request.GET.get('taskid')
#     streamurl = request.GET.get('streamurl')
#     # -------------------------------------- detect here ----------------------------------------
#     # IP:Port/objectDetection/helmet?taskid=1&streamurl=https://abc.yeah
#     #
#     cmd = r'python3 /data/ai/RyAI/AIDevOps/v5/webDetect.py --weights ./weights/RY_FIRE_YV5l_640.pt --imgsz 640 --vid-stride 30 --conf-thres 0.25 --iou-thres 0.45 --project runs/fire --hide-conf --source ' + streamurl + ' --exist-ok --name TaskID_' + taskid 
#     os.system(cmd)
#     # 
#     return HttpResponse(f"Task {taskid}: infer {streamurl} Success! Result saved at: '/data/ai/RyAI/AIDevOps/v5/runs/fire/TaskID_{taskid}'")