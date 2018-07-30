
NAMESPACE = {'tdwg':   'http://rs.tdwg.org/dwc/text/',
             'gbif':   'http://rs.gbif.org/terms/1.0/',
             'eml':    'eml://ecoinformatics.org/eml-2.1.1',
             'xsi':    'http://www.w3.org/2001/XMLSchema-instance',
             'dublin': 'http://purl.org/dc/terms/'}
GBIF_URL = 'http://api.gbif.org/v1'
BISON_UUID = 'c3ad790a-d426-4ac1-8e32-da61f81f0117'
ENCODING = 'utf-8'

DATAPATH = '/tank/data/input/bison/'
SUBDIRS = ('territories', 'us')
DATASET_DIR = 'dataset'
META_FNAME = '/tank/data/input/bison/us/meta.xml'

CLIP_CHAR = '/'
DELIMITER = '\t'
URL_ESCAPES = [ [" ", "%20"], [",", "%2C"] ]

LOG_FORMAT = ' '.join(["%(asctime)s",
                       "%(threadName)s.%(module)s.%(funcName)s",
                       "line",
                       "%(lineno)d",
                       "%(levelname)-8s",
                       "%(message)s"])

LOG_DATE_FORMAT = '%d %b %Y %H:%M'
LOGFILE_MAX_BYTES = 52000000 
LOGFILE_BACKUP_COUNT = 5


INTERPRETED = 'tidy_occurrence.csv'
VERBATIM = 'tidy_verbatim.csv'
OUT_BISON = 'outBison.txt'

NO_OUTPUT = None
COMPUTED = None

TERM_CONVERT = {'humanObservation': 'observation', 
                'machineObservation': 'observation',
                'preservedSpecimen': 'specimen', 
                'fossilSpecimen': 'specimen'}

# Test these against lowercase values
PROHIBITED_VALS = ['na', '#na', 'n/a']

SAVE_FIELDS = {
   # pull canonical name from API and taxonKey
   'gbifID': (str, INTERPRETED),
   # pull canonical name from API and taxonKey
   'taxonKey': (NO_OUTPUT, INTERPRETED),
   'canonicalName': (str, COMPUTED),
   'scientificName': (str, INTERPRETED),
    
   'basisOfRecord': (str, INTERPRETED), 
   'eventDate': (str, INTERPRETED), 
   'year': (int, INTERPRETED),
   'verbatimEventDate': (str, INTERPRETED), 
   'institutionCode': (str, INTERPRETED), 
   'institutionId': (str, INTERPRETED), 
   'ownerInstitutionCode': (str, INTERPRETED),
   'collectionID': (str, INTERPRETED),
   'occurrenceID': (str, INTERPRETED),
   'catalogNumber': (str, INTERPRETED),
   'recordedBy': (str, INTERPRETED),
   'recordNumber': (str, INTERPRETED),
   'decimalLatitude': (float, INTERPRETED),
   'decimalLongitude': (float, INTERPRETED),
   # `elevation` is only in INTERPRETED, `verbatimElevation` in both
   'elevation': (str, INTERPRETED), 
   # `depth` is only in INTERPRETED, `verbatimDepth` in both
   'depth': (str, INTERPRETED), 
   'county': (str, INTERPRETED), 
   'higherGeographyID': (str, INTERPRETED), 
   'stateProvince': (str, INTERPRETED), 
   
   # pull publisher from API and ?
   'publisher': (NO_OUTPUT, INTERPRETED),
   'providerID': (str, COMPUTED), 
   
   # pull resource from API and datasetKey
   'datasetKey': (NO_OUTPUT, INTERPRETED),
   'resourceID': (str, COMPUTED),
   
   'vernacularName': (str, INTERPRETED), 
   'kingdom': (str, INTERPRETED), 
   'geodeticDatum': (str, INTERPRETED), 
   'coordinatePrecision': (str, INTERPRETED), 
   'coordinateAccuracy': (str, INTERPRETED), 
   'verbatimLocality': (str, INTERPRETED), 
   'waterBody': (str, INTERPRETED), 
   'countryCode': (str, INTERPRETED), 
   'license': (str, INTERPRETED), 
   # delete records with status=absent
   'occurrenceStatus': (str, INTERPRETED),
   # only in verbatim
#    'geodeticDatum': (str, INTERPRETED),
 }


ORDERED_OUT_FIELDS = [
   'gbifID', 
   'canonicalName', 'canonicalNameFromTaxonKey', 'canonicalNameFromSciname', 
   'basisOfRecord', 'eventDate', 'year', 
   'verbatimEventDate', 'institutionCode', 'institutionId', 
   'ownerInstitutionCode', 'collectionID', 'occurrenceID', 'catalogNumber', 
   'recordedBy', 'recordNumber', 'decimalLatitude', 'decimalLongitude', 
   'elevation', 'depth', 'county', 'higherGeographyID', 'stateProvince', 
   'providerID', 'resourceID', 'vernacularName', 'kingdom', 'geodeticDatum', 
   'coordinatePrecision', 'coordinateAccuracy', 'verbatimLocality', 'waterBody', 
   'countryCode', 'license', 'occurrenceStatus']

TEST_FIELDS = ['occurrenceStatus', 'decimalLatitude', 'decimalLongitude']
COMPUTE_FIELDS = {'taxonKey': 'canonicalName', 
                  'publisher': 'providerID',
                  'datasetKey': 'resourceID',
                  'basisOfRecord': None}
