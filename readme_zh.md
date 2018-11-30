# Open Smerge | [English](./readme.md)  

> 这是一个在`Sublime Text`中打开`Sublime Merger`的插件.  
> 根据`当前文件的路径`和`项目`去匹配所有的git仓库.  


## 安装  
- Git  
    克隆这个仓库到Sublime的Packages目录下  
    ```sh  
    git clone https://github.com/FloydaGithub/open-smerge.git
    ```

- Package Control  
    暂时不支持  


## 环境  
> ctrl + shift + P -> Open Merge: Settings  
> Menu -> Preferences -> Package Settings -> OpenMerge -> Setting  

将smerge的安装路径加到PATH中, 或者在设置中配置路径:  
```
{
    "smerge_path": "C:\\Program Files\\Sublime Merge\\smerge.exe"
}
```


## 快捷键  
> ctrl + shift + P -> Open Merge: Key Bindings  
> Menu -> Preferences -> Package Settings -> OpenMerge -> Key Bindings  

```py
[
    { 
        "keys": ["ctrl+alt+m"], "command": "open_smerge"
    }
]

```
