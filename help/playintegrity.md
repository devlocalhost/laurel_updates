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
2. We need to install a few packages, so, run this: `pkg i -y wget tsu`. If it fails to install, you need to change the default repositories.
3. Now, paste this: `mkdir ~/pif`. Note: **YOU RUN THIS ONLY ONCE AND NEVER AGAIN!!**
4. Next: `cd ~/pif`
5. This script NEEDS ROOT, so, type `tsu`, press enter, and a popup to approve the root request will appear. Approve it, it is safe.
6. Now, run this: `curl "https://raw.githubusercontent.com/TheFreeman193/PIFS/main/pickaprint.sh" | sh`
   - It might take some time, be patient.
7. Once you see "===== Done. Test your Play Integrity now! =====", download [SPIC - Play Integrity Checker](https://play.google.com/store/apps/details?id=com.henrikherzig.playintegritychecker). Note: do NOT close termux yet!!
8. Open the app, and click "Make play integrity request"
   - If you see "MEETS_DEVICE_INTEGRITY", that means play integrity is not failing anymore. Congrats, that's it. You can now close termux
   - If you see "MEETS_BASIC_INTEGRITY", do **step 6** again

## Play Integrity not working again?
This is normal. If you're unlucky, it won't work anymore. So, avoid sharing your fingerprint (or "pif.json" file) with others. Now, to fix that, continue from **step 4**
