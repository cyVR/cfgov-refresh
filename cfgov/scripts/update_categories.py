from v1.models.base import CFGOVPage
from v1.tests.wagtail_pages.helpers import publish_changes

def run():
    for page in CFGOVPage.objects.all():
        sidefoot = page.sidefoot
        page_updated = False
        if sidefoot:
            stream_data = sidefoot.stream_data
            related_posts = filter(lambda item: item['type'] == 'related_posts', stream_data)
            if related_posts:
                specific_categories = related_posts[0]['value']['specific_categories']
                if specific_categories == [''] or specific_categories == [None]:
                    specific_categories = []
                    page_updated = True
                for cat in specific_categories:
                    if cat == 'Policy &amp; Compliance':
                        specific_categories.remove('Policy &amp; Compliance')
                        specific_categories.append('policy-compliance')
                        page_updated = True
                    elif cat == 'Info for Consumers':
                        specific_categories.remove('Info for Consumers')
                        specific_categories.append('info-for-consumers')
                        page_updated = True
                    elif cat == 'Data, Research &amp; Reports':
                        specific_categories.remove('Data, Research &amp; Reports')
                        specific_categories.append('data-research-reports')
                        page_updated = True
                    elif cat == 'At the CFPB':
                        specific_categories.remove('At the CFPB')
                        specific_categories.append('at-the-cfpb')
                        page_updated = True
                    elif cat == 'Press Release':
                        specific_categories.remove('Press Release')
                        specific_categories.append('press-release')
                        page_updated = True
                related_posts[0]['value']['specific_categories'] = specific_categories
        for cat in page.categories.get_object_list():
            if cat.name == 'policy_compliance': 
                cat.name = 'policy-compliance'
                page_updated = True
        if page_updated:
            publish_changes(page)