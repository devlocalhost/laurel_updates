# How to go back to Stock ROM

1. [Download and extract](/blog/stock-rom-links) the fastboot package of Stock ROM. After extracting, you should see these files: ![image of extracted archive](/static/img/im1.png)
2. Download platform_tools version 33.0.3 for your platform: [Linux](https://dl.google.com/android/repository/platform-tools_r33.0.3-linux.zip), [Windows](https://dl.google.com/android/repository/platform-tools_r33.0.3-windows.zip), [MacOS](https://dl.google.com/android/repository/platform-tools_r33.0.3-darwin.zip), then follow [this guide](https://wiki.lineageos.org/adb_fastboot_guide#installing-adb-and-fastboot). This is required, because recent versions of platform_tools have a bug.
3. After that, go back to the directory/folder you extracted the fastboot package, and open a terminal window there (on windows, you can do that by right clicking in a empty space, then clicking "open terminal". On other platforms, you can use the `cd` command).
4. Execute this command: `fastboot devices`. The expected output is this: ![image of terminal window showing the output of fastboot devices](/static/img/im2.png)
	1. If the output is different, and you do not see your device, follow [this guide (windows)](https://gist.github.com/luk1337/4bfab1d19ee472307f9077fba872d037). For other platforms, check your udev rules (?).
5. Now execute this command: `fastboot set_active a`. This will change the slot to a, since stock ROM boots only in slot a.
6. To finally flash stock ROM, execute the `flash_all` script. On windows, type `.\flash_all.bat` on the terminal, and on Linux/MacOS `./flash_all.sh`. The script then will start to flash the images.
7. After the script finishes doing its job, you should be good to go! Enter this last command: `fastboot reboot` to reboot the device.
8. (Optional) Your phone is still unlocked. If you wish to lock it (the bootloader), first make sure the phone boots and everything is fine. If things look good, reboot the device to fastboot mode again, and run this command: `fastboot flashing lock`. This will lock the bootloader. That means, if you'd like to flash anything again, you must unlock it again.

If you're facing any issues, you can ask for support on [Mi A3 | OFFICIAL](https://t.me/A3Official) telegram group.
