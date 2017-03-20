echo wind_dr.py, download data from wind
echo PyAnalysis.py

taskkill /f /im WBox.exe
taskkill /f /im wim.exe

cd ..\PyWind2
python .\wind_dr.py -m dd -s trading -tf eod -cc y

cd ..\PyAnalysis
python .\PyAnalysis.py -ucf underlying.ini -r cs bf -tsdiff 0 -ex 5
python .\month_list.py -r cs bf

taskkill /f /im WBox.exe
taskkill /f /im wim.exe