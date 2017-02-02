
from django.core.exceptions import ObjectDoesNotExist
from wagtail.wagtailcore.models import Site

from flags.models import Flag, FlagState
from socket import gethostname


def init_missing_flag_states_for_site(site):
    existing_flags = site.flag_states.values_list('flag', flat=True)
    missing_flags = Flag.objects.exclude(key__in=existing_flags)

    FlagState.objects.bulk_create([
        FlagState(
            site=site,
            flag=flag,
            enabled=flag.enabled_by_default
        ) for flag in missing_flags
    ])

def flag_enabled(request, key):
    site = Site.find_for_request(request)

    if request:
	    try:
	        return site.flag_states.get(flag_id=key).enabled
	    except ObjectDoesNotExist:
	        pass

    try:
        return Flag.objects.get(key=key).enabled_by_default
    except ObjectDoesNotExist:
        return False


def flags_enabled(request, *keys):
    return all(flag_enabled(request, key) for key in keys)


def flag_disabled(request, key):
    return not flag_enabled(request, key)


def is_flag_enabled(flag_name):
	flags = FlagState.objects.filter(flag_id=flag_name)
	is_enabled = False
	if flags.count() > 1:
		try:
			site_id = Site.objects.get(hostname=gethostname()).id
		except:
			site_id = Site.objects.get(is_default_site=True).id
		flag = FlagState.objects.get(site_id=site_id, flag_id=flag_name)
		if flag:
			is_enabled = flag.enabled
	elif flags.count() == 1:
		is_enabled = flags.last().enabled

	return is_enabled

