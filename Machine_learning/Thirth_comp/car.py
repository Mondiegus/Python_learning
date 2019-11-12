#!/usr/bin/env python
# coding: utf-8

# In[37]:


from flask import Flask
import eventlet.wsgi
import eventlet
import socketio
import base64
import numpy as np
from io import BytesIO
from PIL import Image
from tensorflow.python.keras.models import load_model


# In[38]:


model = load_model('h:\Pliki ściągnięte\model.h5')
model.summary


# In[2]:


sio = socketio.Server()
app = Flask(__name__)

def send_control(steering_angle, throttle):
    sio.emit("steer", data={'steering_angle': str(steering_angle),
                            'throttle': str(throttle) }, skip_sid=True)


# In[13]:


@sio.on('telemetry')
def telemetry(sid, data):
    if data:
        speed = float(data["speed"])
        image_str = data["image"]

        print(data.keys())
        decoded = base64.b64decode(image_str)
        image = Image.open(BytesIO(decoded))
        image_array = np.asanyarray(image)
        
        
        
        steering_angle = 0.0
        throttle = 0.0

        send_control(steering_angle, throttle)
    else:
        sio.emit('manual', data={}, skip_sid=True)
        
app = socketio.Middleware(sio, app)
eventlet.wsgi.server(eventlet.listen(('', 4567)), app)


# In[ ]:




