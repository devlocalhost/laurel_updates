# Installing Magisk

## Requirements

- An unlocked bootloader
- [platform_tools](/help/platform-tools) installed
- Latest Magisk APK

After meeting these requirements, you can proceed with the installation.

# Installation
## The PC way

1. Open Windows File Explorer and navigate to the platform_tools directory.
2. Click the address bar, type `cmd`, and press Enter. This will open a terminal window in the platform_tools directory.
3. Reboot your phone into recovery mode by typing `adb reboot recovery` or by rebooting the phone and holding the volume up key when the screen goes black.
4. On your phone, click "install" or "apply update" then "apply from adb".
5. On your PC, execute the command `adb sideload` (without quotes) followed by dragging and dropping the Magisk APK into the terminal window. The command should look like this: `adb sideload "C:\...\...\..."`
6. Press Enter and wait for Magisk to finish. If you see "signature verification failed", select "Yes".
7. After finishing, reboot your phone, and you have successfully flashed Magisk.

## The SD Card way

1. Rename the Magisk APK file by replacing ".apk" with ".zip", as only zip files can be sideloaded.
2. Move the renamed file to your SD Card.
3. Reboot your phone into recovery.
4. Click "install update" or "apply update" then choose "apply from SD card" and select the Magisk zip file. If you see "signature verification failed warning", select "Yes"
5. Wait for the installation to complete.
6. After it's done, reboot your phone, and you have successfully flashed Magisk.

## Alternative method

Another method of installing to install magisk, is by patching the boot image of the ROM.

1. Dump/extract the boot image from the rom (if its a fastboot type of ROM, simply click it, and extract the `boot.img` file. If it isnt [you see other files, like payload.bin], you will need to use an [payload_dumper](https://github.com/vm03/payload_dumper))
2. Copy the extracted `boot.img` to your phone
3. Install the magisk APK, and launch it
4. Click on "install, "select and patch a file", and select the `boot.img` file
5. After a few seconds, a new file in your `Download` (`/sdcard/Download`) folder will appear, looking like this: `magisk_patched-xyzxyz-xyzxyz.img`. Copy/move it to your PC
6. Reboot your phone into fastboot mode (reboot, and when the screen goes dark, hold the volume down key)
7. On your PC, go to `platform_tools` ([check the guide](/help/platform-tools)) and launch the terminal, and flash the patched boot image file with fastboot: "`fastboot flash boot `" (dont forget the space), drag and drop the patched image to the cmd window, and press enter. After its done, `fastboot reboot`
8. Launch magisk, if it asks to reboot, do so (direct install), and thats it. You have flashed magisk.
