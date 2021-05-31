@echo off 

PUSHD %~dp0
SET script_dir=%CD%
POPD

CALL %script_dir%\venv\Scripts\activate.bat
python %script_dir%\nv_pdfmerge.py %1
