# -*- coding: utf-8 -*-
import paho.mqtt.client as mqtt

f = open("EncryptTrial.txt")
imagestring = f.read()
byteArray = bytes(imagestring)

mqttc = mqtt.Client("python_pub")
mqttc.connect("iot.eclipse.org", 1883)
mqttc.publish("hello1/world", byteArray)
mqttc.loop(2) 