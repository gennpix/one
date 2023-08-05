# ssh

1. 免交互生成 rsa 私钥

    ```shell
    ssh-keygen -t rsa -P "" -f ~/.ssh/id_rsa
    ```

2. 更新 known_hosts

   ```shell
    TARGET_HOST=[hostname or IP]

    # remove the old keys from know_hosts
    ssh-keygen -R $TARGET_HOST

    # add the new keys(s) to know_hosts
    ssh-keyscann -H $TARGET_HOST >> ~/.ssh/known_hosts
   ```

3. ssh 时忽略known_hosts 检查

   ```shell
   ssh -o StrictHostKeyChecking=no -l <user> -i ~/.ssh/private_key_file
   ```
