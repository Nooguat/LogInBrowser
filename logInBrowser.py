import sublime
import sublime_plugin
import webbrowser
from .handle_SE_parameters import *
import os


class Log_to_browserCommand(sublime_plugin.TextCommand):
    def run(self, edit, **args):
        file_extension = self.view.window().extract_variables()[
            'file_extension']
        sel_texts = self.view.sel()
        file_id = file_id = str(hash(os.path.abspath(self.view.file_name())))
        print(file_extension, " ", file_id)

        if exist("[FILE LINKS]", str(file_id)) is True:
            query = get("[FILE LINKS]", str(file_id))
            self.load_query(sel_texts, query)
            return
        if exist("[FILE EXT LINKS]", file_extension) is True:
            query = get("[FILE EXT LINKS]", file_extension)
            self.load_query(sel_texts, query)
            return
        query = get("[SEARCH ENGINE]", "", True)
        self.load_query(sel_texts, query)

    def load_query(self, sel_texts, query):
        for sel_text in sel_texts:
            command = query.replace("_QUERY_", self.view.substr(sel_text))
            webbrowser.open_new_tab(command)
