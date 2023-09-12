# https://docs.ansible.com/ansible/latest/command_guide/intro_adhoc.html#intro-adhoc

CUR_DIR=$(cd $(dirname $0); pwd)
cd ${CUR_DIR}

# 使用 ANSIBLE_PYTHON_INTERPRETER = auto_silent 或 auto_legacy_silent 禁用自动发现 python interpreter 的警告
# 也可指定 python 解释器路径，比如 ANSIBLE_PYTHON_INTERPRETER=/usr/bin/python3
export ANSIBLE_PYTHON_INTERPRETER=auto_silent

# 需要先配置好免密：ssh-copy-id xin@127.0.0.1
ansible -i inventory/hosts.ini test -m ping -u xin

# 使用 ANSIBLE_INVENTORY 改变默认 inventory 路径
export ANSIBLE_INVENTORY=$CUR_DIR/inventory/hosts.yaml
ansible all -m ping -u xin

# 验证 Inventory 文件
ansible-inventory -i inventory/hosts.yaml --list
