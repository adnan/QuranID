# coding: utf-8


##     Copyright (C) 2009-2012 Assem Chelli <assem.ch [at] gmail.com>

##     This program is free software: you can redistribute it and/or modify
##     it under the terms of the GNU Affero General Public License as published
##     by the Free Software Foundation, either version 3 of the License, or
##     (at your option) any later version.

##     This program is distributed in the hope that it will be useful,
##     but WITHOUT ANY WARRANTY; without even the implied warranty of
##     MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
##     GNU Affero General Public License for more details.

##     You should have received a copy of the GNU Affero General Public License
##     along with this program.  If not, see <http://www.gnu.org/licenses/>.






#:shaping table
SHAPING = {
 u'\u0621' : ( u'\uFE80' ) ,
 u'\u0622' : ( u'\uFE81', u'\uFE82' ) ,
 u'\u0623' : ( u'\uFE83', u'\uFE84' ) ,
 u'\u0624' : ( u'\uFE85' , u'\uFE86' ) ,
 u'\u0625' : ( u'\uFE87' , u'\uFE88' ) ,
 u'\u0626' : ( u'\uFE89' , u'\uFE8B' , u'\uFE8C' , u'\uFE8A' ) ,
 u'\u0627' : ( u'\uFE8D' , u'\uFE8E' ) ,
 u'\u0628' : ( u'\uFE8F' , u'\uFE91' , u'\uFE92' , u'\uFE90' ) ,
 u'\u0629' : ( u'\uFE93' , u'\uFE94' ) ,
 u'\u062A' : ( u'\uFE95' , u'\uFE97' , u'\uFE98' , u'\uFE96' ) ,
 u'\u062B' : ( u'\uFE99' , u'\uFE9B' , u'\uFE9C' , u'\uFE9A' ) ,
 u'\u062C' : ( u'\uFE9D' , u'\uFE9F' , u'\uFEA0', u'\uFE9E' ) ,
 u'\u062D' : ( u'\uFEA1' , u'\uFEA3' , u'\uFEA4' , u'\uFEA2' ) ,
 u'\u062E' : ( u'\uFEA5' , u'\uFEA7' , u'\uFEA8' , u'\uFEA6' ) ,
 u'\u062F' : ( u'\uFEA9' , u'\uFEAA' ) ,
 u'\u0630' : ( u'\uFEAB'  , u'\uFEAC' ) ,
 u'\u0631' : ( u'\uFEAD' , u'\uFEAE' ) ,
 u'\u0632' : ( u'\uFEAF'  , u'\uFEB0' ) ,
 u'\u0633' : ( u'\uFEB1' , u'\uFEB3' , u'\uFEB4' , u'\uFEB2' ) ,
 u'\u0634' : ( u'\uFEB5' , u'\uFEB7' , u'\uFEB8' , u'\uFEB6' ) ,
 u'\u0635' : ( u'\uFEB9' , u'\uFEBB' , u'\uFEBC' , u'\uFEBA' ) ,
 u'\u0636' : ( u'\uFEBD' , u'\uFEBF' , u'\uFEC0' , u'\uFEBE' ) ,
 u'\u0637' : ( u'\uFEC1' , u'\uFEC3' , u'\uFEC4' , u'\uFEC2' ) ,
 u'\u0638' : ( u'\uFEC5' , u'\uFEC7' , u'\uFEC8' , u'\uFEC6' ) ,
 u'\u0639' : ( u'\uFEC9' , u'\uFECB' , u'\uFECC' , u'\uFECA' ) ,
 u'\u063A' : ( u'\uFECD' , u'\uFECF' , u'\uFED0', u'\uFECE' ) ,
 u'\u0640' : ( u'\u0640' ) ,
 u'\u0641' : ( u'\uFED1' , u'\uFED3' , u'\uFED4' , u'\uFED2' ) ,
 u'\u0642' : ( u'\uFED5' , u'\uFED7' , u'\uFED8' , u'\uFED6' ) ,
 u'\u0643' : ( u'\uFED9' , u'\uFEDB' , u'\uFEDC' , u'\uFEDA' ) ,
 u'\u0644' : ( u'\uFEDD' , u'\uFEDF' , u'\uFEE0', u'\uFEDE' ) ,
 u'\u0645' : ( u'\uFEE1' , u'\uFEE3' , u'\uFEE4' , u'\uFEE2' ) ,
 u'\u0646' : ( u'\uFEE5' , u'\uFEE7' , u'\uFEE8' , u'\uFEE6' ) ,
 u'\u0647' : ( u'\uFEE9' , u'\uFEEB' , u'\uFEEC' , u'\uFEEA' ) ,
 u'\u0648' : ( u'\uFEED' , u'\uFEEE' ) ,
 u'\u0649' : ( u'\uFEEF' , u'\uFEF0' ) ,
 u'\u064A' : ( u'\uFEF1' , u'\uFEF3' , u'\uFEF4' , u'\uFEF2' )
}

