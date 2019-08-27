import sublime
import sublime_plugin
from LogInBrowser.handle_SE_parameters import *
import os


class Link_search_engine_fileCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        self.file_id = str(hash(os.path.abspath(self.view.file_name())))
        if exist("[FILE LINKS]", self.file_id):
            msg = "a link already exists between this file and a SE !"
            sublime.message_dialog(msg)
            return
        self.win_name = self.view.file_name()
        search_engines = get_all_values("[SEARCH ENGINE]")
        search_engines = [k.split(' > ')[0] for k in search_engines]
        sublime.Window.show_quick_panel(
            self.view.window(), search_engines, self.on_done)

    def on_done(self, index):
        liste = get_all_values("[SEARCH ENGINE]")
        request = liste[index].split(' > ')[1]
        set_new("[FILE LINKS]", str(self.file_id), request)
        return


class Link_search_engine_file_extensionCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        self.file_extension = self.view.window().extract_variables()['file_extension']
        if exist("[FILE EXT LINKS]", self.file_extension):
            msg = "a link already exists between this file extension and a SE !"
            sublime.message_dialog(msg)
            return
        search_engines = get_all_values("[SEARCH ENGINE]")
        search_engines = [k.split(' > ')[0] for k in search_engines]
        sublime.Window.show_quick_panel(
            self.view.window(), search_engines, self.on_done)

    def on_done(self, index):
        liste = get_all_values("[SEARCH ENGINE]")
        request = liste[index].split(' > ')[1]
        set_new("[FILE EXT LINKS]", self.file_extension, request)
        return
