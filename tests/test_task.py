from unittest import TestCase

from kata.task import Task


class TestTask(TestCase):

    def test_create_task_default(self):
        task = Task('a_task_name')
        assert task.name == 'a_task_name'
        assert task.tags == []
        assert task.checklists == []

    def test_create_task_enriched(self):
        task = Task('a_task_name', description='a_description', tags=['a_tag_1', 'a_tag_2'])
        assert task.name == 'a_task_name'
        assert task.description == 'a_description'
        assert task.tags == ['a_tag_1', 'a_tag_2']

    def test_create_task_with_deadlines(self):
        task = Task('a_task_name', start_date='a_start_date', end_date='a_end_date')
        assert task.name == 'a_task_name'
        assert task.start_date == 'a_start_date'
        assert task.end_date == 'a_end_date'

    def test_create_task_with_checklist(self):
        task = Task('a_task_name', 'a_checklist')
        assert task.name == 'a_task_name'
        assert task.checklists == ['a_checklist']

    def test_create_task_with_checklists(self):
        task = Task('a_task_name', 'a_checklist_1', 'a_checklist_2', 'a_checklist_3')
        assert task.name == 'a_task_name'
        assert task.checklists == ['a_checklist_1', 'a_checklist_2', 'a_checklist_3']

    def test_archive_task(self):
        task = Task('a_task')
        archived = task.archive()

        assert task.archived
        assert archived
