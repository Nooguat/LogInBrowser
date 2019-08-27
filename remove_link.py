import sublime
import sublime_plugin
from .handle_SE_parameters import *


class Remove_linkCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        links = list()
        self.file_id = str(hash(os.path.abspath(self.view.file_name())))
        self.file_extension = self.view.window().extract_variables()[
            'file_extension']
        if exist("[FILE LINKS]", self.file_id):
            links.append("file link")
            self.in_ = 1
        if exist("[FILE EXT LINKS]", self.file_extension):
            links.append("file extension link")
            self.in_ = 2
        if len(links) == 0:
            msg = "No SE links detected for this file"
            sublime.message_dialog(msg)
            return
        if len(links) == 2:
            self.in_ = 3
        sublime.Window.show_quick_panel(
            self.view.window(), links, self.on_done)

    def on_done(self, index):
        print(index, self.in_)
        if self.in_ == 2 or index == 1:
            remove('[FILE EXT LINKS]', self.file_extension)
            return

        if self.in_ == 1 or index == 0:
            print("test1")
            remove('[FILE LINKS]', self.file_id)
            return
