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
