import pytest

from fb_post_v2.models import Reaction

from fb_post_v2.storages.storage_implementation import StorageImplementation

from fb_post_v2.constants import ReactionTypeEnum

@pytest.mark.django_db
def test_update_comment_reaction_with_valid_details(create_users,
                                                    create_posts,
                                                    create_comments,
                                                    create_reactions):

    # Arrange
    user_id = 1
    comment_id = 1
    reaction_type = ReactionTypeEnum.THUMBS_UP.value
    storage = StorageImplementation()

    # Act
    storage.update_comment_reaction(user_id=user_id,
                                    comment_id=comment_id,
                                    reaction_type=reaction_type)

    # Assert
    reaction =  Reaction.objects.get(reacted_by_id=user_id,
                                     comment_id=comment_id,
                                     reaction=reaction_type)

    assert user_id == reaction.reacted_by_id
    assert comment_id == reaction.comment_id
    assert reaction_type == reaction.reaction
