# Open Smerge | [中文读我](./readme_zh.md)  

> This is a package open `Sublime Merge` in `Sublime Text`.  
> Matches all git repositories based on the path to the current file and the folders in project.  


## Install  
- Git  
    git clone this repository to sublime packages folder  
    ```sh  
    git clone https://github.com/FloydaGithub/open-smerge.git
    ```

- Package Control  
    Temporarily not supported  


## Environment
> ctrl + shift + P -> Open Merge: Settings  
> Menu -> Preferences -> Package Settings -> OpenMerge -> Setting  

Add smerge installation path to `$PATH`, Or configure the path in sublime-settings:  
```
{
    "smerge_path": "C:\\Program Files\\Sublime Merge\\smerge.exe"
}
```


## Keymap  
> ctrl + shift + P -> Open Merge: Key Bindings  
> Menu -> Preferences -> Package Settings -> OpenMerge -> Key Bindings  

```py
[
    { 
        "keys": ["ctrl+alt+m"], "command": "open_smerge"
    }
]

```
