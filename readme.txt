(2023-0301: weewx 4.10 breaking change note - if you run weewx 4.10 or later, see  https://weewx.com/docs/upgrading.htm#Breaking_changes_for_skins_that_use_delta_times for changes you will need to make to your .tmpl files)

lastrain - weewx extension that provides extended statistics for reports
Copyright 2015 Vince Skahan

This search list extension offers extra tags:

  'last_rain':            datetime of the last rain recorded in the database
  'time_since_last_rain': time (seconds) since the last rain was recorded


Installation instructions:

0) clone this repository
git clone <url_on_the_right_of_the_github_page> /tmp/extensions/lastrain

1) run the installer (see the Customization Guide for your weewx version for exact syntax)
cd /tmp
setup.py install --extension extensions/lastrain     ### weewx < 3.2
          or
wee_extension --install=/tmp/extensions/lastrain     ### weewx >= 3.2

2) restart weewx:

sudo /etc/init.d/weewx stop
sudo /etc/init.d/weewx start

This will result in a report called lastrain that illustrates the use of the
extended statistics.

Manual installation instructions:

1) copy files to the weewx user directory:

cp bin/user/lastrain.py /home/weewx/bin/user

2) in weewx.conf, modify the report section in which you would like to use the
   extended statistics.  for example, for the StandardReport:

[StdReport]
    [[StandardReport]]
        ...
        [[[CheetahGenerator]]]
            search_list_extensions = user.lastrain.lastRainTags

3) restart weewx

sudo /etc/init.d/weewx stop
sudo /etc/init.d/weewx start


