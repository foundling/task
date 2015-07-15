## Task
A really simple command-line task manager

## Installation - just Unix & BSD so far ... :( 

+ put the top-level directory in your path
+ run `task`


## Usage: 

```

task (prints out current tasks)

task -h, --help (prints this usage message)

task add <task1> <task2> <task3> ... (adds tasks one by one) 

task pop (removes top of stack)

task top (shows top of stack)

task clear (clears task)

** not implemented **

task rm [N] (clears item N from the top of the stack )

task ins[N] (inserts element at position x in task array)



What is a task?
a <task> is by default a single word describing a task you want to get done.
Quote your input to store a multiple-word sequence.
``` 


## To Do
+ improve config to allow at least the following:
  - precede a completed task with an 'x' instead of deleting it, aka an optional history
