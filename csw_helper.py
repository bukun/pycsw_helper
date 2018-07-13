# -*- coding:utf-8 -*-
import peewee
from cfg import pycsw_db

class Records(peewee.Model):
    class Meta:
        database = pycsw_db
    identifier = peewee.TextField(null=False, index=True, primary_key=True, unique=True)
    typename = peewee.TextField(null=False)
    schema = peewee.TextField(null=False)
    mdsource = peewee.TextField(null=False)
    insert_date = peewee.TextField(null=False)
    xml = peewee.TextField(null=False)
    anytext = peewee.TextField(null=False)
    language = peewee.TextField(null=True, default='')
    type = peewee.TextField(null=True, default='')
    title = peewee.TextField(null=True, default='')
    title_alternate = peewee.TextField(null=True, default='')
    abstract = peewee.TextField(null=True, default='')
    keywords = peewee.TextField(null=True, default='')
    keywordstype = peewee.TextField(null=True, default='')
    parentidentifier = peewee.TextField(null=True, default='')
    relation = peewee.TextField(null=True, default='')
    time_begin = peewee.TextField(null=True, default='')
    time_end = peewee.TextField(null=True, default='')
    topicategory = peewee.TextField(null=True, default='')
    resourcelanguage = peewee.TextField(null=True, default='')
    creator = peewee.TextField(null=True, default='')
    publisher = peewee.TextField(null=True, default='')
    contributor = peewee.TextField(null=True, default='')
    organization = peewee.TextField(null=True, default='')
    securityconstraints = peewee.TextField(null=True, default='')
    accessconstraints = peewee.TextField(null=True, default='')
    otherconstraints = peewee.TextField(null=True, default='')
    date = peewee.TextField(null=True, default='')
    date_revision = peewee.TextField(null=True, default='')
    date_creation = peewee.TextField(null=True, default='')
    date_publication = peewee.TextField(null=True, default='')
    date_modified = peewee.TextField(null=True, default='')
    format = peewee.TextField(null=True, default='')
    source = peewee.TextField(null=True, default='')
    crs = peewee.TextField(null=True, default='')
    geodescode = peewee.TextField(null=True, default='')
    denominator = peewee.TextField(null=True, default='')
    distancevalue = peewee.TextField(null=True, default='')
    distanceuom = peewee.TextField(null=True, default='')
    wkt_geometry = peewee.TextField(null=True, default='')
    servicetype = peewee.TextField(null=True, default='')
    servicetypeversion = peewee.TextField(null=True, default='')
    operation = peewee.TextField(null=True, default='')
    couplingtype = peewee.TextField(null=True, default='')
    operateson = peewee.TextField(null=True, default='')
    operatesonidentifier = peewee.TextField(null=True, default='')
    operatesoname = peewee.TextField(null=True, default='')
    degree = peewee.TextField(null=True, default='')
    classification = peewee.TextField(null=True, default='')
    conditionapplyingtoaccessanduse = peewee.TextField(null=True, default='')
    lineage = peewee.TextField(null=True, default='')
    responsiblepartyrole = peewee.TextField(null=True, default='')
    specificationtitle = peewee.TextField(null=True, default='')
    specificationdate = peewee.TextField(null=True, default='')
    specificationdatetype = peewee.TextField(null=True, default='')
    links = peewee.TextField(null=True, default='')


class MRecords(object):
    def __init__(self):
        self.tab_app = Records
        # try:
        #     self.tab_app.create_table()
        # except:
        #     pass

    def delete(self, del_id):
        entry = self.tab_app.delete().where(self.tab_app.identifier == del_id)
        entry.execute()
        return True

    def add_or_update(self, uid, postdata):
        if self.get_by_uid(postdata['identifier']):
            print('To Del ..................')
            self.delete(postdata['identifier'])
        self.add(uid, postdata)

    def add(self, uid, postdata):
        '''
        命令行更新的
        '''
        entry = self.tab_app.create(
            identifier=postdata["identifier"],
            typename=postdata["typename"],
            schema=postdata["schema"],
            mdsource=postdata["mdsource"],
            insert_date=postdata["insert_date"],
            xml=postdata["xml"],
            anytext=postdata["anytext"],
            language=postdata["language"],
            type=postdata["type"],
            title=postdata["title"],
            title_alternate=postdata["title_alternate"],
            abstract=postdata["abstract"],
            keywords=postdata["keywords"],
            keywordstype=postdata["keywordstype"],
            parentidentifier=postdata["parentidentifier"],
            relation=postdata["relation"],
            time_begin=postdata["time_begin"],
            time_end=postdata["time_end"],
            topicategory=postdata["topicategory"],
            resourcelanguage=postdata["resourcelanguage"],
            creator=postdata["creator"],
            publisher=postdata["publisher"],
            contributor=postdata["contributor"],
            organization=postdata["organization"],
            securityconstraints=postdata["securityconstraints"],
            accessconstraints=postdata["accessconstraints"],
            otherconstraints=postdata["otherconstraints"],
            date=postdata["date"],
            date_revision=postdata["date_revision"],
            date_creation=postdata["date_creation"],
            date_publication=postdata["date_publication"],
            date_modified=postdata["date_modified"],
            format=postdata["format"],
            source=postdata["source"],
            crs=postdata["crs"],
            geodescode=postdata["geodescode"],
            denominator=postdata["denominator"],
            distancevalue=postdata["distancevalue"],
            distanceuom=postdata["distanceuom"],
            wkt_geometry=postdata["wkt_geometry"],
            servicetype=postdata["servicetype"],
            servicetypeversion=postdata["servicetypeversion"],
            operation=postdata["operation"],
            couplingtype=postdata["couplingtype"],
            operateson=postdata["operateson"],
            operatesonidentifier=postdata["operatesonidentifier"],
            operatesoname=postdata["operatesoname"],
            degree=postdata["degree"],
            classification=postdata["classification"],
            conditionapplyingtoaccessanduse=postdata["conditionapplyingtoaccessanduse"],
            lineage=postdata["lineage"],
            responsiblepartyrole=postdata["responsiblepartyrole"],
            specificationtitle=postdata["specificationtitle"],
            specificationdate=postdata["specificationdate"],
            specificationdatetype=postdata["specificationdatetype"],
            links=postdata["links"],
        )
        return uid

    def get_by_uid(self, sig):
        try:
            return self.tab_app.get(identifier=sig)
        except:
            return False
