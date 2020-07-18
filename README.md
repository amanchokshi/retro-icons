# retro-icons

![Retro Dock](docs/dock.png)

Transform your mac with this custom set of *retro icons*

Changing icons of MacOS requires certain system restrictions to be disables. Proceed with caution!

We begin by disabling System Integrity Protection, which enables mac system icons to be changed.

Reboot your mac into recovery mode by holding down `⌘R` while the system is being rebooted. Enter your system password and then select `Utilities > Terminal`

```
csrutil disable
```

Now reboot your mac once again

To be able to change some obstinate icons, enter the following commands into the terminal

```
sudo mount -uw /
killall Finder
```

Once you have completed changing all the icons, remember to re-enable System Inegrity Protection, by rebooting your mac

```
csrutil enable
```

![Retro Apps](docs/apps.png)
