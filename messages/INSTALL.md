# Open Smerge
> This is a package open `Sublime Merge` in `Sublime Text`.  
> Matches all git repositories based on the path to the current file and the folders in project.  


## How To Use
1. install [Sublime Merge](https://www.sublimemerge.com/)
2. If not the default installation, please configure the `smerge` path in sublime-setting.
3. this package matches all git repositories based on the path to the current file and the folders in project.  


## Bugs  
create a issee to [issues](https://github.com/FloydaGithub/open-smerge/issues)  


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
