#!/usr/bin/env python
# coding: utf-8

# In[1]:


from flask import Flask
import eventlet.wsgi
import eventlet
import socketio
import numpy as np
import base64
from PIL import Image
from io import BytesIO
from keras.models import load_model


# In[11]:


sio = socketio.Server()
app = Flask(__name__)

def send_control(steering_angle, throttle):
    sio.emit("steer", data = {"steering_angle": str(steering_angle),
                             "throttle": str(throttle)}, skip_sid = True)

def process_image(image):
    return image[10:130:2, ::4, :]


# In[7]:


model = load_model('d:\Pliki ściągnięte\mymodel.h5')


# In[14]:


@sio.on('telemetry')
def telemetry(sid, data):
    if data:
        speed = float(data["speed"])
        image_str = data["image"]
        
        decoded = base64.b64decode(image_str)
        image = Image.open(BytesIO(decoded))
        image_array = np.asarray(image)
        
        img = process_image(image_array)
        img_batch = np.expand_dims(img, axis=0)
        steering_angle = float(model.predict(img_batch))
        
        throttle = 0.15
        if speed < 15:
            throttle = 0.8
        if speed > 17:
            throttle = -0.1

        send_control(steering_angle, throttle)
    else:
        sio.emit("manual", data = (), skip_sid = True)
        
app = socketio.Middleware(sio, app)
eventlet.wsgi.server(eventlet.listen(('',4567)), app)


# In[ ]:




