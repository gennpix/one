
CUR_DIR=$(cd $(dirname $0); pwd)
cd ${CUR_DIR}
export ANSIBLE_PYTHON_INTERPRETER=auto_silent
# 需要先配置好免密：ssh-copy-id xin@127.0.0.1
ansible-playbook -i 127.0.0.1, -u xin playbook/main.yaml
