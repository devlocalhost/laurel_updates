# Spoofings and mods i use on laurel
With the spoofing methods and mods i am using, i currently can achieve this:

## Things used
1. Modules:
    1. [PlayIntegrityFix (magisk)](https://github.com/chiteroman/PlayIntegrityFix)
    2. [Zygisk-Assistant (magisk)](https://github.com/snake-4/Zygisk-Assistant)
    3. [BootloaderSpoofer (lsposed)](https://github.com/chiteroman/BootloaderSpoofer)
2. Detection apps:
    1. Play Store
    2. [PIAC](https://play.google.com/store/apps/details?id=gr.nikolasspyr.integritycheck)
    3. [YASNAC](https://play.google.com/store/apps/details?id=rikka.safetynetchecker)
    4. [Key Attestation](https://github.com/vvb2060/KeyAttestation)
    5. [RootbeerFresh](https://github.com/KimChangYoun/rootbeerFresh)
    6. [MemoryDetector](https://github.com/rushiranpise/detection/blob/main/MemoryDetector_2.1.0.apk)
    7. [Momo](https://t.me/magiskalpha/529)
    8. [Native Detector](https://t.me/reveny1/57)
    9. [Ruru](https://github.com/byxiaorun/Ruru/)

## The good
1. Basic and device integrity passing (play store): ![basic and device integrity (play store)](/static/img/pi-result.png)
1. Basic and device integrity passing (other app): ![basic and device integrity (other app)](/static/img/pi-other.png)
2. SafetyNet passing (YASNAC): ![safetynet passing](/static/img/sn-result.png)
3. MicroG SafetyNet checks: ![microg safetynet checks](/static/img/microg-checks.png)
4. Key Attestation result: ![key attestation/bootloader spoof](/static/img/ka-bs.png)
5. RootBeer app: ![rootbeer app](/static/img/rb.png)

## The bad
1. MemoryDetector app: ![memory detector app](/static/img/md.png)
2. Momo app (adding to denylist makes app crash on launch): ![momo app](/static/img/momo.png)
3. NativeDetector app: ![nativedetector app](/static/img/nd.png)
4. Ruru app: ![ruru app](/static/img/ruru.png)

## Denylist & lsposed
1. Denylist apps: ![denylist apps](/static/img/denylist.png)
2. LSposed bootloader spoof apps: ![lsposed bootloader spoof](/static/img/lsposed-bs.png)

## Magisk and LSPosed modules
1. Magisk modules: ![magisk modules](/static/img/m-mods.png)
2. LSPosed modules: ![lsposed modules](/static/img/lsp-mods.png)
