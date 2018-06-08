#!/usr/bin/etc python

from socket import *
import os
import ftplib

HOST = '192.168.56.1'
PORT = 8888

class DBdata_Trans:
     def dbdata_trans_run(self):
          Csocket=socket(AF_INET, SOCK_STREAM)
          try:
               Csocket.connect((HOST,PORT))
          except Exception as e:
               print ('Server not connect %s' %HOST)
               return "FALSE"

          var = input(" -> ")

          while var != 'q':

               Csocket.send(var.encode())
               Msentence = Csocket.recv(1024).decode()

               print('Received from server: ' + Msentence)

               var = input(" -> ")



          Csocket.close() 
          return "TRUE"


 
