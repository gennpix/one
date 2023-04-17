# coding:utf8
import subprocess


def exec_cmd(cmd, error_raise=False):
    p = subprocess.Popen(
        cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True
    )
    outs = []
    for line in iter(p.stdout.readline, b""):
        outs.append(line.decode("utf-8"))

    for line in iter(p.stderr.readline, b""):
        outs.append(line.decode("utf-8"))

    p.stdout.close()
    p.wait()
    
    if error_raise and p.returncode != 0:
        print("".join(outs))
        raise TPPluginError("[ERROR] 执行命令失败:{}".format(cmd))

    return p.returncode, "".join(outs)


class TPPluginError(RuntimeError):
    pass
