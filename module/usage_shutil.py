#!/usr/bin/env python

import shutil

def main():
    """
    about file copy
    """

    # will name file copy name_1 file only copy file content
    #shutil.copyfile('name', 'name_1')

    # will name file copy name_2 file, include copy file content and file limit
    #shutil.copy('name', 'name_2')

    # will test file zip name.tar.gz file
    shutil.make_archive('name', 'gztar', root_dir='test')


if __name__ == "__main__":
    main()
