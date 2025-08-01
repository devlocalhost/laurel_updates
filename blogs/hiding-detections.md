# Hiding various detections
In this guide, I will show how you can possibly hide detections, such as Custom ROM detected, unlocked bootloader, and more. Keep in mind that this guide isn't guaranteed to work 100%.

## Steps/Requirements
We are going to achieve all this using some root modules. So, if your device is not rooted, you have to do that first. We are also going to use the app "[Native Detector](https://t.me/rootdetector)" to see our progress.

First, **if you are using Magisk**, you should hide Magisk if you haven't so, by going to Settings, and clicking "Hide the Magisk app". Enter anything you want when asked, it does not matter (hopefully). Another important thing is, if you are using the default built-in Zygisk implementation of Magisk, you should disable it and use alternatives such as [Zygisk Next](https://github.com/Dr-TSNG/ZygiskNext) (recommended) or [ReZygisk](https://github.com/PerformanC/ReZygisk) (open source). Built-in Zygisk implementation is easy to detect.

One thing that could also help is deleting the "/data/magisk" (magisk folder in data) folder. If it exists, you can delete it by running the **SAME EXACT** command: `su -c rm -r /data/magisk`

The following modules we are going to use are [NoHello](https://github.com/MhmRdd/NoHello/releases), and [Tricky Store](https://github.com/5ec1cff/TrickyStore). NoHello will help us to get rid of various detections, and Tricky Store should help us with the bootloader status. 

Install both modules mentioned above. Then, go to the WebUI of Tricky store, click the 3 line button at the top right, and click "Set Verified Boot Hash". Paste the boot hash your device reports there. If you do not know the boot hash, you can get that by running the following command: `getprop | grep vbmeta`, Look for "ro.boot.vbmeta.digest". It should look like a bunch of random characters. This step should help us to get rid of the unverified boot state detection.

For the rest of the detections you might be getting, NoHello should take care of them. If it isn't, additional modules might be needed, which i do not know any, except [Shamiko](https://github.com/LSPosed/LSPosed.github.io/releases). Following these steps i mentioned, i got rid of various detections, such as bootloader status and state, Magisk detection and custom ROM detection. Using a "less bloated" ROM, such as LineageOS, or a kernel that doesn't have any banned strings should also help.
