import uuid
from pycsw_helper.csw_helper import MRecords

mrec = MRecords()

def insert_into_db():
    out_dic = {"identifier": uuid.uuid1(),
               "typename": '',
               "schema": '',
               "mdsource": '',
               "insert_date": '',
               "xml": "",
               "anytext": '',
               "language": '',
               "type": 'Zip File',
               "title": '',
               "title_alternate": '',
               "abstract": '',
               "keywords": '',
               "keywordstype": '',
               "parentidentifier": '',
               "relation": '',
               "time_begin": '',
               "time_end": '',
               "topicategory": '',
               "resourcelanguage": '',
               "creator": '',
               "publisher": '',
               "contributor": '',
               "organization": '',
               "securityconstraints": '',
               "accessconstraints": '',
               "otherconstraints": '',
               "date": '',
               "date_revision": '',
               "date_creation": '',
               "date_publication": '',
               "date_modified": '',
               "format": '',
               "source": '',
               "crs": '',
               "geodescode": '',
               "denominator": '',
               "distancevalue": '',
               "distanceuom": '',
               "wkt_geometry": '',
               "servicetype": '',
               "servicetypeversion": '',
               "operation": '',
               "couplingtype": '',
               "operateson": '',
               "operatesonidentifier": '',
               "operatesoname": '',
               "degree": '',
               "classification": '',
               "conditionapplyingtoaccessanduse": '',
               "lineage": '',
               "responsiblepartyrole": '',
               "specificationtitle": '',
               "specificationdate": '',
               "specificationdatetype": '',
               "links": ''}

    # out_dic['conditionapplyingtoaccessanduse'] = raw_dic['USELIMIT'.lower()]
    out_dic["organization"] = 'OSGeo China Chapter'
    # out_dic["format"] = raw_dic['FORMDES'.lower()]
    # out_dic['date_publication'] = raw_dic['PUBTIME'.lower()]
    out_dic["source"] = 'http://www.maphub.cn'
    out_dic['publisher'] = 'OSGeo China Chapter'

    mrec.add_or_update(out_dic, force=True)
