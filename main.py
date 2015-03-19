#!/usr/bin/python
# -*- coding: utf-8 -*-

import os, sys
from optparse import OptionParser
from ndev.core import NDEVCredentials, HEADER, red, magenta
from ndev.asr import *

# import Output object
from alfanous.Outputs import Raw

# import default Paths
from alfanous.Data import Paths

# Initialize search engines
RAWoutput = Raw(
                    QSE_index = Paths.QSE_INDEX    , # Quranic Main index path
                    TSE_index = Paths.TSE_INDEX,  # Translations index path
                    WSE_index = Paths.WSE_INDEX,  # Quranic words index path
                    Recitations_list_file = Paths.RECITATIONS_LIST_FILE,
                    Translations_list_file = Paths.TRANSLATIONS_LIST_FILE ,
                    Hints_file = Paths.HINTS_FILE,
                    Stats_file = Paths.STATS_FILE,
                    Information_file = Paths.INFORMATION_FILE
                )


parser = OptionParser(usage="usage: %prog {source_file.wav} [options]")
parser.add_option("-l", "--lang", action="store", type="string", dest="language",
                  help="desired language via language code")
(options, args) = parser.parse_args()


if __name__ == "__main__":
    
    if len(args) != 1:
        parser.error("Please provide a source_file to perform recognition on.")
        sys.exit(-1)

    #print green(HEADER)
    
    creds = NDEVCredentials()
    if not creds.has_credentials():
         print red("Please provide NDEV credentials.")
         sys.exit(-1)

    filename = args[0]
    
    language = getattr(options, 'language')
    desired_asr_lang = ASR.get_language_input(language)
    print "OK. Using Language: %s (%s)\n" % (desired_asr_lang['display'], desired_asr_lang['properties']['code'])

    try:
        asr_req = ASR.make_request(creds=creds, desired_asr_lang=desired_asr_lang, filename=filename)

        if asr_req.response.was_successful():
	         print "\n%s" % magenta(asr_req.response.get_recognition_result()) # instead of looping through, pick head
	         text = asr_req.response.get_recognition_result()
	         search_flags = {
			                   "action":"search",
			                   "query": text,
			                   "sortedby":"score",
			                   "page": 1,
			                   "word_info":True,
			                   "highlight":"css",
			                   "script": "standard",
			                   "prev_aya": True,
			                   "next_aya": True,
			                   "sura_info": True,
			                   "aya_position_info":  True,
			                   "aya_theme_info":  True,
			                   "aya_stat_info":  True,
			                   "aya_sajda_info":  True,
			                   "translation":1,
			                   "recitation": 1
	            			}
	         results = RAWoutput.do(search_flags)
	         print(results["search"]["ayas"][1]["sura"]["name"])
	         print(results["search"]["ayas"][1]["sura"]["id"])
	         print("verse" , results["search"]["ayas"][1]["aya"]["id"])
	         
	           	    
		    
        else:
             print "\n%s" % red(asr_req.response.error_message)
    except Exception as e:
        print red(e)
        sys.exit(-1)


