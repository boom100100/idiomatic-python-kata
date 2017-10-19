import pytest
from unittest.mock import MagicMock, Mock

from kata.board import Board, BoardException
from kata.task import Task, TaskException

TITLE = 'irrelevant_title'


def test_is_public():
    board = Board(title=TITLE, is_public=True)
    assert isinstance(board, Board)
    assert board.is_public


def test_is_not_public_when_false():
    board = Board(title=TITLE, is_public=False)
    assert isinstance(board, Board)
    assert board.is_public is False


def test_is_not_public_when_none():
    board = Board(title=TITLE, is_public=None)
    assert isinstance(board, Board)
    assert board.is_public is False


def test_add_tag_list():
    board = Board(title=TITLE)
    tags = ['tag_1', 'tag_2', 'tag_3']
    board.add_tags(tags)
    assert board.tags == tags


def test_add_single_tag():
    board = Board(title=TITLE)
    tag = 'tag_1'
    board.add_tags(tag)
    assert board.tags == [tag]


def test_add_none_empty_tags():
    board = Board(title=TITLE)
    board.add_tags('TAG')
    board.add_tags('')
    board.add_tags(None)
    assert board.tags == ['TAG']


def test_columns():
    board1 = Board(title=TITLE, columns=['ToDo', 'Done'])

    board2 = Board(title=TITLE)
    board3 = Board(title=TITLE)

    board2.add_column('Doing')
    board3.add_column('OnHold')
    board2.add_column('Archived')

    assert board1.columns == ['ToDo', 'Done']
    assert board2.columns == ['Doing', 'Archived']
    assert board3.columns == ['OnHold']


def test_add_task():
    board = Board(title=TITLE, columns=['ToDo', 'Done'])
    task = Task('a_task')
    board.add_task(column='ToDo', task=task)

    assert board.tasks == [task]


def test_add_tasks():
    board = Board(title=TITLE, columns=['ToDo', 'Done'])
    task1 = Task('a_task_1')
    task2 = Task('a_task_2')
    board.add_task(column='ToDo', task=task1)
    board.add_task(column='ToDo', task=task2)

    assert board.tasks == [task1, task2]


def test_archive_all():
    board = Board(title=TITLE, columns=['ToDo', 'Done'])
    board.add_task(column='ToDo', task=Task('a_task_1'))
    board.add_task(column='ToDo', task=Task('a_task_2'))
    board.add_task(column='Done', task=Task('a_task_3'))

    archived = board.archive_all()

    assert archived
    for task in board.tasks:
        assert task.archived


def test_archive_all_by_column():
    board = Board(title=TITLE, columns=['ToDo', 'Done'])
    board.add_task(column='ToDo', task=Task('a_task_1'))
    board.add_task(column='ToDo', task=Task('a_task_2'))
    board.add_task(column='Done', task=Task('a_task_3'))

    archived = board.archive_all(columns=['ToDo'])

    assert archived
    for task in board.tasks:
        if task.name != 'a_task_3':
            assert task.archived
        else:
            assert not task.archived


def test_close_board():
    board = Board(title=TITLE, columns=['ToDo'])
    board.notify_close = Mock()
    board.add_task(column='ToDo', task=Task('a_task_1'))
    board.add_task(column='ToDo', task=Task('a_task_2'))

    board.close()

    assert board.is_closed
    for task in board.tasks:
        assert task.archived
    board.notify_close.assert_called_once()


def test_close_board_when_archive_fail():
    board = Board(title=TITLE, columns=['ToDo'])
    task = Task('a_task_1')
    task.archive = Mock(side_effect=TaskException('irrelevant_message'))
    task.notify_close = MagicMock()
    board.add_task(column='ToDo', task=Task('a_task_2'))
    board.add_task(column='ToDo', task=task)

    with pytest.raises(BoardException):
        board.close()

    assert not board.is_closed
    assert not task.archived
    task.notify_close.assert_not_called()