#:invert*ed shaping table
INVERTEDSHAPING = {
u'\ufe83': u'\u0623',
u'\ufe87': u'\u0625',
u'\ufe8b': u'\u0626',
u'\ufe8f': u'\u0628',
u'\ufe93': u'\u0629',
u'\ufe97': u'\u062a',
u'\ufe9b': u'\u062b',
u'\ufe9f': u'\u062c',
u'\ufea3': u'\u062d',
u'\ufea7': u'\u062e',
u'\ufeab': u'\u0630',
u'\ufeaf': u'\u0632',
u'\ufeb3': u'\u0633',
u'\ufeb7': u'\u0634',
u'\ufebb': u'\u0635',
u'\ufebf': u'\u0636',
u'\u0640': u'\u0640',
u'\ufec3': u'\u0637',
u'\ufec7': u'\u0638',
u'\ufecb': u'\u0639',
u'\ufecf': u'\u063a',
u'\ufed3': u'\u0641',
u'\ufed7': u'\u0642',
u'\ufedb': u'\u0643',
u'\ufedf': u'\u0644',
u'\ufee3': u'\u0645',
u'\ufee7': u'\u0646',
u'\ufeeb': u'\u0647',
u'\ufeef': u'\u0649',
u'\ufef3': u'\u064a',
u'\ufe80': u'\u0621',
u'\ufe84': u'\u0623',
u'\ufe88': u'\u0625',
u'\ufe8c': u'\u0626',
u'\ufe90': u'\u0628',
u'\ufe94': u'\u0629',
u'\ufe98': u'\u062a',
u'\ufe9c': u'\u062b',
u'\ufea0': u'\u062c',
u'\ufea4': u'\u062d',
u'\ufea8': u'\u062e',
u'\ufeac': u'\u0630',
u'\ufeb0': u'\u0632',
u'\ufeb4': u'\u0633',
u'\ufeb8': u'\u0634',
u'\ufebc': u'\u0635',
u'\ufec0': u'\u0636',
u'\ufec4': u'\u0637',
u'\ufec8': u'\u0638',
u'\ufecc': u'\u0639',
u'\ufed0': u'\u063a',
u'\ufed4': u'\u0641',
u'\ufed8': u'\u0642',
u'\ufedc': u'\u0643',
u'\ufee0': u'\u0644',
u'\ufee4': u'\u0645',
u'\ufee8': u'\u0646',
u'\ufeec': u'\u0647',
u'\ufef0': u'\u0649',
u'\ufef4': u'\u064a',
u'\ufe81': u'\u0622',
u'\ufe85': u'\u0624',
u'\ufe89': u'\u0626',
u'\ufe8d': u'\u0627',
u'\ufe91': u'\u0628',
u'\ufe95': u'\u062a',
u'\ufe99': u'\u062b',
u'\ufe9d': u'\u062c',
u'\ufea1': u'\u062d',
u'\ufea5': u'\u062e',
u'\ufea9': u'\u062f',
u'\ufead': u'\u0631',
u'\ufeb1': u'\u0633',
u'\ufeb5': u'\u0634',
u'\ufeb9': u'\u0635',
u'\ufebd': u'\u0636',
u'\ufec1': u'\u0637',
u'\ufec5': u'\u0638',
u'\ufec9': u'\u0639',
u'\ufecd': u'\u063a',
u'\ufed1': u'\u0641',
u'\ufed5': u'\u0642',
u'\ufed9': u'\u0643',
u'\ufedd': u'\u0644',
u'\ufee1': u'\u0645',
u'\ufee5': u'\u0646',
u'\ufee9': u'\u0647',
u'\ufeed': u'\u0648',
u'\ufef1': u'\u064a',
u'\ufe82': u'\u0622',
u'\ufe86': u'\u0624',
u'\ufe8a': u'\u0626',
u'\ufe8e': u'\u0627',
u'\ufe92': u'\u0628',
u'\ufe96': u'\u062a',
u'\ufe9a': u'\u062b',
u'\ufe9e': u'\u062c',
u'\ufea2': u'\u062d',
u'\ufea6': u'\u062e',
u'\ufeaa': u'\u062f',
u'\ufeae': u'\u0631',
u'\ufeb2': u'\u0633',
u'\ufeb6': u'\u0634',
u'\ufeba': u'\u0635',
u'\ufebe': u'\u0636',
u'\ufec2': u'\u0637',
u'\ufec6': u'\u0638',
u'\ufeca': u'\u0639',
u'\ufece': u'\u063a',
u'\ufed2': u'\u0641',
u'\ufed6': u'\u0642',
u'\ufeda': u'\u0643',
u'\ufede': u'\u0644',
u'\ufee2': u'\u0645',
u'\ufee6': u'\u0646',
u'\ufeea': u'\u0647',
u'\ufeee': u'\u0648',
u'\ufef2': u'\u064a'
}


