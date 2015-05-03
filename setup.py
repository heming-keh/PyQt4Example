# coding=utf-8

from distutils.core import setup
import py2exe

options = {'py2exe': 
        {'bundle_files': 1, # bundle dlls in the zipfile or the exe
        'includes': ['sip', 'functools'], # pyqt需要
        'dll_excludes': ['w9xpopen.exe', 'msvcp90.dll'], # 不使用popen，更不用需要支持win98
        'compressed': True, # 压缩
        'optimize':2,   # 优化，使用其不含doc
        'excludes': ['_ssl', 'pyreadline', 'difflib', 'doctest', 'locale',
            'optparse', 'pickle', 'calendar',
            'pdb', 'unittest', 'inspect',
            'bz2', 'select', 'unicodedata'],    # 去除一些不常用的类库
        'ascii': False, # 这是默认的值，如果不使用其它字符编码，可以改变True
        }}
windows = [
        {'script': 'notepad.py',
            'icon_resources': [(0, 'ico/logo.ico')]}    # 图标
        ]
setup(windows = windows,
        options = options,
        zipfile = None,  # 将zip文件打包进exe
        )
