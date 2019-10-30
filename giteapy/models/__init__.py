# coding: utf-8

# flake8: noqa
"""
    Gitea API.

    This documentation describes the Gitea API.  # noqa: E501

    OpenAPI spec version: 1.1.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

# import models into model package
from giteapy.models.api_error import APIError
from giteapy.models.access_token import AccessToken
from giteapy.models.add_collaborator_option import AddCollaboratorOption
from giteapy.models.add_time_option import AddTimeOption
from giteapy.models.annotated_tag import AnnotatedTag
from giteapy.models.annotated_tag_object import AnnotatedTagObject
from giteapy.models.attachment import Attachment
from giteapy.models.branch import Branch
from giteapy.models.comment import Comment
from giteapy.models.commit import Commit
from giteapy.models.commit_meta import CommitMeta
from giteapy.models.commit_user import CommitUser
from giteapy.models.contents_response import ContentsResponse
from giteapy.models.create_email_option import CreateEmailOption
from giteapy.models.create_file_options import CreateFileOptions
from giteapy.models.create_fork_option import CreateForkOption
from giteapy.models.create_gpg_key_option import CreateGPGKeyOption
from giteapy.models.create_hook_option import CreateHookOption
from giteapy.models.create_issue_comment_option import CreateIssueCommentOption
from giteapy.models.create_issue_option import CreateIssueOption
from giteapy.models.create_key_option import CreateKeyOption
from giteapy.models.create_label_option import CreateLabelOption
from giteapy.models.create_milestone_option import CreateMilestoneOption
from giteapy.models.create_org_option import CreateOrgOption
from giteapy.models.create_pull_request_option import CreatePullRequestOption
from giteapy.models.create_release_option import CreateReleaseOption
from giteapy.models.create_repo_option import CreateRepoOption
from giteapy.models.create_status_option import CreateStatusOption
from giteapy.models.create_team_option import CreateTeamOption
from giteapy.models.create_user_option import CreateUserOption
from giteapy.models.delete_email_option import DeleteEmailOption
from giteapy.models.delete_file_options import DeleteFileOptions
from giteapy.models.deploy_key import DeployKey
from giteapy.models.edit_attachment_options import EditAttachmentOptions
from giteapy.models.edit_deadline_option import EditDeadlineOption
from giteapy.models.edit_git_hook_option import EditGitHookOption
from giteapy.models.edit_hook_option import EditHookOption
from giteapy.models.edit_issue_comment_option import EditIssueCommentOption
from giteapy.models.edit_issue_option import EditIssueOption
from giteapy.models.edit_label_option import EditLabelOption
from giteapy.models.edit_milestone_option import EditMilestoneOption
from giteapy.models.edit_org_option import EditOrgOption
from giteapy.models.edit_pull_request_option import EditPullRequestOption
from giteapy.models.edit_release_option import EditReleaseOption
from giteapy.models.edit_repo_option import EditRepoOption
from giteapy.models.edit_team_option import EditTeamOption
from giteapy.models.edit_user_option import EditUserOption
from giteapy.models.email import Email
from giteapy.models.external_tracker import ExternalTracker
from giteapy.models.external_wiki import ExternalWiki
from giteapy.models.file_commit_response import FileCommitResponse
from giteapy.models.file_delete_response import FileDeleteResponse
from giteapy.models.file_links_response import FileLinksResponse
from giteapy.models.file_response import FileResponse
from giteapy.models.gpg_key import GPGKey
from giteapy.models.gpg_key_email import GPGKeyEmail
from giteapy.models.git_blob_response import GitBlobResponse
from giteapy.models.git_entry import GitEntry
from giteapy.models.git_hook import GitHook
from giteapy.models.git_object import GitObject
from giteapy.models.git_tree_response import GitTreeResponse
from giteapy.models.hook import Hook
from giteapy.models.identity import Identity
from giteapy.models.inline_response200 import InlineResponse200
from giteapy.models.inline_response2001 import InlineResponse2001
from giteapy.models.internal_tracker import InternalTracker
from giteapy.models.issue import Issue
from giteapy.models.issue_deadline import IssueDeadline
from giteapy.models.issue_labels_option import IssueLabelsOption
from giteapy.models.label import Label
from giteapy.models.markdown_option import MarkdownOption
from giteapy.models.merge_pull_request_option import MergePullRequestOption
from giteapy.models.migrate_repo_form import MigrateRepoForm
from giteapy.models.milestone import Milestone
from giteapy.models.organization import Organization
from giteapy.models.pr_branch_info import PRBranchInfo
from giteapy.models.payload_commit import PayloadCommit
from giteapy.models.payload_commit_verification import PayloadCommitVerification
from giteapy.models.payload_user import PayloadUser
from giteapy.models.permission import Permission
from giteapy.models.public_key import PublicKey
from giteapy.models.pull_request import PullRequest
from giteapy.models.pull_request_meta import PullRequestMeta
from giteapy.models.reference import Reference
from giteapy.models.release import Release
from giteapy.models.repo_commit import RepoCommit
from giteapy.models.repo_topic_options import RepoTopicOptions
from giteapy.models.repository import Repository
from giteapy.models.search_results import SearchResults
from giteapy.models.server_version import ServerVersion
from giteapy.models.state_type import StateType
from giteapy.models.status import Status
from giteapy.models.status_state import StatusState
from giteapy.models.tag import Tag
from giteapy.models.team import Team
from giteapy.models.time_stamp import TimeStamp
from giteapy.models.topic_name import TopicName
from giteapy.models.topic_response import TopicResponse
from giteapy.models.tracked_time import TrackedTime
from giteapy.models.update_file_options import UpdateFileOptions
from giteapy.models.user import User
from giteapy.models.user_heatmap_data import UserHeatmapData
from giteapy.models.watch_info import WatchInfo
