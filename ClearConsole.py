import sublime
import sublime_plugin

class ClearConsoleCommand(sublime_plugin.ApplicationCommand):
    """ Plugin to 'clear' the console by printing newlines """

    def run(self):
        """ Print the amount of newlines specified by the settings (100 by default) """
        settings = sublime.load_settings('ClearConsole.sublime-settings')
        newline_count = settings.get('newline_count') or 100
        print('\n' * newline_count)
