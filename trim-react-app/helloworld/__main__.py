import sys
import logging
from os import path
import os


def main():
    if(len(sys.argv) != 2):
        logging.warning('takes one argument: "trim"')
        print(sys.argv[1])
        return None
    print('Trimming your Create React app project!...')
    args = sys.argv[1]
    # files
    srcDest = os.getcwd() + r'\src'
    Appjs = srcDest + r'\App.js'
    Appcss = srcDest + r'\App.css'
    Apptest = srcDest + r'\App.test.js'
    indexcss = srcDest + r'\\index.css'
    indexjs = srcDest + r'\\index.js'
    logosvg = srcDest + r'\\logo.svg'
    serviceWorkerjs = srcDest + r'\\serviceWorker.js'
    # Block where we do things
    if(path.isfile(Appjs) and args == 'trim'):
        length = len(args)
        with open(Appjs, 'r') as f:
            lines = f.readlines()
            for i, line in enumerate(lines):
                if(line == "import logo from './logo.svg';\n"):
                    lines[i] = '//removed\n'
        with open(Appjs, 'w') as trimmed:
            trimmed.writelines(lines)
            # -----------------------------
    else:
        if not (args == 'trim'):
            logging.warning('\n Valid arguments:')
            print('\ntrim')
        else:
            print('incorrect directory')

    # my_function('hello world')
    # my_object = MyClass('Thomas')
    # my_object.say_name()
if __name__ == '__main__':
    main()
