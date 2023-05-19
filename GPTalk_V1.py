#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 29 21:36:10 2023

@author: yannick
"""

import whisper

model = whisper.load_model("base")

result = model.transcribe("audio.mp3")

print(result["text"])
