

CUR_DIR=$(cd $(dirname $0); pwd)
cd ${CUR_DIR}

ansible-config init > ansible.cfg
# ansible-config init --disabled -t all > ansible.cfg