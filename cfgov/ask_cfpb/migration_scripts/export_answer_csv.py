import datetime

from django.utils import html
from paying_for_college.csvkit import csvkit

from knowledgebase.models import Question

"""
output goals:
- Question ID
- Question
- English answer (richtext?)
- English short answer
- URL
- status
- Topic
- Categories, pipe-delimited
- Audiences
- Related Questions (ID/question)
- Upsell items
"""

HEADINGS = [
    'ASK_ID',
    'Question',
    'ShortAnswer',
    'Answer',
    'URL',
    'Status',
    'Topic',
    'SubCategories',
    'Audiences',
    'RelatedQuestions',
    'UpsellItems',
]


def assemble_output():
    english_questions = Question.objects.exclude(englishanswer=None)
    output_rows = []
    for q in english_questions:
        output = {heading: '' for heading in HEADINGS}
        output['ASK_ID'] = q.id
        output['Question'] = q.title
        output['Answer'] = html.strip_tags(q.englishanswer.answer)
        output['ShortAnswer'] = html.strip_tags(
            q.englishanswer.one_sentence_answer)
        output['URL'] = q.englishanswer.get_absolute_url()
        output['Status'] = q.englishanswer.workflow_state
        output['Topic'] = q.question_category.filter(parent=None).first().name
        output['SubCategories'] = " | ".join(
            [qc.name for qc in q.question_category.exclude(parent=None)])
        output['Audiences'] = " | ".join(a.name for a in q.audiences.all())
        output['RelatedQuestions'] = " | ".join(
            [question.__repr__() for question in q.related_questions.all()])
        output['UpsellItems'] = (
            q.englishanswer.upsellitem.title
            if q.englishanswer.upsellitem
            else '')
        output_rows.append(output)
    return output_rows


def export_questions():
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d")
    with open('questions_{}.csv'.format(timestamp), 'w') as f:
        writer = csvkit.writer(f)
        writer.writerow(HEADINGS)
        for row in assemble_output():
            writer.writerow([row[key] for key in HEADINGS])


if __name__ == "__main__":
    export_questions()
