## MEMT

#### Some use cases

Sometimmes when I'm working, i might have an interesting idea and in comes my more productive self, basically pulling rank with a cordial SIGTERM.  I forget whatever idea I had in my head but would like it back.

Other times, when i'm working on an especially tough part of a project, I have one wrong idea for a while and then all of a sudden, I get a lot of ideas at once. It's nice to be able to store that info in rapid, succint succesion.

Plus, with all the reading and digesting of stuff, the need for a list becomes clearer.  But not a list to end all lists. Just a normal, functional list, that keeps your thoughts ... sorry, memts ... as long as you think they're valid.

`memt` is a command-line task/idea management tool that aims to be minimal by allowing only single words without description to identify particular actions you want to remember to do. Or ideas that you had. Or albums you liked. You can mark memts as done with an 'x', remove a memt by number, remove the most recent memt, clear all the memts, view them all or just view the most recent one.  I envision it as a memory tool for command-line creative work.  It also may just be completely useless, we'll see.

MEMT will install a .memtrc and .memt/memt.db in your $HOME directory. 

`.memtrc` should soon provide some configurations, which are currently listed in the `To Do` section.

The database is just a flat file.

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

memt clear (clears all memts)

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

+ Configurations to provide through the .memtrc
  - sentence mode ( all args after 'add' are turned back into a sentence )
  - analytics on (default off)
  - choose default list (including some sensible programmatic defaults so you're not tied to a single file)
  
+ Load and store multiple lists
  
