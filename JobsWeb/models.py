# -*- coding: utf-8 -*-

# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#     * Rearrange models' order
#     * Make sure each model has one field with primary_key=True
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [appname]'
# into your database.

from __future__ import unicode_literals

from django.db import models

import datetime

import django.db.models.options as options

class Alertjobhost(models.Model):
    #unique
    id = models.AutoField(primary_key=True)
    #name
    name = models.CharField(max_length=50L, blank=True)
    #group
    env = models.CharField(max_length=100L, blank=True)
    #load
    capacity = models.CharField(max_length=50L, blank=True)
    #time
    time = models.CharField(max_length=100L, blank=True)
    def __unicode__(self):
	return u"%s %s " %(self.name,self.env)
    class Meta:
        db_table = 'alertjobhost'
	#verbose_name = 'user'

class Alertgroup(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50L, blank=True)
    userlist = models.CharField(max_length=255L, blank=True)
    class Meta:
        db_table = 'alertgroup'

class Alertjobalert(models.Model):
    id = models.IntegerField(primary_key=True)
    job_id = models.IntegerField(null=True, blank=True)
    error_type = models.IntegerField(null=True, blank=True)
    created_time = models.DateTimeField()
    content = models.CharField(max_length=500L)
    log_id = models.IntegerField()
    stat = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = 'alertjobalert'

class Alertjobdatasource(models.Model):
    id = models.IntegerField(primary_key=True)
    job_id = models.IntegerField(null=True, blank=True)
    type = models.IntegerField()
    operation = models.IntegerField(null=True, blank=True)
    server = models.CharField(max_length=50L, blank=True)
    dbname = models.CharField(max_length=50L, blank=True)
    dbtable = models.CharField(max_length=50L, blank=True)
    other = models.CharField(max_length=500L, blank=True)
    mod_time = models.DateTimeField()
    class Meta:
        db_table = 'alertjobdatasource'

class Alertjobdepend(models.Model):
    id = models.IntegerField(primary_key=True)
    job_id = models.IntegerField(null=True, blank=True)
    depend_id = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = 'alertjobdepend'

class Alertjobdeploy(models.Model):
    id = models.IntegerField(primary_key=True)
    job_id = models.IntegerField(null=True, blank=True)
    content = models.CharField(max_length=300L, blank=True)
    deployfile = models.CharField(max_length=100L, blank=True)
    stat = models.IntegerField(null=True, blank=True)
    mod_time = models.DateTimeField(null=True, blank=True)
    class Meta:
        db_table = 'alertjobdeploy'

class Alertjoberror(models.Model):
    id = models.IntegerField(primary_key=True)
    job_id = models.IntegerField(null=True, blank=True)
    error_id = models.IntegerField()
    findtime = models.DateTimeField(null=True, blank=True)
    reason = models.CharField(max_length=500L, blank=True)
    errorresult = models.CharField(max_length=500L, blank=True)
    errorlevel = models.CharField(max_length=10L, blank=True)
    process = models.CharField(max_length=500L, blank=True)
    finetime = models.DateTimeField(null=True, blank=True)
    mod_time = models.DateTimeField(null=True, blank=True)
    error_type = models.IntegerField()
    stat = models.IntegerField()
    class Meta:
        db_table = 'alertjoberror'

class Alertjoblist(models.Model):
    id = models.AutoField(primary_key=True)
    code = models.CharField(max_length=10L)
    #JOB名称
    name = models.CharField(max_length=50L, blank=True)
    #运行环境
    env = models.CharField(max_length=50L, blank=True)
    #运行服务器
    server = models.CharField(max_length=100L, blank=True)
    #TAG
    effect = models.CharField(max_length=500L, blank=True)
    #负责人
    owner = models.CharField(max_length=100L, blank=True)
    #相关人
    relate_owner = models.CharField(max_length=100L, blank=True)
    iswatch = models.IntegerField(null=True, blank=True)
    watchmethod = models.CharField(max_length=500L)
    #Log地址
    islog = models.CharField(max_length=100L, blank=True)
    #游标地址
    cur_log=models.CharField(max_length=100L, blank=True)
    delete_log = models.CharField(max_length=500L, blank=True)
    dbstat = models.CharField(max_length=500L, blank=True)
    #上线时间
    ontime = models.CharField(max_length=100L, blank=True)
    #备注信息
    remark = models.CharField(max_length=500L, blank=True)
    read_db = models.CharField(max_length=500L, blank=True)
    write_db = models.CharField(max_length=500L, blank=True)
    mod_time = models.DateTimeField(null=True, blank=True)
    #3 存在依赖JOB
    job_type = models.IntegerField(null=True, blank=True)
    #运行时间
    job_start = models.CharField(max_length=10L)
    #依赖job标注
    #dependjob = models.IntegerField()
    #运行时长
    job_expected_end = models.CharField(max_length=10L, blank=True)
    job_threshold_up = models.IntegerField(null=True, blank=True)
    job_threshold_down = models.IntegerField(null=True, blank=True)
    job_end = models.CharField(max_length=10L)
    offset = models.IntegerField(null=True, blank=True)
    job_max_times = models.IntegerField(null=True, blank=True)
    #运行间隔
    job_run_interval = models.CharField(max_length=10L)
    job_interval = models.CharField(max_length=10L)
    job_interval_type = models.IntegerField(null=True, blank=True)
    #job开始时间
    job_first_start=models.IntegerField()
    #job运行时间时长
    job_runtime=models.IntegerField()
    #job运行间隔
    job_runinterval=models.IntegerField()
    #运行命令
    command = models.CharField(max_length=255L, blank=True)
    business_level = models.CharField(max_length=3L)
    run_time_level = models.CharField(max_length=10L, blank=True)
    data_source = models.CharField(max_length=500L, blank=True)
    #逻辑删除 0删除 1正常
    runstat = models.IntegerField(null=True, blank=True, default=1)
    #调度状态
    run_status = models.IntegerField(null=True, blank=True, default=0)
    queue_status = models.IntegerField()
    #是否调度
    is_manage = models.IntegerField(null=True, blank=True)
    error_group = models.IntegerField(null=True, blank=True)
    error_code = models.IntegerField(null=True, blank=True)
    #事业部
    site = models.IntegerField()
    class Meta:
        db_table = 'alertjoblist'

