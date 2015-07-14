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

def get_task():

def 

def main():

  db = DB(config['config_file'])

  if len(sys.argv) < 2:
    usage()
    sys.exit()

  else:
    action, tasks = sys.argv[1], sys.argv[2:]
    if action == 'add':
      add_tasks(db,tasks)
      print action + 'ing' + ','.join(sys.argv[2:])

    if action == 'top':
      get_latest_task(db)

    if action == 'pop':
      remove_task(-1)

main()
