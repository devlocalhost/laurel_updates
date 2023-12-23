# How to fix Play integrity

## Installing PlayIntegrityFix
1. First, make sure you have [magisk](/help/installing-magisk) installed
   - Make sure you enable zygisk in magisk settings!!
   - Also make sure you add play store to denylist, and clear play store data
2. Install [PlayIntegrityFix module](https://github.com/chiteroman/PlayIntegrityFix/releases/latest)
3. Reboot device

## Getting a fingerprint
To make play integrity work, we need to find a "valid", working fingerprint. For that, you will need [termux](https://f-droid.org/en/packages/com.termux/) installed (click the "download apk" button, not "download fdroid")

1. Open termux
2. Paste this: `mkdir ~/pif`. Note: **YOU RUN THIS ONLY ONCE AND NEVER AGAIN!!**
3. Now, paste this: `cd ~/pif`
4. This script NEEDS ROOT, so, type `su` (approve the root request), then paste this: `/data/data/com.termux/files/usr/bin/curl "https://raw.githubusercontent.com/TheFreeman193/PIFS/main/pickaprint.sh" | sh`
   - It might take some time, be patient.
4. Once you see "===== Done. Test your Play Integrity now! =====", download [SPIC - Play Integrity Checker](https://play.google.com/store/apps/details?id=com.henrikherzig.playintegritychecker)
5. Open the app, and click "Make play integrity request"
   - If you see "MEETS_DEVICE_INTEGRITY", that means play integrity is not failing anymore. Congrats, that's it
   - If you see "MEETS_BASIC_INTEGRITY", do step 4 again (no need to enter su again, just the long command)