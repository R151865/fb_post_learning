from fb_post_clean_arch.exceptions.custom_exceptions import InvalidPostId
from fb_post_clean_arch.interactors.presenters.presenter_interface import \
    PresenterInterface
from fb_post_clean_arch.interactors.storages.storage_interface import \
    StorageInterface
from fb_post_clean_arch.models import Post


class InvalidUserToDeletePost(Exception):
    pass


class DeletePostInteractor:

    def __init__(self, storage: StorageInterface,
                 presenter: PresenterInterface):
        self.storage = storage
        self.presenter = presenter

    def get_response_for_delete_post(self, user_id: int, post_id:int):

        try:
            self.storage.validate_post_id(post_id=post_id)
            self.check_is_post_created_by_user(post_id=post_id,
                                               user_id=user_id)

        except InvalidPostId:
            self.presenter.raise_exception_for_invalid_post()
            return
        except InvalidUserToDeletePost:
            self.presenter.raise_exception_for_invalid_post()
            return

        Post.objects.filter(id=post_id).delete()

    def check_is_post_created_by_user(self, post_id: int, user_id: int):
        is_post_posted_by_user = Post.objects\
                                     .filter(id=post_id,
                                             user_id=user_id).exists()
        is_not_post_posted_by_user = not is_post_posted_by_user
        if is_not_post_posted_by_user:
            raise InvalidUserToDeletePost()
