from cx_Freeze import setup, Executable

setup(
    name="MyApp",
    version="1.0",
    description="My Description",
    executables=[Executable("app.py")]
)
