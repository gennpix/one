# zsh

1. zsh-autosuggestions插件导致粘贴内容很慢的问题
   zsh开启autosuggestions 插件的时候，在终端中粘贴大量的内容的时候，会粘贴的很慢，基本上是一个字符一个字符的粘贴的。
   解决方法：

   ```shell
   vi ~/.zshrc  # 增加如下内容
    # This speeds up pasting w/ autosuggest
    # https://github.com/zsh-users/zsh-autosuggestions/issues/238
    pasteinit() {
        OLD_SELF_INSERT=${${(s.:.)widgets[self-insert]}[2,3]}
        zle -N self-insert url-quote-magic 
        # I wonder if you'd need `.url-quote-magic`? 
    }

    pastefinish() {
        zle -N self-insert $OLD_SELF_INSERT
    }
    zstyle :bracketed-paste-magic paste-init pasteinit
    zstyle :bracketed-paste-magic paste-finish pastefinish
   ```

   立即生效： `source ./zshrc` 或者 `. ~/.zshrc`。
