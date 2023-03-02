
## lastrain - weewx extension that provides extended statistics for reports
Copyright 2015-2023 Vince Skahan

This search list extension offers extra tags:

  * 'last_rain':            datetime of the last rain recorded in the database
  * 'time_since_last_rain': time (seconds) since the last rain was recorded

An example minimal skin is provided to show usage for including last rain data in your skin(s).

### VERSION COMPATIBILITY NOTE
This branch is compatible with WeeWX versions 4.09 and earlier.   For WeeWX versions >= 4.10 please use the master branch.

### Installation instructions:
This extension can be installed/uninstalled using the WeeWX extension installer.

#### 1. download the .zip file for this branch

`wget https://github.com/vinceskahan/vds-weewx-lastrain-extension/archive/refs/heads/weewx-pre-4.10.zip -O /var/tmp/lastrain-extension.zip`

#### 2. install the extension with the WeeWX extension installer

`wee_extension --install /var/tmp/lastrain-extension.zip`

#### 3. restart weewx

`sudo systemctl restart weewx`

