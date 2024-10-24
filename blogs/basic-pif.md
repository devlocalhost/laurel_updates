# PlayIntegrityFix

## Fixing Play Integrity
According to the tutorial from [PlayIntegrityFix GitHub repo](https://github.com/chiteroman/PlayIntegrityFix?tab=readme-ov-file#tutorial), you need one of these:

- [Magisk](https://github.com/topjohnwu/Magisk) with Zygisk enabled.
- [KernelSU](https://github.com/tiann/KernelSU) with [ZygiskNext](https://github.com/Dr-TSNG/ZygiskNext) module installed.
- [APatch](https://github.com/bmax121/APatch) with [ZygiskNext](https://github.com/Dr-TSNG/ZygiskNext) module installed.

---

My current setup is the first one. Let's move on now. If you are using magisk, you NEED to:

1. Hide magisk app from settings. Go to magisk settings, click the "Hide the Magisk app", enter anything and click ok.
2. Remove `/data/magisk` directory. If you have root, use an file explorer with root, and delete the magisk folder in /data (i use termux, so i ran `su -c rm -r /data/magisk`).
3. Install [Zygisk-Assistant magisk module](https://github.com/snake-4/Zygisk-Assistant/releases/latest)
4. Install [PlayIntegrityFix module](https://github.com/chiteroman/PlayIntegrityFix/releases/latest). **NOTE**: If your rom is signed with test keys (ask your ROM maintainer or check with with `su` and `unzip -l /system/etc/security/otacerts.zip` in Termux. If you see `testkey.x509.pem`, rom is signed with test keys) open `/data/adb/modules/playintegrityfix/pif.json` and change spoofSignature to true. ([source](https://t.me/A3Official/502180))

Following these steps should help you pass `MEETS_BASIC_INTEGRITY` and `MEETS_DEVICE_INTEGRITY`.
![image showing basic and device integrity with green checks.](/static/img/pi-result.png)
