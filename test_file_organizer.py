import unittest
import file_organizer
from pathlib import Path
import os
import shutil
from dotenv import load_dotenv
from distutils.dir_util import copy_tree
import json

load_dotenv()
SOURCE_FOLDER = os.getenv('SOURCE_FOLDER')
DEST_FOLDER = os.getenv('DESTINATION_FOLDER')


class TestFileOpener(unittest.TestCase):

    # BEFORE ALL TESTS
    @classmethod
    def setUpClass(cls):
        # print('setup')
        copy_tree('file_types',f'{SOURCE_FOLDER}')

    # AFTER ALL TESTS
    @classmethod
    def tearDownClass(cls):
        shutil.rmtree(SOURCE_FOLDER)
        shutil.rmtree(DEST_FOLDER)
        os.mkdir(SOURCE_FOLDER)
        os.mkdir(DEST_FOLDER)

    # # BEFORE EACH TEST
    # def setUp(self):
    #     # print('setup')

    # # AFTER EACH TEST
    # def tearDown(self):
    #     # print('teardown')

    # TESTS
    

    def test_build_directories(self):
        # Checks if the file structure already exists - if not, then the file structure will be built

        filter_object = file_organizer.scan_json('filters.json')

        self.assertTrue(len(os.listdir(DEST_FOLDER)) == 0)
        file_organizer.build_directories(DEST_FOLDER,filter_object)
        self.assertTrue(len(os.listdir(DEST_FOLDER)) == 8)
        file_organizer.build_directories(DEST_FOLDER, filter_object)
        self.assertTrue(len(os.listdir(DEST_FOLDER)) == 8)
    
    def test_scan_source(self):
        # should return a list of all items with file extensions in the source folder except for the folder
        direct_list = os.listdir(SOURCE_FOLDER)
        test_list = file_organizer.scan_source(SOURCE_FOLDER)
        for test_entry in test_list:
            self.assertTrue(test_entry in direct_list)
        self.assertTrue('oop' not in test_list and 'oop' in direct_list)

    def test_sort(self):
        filter_object = file_organizer.scan_json('filters.json')
        file_organizer.build_directories(DEST_FOLDER, filter_object)
        # Checks file type and sorts them in either 
        test_files = [f'{SOURCE_FOLDER}\\f.png',f'{SOURCE_FOLDER}\SOV.psd',f'{SOURCE_FOLDER}\\Cardero Tips.xlsx',f'{SOURCE_FOLDER}\\random.txt',f'{SOURCE_FOLDER}\\other.other']
        for file in test_files:
            file_organizer.sort(file,SOURCE_FOLDER,DEST_FOLDER, filter_object)
        self.assertTrue(len(os.listdir(f'{DEST_FOLDER}\\Graphics')) == 2)
        self.assertTrue(len(os.listdir(f'{DEST_FOLDER}\\Documents')) == 1)
        self.assertTrue(len(os.listdir(f'{DEST_FOLDER}\\Notes')) == 1)
        self.assertTrue(len(os.listdir(f'{DEST_FOLDER}\\Others')) == 1)




if __name__ == '__main__':
    unittest.main()
