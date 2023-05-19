#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 30 07:33:17 2023

@author: yannick
"""

import openai

# Define OpenAI API key
openai.api_key = "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"

# Set up the model and prompt
model_engine = "text-davinci-003"
prompt = "Tell me a story about a young boy working his way to success in a weak world"

# Generate a response
completion = openai.Completion.create(
    engine=model_engine,
    prompt=prompt,
    max_tokens=1024,
    n=1,
    stop=None,
    temperature=0.5,
)

response = completion.choices[0].text
print(response)
