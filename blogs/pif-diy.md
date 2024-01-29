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
    "PRODUCT": "",
    "DEVICE": "",
    "MANUFACTURER": "",
    "BRAND": "",
    "MODEL": "",
    "FINGERPRINT": "",
    "SECURITY_PATCH": "",
    "ID": "",
    "FIRST_API_LEVEL": ,
    "KERNEL": ""
}
```

1. PRODUCT: in the build prop file as "ro.build.product" or "ro.product.device"
2. DEVICE: probably the same as above...?
3. MANUFACTURER: in the build prop file as "ro.product.brand"
4. BRAND: same as above
5. MODEL: in the build prop file as "ro.product.model"
6. FINGERPRINT: in the build prop file as "ro.build.fingerprint"
7. SECURITY_PATCH: in the build prop file as "ro.build.version.security_patch"
8. ID: in the build prop file as "ro.build.id"
9. FIRST_API_LEVEL: just set this to whatever "ro.build.version.sdk" is lol
10. KERNEL: for this one, we have to dig into the kernel image...

Save it as "pif.json", and move it to `/data/adb/pif.json`, then, using [SPIC - Play Integrity Checker](https://play.google.com/store/apps/details?id=com.henrikherzig.playintegritychecker), check if it passes. It doesnt? Repeat from "Hunting for a fingerprint"

Heres an example of how it should look like:
```json
{
    "PRODUCT" : "zeroflte",
    "DEVICE" : "zeroflte",
    "MANUFACTURER" : "samsung",
    "BRAND" : "samsung",
    "MODEL" : "SM-G920F",
    "FINGERPRINT" : "samsung/zerofltexx/zeroflte:7.0/NRD90M/G920FXXS6ETI6:user/release-keys",
    "SECURITY_PATCH" : "2018-06-01",
    "ID": "NRD90M"
    "FIRST_API_LEVEL" : 24,
    "KERNEL": "3.10.61-13830439"
}
```

### Getting KERNEL string
If you're using the device you're getting the props from, run this command: `uname --kernel-release`. Thats what goes in that field. If youre not using the device, then:

1. Navigate to the dump of the device
2. Go to the "bootimg" dirrectory, and download "kernel" file (not anything else!!).

Now heres the hard and important part:

- If its a gzip file (check using `file kernel`, for example `kernel: gzip compressed data, max compression, from Unix, original size modulo 2^32 35164672` means its a gzip file)
   1. rename to kernel.gz, run `gzip --decompress kernel.gz`
   2. run `strings kernel | grep "Linux version"`, and you should see something like this: `Linux version 4.14.180-perf-g1dd7e92 (builder@c5-miui-ota-bd30.bj) (clang version 10.0.7 for Android NDK, GNU ld (binutils-2.27-bd24d23f) 2.27.0.20170315) #1 SMP PREEMPT Tue Jun 15 19:57:12 CST 2021`. `4.14.180-perf-g1dd7e92` is the important part. thats what goes into the kernel field.

- If its not a gzip file, for example `kernel_zeroflte: Linux kernel ARM64 boot executable Image, little-endian`
   - Follow step 2, from above.

Note (from Play Integrity Fix telegram group) for the KERNEL string field: "Just put a funny name instead of all that. You don't need to change your kernel string to another one to "spoof it". Google just has a blacklist with some kernel names. A kernel name change will do". [Source1](https://t.me/playintegrityfix/148653/170298), [Source2](https://t.me/playintegrityfix/148653/170302)
