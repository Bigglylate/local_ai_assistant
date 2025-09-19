@echo off
echo ==============================
echo Starting Local AI Assistant
echo ==============================

:: ---------------------------------
:: Start Backend 
:: ---------------------------------

echo Starting Backend....
cd backend

::Check if venv is already active
if "% VIRTUAL_ENV%"=="" (
	echo Activating virtual environment...
	call venv\Scripts\activate
) else (
	echo Virtual environment already active.
)
start cmd /k "uvicorn app.main:app --reload"
cd ..

::---------------------------------
:: Start Frontend
::---------------------------------

echo Starting frontend...
cd frontend
start cmd /k "npm run dev"
cd ..

echo ==============================
echo Both frontend and backend are running
echo =============================
pause