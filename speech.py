#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 19:29:43 2019

@author: maulik
"""

import speech_recognition as sr
Audio1= ("female.wav")
r= sr.Recognizer
with sr.AudioFile(Audio1) as source1:
    audio= r.record(source1)
try:
    print(r.recognize_google(audio))
except sr.UnknownValueError:
    print("cannot recognize")
except sr.RequestError:
    print("could not recognize")
    