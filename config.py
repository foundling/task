import os
import sys

home = os.path.expanduser('~')


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
