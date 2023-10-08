# Installing Magisk

## Requirements
- An unlocked bootloader
- platform_tools installed
- Latest Magisk APK

After meeting these requirements, you can proceed with the installation.

## The PC way
1. Open Windows File Explorer and navigate to the platform_tools directory.
2. Click the address bar, type `cmd`, and press Enter. This will open a terminal window in the platform_tools directory.
3. Reboot your phone into recovery mode by typing `adb reboot recovery` or by rebooting the phone and holding the volume down key when the screen goes black.
4. On your phone, click "install" or "apply update" then "apply from adb".
5. On your PC, execute the command `adb sideload` (without quotes) followed by dragging and dropping the Magisk APK into the terminal window. The command should look like this: `adb sideload "C:\...\...\..."`
6. Press Enter and wait for Magisk to finish. If you see "signature verification failed", select "Yes".
7. After finishing, reboot your phone, and you have successfully flashed Magisk.

## The SD Card way
1. Rename the Magisk APK file by replacing ".apk" with ".zip," as only zip files can be sideloaded.
2. Move the renamed file to your SD Card.
3. Reboot your phone into recovery.
4. Click "install update" or "apply update" then choose "apply from SD card" and select the Magisk zip file. If you see "signature verification failed warning", select "Yes"
5. Wait for the installation to complete.
6. After it's done, reboot your phone, and you have successfully flashed Magisk.

