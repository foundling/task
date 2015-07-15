## Task

MEMT is a command-line task management tool.  It's right now only for singles.  The default allows only single words without description to identify tasks. You can mark tasks done with an 'x', remove a task by number, or the most recent, clear all the tasks, or just view the last one.  I envision it as a short-game tool when it comes to command-line creative work.  It also may just be completely useless, we'll see.

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

#### review command-line hierarchy semantics with what people will probably do in mind, from most to least frequent
- looking
- adding
- marking last as done
- seeing last
- clearing
- 

+ change name
  - memt
  - mem
  - mt

+ improve config to allow at least the following:
  - an optional history on two levels:
    + one: precede a completed task with an 'x' instead of deleting it, so you can see what you completed
    + two: offer some stats on when the tasks were completed use a decorator to write dates/times somewhere upon each write (maybe use a decorator)

