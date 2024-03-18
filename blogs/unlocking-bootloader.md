# How to unlock the bootloader

NOTE: Your data WILL BE ERASED. TAKE A BACKUP. No, there is NOT any method without erasing. Also, a PC is needed.

## Installing platform_tools
Check the tutorial [here](/help/platform-tools)

## Getting the phone ready
We have to enable OEM unlocking on the phone. To do that, we have to enable "developer options". Go to phone settings, about phone, scroll down till you see "build number" and click it 7 times. It will ask for your password, enter it, and thats it. "Youre a developer!!".

Go back to settings, go to system, advanced, developer options, scroll a bit down and you should see "enable oem unlocking". Enable it, and we are now one step closer

## Unlocking the bootloader
To unlock the bootloader, we have to boot into fastboot mode. To reboot into fastboot mode, reboot your phone, and hold the volume down key. If done correctly, you will see a bunny logo and "fastboot".

Connect your phone with your PC using a cable, on your PC, go to the platform_tools you extracted earlier, and open cmd right there (right clicking on a blank space while being in the platform_tools folder should show a "open command prompt here" or something like that).

Then, type `fastboot flashing unlock`. This is the first command. If your phone reboots, reboot back to fastboot. Now, the second command: `fastboot flashing unlock_critical`. And thats it, you have successfully unlocked the bootloader!

# Any ROM suggestion?
Sure. [LineageOS (21)](/roms/LineageOS_14). More ROMs available [here](/roms).

## But how do i install it??
Click one of the links, or click the "ROMs" tab. Find a ROM. Join the support forum/group. If its a telegram group, there is 100% a installation note. Enter the chat, and either ask or type `/notes`

# Ok, what about custom kernels?
There are only 2: [No.912/No.33](/kernels/no912), and [NoName/Xavis](/kernels/noname) kernel. Note: 4.14 kernel is deprecated, so, dont really expect any linux kernel upgrades.
