# Installing ViPER4AndroidFX

## What is ViPER4AndroidFX?

ViPER4AndroidFX is a powerful EQ app which requires root ([magisk](/help/how-install-magisk)), with many options and modifications you can use/do.

## How to install <abbr title="ViPER4AndroidFX">V4A</abbr>

1. Make sure you have [magisk](/help/how-install-magisk) installed.
2. Download
   1. [V4A APK](https://thebiggestboi.skyblueborb.workers.dev/0:/V4A/v4a.apk)
   2. [Audio Modification Library](https://thebiggestboi.skyblueborb.workers.dev/0:/V4A/aml.zip)
   3. [Audio Compatibility Patch](https://thebiggestboi.skyblueborb.workers.dev/0:/V4A/acp.zip)
   4. [post-fs-data script](https://thebiggestboi.skyblueborb.workers.dev/0:/V4A/post-fs-data.sh)
4. Install Audio Modification Library module and reboot. Do the same for Audio Compatibility Patch module. When Audio Compatibility Patch module asks you what options to select, do this: Volume Up, Down, Up, Down, Up, Down.
5. Install the apk and let it install the module, then reboot (the app will ask you to reboot).
6. Move the `post-fs-data.sh` script to `/data/adb/modules/ViPER4AndroidFX` using termux (or a file manager, up to you): First, type "su" and allow superuser access, then: `cp /sdcard/Download/post-fs-data.sh /data/adb/modules/ViPER4AndroidFX` and reboot.
7. Launch the apk, enable "Master limiter" and configure the options.
   - If modifications are not applied, try enabling "Legacy mode" in settings.
   - Having issues? Modifications are not applied? You can try [V4ARE guide.](https://telegra.ph/ViPER4AndroidRepackaged-installation-09-06)
