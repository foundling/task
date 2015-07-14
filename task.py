#!/usr/bin/python

import os
import sys

import config

class DB(object):
 
  ''' a small database class to organize the db operations.'''

  def __init__(self,handle):

    if not os.path.fileexists(handle):
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

def new_task(name,_db=db):
  _db = open(_db,'a')
  _db.write(sys.argv[1] + '\n')

def usage():
  print 'task: give one word to describe the task.\n To add a list, separate by whitespace.'

def get_one_task(db):
  pass

def admin_panel():
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
    admin_panel.run()

def add_tasks(db,new_tasks):

  for task in new_tasks:
    new_task(task)

  administration_interface(db)

def main():
  new_tasks = sys.argv[1:]
  db = DB(config['config_file'])

  if __name__ == '__main__':
    add_tasks(db,new_tasks)

main()
