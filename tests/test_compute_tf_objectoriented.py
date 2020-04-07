"""Test cases for the object-oriented implementation"""

from termfrequency import compute_tf_objectoriented


def test_read_file_populates_data_0():
    """ Checks that the reading of the small text file works """
    storage_manager = compute_tf_objectoriented.DataStorageManager("inputs/input.txt")
    word_list = storage_manager.words()
    assert word_list is not None
    assert len(word_list) == 12
