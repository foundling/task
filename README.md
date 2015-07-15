## MEMT

  `memt` is a command-line memt management tool.  It's right now only for singles.  The default allows only single words without description to identify memts. You can mark memts done with an 'x', remove a memt by number, or the most recent, clear all the memts, or just view the last one.  I envision it as a short-game tool when it comes to command-line creative work.  It also may just be completely useless, we'll see.

## Installation - just Unix & BSD so far ... :( 

+ put the top-level directory in your path
+ run `memt`


## Usage: 

```

memt (prints out current memts)

memt -h, --help (prints this usage message)

memt add <memt1> <memt2> <memt3> ... (adds memts one by one)

memt pop (removes top of stack)

memt top (shows top of stack)

memt clear (clears memt)

** not implemented **

memt rm [N] (clears item N from the top of the stack )

memt ins[N] (inserts element at position x in memt array)



What is a memt?
a <memt> is by default a single word describing a memt you want to get done.
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
    + one: precede a completed memt with an 'x' instead of deleting it, so you can see what you completed
    + two: offer some stats on when the memts were completed use a decorator to write dates/times somewhere upon each write (maybe use a decorator)

