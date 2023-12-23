# How to fix Play integrity

## Installing PlayIntegrityFix
1. First, make sure you have [magisk](/help/installing-magisk) installed
   - Make sure you enable zygisk in magisk settings!!
   - Also make sure you add play store to denylist, and clear play store data
2. Install [PlayIntegrityFix module](https://github.com/chiteroman/PlayIntegrityFix/releases/latest)
3. Reboot device

## Getting a fingerprint
To make play integrity work, we need to find a fingerprint that passes. For that, you will need [termux](https://f-droid.org/en/packages/com.termux/) installed (click the "download apk" button, not "download fdroid)

1. Open termux
2. Paste this: `cd && mkdir pif && cd pif`
   - This will create a new directory on temux's home directory.
3. This script NEEDS ROOT, so, type `su` (approve the root request), then paste this: `curl "https://raw.githubusercontent.com/TheFreeman193/PIFS/main/pickaprint.sh" | sh`
   - It might take some time, be patient.
4. Once you see "===== Done. Test your Play Integrity now! =====", download [SPIC - Play Integrity Checker](https://play.google.com/store/apps/details?id=com.henrikherzig.playintegritychecker)
5. Open the app, and click "Make play integrity request"
   - If you see "MEETS_DEVICE_INTEGRITY", that means play integrity is not failing anymore. Congrats, thats it
   - If you see "MEETS_BASIC_INTEGRITY", rerun the command (step 3), and try step 5 again
