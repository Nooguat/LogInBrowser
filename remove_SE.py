import sublime
import sublime_plugin
from .handle_SE_parameters import *


class Remove_search_engineCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        self.se = get_all_values("[SEARCH ENGINE]")
        sublime.Window.show_quick_panel(
            self.view.window(), self.se, self.on_done)

    def on_done(self, index):
        remove_SE = self.se[index].split(" > ")[0]
        if remove_SE == "default":
            msg = "Impossible to remove the default search engine !"
            sublime.message_dialog(msg)
            return
        remove("[SEARCH ENGINE]", remove_SE)
