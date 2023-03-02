
## lastrain - weewx extension that provides extended statistics for reports
Copyright 2015-2023 Vince Skahan

This search list extension offers extra tags:

  * 'last_rain':            datetime of the last rain recorded in the database
  * 'time_since_last_rain': time (seconds) since the last rain was recorded

An example minimal skin is provided to show usage for including last rain data in your skin(s).

### VERSION COMPATIBILITY NOTE
This branch is compatible with WeeWX versions 4.10 and later. For older WeeWX versions please use the weewx-pre-4.10 branch.

### Installation instructions:
This extension can be installed/uninstalled using the WeeWX extension installer.

#### 1. download the .zip file for this branch

`wget https://github.com/vinceskahan/vds-weewx-lastrain-extension/archive/refs/heads/master.zip -O /var/tmp/lastrain-extension.zip`

#### 2. install the extension with the WeeWX extension installer

For weewx 4.x:

`wee_extension --install /var/tmp/lastrain-extension.zip`

For weewx 5.x:

`weectl extension install /var/tmp/lastrain-extension.zip`

#### 3. restart weewx

`sudo systemctl restart weewx`

