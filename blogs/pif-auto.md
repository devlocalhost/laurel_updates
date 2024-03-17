# Fixing PlayIntegrity (#2)
Note: this guide is OUTDATED AND DOES NOT WORK ANYMORE!!! Check [The news - 01/03/2024](/blog/news).

Help needed! Check the bottom of [#1](/blog/playintegrity).

## Installing PlayIntegrityFix - basic setup
1. First, make sure you have [magisk](/help/installing-magisk) installed
   - Make sure you **enable zygisk in magisk settings**!!
   - Also make sure you **add play store to denylist, and clear play store data**
2. Install [PlayIntegrityFix module](https://github.com/chiteroman/PlayIntegrityFix/releases/latest)
3. Reboot device

## Getting a fingerprint
To make play integrity work, we need to find a "valid", working fingerprint. For that, you will need [termux](https://f-droid.org/en/packages/com.termux/) installed (click the "download apk" button, not "download fdroid")

1. Open termux
2. We need to install a few packages, run this: `pkg i -y wget tsu`. Enter "y" for every question it asks. If it fails to install, you need to **change the default repositories**.
   - If this is the first time you install/run termux, run these commands first: `pkg updt && pkg upgr`. This will update and upgrade your termux environment packages. Again, if it fails, you need to change the repositories.
3. Now, create a folder for the script that will fetch and apply a fingerprint: `mkdir ~/pif`. Note: you only have to run this command **ONCE, never again**.
4. Let's go inside that folder we made: `cd ~/pif`
5. Time to download the script: `wget -O pickaprint.sh "https://raw.githubusercontent.com/TheFreeman193/PIFS/main/pickaprint.sh"`. You also run this command **ONCE**, never again, unless the script changes.
6. We need to run the script as root, type: `tsu`. A prompt to approve or deny the request will appear. Approve it.
7. To execute the script, we need to make it executable: `chmod 755 pickaprint.sh`. We also run this **once** (if the file "pickaprint.sh" exists in ~/pif.)
8. Let's finally execute it: `./pickaprint.sh`. When you see "===== Test your Play Integrity now =====", download [SPIC - Play Integrity Checker](https://play.google.com/store/apps/details?id=com.henrikherzig.playintegritychecker). Note: do NOT close termux yet!!
8. Open the app, and click "Make play integrity request"
   - If you see "MEETS_DEVICE_INTEGRITY", that means play integrity is not failing anymore. Congrats, that's it. Go back to termux, type "y", and you can now close termux
   - If you see "MEETS_BASIC_INTEGRITY", do **step 8** again

## Play Integrity not working again?
This is normal. If you're unlucky, it won't work anymore. So, avoid sharing your fingerprint (or "pif.json" file) with others. Now, to fix that, continue from **step 4**, but **ignore** steps 5, 6, 7, and go with **step 8**, after doing step 4
