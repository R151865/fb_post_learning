from fb_post_clean_arch.models import *
import factory
import datetime

import factory

class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User
    name = factory.Sequence(lambda n: "user%d" % n)
    username = factory.Sequence(lambda n: "username %d" % n)
    profile_pic = factory.Sequence(lambda n: "profile_pic/user%d.png" % n)


class PostFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Post
    user = factory.SubFactory(UserFactory)
    post_content = factory.Sequence(lambda n: "post content%d" % n)
    pub_date_time = factory.LazyFunction(datetime.datetime.now)


# class CommentFactory(factory.django.DjangoModelFactory):
#     class Meta:
#         model = Comment
#     content = factory.Sequence(lambda n: "comment content%d" % n)
#     commented_at = factory.LazyFunction(datetime.datetime.now)
#     commented_by = factory.SubFactory(UserFactory)
#     post = factory.SubFactory(PostFactory)



# class ReplyFactory(factory.django.DjangoModelFactory):
#     class Meta:
#         model = Comment
#     content = factory.Sequence(lambda n: "reply content%d" % n)
#     commented_at = factory.LazyFunction(datetime.datetime.now)
#     commented_by = factory.SubFactory(UserFactory)
#     post = factory.SubFactory(PostFactory)
#     parent_comment = factory.SubFactory(CommentFactory,
#         post=factory.LazyAttribute(lambda o: o.factory_parent.post)
#         )


# class PostReactionFactory(factory.django.DjangoModelFactory):
#     class Meta:
#         model = Reaction
#     reaction = factory.fuzzy.FuzzyChoice(REACTION_CHOICES,
#                                          getter=lambda rc: rc[0])
#     post = factory.SubFactory(PostFactory)
#     reacted_by = factory.SubFactory(UserFactory)
#     reacted_at = factory.LazyFunction(datetime.datetime.now)


# class CommentReactionFactory(factory.django.DjangoModelFactory):
#     class Meta:
#         model = Reaction
#     reaction = factory.fuzzy.FuzzyChoice(REACTION_CHOICES,
#                                          getter=lambda rc: rc[0])
#     comment = factory.SubFactory(CommentFactory)
#     reacted_by = factory.SubFactory(UserFactory)
#     reacted_at = factory.LazyFunction(datetime.datetime.now)
