mkdir Patched_Roms
for %%f in (*.bs) do copy "%%f" .\Patched_Roms
for /r  ./Patched_Roms %%v in (*.bs) do BSX_Patcher.py "%%v"
