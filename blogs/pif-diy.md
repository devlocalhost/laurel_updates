# Fixing PlayIntegrity - DIY (#3)
This is a detailed guide on how to fix it, by yourself, by "hunting" for fingerprints. This note assumes you have basic terminal knowledge, this isnt for noobs. See [#2](/help/pif-auto) instead. This is basically [#2](/help/pif-auto), but DIY lol

## PIF module
Check [#2](/help/pif-auto) and do the basic setup, and come back here.

## Hunting for a fingerprint
Go to [android dumps](https://t.me/android_dumps), and search for: `"Version: INT"`. INT is the android version. Look for versions >= 7, for example, `"Version: 7"`. Pick a random message, and click on the second link of the message (below "commit"). A gitlab repo will be shown. Click the "all_files.txt" file, and search for "build.prop". Search for "build.prop", and look for lines starting with "/system". Thats the path for the build.prop file. Find the build.prop file, and now its time to create the pif.json file

## The pif.json file
This file should be placed in /data/adb/ as pif.json (`/data/adb/pif.json`). Copy this into a text editor:
```json
{
    "PRODUCT" : "",
    "DEVICE" : "",
    "MANUFACTURER" : "",
    "BRAND" : "",
    "MODEL" : "",
    "FINGERPRINT" : "",
    "SECURITY_PATCH" : "",
    "FIRST_API_LEVEL" : ""
}
```

1. PRODUCT: in the build prop file as "ro.build.product" or "ro.product.device"
2. DEVICE: probably the same as above...?
3. MANUFACTURER: in the build prop file as "ro.product.brand"
4. BRAND: same as above
5. MODEL: in the build prop file as "ro.product.model"
6. FINGERPRINT: in the build prop file as "ro.build.fingerprint"
7. SECURITY_PATCH: in the build prop file as "ro.build.version.security_patch"
8. FIRST_API_LEVEL: just set this to whatever "ro.build.version.sdk" is lol

Save it as "pif.json", and move it to `/data/adb/pif.json`, then, using [SPIC - Play Integrity Checker](https://play.google.com/store/apps/details?id=com.henrikherzig.playintegritychecker), check if it passes. It doesnt? Repeat from "Hunting for a fingerprint"

Heres an sample of how it should look like:
```json
{
    "PRODUCT" : "zeroflte",
    "DEVICE" : "zeroflte",
    "MANUFACTURER" : "samsung",
    "BRAND" : "samsung",
    "MODEL" : "SM-G920F",
    "FINGERPRINT" : "samsung/zerofltexx/zeroflte:7.0/NRD90M/G920FXXS6ETI6:user/release-keys",
    "SECURITY_PATCH" : "2018-06-01",
    "FIRST_API_LEVEL" : "24"
}
```

