from cx_Freeze import setup, Executable
base = "Win32GUI"
executables = [Executable("app.py",
                          targetName='test.exe',
                          base=base,
                          icon='img.ico')]

excludes = ['logging', 'unittest', 'email', 'html', 'http', 'urllib', 'xml', 'bz2']
include_files = ['question.json', 'config.py']
zip_include_packages = ['collections', 'encodings', 'importlib', 'distutils', 'json', 'pydoc_data', 'tkinter',
                        '_bisect.cpython-39-darwin.so']

options = {
    'build_exe': {'excludes': excludes,
                  'zip_include_packages': zip_include_packages,
                  'build_exe': 'build_windows',
                  'include_files': include_files}}

setup(name="app-testing-complex",
      version="1.0.1",
      executables=executables,
      options=options)
