from django.urls import path, include, re_path
from friendship.views import view_friends, friendship_add_friend, friendship_accept, \
    friendship_reject, friendship_cancel, friendship_request_list, \
    friendship_request_list_rejected, friendship_requests_detail, followers,\
    following, follower_add, follower_remove, all_users

urlpatterns = [
    re_path(
        r'^users/$',
        view=all_users,
        name='friendship_view_users',
    ),
    re_path(
        r'^friends/(?P<username>[\w-]+)/$',
        view=view_friends,
        name='friendship_view_friends',
    ),
    re_path(
        r'^friend/add/(?P<to_username>[\w-]+)/$',
        view=friendship_add_friend,
        name='friendship_add_friend',
    ),
    re_path(
        r'^friend/accept/(?P<friendship_request_id>\d+)/$',
        view=friendship_accept,
        name='friendship_accept',
    ),
    re_path(
        r'^friend/reject/(?P<friendship_request_id>\d+)/$',
        view=friendship_reject,
        name='friendship_reject',
    ),
    re_path(
        r'^friend/cancel/(?P<friendship_request_id>\d+)/$',
        view=friendship_cancel,
        name='friendship_cancel',
    ),
    re_path(
        r'^friend/requests/$',
        view=friendship_request_list,
        name='friendship_request_list',
    ),
    re_path(
        r'^friend/requests/rejected/$',
        view=friendship_request_list_rejected,
        name='friendship_requests_rejected',
    ),
    re_path(
        r'^friend/request/(?P<friendship_request_id>\d+)/$',
        view=friendship_requests_detail,
        name='friendship_requests_detail',
    ),
    re_path(
        r'^followers/(?P<username>[\w-]+)/$',
        view=followers,
        name='friendship_followers',
    ),
    re_path(
        r'^following/(?P<username>[\w-]+)/$',
        view=following,
        name='friendship_following',
    ),
    re_path(
        r'^follower/add/(?P<followee_username>[\w-]+)/$',
        view=follower_add,
        name='follower_add',
    ),
    re_path(
        r'^follower/remove/(?P<followee_username>[\w-]+)/$',
        view=follower_remove,
        name='follower_remove',
    ),
]
