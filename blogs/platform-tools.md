# platform_tools

platform_tools are essential drivers used to communicate with your phone, including ADB (Android Debug Bridge) and Fastboot.

## Getting platform_tools

1. Navigate to the [official Android Developer website](https://developer.android.com/tools/releases/platform-tools#downloads), where you can find the download links for platform_tools.
2. Select the platform that matches your operating system, and download the zip file.
3. Extract the downloaded zip file to any location on your computer.
4. To use ADB or Fastboot, follow these steps:
    - Go to the directory where you extracted the files.
    - Click on the address bar of Windows File Explorer and type `cmd`, then press Enter.
    - A command prompt window will appear, allowing you to use ADB or Fastboot commands. Type `adb --help` or `fastboot --help`

# Check CRC Failed error

This is a known issue, and the solution is to download an older version of platform_tools: 33.0.3
`https://dl.google.com/android/repository/platform-tools_r33.0.3-PLATFORM.zip`

Replace `PLATFORM` with your platform:
 - windows
 - darwin (MacOS)
 - linux
