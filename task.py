#!/usr/bin/python

import os
import sys

from config import config

'''
   usage: 

     task top (shows top of stack)

     task pop (removes top of stack)

     task add <task1> <task2> <task3> ... 
 
'''

class DB(object):
 
  ''' a small database class to organize the db operations.'''

  def __init__(self,handle):

    if not os.path.isfile(handle):
      print "The file doesn't exist, quitting."
      sys.exit()

    print 'file exists'

    self.f = open(handle,'a')

  def read(self):
    return self.f.read()

  def readlines(self):
    return self.f.readlines()

  def write(self, content):
    return self.f.write(content + '\n')
 
  def appendTo(self):
    pass

def usage():
  print '''usage: 

     task top (shows top of stack)

     task pop (removes top of stack)

     task add <task1> <task2> <task3> ... 
 
  '''
def get_one_task(db):
  pass

class AdminPanel(object):

  def __init__():
    pass

  def run():
    while True:
      pass

  def voice_problem():
		problem = raw_input('problem description:').strip()
		# gh pull req here 


def administration_interface():

  response = raw_input('administration here! need anything done?' + '\n')
  answer = response.strip()

  if answer in ('n','N','q','Q'):
    sys.exit()

  if answer in ('Y','y',''):
    admin_panel = AdminPanel()
    print "admin_panel.run()"

def add_tasks(db,new_tasks):

  for task in new_tasks:
    #new_task(task)
    print 'adding task %s' % (task)

  #administration_interface(db)

def main():

  db = DB(config['config_file'])

  actions = ['top','pop','add'] 
  if len(sys.argv) < 2:
    usage()
    sys.exit()

  else:
    action = sys.argv[1]
    if action == 'add':
      add_tasks(db,sys.argv[2:])
      print action + 'ing' + ','.join(sys.argv[2:])

main()
