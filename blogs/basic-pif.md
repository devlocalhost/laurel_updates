# Basic guide to achieve BASIC, DEVICE and STRONG integrity.
Following the steps below should help you achieve all 3 verdicts (BASIC, DEVICE & STRONG). If you cannot achieve them, Google possibly broke or changed stuff again, you did not follow the steps, or... something else. This guide isn't guaranteed to work, or help everyone. If it works for you, congratulations. If not, I'm sorry.

## Requirements
- [Magisk](https://github.com/topjohnwu/Magisk/releases) ([tutorial](/blog/installing-magisk). Other root solutions should work, but have been not tested).
- Zygisk implementation
	1. [Zygisk Next](https://github.com/Dr-TSNG/ZygiskNext) (recommended)
	2. [ReZygisk](https://github.com/PerformanC/ReZygisk) (open source)
- [PlayIntegrityFork (module)](https://github.com/osm0sis/PlayIntegrityFork), [Tricky Store (module)](https://github.com/5ec1cff/TrickyStore) and [Tricky Addon - Update Target List (module)](https://github.com/KOWX712/Tricky-Addon-Update-Target-List/)
- Optional: a WebUI manager if the rooting solution you have does not have such function. One recommended manager is [WebUI X Portable (app)](https://github.com/MMRLApp/WebUI-X-Portable/releases). Of course, you can use any.

## Steps
1. **Skip** if you are not using **Magisk**. If built-in Zygisk is enabled in your Magisk settings, disable it and reboot. Then, install one of the mentioned Zygisk implementations.
2. Flash PlayIntegrityFork, Tricky Store, install the mentioned or any WebUI solution, and reboot your device again.
3. Open your root manager, and go to your modules list. Click the "Action" button below the Tricky Store module, and a menu should appear. If for any reason, it does not appear, open the WebUI manager you installed, and click Tricky Store card.
	1. Click the 3 line button, on the top right, and click "Select All". This will select all of your installed apps.
	2. Click the 3 line button again, and this time, click "Deselect Unnecessary"
	3. Now for the keybox, click the 3 line button again, then "Set Valid Keybox". If you have your own Keybox, click "Set Custom Keybox" instead, and choose your keybox xml file.
	4. Lastly, 3 line button again, and click "Set Security Patch", then "Auto". This will spoof the security patch date.
4. Last step: Go to your modules list again, and click the "Action" button for PlayIntegrityFork. It should auto-fetch a random fingerprint, and it should be done.
5. Now, all that's left is to check the Play Integrity status. This can be done using 2 ways:
	1. Using Play Store: go to Play Store settings, spam click Play Store version to enable developer mode, go to General > Developer options, and click Check Integrity.
	2. Using an app: Download [Play Integrity API Checker](https://play.google.com/store/apps/details?id=gr.nikolasspyr.integritycheck) by Nikolas Spiridakis.

## Final words
If you achieved all 3 verdicts, congratulations. Keep in mind that if, after some days, you can only achieve BASIC integrity, you should click the "Action" button on PlayIntegrityFork, and/or update your keybox from Tricky Store.

You can also check [this guide](/blog/hiding-detections) if you want to hide various detections like running magisk, ROM detections, etc.
