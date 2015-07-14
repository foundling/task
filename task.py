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

    self.f = open(handle,'r+')

  def add_tasks(self,db,new_tasks):

    for task in new_tasks:
      print 'adding task %s' % (task)
      self.f.write(task+'\n')

  def get_latest(self):
    self.f.seek(0)
    return self.f.readlines()[-1]

  def remove_latest(self):
    self.f.seek(0)
    content = self.f.read()
    self.f.seek(0);
    self.f.write(content[:-1])
    self.f.seek(0);
    print self.f.read()
    self.f.seek(0);
    
def usage():
  print '''usage: 

     task top (shows top of stack)

     task pop (removes top of stack)

     task add <task1> <task2> <task3> ... 
 
  '''

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

def get_latest_task(db,i=-1):
  try:
    db.get_task[i]
  except indexError:
    print 'that index doesnt exist'
    sys.exit(1)
  

def main():

  db = DB(config['config_file'])

  if len(sys.argv) < 2:
    usage()
    sys.exit()

  else:
    action, tasks = sys.argv[1], sys.argv[2:]

    if action == 'add':
      db.add_tasks(db,tasks)
      print action + 'ing' + ','.join(sys.argv[2:])

    if action == 'top':
      print 'getting latest ...'
      print db.get_latest(db)

    if action == 'pop':
      db.remove_latest()

main()
