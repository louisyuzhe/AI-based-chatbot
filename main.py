# -*- coding: utf-8 -*-
"""
Created on Mon Sep  7 15:59:18 2020

@author: Yu Zhe
"""
#Importing modules
from chatterbot import ChatBot
from chatterbot.trainers import ListTraine #train chatbot on a custom list of statements 
from chatterbot.trainers import ChatterBotCorpusTrainer

#%%
"""
Instantiating a ChatBot Instance
"""
#chatbot will be set to read_only to avoid learning after training
chatbot1 = ChatBot(name = 'BankBot',
                  read_only = False,                  
                  logic_adapters = ["chatterbot.logic.BestMatch"],                 
                  storage_adapter = "chatterbot.storage.SQLStorageAdapter")