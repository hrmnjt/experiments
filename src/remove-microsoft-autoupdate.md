# How to remove Microsoft Autoupdate from MacOS completely

On current MacOS Version

```bash
system_profiler SPSoftwareDataType
# Software:

#     System Software Overview:

#       System Version: macOS 11.1 (20C69)
#       Kernel Version: Darwin 20.2.0
#       Boot Volume: Macintosh HD
#       Boot Mode: Normal
#       Computer Name: Harman’s MacBook Pro
#       User Name: Harman (hsingh)
#       Secure Virtual Memory: Enabled
#       System Integrity Protection: Enabled
#       Time since boot: 13:46

```

Remove the app

```bash
rm -rf /Library/Application\ Support/Microsoft/MAU2.0
```

Remove the preferences

```bash
rm -rf /Library/Preferences/com.microsoft.autoupdate2.plist
rm -rf /Library/PrivilegedHelperTools/com.microsoft.autoupdate.helper
```
