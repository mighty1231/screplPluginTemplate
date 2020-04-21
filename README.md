# SC-REPL Plugin Template

Plugin template for [SC-REPL](https://github.com/mighty1231/screpl)

## Plugin

* SC-REPL plugin is a simple directory.
* \_\_init\_\_.py makes the directory be package, you can add your commands for REPL
* Also, you can define apps.

## How to develop

* SC-REPL installation is required.
* Modify your euddraft project file as follows.

```
[prepl.py]
superuser: P1
plugins: OTHER_MODULES mymodule
```

* Place your plugin on `euddraft` or the folder which contains `make.edd`.

```bash
euddraft0.*.*.*
├── lib
│   ├── repl
│   ├── apps (apps provided by SC-REPL)
│   └── mymodule
│       ├── __init__.py
│       ├── app1.py
│       ├── app2.py
│       ...
│       └── appN.py
├── plugins
│   └── prepl.py
└── euddraft.exe
```

or

```bash
YOUR_PROJECT
├── mymodule
│   ├── __init__.py
│   ├── app1.py
│   ├── app2.py
│   ...
│   └── appN.py
└── make.edd
```
