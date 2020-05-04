# SC-REPL Plugin Template

Plugin template for [SC-REPL](https://github.com/mighty1231/screpl)

## Plugin

* Each SC-REPL plugin has a form of python package.
* Each plugin consists of one \_\_init\_\_.py file and multiple application files.
* You can add your commands for REPL on \_\_init\_\_.py
* You can define apps with python codes.

## How to develop

* [SC-REPL](https://github.com/mighty1231/screpl) installation is required.
* Modify your euddraft project file (\*.edd) as follows.

```
[prepl]
superuser: P1
plugins: OTHER_PLUGINS myplugin
```

* Place your plugin on `euddraft/lib` or the directory which contains euddraft project file, `your_project.edd`.

```bash
euddraft0.*.*.*
├── lib
│   ├── repl
│   ├── plugins  // plugins provided by REPL
│   └── myplugin
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
├── myplugin
│   ├── __init__.py
│   ├── app1.py
│   ├── app2.py
│   ...
│   └── appN.py
└── your_project.edd
```
* You may use many functionalities of `eudplib`. You can visit [here](https://cafe.naver.com/edac) to get some information.