LANGS = {
        'el': 'Greek',
        'eo': 'Esperanto',
        'en': 'English',
        'vi': 'Vietnamese',
        'ca': 'Catalan',
        'it': 'Italian',
        'lb': 'Luxembourgish',
        'eu': 'Basque',
        'ar': 'Arabic',
        'bg': 'Bulgarian',
        'cs': 'Czech',
        'et': 'Estonian',
        'gl': 'Galician',
        'id': 'Indonesian',
        'ru': 'Russian',
        'nl': 'Dutch',
        'pt': 'Portuguese',
        'no': 'Norwegian',
        'tr': 'Turkish',
        'lv': 'Latvian',
        'lt': 'Lithuanian',
        'th': 'Thai',
        'es': 'Spanish',
        'ro': 'Romanian',
        'en_GB': 'British English',
        'fr': 'French',
        'hy': 'Armenian',
        'uk': 'Ukrainian',
        'pt_BR': 'Brazilian',
        'hr': 'Croatian',
        'de': 'German',
        'da': 'Danish',
        'fa': 'Persian',
        'bs': 'Bosnian',
        'fi': 'Finnish',
        'hu': 'Hungarian',
        'ja': 'Japanese',
        'he': 'Hebrew',
        'ka': 'Georgian',
        'zh': 'Chinese',
        'kk': 'Kazakh',
        'sr': 'Serbian',
        'sq': 'Albanian',
        'ko': 'Korean',
        'sv': 'Swedish',
        'mk': 'Macedonian',
        'sk': 'Slovak',
        'pl': 'Polish',
        'ms': 'Malay',
        'sl': 'Slovenian',
        'sw': 'Swahili',
        'sd': 'Sindhi',
        'ml': 'Malayalam',
        'tg': 'Tajik',
        'ta': 'Tamil',
        'ur': 'Urdu',
        'uz': 'Uzbek',
        'hi': 'Hindi',
        'tt': 'Tatar',
        'so': 'Somali',
        'az': 'Azerbaijani',
        'bn': 'Bengali',
        'dv': 'Divehi',
        'ha': 'Hausa',
        'ug': 'Uughur'
        } #languages
