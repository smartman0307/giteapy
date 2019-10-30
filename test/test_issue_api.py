# coding: utf-8

"""
    Gitea API.

    This documentation describes the Gitea API.  # noqa: E501

    OpenAPI spec version: 1.1.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import giteapy
from giteapy.api.issue_api import IssueApi  # noqa: E501
from giteapy.rest import ApiException


class TestIssueApi(unittest.TestCase):
    """IssueApi unit test stubs"""

    def setUp(self):
        self.api = giteapy.api.issue_api.IssueApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_issue_add_label(self):
        """Test case for issue_add_label

        Add a label to an issue  # noqa: E501
        """
        pass

    def test_issue_add_time(self):
        """Test case for issue_add_time

        Add a tracked time to a issue  # noqa: E501
        """
        pass

    def test_issue_clear_labels(self):
        """Test case for issue_clear_labels

        Remove all labels from an issue  # noqa: E501
        """
        pass

    def test_issue_create_comment(self):
        """Test case for issue_create_comment

        Add a comment to an issue  # noqa: E501
        """
        pass

    def test_issue_create_issue(self):
        """Test case for issue_create_issue

        Create an issue. If using deadline only the date will be taken into account, and time of day ignored.  # noqa: E501
        """
        pass

    def test_issue_create_label(self):
        """Test case for issue_create_label

        Create a label  # noqa: E501
        """
        pass

    def test_issue_create_milestone(self):
        """Test case for issue_create_milestone

        Create a milestone  # noqa: E501
        """
        pass

    def test_issue_delete_comment(self):
        """Test case for issue_delete_comment

        Delete a comment  # noqa: E501
        """
        pass

    def test_issue_delete_comment_deprecated(self):
        """Test case for issue_delete_comment_deprecated

        Delete a comment  # noqa: E501
        """
        pass

    def test_issue_delete_label(self):
        """Test case for issue_delete_label

        Delete a label  # noqa: E501
        """
        pass

    def test_issue_delete_milestone(self):
        """Test case for issue_delete_milestone

        Delete a milestone  # noqa: E501
        """
        pass

    def test_issue_edit_comment(self):
        """Test case for issue_edit_comment

        Edit a comment  # noqa: E501
        """
        pass

    def test_issue_edit_comment_deprecated(self):
        """Test case for issue_edit_comment_deprecated

        Edit a comment  # noqa: E501
        """
        pass

    def test_issue_edit_issue(self):
        """Test case for issue_edit_issue

        Edit an issue. If using deadline only the date will be taken into account, and time of day ignored.  # noqa: E501
        """
        pass

    def test_issue_edit_issue_deadline(self):
        """Test case for issue_edit_issue_deadline

        Set an issue deadline. If set to null, the deadline is deleted. If using deadline only the date will be taken into account, and time of day ignored.  # noqa: E501
        """
        pass

    def test_issue_edit_label(self):
        """Test case for issue_edit_label

        Update a label  # noqa: E501
        """
        pass

    def test_issue_edit_milestone(self):
        """Test case for issue_edit_milestone

        Update a milestone  # noqa: E501
        """
        pass

    def test_issue_get_comments(self):
        """Test case for issue_get_comments

        List all comments on an issue  # noqa: E501
        """
        pass

    def test_issue_get_issue(self):
        """Test case for issue_get_issue

        Get an issue  # noqa: E501
        """
        pass

    def test_issue_get_label(self):
        """Test case for issue_get_label

        Get a single label  # noqa: E501
        """
        pass

    def test_issue_get_labels(self):
        """Test case for issue_get_labels

        Get an issue's labels  # noqa: E501
        """
        pass

    def test_issue_get_milestone(self):
        """Test case for issue_get_milestone

        Get a milestone  # noqa: E501
        """
        pass

    def test_issue_get_milestones_list(self):
        """Test case for issue_get_milestones_list

        Get all of a repository's opened milestones  # noqa: E501
        """
        pass

    def test_issue_get_repo_comments(self):
        """Test case for issue_get_repo_comments

        List all comments in a repository  # noqa: E501
        """
        pass

    def test_issue_list_issues(self):
        """Test case for issue_list_issues

        List a repository's issues  # noqa: E501
        """
        pass

    def test_issue_list_labels(self):
        """Test case for issue_list_labels

        Get all of a repository's labels  # noqa: E501
        """
        pass

    def test_issue_remove_label(self):
        """Test case for issue_remove_label

        Remove a label from an issue  # noqa: E501
        """
        pass

    def test_issue_replace_labels(self):
        """Test case for issue_replace_labels

        Replace an issue's labels  # noqa: E501
        """
        pass

    def test_issue_start_stop_watch(self):
        """Test case for issue_start_stop_watch

        Start stopwatch on an issue.  # noqa: E501
        """
        pass

    def test_issue_stop_watch(self):
        """Test case for issue_stop_watch

        Stop an issue's existing stopwatch.  # noqa: E501
        """
        pass

    def test_issue_tracked_times(self):
        """Test case for issue_tracked_times

        List an issue's tracked times  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
