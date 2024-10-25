# platform_tools

platform_tools are essential drivers used to communicate with your phone, including ADB (Android Debug Bridge) and Fastboot.

## Getting platform_tools

If you are using windows 10 or 11, you can skip steps 1, 2 and 3 by doing this:
1. Open cmd (windows key + r, type `cmd`, then enter)
2. Execute this command: `winget install Google.PlatformTools`

If you are using linux, you can skip steps 1, 2 and 3 by using your package manager

1. Navigate to the [official Android Developer website](https://developer.android.com/tools/releases/platform-tools#downloads), where you can find the download links for platform_tools.
2. Select the platform that matches your operating system, and download the zip file.
3. Extract the downloaded zip file to any location on your computer.
4. To use ADB or Fastboot, follow these steps:
    - Go to the directory where you extracted the files.
    - Click on the address bar of Windows File Explorer (if using windows) and type `cmd`, then press Enter.
    - A command prompt window will appear, allowing you to use ADB and Fastboot commands. Type `adb --help` or `fastboot --help`

# Check CRC Failed error

This is a known issue, and the solution is to download an older version of platform_tools: 33.0.3
`https://dl.google.com/android/repository/platform-tools_r33.0.3-PLATFORM.zip`

Replace `PLATFORM` with your platform:
 - windows
 - darwin (MacOS)
 - linux
