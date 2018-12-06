echo "\nFlock Installer 1.0.1 beta"
echo "\nInstalling core program"
pip install --user Flock_SSG >> install_log.txt
echo "\nInstalling libraries and dependencies"
pip install --user markdown >> install_log.txt
echo "\nCreating preferences directory"
mkdir ~/.flock_preferences/ >> install_log.txt
mkdir ~/.flock_preferences/log/ >> install_log.txt
echo "\nCopying files..."
cp -r assets/Themes/ ~/.flock_preferences/Themes >> install_log.txt
cp -r assets/docs/ ~/.flock_preferences/docs >> install_log.txt
echo "\nInstallation completed\n"
echo "\nTo run Flock type:  \"python -m Flock.flock\"\n\n"
