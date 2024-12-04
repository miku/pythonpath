# Ansible Module

> Modules are expressed as code, usually in Python, and contain metadata that
> defines when and where a specific automation task is executed and which users
> can execute it. -- [What is an ansible module](https://www.redhat.com/en/topics/automation/what-is-an-ansible-module)

Any language can be used, e.g. bash:

```
$ tree
.
├── custom.yml
├── library
│   └── hello
├── Makefile
└── README.md

2 directories, 4 files
```

Where does ansible look for modules?

```
$ ansible-config dump | grep DEFAULT_MODULE_PATH
DEFAULT_MODULE_PATH(default) = ['~/.ansible/plugins/modules', '/usr/share/ansible/plugins/modules']
```

Run a standalone module, the module needs to be on some path. See also: [https://docs.ansible.com/ansible/latest/dev_guide/developing_locally.html#adding-standalone-local-modules-for-all-playbooks-and-roles](https://docs.ansible.com/ansible/latest/dev_guide/developing_locally.html#adding-standalone-local-modules-for-all-playbooks-and-roles)

``` 
$ ansible localhost -m hello 
[WARNING]: No inventory was parsed, only implicit localhost is available
localhost | FAILED! => {
    "msg": "The module hello was not found in configured module paths"
}
```

Adjust.

```
$ ANSIBLE_LIBRARY=.  ansible localhost -m hello 
[WARNING]: No inventory was parsed, only implicit localhost is available
localhost | SUCCESS => {
    "changed": false,
    "message": "This is a simple bash module."
}
```