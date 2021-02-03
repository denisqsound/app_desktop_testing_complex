from cx_Freeze import setup, Executable

executables = [Executable("app.py")]

excludes = ['logging', 'unittest', 'email', 'html', 'http', 'urllib', 'xml', 'bz2']

options = {'build_exe': {'excludes': excludes}}

setup(name="app-testing-complex",
      version="1.0.1",
      executables=executables,
      options=options)
