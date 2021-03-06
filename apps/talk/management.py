from django.conf import settings
from django.db.models import signals
from django.utils.translation import ugettext_noop as _

if "notification" in settings.INSTALLED_APPS:
    from notification import models as notification

    def create_notice_types(app, created_models, verbosity, **kwargs):
        notification.create_notice_type("talk_added", 
                                        _("Talk added"),
                                        _("a talk has been added"), 
                                        default = 2)
        notification.create_notice_type("talk_accepted", 
                                        _("Talk accepted"),
                                        _("a talk has been accepted"), 
                                        default = 2)
        notification.create_notice_type("talk_scheduled", 
                                        _("Talk scheduled"),
                                        _("a talk has been scheduled"), 
                                        default = 2)
        notification.create_notice_type("talk_comment_added", 
                                        _("Talk comment"),
                                        _("a comment has been posted on a talk"), 
                                        default = 2)

    signals.post_syncdb.connect(create_notice_types, sender=notification)
else:
    print "Skipping creation of NoticeTypes as notification app not found"

