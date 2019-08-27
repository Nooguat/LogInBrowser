import sublime
import sublime_plugin
from .handle_SE_parameters import *


class Mod_search_engineCommand(sublime_plugin.TextCommand):

    def run(self, edit):
        search_engines = get_all_values("[SEARCH ENGINE]")
        search_engines = [k.split('>')[0] for k in search_engines]
        sublime.Window.show_quick_panel(
            self.view.window(), search_engines, self.on_done_SE)

    def on_done_SE(self, index):
        search_engines = get_all_values("[SEARCH ENGINE]")
        self.name = search_engines[index].split(" > ")[0]
        self.view.window().show_input_panel(
            "insert new search engine query", "replace the query location by _QUERY_", self.on_done, None, None)

    def on_done(self, string):
        if '_QUERY_' not in string:
            msg = "Please insert _QUERY_ ; your SE query is " + string
            sublime.message_dialog(msg)
            return 0
        set_new("[SEARCH ENGINE]", self.name, string, True)