class AlertjoblistOld(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100L, blank=True)
    server = models.CharField(max_length=100L, blank=True)
    runtime = models.CharField(max_length=100L, blank=True)
    effect = models.CharField(max_length=255L, blank=True)
    owner = models.CharField(max_length=100L, blank=True)
    runstat = models.IntegerField(null=True, blank=True)
    iswatch = models.IntegerField(null=True, blank=True)
    isrecover = models.IntegerField(null=True, blank=True)
    islog = models.IntegerField(null=True, blank=True)
    dbstat = models.CharField(max_length=255L, blank=True)
    ontime = models.CharField(max_length=100L, blank=True)
    remark = models.CharField(max_length=255L, blank=True)
    class Meta:
        db_table = 'alertjoblist_old'

class Alertjoblog(models.Model):
    id = models.AutoField(primary_key=True)
    job_id = models.IntegerField()
    starttime = models.DateTimeField(null=True, blank=True)
    endtime = models.DateTimeField(null=True, blank=True)
    status = models.IntegerField()
    class Meta:
        db_table = 'alertjoblog'

class AlertjoblogOld(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100L, blank=True)
    content = models.CharField(max_length=255L, blank=True)
    logtime = models.DateTimeField(null=True, blank=True)
    class Meta:
        db_table = 'alertjoblog_old'

class Alertjobmodlog(models.Model):
    #modify log  -->>  user audit log
    id = models.AutoField(primary_key=True)
    job_id = models.IntegerField(null=True, blank=True)
    owner = models.CharField(max_length=50L, blank=True)
    ontime = models.CharField(max_length=50L, blank=True)
    content = models.CharField(max_length=500L, blank=True)
    mod_time = models.DateTimeField(null=True, blank=True)
    class Meta:
        db_table = 'alertjobmodlog'

class Alertjobqueue(models.Model):
    id = models.AutoField(primary_key=True)
    job_id = models.IntegerField()
    status = models.IntegerField(default='0')
    pid = models.IntegerField(null=True, blank=True)
    env = models.CharField(max_length=100L)
    server = models.CharField(max_length=100L)
    create_time = models.DateTimeField(default=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    class Meta:
        db_table = 'alertjobqueue'

class Alertjobrunlog(models.Model):
    id = models.IntegerField(primary_key=True)
    job_id = models.IntegerField()
    content = models.CharField(max_length=255L)
    create_time = models.DateTimeField(null=True, blank=True)
    class Meta:
        db_table = 'alertjobrunlog'

class Alertjobsystem(models.Model):
    id = models.IntegerField(primary_key=True)
    cpu = models.FloatField()
    memory = models.FloatField()
    server = models.CharField(max_length=255L)
    class Meta:
        db_table = 'alertjobsystem'

class Alertlist(models.Model):
    id = models.AutoField(primary_key=True)
    level_id = models.IntegerField(null=True, blank=True)
    module_id = models.IntegerField(null=True, blank=True)
    group_id = models.IntegerField(null=True, blank=True)
    content = models.CharField(max_length=255L, blank=True)
    param = models.CharField(max_length=500L, blank=True)
    stat = models.IntegerField(null=True, blank=True)
    created_time = models.DateTimeField(null=True, blank=True)
    class Meta:
        db_table = 'alertlist'

class Alertlogmodule(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100L, blank=True)
    code = models.CharField(max_length=100L, blank=True)
    class Meta:
        db_table = 'alertlogmodule'

class Alertmodule(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100L, blank=True)
    code = models.CharField(max_length=100L, blank=True)
    class Meta:
        db_table = 'alertmodule'

class Alertpublish(models.Model):
    id = models.IntegerField(primary_key=True)
    owner = models.IntegerField()
    release = models.CharField(max_length=15L)
    pmt = models.IntegerField()
    branch = models.CharField(max_length=255L, blank=True)
    review = models.IntegerField(null=True, blank=True)
    business_level = models.CharField(max_length=10L, blank=True)
    tech_level = models.CharField(max_length=10L, blank=True)
    no_test = models.IntegerField()
    test = models.IntegerField(null=True, blank=True)
    second_test = models.IntegerField(null=True, blank=True)
    self_test = models.IntegerField(null=True, blank=True)
    create_time = models.DateTimeField(null=True, blank=True)
    class Meta:
        db_table = 'alertpublish'


class UserCenter(models.Model):
    MId =models.AutoField(primary_key=True)
    UserName=models.CharField(max_length=255L, blank=True)
    UserPasswd=models.CharField(max_length=255L, blank=True)
    class Meta:
        db_table ='ajk_admin_manager'
        #verbose_name = 'user'
        app_label = 'user'
