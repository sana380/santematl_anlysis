#!/usr/bin/env python
# coding: utf-8

# In[24]:


pip install textblob


# In[27]:


from textblob import TextBlob
from dataclasses import dataclass

@dataclass
class Mood:
    emoji: str
    sentiment: float


# In[28]:


def get_mood(input_text: str, *, threshold: float) -> Mood:
    sentiment: float = TextBlob(input_text).sentiment.polarity
    
    friendly_threshold: float = threshold
    hostile_threshold: float = -threshold
        
    if sentiment >= friendly_threshold:
        return Mood('😊', sentiment)
    elif sentiment <= hostile_threshold:
        return Mood('😠', sentiment)
    else:
        return Mood('😐', sentiment)


# In[ ]:


if __name__ == '__main__':
    while True:
        text: str = input('text: ')
        mood: Mood = get_mood(text, threshold=0.3)
        
        print(f'{mood.emoji} ({mood.sentiment})')


# In[ ]:




