lastrain - weewx extension that provides extended statistics for reports
Copyright 2015 Vince Skahan

This search list extension offers extra tags:

  'last_rain':            datetime of the last rain recorded in the database
  'time_since_last_rain': time (seconds) since the last rain was recorded


Installation instructions:

1) run the installer:

setup.py install --extension extensions/lastrain

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


