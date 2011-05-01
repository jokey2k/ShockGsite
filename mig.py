from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.schema import ForeignKeyConstraint

old_engine = create_engine('postgresql://web1_shockg:b7TWQZZRvMvBKbFu@127.0.0.1:5432/web1_shockg')
new_engine = create_engine('postgresql://shockgsite:W7UQdaPvTQrN71J92USrghLii@127.0.0.1:5432/shockgsite')

OldBase = declarative_base()
NewBase = declarative_base()

OldSession = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=old_engine))
NewSession = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=new_engine))
OldBase.metadata.reflect(old_engine)
NewBase.metadata.reflect(new_engine)

class OldUser(OldBase):
    __tablename__ = 'users'
    __table_args__ = (
        {'autoload':True}
    )

class OldCategory(OldBase):
    __tablename__ = 'board_categories'
    __table_args__ = (
        {'autoload':True, 'useexisting':True}
    )

class OldTopic(OldBase):
    __tablename__ = 'board_topics'
    __table_args__ = (
        {'autoload':True, 'useexisting':True}
    )

class OldForum(OldBase):
    __tablename__ = 'board_forums'
    __table_args__ = (
        {'autoload':True, 'useexisting':True}
    )

class OldPost(OldBase):
    __tablename__ = 'board_posts'
    __table_args__ = (
        {'autoload':True, 'useexisting':True}
    )

class NewUser(NewBase):
    __tablename__ = 'auth_user'
    __table_args__ = (
        {'autoload':True}
    )

class NewCategory(NewBase):
    __tablename__ = 'djangobb_forum_category'
    __table_args__ = (
        {'autoload':True, 'useexisting':True}
    )

class NewForum(NewBase):
    __tablename__ = 'djangobb_forum_forum'
    __table_args__ = (
        {'autoload':True, 'useexisting':True}
    )

class NewTopic(NewBase):
    __tablename__ = 'djangobb_forum_topic'
    __table_args__ = (
        {'autoload':True, 'useexisting':True}
    )

class NewPost(NewBase):
    __tablename__ = 'djangobb_forum_post'
    __table_args__ = (
        {'autoload':True, 'useexisting':True}
    )

class NewUserProfile(NewBase):
    __tablename__ = 'djangobb_forum_profile'
    __table_args__ = (
        ForeignKeyConstraint(['user_id'], ['auth_user.id']),
        {'autoload':True, 'useexisting':True}
    )

import datetime
known_userids = []
for user in OldSession.query(OldUser).order_by(OldUser.user_id).all():
    new_user = NewUser()
    known_userids.append(user.user_id)
    for right, left in [('user_id','id'), ('username','username'), ('email','email'), ('pw_hash','password'),('creation_date','date_joined'),('last_visited','last_login'),('real_name','first_name')]:
        setattr(new_user,left,getattr(user,right))
    new_user.last_name=""
    new_user.is_active=True
    new_user.is_staff=False
    new_user.is_superuser=False
    new_user.password = new_user.password.replace("sha$","sha1$")
    NewSession.add(new_user)
    new_user_profile = NewUserProfile()
    NewSession.add(new_user_profile)
    for right, left in [('user_id','user_id'),('user_id','id'),('city','location'),('birthday','birthday'),('notes','signature')]:
        setattr(new_user_profile,left,getattr(user,right))
    for key in new_user_profile.__table__.columns._data.keys():
        attr = getattr(new_user_profile, key)
        if attr is None:
            setattr(new_user_profile,key,"")
    new_user_profile.time_zone=1
    new_user_profile.theme="default"
    new_user_profile.show_avatar=False
    new_user_profile.show_signatures=False
    new_user_profile.show_smilies=False
    new_user_profile.privacy_permission=1
    new_user_profile.markup="bbcode"
    new_user_profile.country="DE"
    new_user_profile.post_count=0
    new_user_profile.birthday=datetime.date.today()

NewSession.commit()

