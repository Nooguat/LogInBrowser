import sublime
import sublime_plugin
from .handle_SE_parameters import *


class Add_search_engineCommand(sublime_plugin.TextCommand):

    def run(self, edit):

        self.view.window().show_input_panel(
            "insert search engine name", "", self.on_done_name, None, None)

    def on_done_name(self, string):
        if exist("[SEARCH ENGINE]", string) is True:
            msg = string + " already exist in SE  file ! Use modify SE instead"
            sublime.message_dialog(msg)
            return 0
        self.name = string
        self.view.window().show_input_panel(
            "insert search engine query", "replace the query location by _QUERY_", self.on_done, None, None)
        print(string)

    def on_done(self, string):
        if '_QUERY_' not in string:
            msg = "Please insert _QUERY_ ; your SE query is " + string
            sublime.message_dialog(msg)
            return 0
        set_new("[SEARCH ENGINE]", self.name, string)
