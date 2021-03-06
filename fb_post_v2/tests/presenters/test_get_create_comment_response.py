from fb_post_v2.presenters import PresenterImplementation


def test_get_create_comment_response():

    # Arrange
    comment_id = 1
    expected_comment_id_dict = {
        "comment_id": comment_id
    }

    json_presenter = PresenterImplementation()

    # Act
    actual_comment_id = json_presenter.get_create_comment_response(comment_id=comment_id)

    # Assert
    assert actual_comment_id == expected_comment_id_dict