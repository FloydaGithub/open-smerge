import sublime
import sublime_plugin
import os
import subprocess

# ------------------ Split Line By Floyda ------------------
# Debug
# ------------------ Split Line By Floyda ------------------
DEBUG = False
import time


def log(*args):
    if DEBUG:
        print('[Debug]:', *args)


class timer():
    def __call__(self, func):
        def wrapper(*args, **kwargs):
            stime = time.time()
            ret = func(*args, **kwargs)
            etime = time.time()
            log(func.__name__, etime - stime, args[0])
            return ret

        return wrapper


# ------------------ Split Line By Floyda ------------------


def get_settings():
    setting = sublime.load_settings('open_smerge.sublime-settings')
    return setting


def edit_setting():
    sublime.run_command(
        'edit_settings', {
            "base_file":
            "${packages}/open-smerge/open_smerge.sublime-settings",
            "default":
            "{\n\t\"smerge_path\": \"sublime merge installed path\"\n}"
        })


def open_smerge_setting(path):
    smerge_path = get_settings().get('smerge_path')

    if smerge_path is None:
        if sublime.ok_cancel_dialog("Please set the path to smerge"):
            edit_setting()
        return

    cmd = '"%s" "%s"' % (smerge_path, path)
    err = subprocess.call(cmd, shell=True)
    if err != 0:
        sublime.message_dialog("open smerge faild:[%d]" % err)


def open_smerge(path):
    cmd = 'smerge "%s"' % path
    err = subprocess.call(cmd, shell=True)
    if err != 0:
        open_smerge_setting(path)


@timer()
def get_repo_forward(path, repos={}):
    cpath = os.path.abspath(os.path.join(path, '..'))
    if cpath == path:
        return repos
    for name in os.listdir(cpath):
        dirname = os.path.join(cpath, name)
        if os.path.isdir(dirname) and name == '.git':
            repos[cpath] = cpath
            break
    return get_repo_forward(cpath, repos)


@timer()
def get_repo_back(path):
    repos = {}
    for name in os.listdir(path):
        dirname = os.path.join(path, name)
        if os.path.isdir(dirname):
            if name == '.git':
                repos[path] = path
            else:
                repos = dict(repos, **get_repo_back(dirname))
    return repos


def get_active_fname(window):
    view = window.active_view()
    if view is None:
        return ''
    return view.file_name()


class OpenSmergeCommand(sublime_plugin.WindowCommand):
    def show_repos(self):
        path_list = []
        show_list = []

        for key, value in self.repos.items():
            show_list.append(key)
            path_list.append(value)

        def on_select(x):
            if x != -1:
                open_smerge(path_list[x])

        if len(path_list) == 1:
            open_smerge(path_list[0])
            return

        log('self.repos length:', len(self.repos))
        self.window.show_quick_panel(show_list, on_select)

    def join_repo(self, items):
        if isinstance(items, dict):
            self.repos = dict(self.repos, **items)

    def run(self):
        self.repos = {}

        # Current File
        cname = get_active_fname(self.window)
        if cname:
            self.join_repo(get_repo_forward(cname))

        # Project Folders
        project_data = self.window.project_data()
        if project_data:
            log('project_data:', project_data)
            for project in project_data.get('folders'):
                path = project.get('path')
                self.join_repo(get_repo_back(path))

        self.show_repos()