def get_or_create_user(username):
    user = NewSession.query(NewUser).filter(NewUser.username==username).first()
    if user is None:
        user = NewUser()
        user.first_name = user.last_name = user.email = user.password = ""
        user.is_staff = user.is_active = user.is_superuser = False
        user.last_login = user.date_joined = datetime.date.today()
        user.username = username
        NewSession.add(user)
        NewSession.commit()
        new_user_profile = NewUserProfile()
        new_user_profile.id=user.id
        new_user_profile.user_id=user.id
        new_user_profile.time_zone=1
        new_user_profile.theme="default"
        new_user_profile.show_avatar=False
        new_user_profile.show_signatures=False
        new_user_profile.show_smilies=False
        new_user_profile.privacy_permission=1
        new_user_profile.markup="bbcode"
        new_user_profile.country="DE"
        new_user_profile.post_count=0
        new_user_profile.birthday=datetime.date.today()
        for key in new_user_profile.__table__.columns._data.keys():
            attr = getattr(new_user_profile, key)
            if attr is None:
                setattr(new_user_profile,key,"")
        NewSession.add(new_user_profile)
        NewSession.commit()
    return user

user = NewUser()
user.first_name = user.last_name = user.email = user.password = ""
user.is_staff = user.is_active = user.is_superuser = False
user.last_login = user.date_joined = datetime.date.today()
user.username = "Anonymous User"
user.id = -1
NewSession.add(user)
NewSession.commit()

catnr = 0
for cat in OldSession.query(OldCategory).order_by(OldCategory.category_id).all():
    new_cat = NewCategory()
    catnr = cat.category_id
    for left, right in [
        ('id','category_id'),
        ('name','name'),
        ('position','ordering')]:
        setattr(new_cat,left,getattr(cat,right))
    NewSession.add(new_cat)

forumnum = 0
for forumnr, forum in enumerate(OldSession.query(OldForum).order_by(OldForum.forum_id).all()):
    new_forum = NewForum()
    forumnum = forum.forum_id
    for left, right in [
        ('forum_id','id'),
        ('category_id','category_id'),
        ('name','name'),
        ('ordering','position'),
        ('topiccount','topic_count'),
        ('postcount','post_count'),
        ('lastpost_id','last_post_id'),
        ('description','description'),
        ('modification_date','updated')]:
        setattr(new_forum,right,getattr(forum,left) if getattr(forum,left) is not None else  '')
    NewSession.add(new_forum)

topicnum = 0
for topicnr, topic in enumerate(OldSession.query(OldTopic).order_by(OldTopic.topic_id).all()):
    topicnum = topic.topic_id
    new_topic = NewTopic()
    for left, right in [
        ('id','topic_id'),
        ('forum_id','forum_id'),
        ('name','name'),
        ('created','date'),
        ('user_id','author_id'),
        ('post_count','postcount'),
        ('last_post_id','lastpost_id'),
        ('updated','modification_date')]:
        setattr(new_topic,left,getattr(topic,right) if getattr(topic,right) is not None else  '')
    new_topic.views=0
    new_topic.closed=False
    new_topic.sticky = True if topic.is_sticky else False
    if new_topic.user_id not in known_userids:
        new_topic.user_id = -1
    NewSession.add(new_topic)

postnum = 0
for post in OldSession.query(OldPost).order_by(OldPost.post_id).all():
    postnum = post.post_id
    new_post = NewPost()
    for left, right in [
        ('id','post_id'),
        ('topic_id','topic_id'),
        ('user_id','author_id'),
        ('body','text'),
        ('body_html','text'),
        ('user_ip','ip'),
        ('created','date')]:
        setattr(new_post,left,getattr(post,right))
    new_post.markup = 'bbcode'
    if new_post.user_id is None:
        new_post.user_id=-1
    NewSession.add(new_post)
NewSession.commit()

new_engine.execute("SELECT setval('auth_user_id_seq', %i);" % max(known_userids))
new_engine.execute("SELECT setval('djangobb_forum_category_id_seq', %i);" % catnr)
new_engine.execute("SELECT setval('djangobb_forum_forum_id_seq', %i);" % forumnum)
new_engine.execute("SELECT setval('djangobb_forum_topic_id_seq', %i);" % topicnum)
new_engine.execute("SELECT setval('djangobb_forum_post_id_seq', %i);" % postnum)

for post in NewSession.query(NewPost).filter(NewPost.user_id==-1).all():
    oldpost = OldSession.query(OldPost).get(post.id)
    post.user_id = get_or_create_user(oldpost.author_str).id
NewSession.commit()
for topic in NewSession.query(NewTopic):
    post = NewSession.query(NewPost).filter(NewPost.topic_id==topic.id).order_by(NewPost.id).first()
    topic.user_id = post.user_id
NewSession.commit()

