import os
import sys

home = os.path.expanduser('~')

usage = '''
   usage: 

     task top (shows top of stack)

     task pop (removes top of stack)

     task add <task1> <task2> <task3> ... (adds tasks one by one) 

       <task> is a single word describing the task.
       Quote your input to express a multiple-word sequence
 
'''




config = { 
  'data': {},
}
config['data']['data_dir'] = os.path.join(home,'.task')
config['data']['database_file'] = os.path.join(
   config['data']['data_dir'],'task.db'
)
config['data']['config_file'] = os.path.join(home,'.taskrc')


if __name__ == '__main__':
  for v in config['data'].itervalues():
    print v
