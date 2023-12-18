# Fix bootloop caused by a magisk module

There are two methods to save yourself from a bootloop CAUSED BY A MAGISK MODULE:

## Booting into safe mode
1. Hold power button so the phone reboots
2. When you see the boot animation, hold the volume down button AND KEEP HOLDING till you feel a vibration. If you don't feel a vibration, wait and see if it boots. If it doesn't boot, start from step 1 again

Then, reboot to get out of safe mode when the phone boots, and you should be able to boot. Note: all of your modules WILL be disabled

## Using a magisk module
Flash [huskydg's bootloop saver module](https://laurelupdates.dev64.workers.dev/HuskyDG_BootloopSaver.zip) on magisk

And that's it. Next time you face a bootloop, your phone should reboot automatically. Could take some time but it will. When a bootloop is detected, the module will disable all modules and reboot. Note: you have to reflash the module EVERY TIME you change the kernel
