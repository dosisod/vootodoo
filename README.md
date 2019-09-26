# vootodoo

Terminal-based todo manager

Vootodo is a python based todo manager with a simple command-line interface

Five files deep into your project? Keep it in your project root, Vootodoo will find the nearest `.todo` file for you

## Installing

Download:

`git clone https://github.com/dosisod/vootodo.git`

Bind `vtd` command to `main.py` file:

`alias vtd="python3 /absolute/path/to/vootodoo/main.py"`

Put above line into your `.bashrc` to stay persistent

### Setup

Create a `.todo` file using `vtd init`

This will prompt you to setup a file in whichever directory you choose, from the current directory to the home directory

If an existing file is found, vootodoo will skip it

## HELP

```
USAGE: python3 main.py [Command] [Params]

(No command)  - Print all tasks
h[elp]        - This message
i[nit]        - Make .todo file
a[dd] STR     - Add STR to todo list
r[m] NUM      - Removes task NUM from list
r[m] NUM,NUM  - Removes comma-seperated list of tasks from list
impor[t] STR  - Import an existing file STR to a .todo file
s[earch] STR  - Search and print tasks that match substring STR
rege[x] REG   - Search and print tasks that match regex REG
c[lean]       - Cleans current file of newlines and whitespace
v[im]         * Open list in vim
v[im] REG     * Open list in vim with regex REG highlighted
```
