package main

import (
	"fmt"
	"github.com/helloyi/go-sshclient"
	"golang.org/x/crypto/ssh"
	"net"
	"strings"
	"time"
)

var loadConfigScript = strings.Join(
	[]string{
		"if [[ \"${SHELL}\" =~ \"zsh\" && -f ~/.zshrc ]]; then",
		"    source ~/.zshrc >/dev/null 2>&1 || true",
		"elif [[ \"${SHELL}\" =~ \"bash\" && -f ~/.bashrc ]]; then",
		"    source ~/.bashrc >/dev/null 2>&1 || true",
		"fi",
	}, "\n")

var checkHealthScripts = `
if [ -f /etc/os-release ]; then
    . /etc/os-release
    OS=$NAME
    VER=$VERSION_ID
elif type lsb_release >/dev/null 2>&1; then
    # linuxbase.org
    OS=$(lsb_release -si)
    VER=$(lsb_release -sr)
elif [ -f /etc/lsb-release ]; then
    # For some versions of Debian/Ubuntu without lsb_release command
    . /etc/lsb-release
    OS=$DISTRIB_ID
    VER=$DISTRIB_RELEASE
else
    # Fall back to uname, e.g. "Linux <version>", also works for BSD, etc.
    OS=$(uname -s)
    VER=$(uname -r)
fi
echo NAME=\"$OS\"
`

func runScript() {
	//client, err := DialWithPasswd("10.28.132.44:22", "root", "whFsctmp_044", 5*time.Second)
	client, err := DialWithPasswd("103.21.117.58:36000", "root", "Meiyisi@123", 5*time.Second)
	if err != nil {
		fmt.Println("conn failed.", err)
	}
	defer client.Close()

	//out, err := client.Script(loadConfigScript + "\n" + checkHealthScripts).Output()
	out, err := client.Script("pwd").Output()
	if err != nil {
		fmt.Println("exec failed.", err)
	}
	fmt.Println(string(out))
}

func DialWithPasswd(addr, user, passwd string, connTimeout time.Duration) (*sshclient.Client, error) {
	config := &ssh.ClientConfig{
		User: user,
		Auth: []ssh.AuthMethod{
			ssh.Password(passwd),
		},
		HostKeyCallback: ssh.HostKeyCallback(func(hostname string, remote net.Addr, key ssh.PublicKey) error { return nil }),
		Timeout:         connTimeout,
	}

	return sshclient.Dial("tcp", addr, config)
}

func main() {
	runScript()
}
