from django.shortcuts import render, render_to_response, get_object_or_404
from django.template import RequestContext
from django.db import connections
from django.conf import settings
from datetime import datetime

# Create your views here.
def main(request):


    with connections['mysql'].cursor() as c:
        c.execute("SELECT id, subject, first_post_id FROM forum_topics WHERE forum_id = %s ORDER BY id DESC LIMIT %s" % (settings.FORUM_ID, settings.LIMIT_POST))
        topics =  dictfetchall(c)
    posts = []
    for topic in topics:
        with connections['mysql'].cursor() as c:
            c.execute("SELECT poster, id, poster_id, topic_id, message, posted FROM forum_posts WHERE id = %s" % (topic['first_post_id']))
            post = dictfetchall(c)
            post = post[0]
            post['topic_id'] = topic['id']
            post['subject'] = topic['subject']
            posts.append(post)
    older_posts = posts[6:]
    
    return render_to_response('main.html',
            {'posts': posts, 'older_posts': older_posts, 'FORUM_URL': settings.FORUM_URL,
                'FORUM_ID': settings.FORUM_ID},
            context_instance=RequestContext(request))


def dictfetchall(cursor):
    "Return all rows from a cursor as a dict"
    desc = cursor.description
    return [
            dict(zip([col[0] for col in desc], row))
            for row in cursor.fetchall()
            ]

def about(request):
    return render_to_response('about.html',
            {},
            context_instance=RequestContext(request))
