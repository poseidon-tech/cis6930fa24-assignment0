import pytest
import time
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import main


file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'Resources', 'data.json'))


def test_non_empty_page():
    for page in range(1,52,10):
        data = main.downloadData(page)
        assert data is not None
        assert len(data['items']) > 0
        time.sleep(2)  # Sleep for 0.5 second between requests
        
def test_empty_page():
    data = main.downloadData(999)  
    assert len(data['items']) == 0

def test_parse_file():
    data = main.parseFile(file_path)
    assert data is not None
    
def test_invalid_parse_file():
    data = main.parseFile("nofile")
    assert data is None

def test_title_extraction():
    data = main.downloadData(1)
    for item in data['items']:
        assert 'title' in item
        assert isinstance(item['title'], str)

def test_subjects_data():
    data = main.downloadData(1)
    for item in data['items']:
        assert 'subjects' in item
        if item['subjects'] != None :
            assert isinstance(item['subjects'],list)
        else:
            assert item['subjects'] is None
        
def test_field_offices():
    data = main.downloadData(1)
    for item in data['items']:
        assert 'field_offices' in item
        if item['field_offices'] != None :
            assert isinstance(item['field_offices'], list)
        else:
            assert item['field_offices'] is None

def test_reformat():
    data = main.downloadData(1)
    output = main.reformat(data, 1)
    for index,item in enumerate(data['items']):
        title = item.get('title')
        subjects = ','.join(item['subjects']) if item['subjects'] else ""
        field_offices = ','.join(item['field_offices']) if item['field_offices'] else ""
        expected_output = f"{title}þ{subjects}þ{field_offices}"
        assert expected_output == output[index]


    

