import os
import sys

class DB(object):
 
  ''' a small-ish database class to do reads and writes to a flat file '''

  def __init__(self,handle):

    if not os.path.isfile(handle):
      sys.stdout.write("The file doesn't exist, quitting.")
      sys.exit()

    self.db_file = handle

  def add_tasks(self,db,new_tasks):

    f = open(self.db_file,'a')
    task_string = '\n'.join(new_tasks)
    f.write(task_string+'\n')
    f.close()

  def top(self):

    f = open(self.db_file,'r')
    lines = f.readlines()
    f.close()
    if lines:
      sys.stdout.write(lines[-1])

  def show_all_tasks(self):

    f = open(self.db_file,'r')
    task_text = f.read()
    f.close()
    sys.stdout.write(task_text) 

  def pop(self):

    f = open(self.db_file,'r')
    lines = [ line for line in f.readlines() if len(line)]
    f.close()

    f = open(self.db_file,'w')
    f.truncate() # 0 it
    f.write(''.join(lines[:-1]))
    f.close()

    f = open(self.db_file,'r')
    lines = [ line for line in f.readlines() if len(line)]
    f.close()
    sys.stdout.write(''.join(lines))

  def clean():
    pass

  def clear(self):
    f = open(self.db_file,'w').close()
