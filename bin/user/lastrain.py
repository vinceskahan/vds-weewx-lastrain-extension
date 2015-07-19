
import syslog
import time

from weewx.cheetahgenerator import SearchList
from weewx.units import ValueHelper

#
#"""
#    taken from wdSearchX3.py in weewx-wd 1.0 at Gary's suggestion
#    credit to the weewx-wd team, blame/bug-reports to me please
#
#    some code reused_from/stolen_from/insulting weewx station.py 
#    per Tom's suggestion
#"""
#
class wdLastRainTags(SearchList):

    def logdbg(self,message):
        """Syslog a debug message
            This function didn't come from weewx-wd, just forcing
            a routine to use the normal syslogging weewx uses
            in case we need it someday below
        """
        syslog.syslog(syslog.LOG_DEBUG, message)

    def __init__(self, generator):
        SearchList.__init__(self, generator)

    def get_extension_list(self, timespan, db_lookup):
        """Returns a search list extension with datetime of last rain.

        Parameters:
          timespan: An instance of weeutil.weeutil.TimeSpan. This will
                    hold the start and stop times of the domain of 
                    valid times.

          db_lookup: This is a function that, given a data binding
                     as its only parameter, will return a database manager
                     object.

        Returns:
          last_rain: A ValueHelper containing the datetime of the last rain
        """

        ##
        ## Get date and time of last rain
        ##
        ## Returns unix epoch of archive period of last rain
        ##
        ## Result is returned as a ValueHelper so standard Weewx formatting
        ## is available eg $last_rain.format("%d %m %Y")
        ##

        # Get ts for day of last rain from statsdb
        # Value returned is ts for midnight on the day the rain occurred
        _row = db_lookup().getSql("SELECT MAX(dateTime) FROM archive_day_rain WHERE sum > 0")

        lastrain_ts = _row[0]
        # Now if we found a ts then use it to limit our search on the archive 
        # so we can find the last archive record during which it rained. Wrap
        # in a try statement just in case
        if lastrain_ts is not None:
            try:
                _row = db_lookup().getSql("SELECT MAX(dateTime) FROM archive WHERE rain > 0 AND dateTime > ? AND dateTime <= ?", (lastrain_ts, lastrain_ts + 86400))
                lastrain_ts = _row[0]
		print lastrain_ts
            except:
                lastrain_ts = None
	else:
            lastrain_ts = None

        # Wrap our ts in a ValueHelper
        lastrain_vt = (lastrain_ts, 'unix_epoch', 'group_time')
        lastrain_vh = ValueHelper(lastrain_vt, formatter=self.generator.formatter, converter=self.generator.converter)

	# next idea stolen with thanks from weewx station.py
	# note this is delta time from 'now' not the last weewx db time
        delta_time = time.time() - lastrain_ts if lastrain_ts else None

        # Wrap our ts in a ValueHelper
        delta_time_vt = (delta_time, 'second', 'group_deltatime')
        delta_time_vh = ValueHelper(delta_time_vt, formatter=self.generator.formatter, converter=self.generator.converter)

        # Create a small dictionary with the tag names (keys) we want to use
        search_list_extension = {'last_rain' : lastrain_vh,  'lastrain_delta_time' :  delta_time_vh }

	#### debug only
	####print ("delta_time=%s" % delta_time)

        return [search_list_extension]

