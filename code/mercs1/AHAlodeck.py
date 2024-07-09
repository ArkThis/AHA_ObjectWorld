# This Python file uses the following encoding: utf-8
import xattr
import argparse
from pprint import pprint


class AHAlodeck():

    def __init__(self, main_window):
        window = main_window
        self.metadata: list = []
        # super().__init__(parent)
        print("Roger: Init.")
        print("Window: {}".format(window.windowTitle()))

    def get_args(self):
        parser = argparse.ArgumentParser(
            prog='RightClickEditMetadata',
            description='What you\'ve always dreamed of: Simply right-click and: Edit. Save.',
            epilog='Text at the bottom of help')

        parser.add_argument('file')

        return parser

    def longestWord(self, data):
        maximum = 0
        for i in data:
            length = len(i)
            if length > maximum:
                maximum = length
                word = i
        return word

    ##
    # Converts byte-sequence list to unicode.
    #
    def BinToUnicode(self, metadata):
        text = []
        for key, value in metadata:
            keyvalue = [
                    key.decode("utf-8"),
                    value.decode("utf-8")
                    ]
            text.append(keyvalue)

        return text

    ##
    # Read xattr (POSIX eXtended ATTRibutes) key/value metadata about "a file" from
    # the filesystem.
    #
    def get_keys(self, file):
        #md_keys = xattr.listxattr(file)
        md_keys = xattr.list( file)
        return md_keys

    ##
    # Expects a tuples list [(), ()]
    # or nested lists?
    #
    def get_values(self, metadata):
        #pprint(metadata) # DEBUG DELME
        kv_list = list(zip(*metadata))  # 😘️ to Python! this is beautiful.
        return kv_list

    def init_parameters(self):
        # Read CLI arguments/parameters:
        self.parser = self.get_args()
        self.args = self.parser.parse_args()
        print(self.args.file)

        # Read xattr metadata:
        self.metadata = xattr.get_all(self.args.file)
        # TODO: convert that dictionary to a table structure so we can use it as data in our widget:
        return self.metadata
